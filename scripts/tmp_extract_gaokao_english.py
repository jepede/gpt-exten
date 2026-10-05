#!/usr/bin/env python3
import hashlib
import html as htmlmod
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

OUT = Path("gaokao_english_txt")
OUT.mkdir(exist_ok=True)

S = requests.Session()
S.headers.update({
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
})

SOURCES = {
    2017: [
        "https://read01.com/DgBnGA.html",
        "https://www.yjbys.com/edu/zhukao/297768.html",
    ],
    2018: [
        "https://www.sohu.com/a/234718898_809571",
        "https://kknews.cc/zh-cn/education/mqxbljp.html",
    ],
    2019: [
        "https://www.cpsenglish.com/question/33442",
        "https://gaokao.exam8.com/4474201.html",
    ],
    2020: [
        "https://www.en-sky.com/post/275.html",
        "https://zy.21cnjy.com/7996753",
    ],
    2021: [
        "https://www.en-sky.com/post/589.html",
        "https://zy.21cnjy.com/9420474",
    ],
    2022: [
        "https://www.en-sky.com/post/773.html",
        "https://zy.21cnjy.com/12401051",
    ],
    2023: [
        "https://www.cpsenglish.com/article/1168",
        "https://zy.21cnjy.com/16187687",
    ],
    2024: [
        "https://www.cpsenglish.com/article/1223",
        "https://www.kaosheng.com/down/202410/23/559.html",
        "https://zy.21cnjy.com/20569440",
    ],
    2025: [
        "https://www.yeyulingfeng.com/wendang/350971.html",
        "https://zy.21cnjy.com/23168059",
    ],
    2026: [
        "https://www.en-sky.com/post/1238.html",
        "https://zy.21cnjy.com/25946873",
    ],
}

def fetch(url: str, timeout: int = 35) -> str:
    last = None
    for attempt in range(3):
        try:
            r = S.get(url, timeout=timeout, allow_redirects=True)
            if r.status_code == 200 and len(r.content) > 1200:
                if not r.encoding or r.encoding.lower() in {"iso-8859-1", "latin-1"}:
                    r.encoding = r.apparent_encoding or "utf-8"
                return r.text
            last = RuntimeError(f"HTTP {r.status_code}, bytes={len(r.content)}")
        except Exception as exc:
            last = exc
        time.sleep(1.2 * (attempt + 1))
    raise RuntimeError(f"{url}: {last}")

def html_to_text(raw: str) -> str:
    soup = BeautifulSoup(raw, "lxml")
    for tag in soup(["script", "style", "noscript", "svg", "header", "footer", "nav"]):
        tag.decompose()
    text = htmlmod.unescape(soup.get_text("\n")).replace("\r", "").replace("\u3000", " ")
    lines = []
    for line in text.splitlines():
        line = re.sub(r"[ \t\xa0]+", " ", line).strip()
        if not line:
            continue
        if line in {
            "资源下载", "立即下载", "免费下载", "收藏", "分享", "网站首页",
            "登录", "注册", "展开全文", "收起全文", "下载", "查看答案"
        }:
            continue
        lines.append(line)
    return "\n".join(lines)

def choose_start(text: str, year: int) -> int:
    pats = [
        rf"{year}\s*年普通高等学校招生全国统一考试",
        rf"{year}\s*年普通高等学校全国统一考试",
        r"绝密[★*]?\s*(?:启用前|启封前|考试启用前)",
    ]
    hits = []
    for p in pats:
        m = re.search(p, text)
        if m:
            hits.append(m.start())
    if hits:
        # Prefer the year title if available; it is less likely to be a navigation mention.
        year_hits = []
        for p in pats[:2]:
            m = re.search(p, text)
            if m:
                year_hits.append(m.start())
        return min(year_hits) if year_hits else min(hits)

    # Some carefully edited pages omit the official title and start directly at the paper.
    candidates = []
    for token in ("第一部分", "第一部分听力", "第一部分 听力", "第一部分阅读", "第一部分 阅读"):
        p = text.find(token)
        if p >= 0:
            candidates.append(p)
    if candidates:
        return min(candidates)
    return 0

def strip_embedded_answers(lines):
    out = []
    for line in lines:
        # Keep the standard sample sentence “答案是C。” but remove actual answer keys.
        if re.match(r"^(?:答案|参考答案|正确答案)[：:]\s*", line):
            continue
        if line.startswith("〖答案〗"):
            continue
        if re.fullmatch(r"(?:\d{1,2}\s*[—–-]\s*\d{1,2}\s*[：:]?\s*[A-D]{3,}\s*){1,8}", line):
            continue
        if re.fullmatch(r"[A-D]{5,}(?:\s+[A-D]{5,})*", line):
            continue
        out.append(line)
    return out

END_PATTERNS = [
    r"\n(?:[^\n]{0,30})参考答案(?:[：:]|\n)",
    r"\n答案(?:及|与)?解析(?:[：:]|\n)",
    r"\n解析(?:[：:]|\n)",
    r"\nImage资源列表",
    r"\n资源列表",
    r"\n缩略图、资源来源",
    r"\n发表于\s*20\d\d",
    r"\n你可能感兴趣的文章",
    r"\n相关问题",
    r"\n相关文档",
    r"\n相关推荐",
    r"\n上一篇",
    r"\n下一篇",
]

def clean_exam(text: str, year: int) -> str:
    text = text.replace("英 语", "英语")
    start = choose_start(text, year)
    text = text[start:]

    # Cut site appendices / final answer section only after enough exam body exists.
    cut_points = []
    for p in END_PATTERNS:
        m = re.search(p, text)
        if m and m.start() > 7000:
            cut_points.append(m.start())
    if cut_points:
        text = text[:min(cut_points)]

    lines = []
    for line in text.splitlines():
        if re.search(r"英语试题第\s*\d+\s*页.*共\s*\d+\s*页", line):
            continue
        if re.fullmatch(r"(?:PAGE\s*){1,4}\d*", line, flags=re.I):
            continue
        if re.fullmatch(r"[裂口Zz0-9 ]{6,}", line):
            continue
        # Remove obvious site chrome that can survive semantic HTML.
        if re.match(r"^(?:来源[:：]|阅读\s*\(|分类[:：]|扫一扫关注|本网站除注明原创|本文地址[:：])", line):
            continue
        lines.append(line)

    lines = strip_embedded_answers(lines)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text

def quality(text: str, year: int):
    score = 0
    reasons = []

    n = len(text)
    if n >= 10000:
        score += 4
    elif n >= 7000:
        score += 2
    else:
        reasons.append(f"too short ({n} chars)")

    required_any = [
        ("听力", "第一部分"),
        ("阅读", "阅读理解"),
        ("写作", "书面表达"),
    ]
    for group in required_any:
        if any(x in text for x in group):
            score += 1
        else:
            reasons.append("missing " + "/".join(group))

    # Typical multiple-choice body and final writing task.
    if len(re.findall(r"(?m)^\s*\d{1,2}[\.．]\s+", text)) >= 25:
        score += 2
    else:
        reasons.append("too few numbered questions")

    if "A." in text and "B." in text and "C." in text:
        score += 1
    else:
        reasons.append("choice markers missing")

    if year <= 2020:
        if "短文改错" in text:
            score += 1
        if "书面表达" in text:
            score += 1
    else:
        if "语言运用" in text:
            score += 1
        if "续写" in text:
            score += 1

    return score, reasons

manifest = ["Year\tPaper\tSource\tChars\tBytes\tSHA256\tQuality\tStatus"]
combined = []
log_lines = []

for year in range(2017, 2027):
    candidates = []
    for url in SOURCES[year]:
        try:
            raw = fetch(url)
            text = clean_exam(html_to_text(raw), year)
            q, reasons = quality(text, year)
            log_lines.append(f"{year}\t{url}\tquality={q}\tchars={len(text)}\t{' ; '.join(reasons) or 'OK'}")
            candidates.append((q, len(text), url, text, reasons))
        except Exception as exc:
            log_lines.append(f"{year}\t{url}\tERROR\t{exc}")

    if not candidates:
        manifest.append(f"{year}\t-\t-\t0\t0\t-\t0\tFAILED")
        continue

    candidates.sort(key=lambda x: (x[0], x[1]), reverse=True)
    q, _, url, text, reasons = candidates[0]

    # A conservative acceptance threshold: enough structure plus enough length.
    status = "OK" if q >= 8 and len(text) >= 7000 else "FAILED"
    label = (
        "全国I卷" if year <= 2020 else
        ("新高考全国I卷" if year <= 2022 else
         ("新课标I卷" if year <= 2024 else "全国I卷"))
    )

    header = (
        f"{year}年高考英语 {label}\n"
        "纯文本提取版（UTF-8）\n"
        f"Source: {url}\n"
        f"Extraction-Quality: {q}/10\n"
        "Note: 仅保留试题文本、题号、选项和写作要求；已尽量移除答案、解析和网页导航。"
        "个别网页转写源可能保留少量排版/OCR差异。\n"
        + "=" * 72 + "\n\n"
    )
    final = header + text
    filename = (
        f"{year}_gaokao_english_national_I.txt"
        if year <= 2020 or year >= 2025
        else f"{year}_gaokao_english_new_gaokao_I.txt"
    )

    if status == "OK":
        (OUT / filename).write_text(final, encoding="utf-8")
        combined.append(final + "\n\n")
    else:
        fail = header + "[QUALITY CHECK FAILED]\n" + "; ".join(reasons) + "\n\n" + text
        (OUT / filename.replace(".txt", "_FAILED.txt")).write_text(fail, encoding="utf-8")

    b = final.encode("utf-8")
    sha = hashlib.sha256(b).hexdigest()
    manifest.append(
        f"{year}\t{label}\t{url}\t{len(final)}\t{len(b)}\t{sha}\t{q}\t{status}"
    )

(OUT / "2017-2026_gaokao_english_national_I_combined.txt").write_text(
    "".join(combined), encoding="utf-8"
)
(OUT / "MANIFEST.tsv").write_text("\n".join(manifest) + "\n", encoding="utf-8")
(OUT / "EXTRACTION_LOG.txt").write_text("\n".join(log_lines) + "\n", encoding="utf-8")

ok = sum(line.endswith("\tOK") for line in manifest[1:])
print("\n".join(manifest))
print(f"OK={ok}/10")
print("\n--- extraction log ---")
print("\n".join(log_lines))

if ok != 10:
    print(f"ERROR: expected 10/10, got {ok}/10", file=sys.stderr)
    sys.exit(2)
