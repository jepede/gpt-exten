#!/usr/bin/env python3
from pathlib import Path
import re, csv, json, hashlib, shutil, unicodedata, subprocess, sys
from collections import defaultdict, Counter

ROOT = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve()
OUT.mkdir(parents=True, exist_ok=True)
PAPERS = OUT / "试卷"
TEXTS = OUT / "结构化重建文本"
RAW_STRUCT = OUT / "结构化语料补充"
REPORT = OUT / "报告"
for p in (PAPERS, TEXTS, RAW_STRUCT, REPORT):
    p.mkdir(parents=True, exist_ok=True)

SUBJECT_ALIASES = {
    "语文":"语文","chinese":"语文","chn":"语文",
    "数学":"数学","math":"数学",
    "英语":"英语","english":"英语","eng":"英语",
    "物理":"物理","physics":"物理","phys":"物理",
    "化学":"化学","chemistry":"化学","chem":"化学",
    "生物":"生物","biology":"生物","bio":"生物",
    "政治":"政治","politics":"政治","political":"政治",
    "历史":"历史","history":"历史","hist":"历史",
    "地理":"地理","geography":"地理","geo":"地理",
    "综合理综":"综合理综","理综":"综合理综","综合文综":"综合文综","文综":"综合文综",
    "日语":"日语"
}
PROVINCES = [
    "全国","北京","天津","上海","重庆","河北","河南","山东","山西","安徽","江西","江苏",
    "浙江","福建","广东","广西","海南","湖北","湖南","四川","贵州","云南","陕西","甘肃",
    "青海","宁夏","新疆","内蒙古","辽宁","吉林","黑龙江","西藏"
]
FILE_EXTS = {".pdf", ".doc", ".docx"}

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()

def sanitize(s):
    s = str(s or "").strip().replace("/", "_").replace("\\", "_")
    s = re.sub(r'[<>:"|?*\x00-\x1f]', "_", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s or "未标注"

def infer_year(text):
    m = re.search(r"(?<!\d)(19[5-9]\d|20[0-2]\d)(?!\d)", text)
    return int(m.group(1)) if m else None

def infer_subject(text, fixed=None):
    if fixed:
        return fixed
    low = text.lower()
    for k, v in SUBJECT_ALIASES.items():
        if k.lower() in low:
            return v
    return None

def infer_region(text, default="未标注"):
    for p in PROVINCES:
        if p in text:
            return p
    if "甲卷" in text or "乙卷" in text or "全国卷" in text or "新高考" in text or "新课标" in text:
        return "全国"
    return default

def norm_text(s):
    s = unicodedata.normalize("NFKC", s or "")
    s = re.sub(r"\s+", "", s)
    return s.replace("（", "(").replace("）", ")").replace("，", ",").replace("。", ".")

def pdf_text(path):
    try:
        cp = subprocess.run(
            ["pdftotext", "-enc", "UTF-8", str(path), "-"],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=90
        )
        return cp.stdout.decode("utf-8", "ignore")
    except Exception:
        return ""

def find_root(name):
    hits = list(ROOT.rglob(name))
    return hits[0] if hits else None

qroot = find_root("qingshuo-China-Gaokao-Papers-Collection")
qmeta = {}
if qroot:
    meta_csv = qroot / "data" / "exams.csv"
    if meta_csv.exists():
        with open(meta_csv, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                lp = (r.get("local_path") or "").strip()
                if lp:
                    qmeta[lp] = r

candidates = []

def add_candidate(path, source, year=None, subject=None, region=None, paper_type=None,
                  title=None, status=None, priority=50):
    if not path.is_file() or path.suffix.lower() not in FILE_EXTS:
        return
    text = str(path)
    year = year or infer_year(text)
    subject = subject or infer_subject(text)
    if not year or not subject:
        return
    title = title or path.stem
    region = region or infer_region(title)
    candidates.append({
        "src_path": path,
        "source": source,
        "year": year,
        "subject": subject,
        "region": region,
        "paper_type": paper_type or title,
        "title": title,
        "status": status or "",
        "priority": priority,
        "ext": path.suffix.lower(),
        "size": path.stat().st_size,
    })

# qingshuo: central metadata-backed local complete papers.
if qroot and (qroot / "papers").exists():
    for p in (qroot / "papers").rglob("*"):
        if not p.is_file() or p.suffix.lower() not in FILE_EXTS:
            continue
        rel = p.relative_to(qroot).as_posix()
        if rel.startswith("papers/supplements/") or rel.startswith("papers/partials/"):
            continue
        m = qmeta.get(rel, {})
        if m and (m.get("material_type") or "") not in ("", "完整试卷"):
            continue
        y = int(m["year"]) if (m.get("year") or "").isdigit() else None
        add_candidate(
            p, "qingshuo/China-Gaokao-Papers-Collection",
            year=y, subject=m.get("subject") or None, region=m.get("region") or None,
            paper_type=m.get("paper_type") or None, title=m.get("title") or None,
            status=m.get("status") or None,
            priority=10 if m.get("status") == "verified" else 20
        )

# deekur math and physics: authoritative breadth supplements.
for dirname, subject, source in [
    ("deekur-gaokaomath", "数学", "deekur/gaokaomath"),
    ("deekur-gaokaophysics", "物理", "deekur/gaokaophysics"),
]:
    rr = find_root(dirname)
    if not rr:
        continue
    for p in rr.rglob("*.pdf"):
        add_candidate(p, source, subject=subject, region=infer_region(p.stem), priority=30)

# Zaxaerith Chinese/English/Geography original document supplements.
for dirname, subject, source in [
    ("Zaxaerith-GaokaoCHN", "语文", "Zaxaerith/GaokaoCHN"),
    ("Zaxaerith-GaokaoENG", "英语", "Zaxaerith/GaokaoENG"),
    ("Zaxaerith-GaokaoGEO", "地理", "Zaxaerith/GaokaoGEO"),
]:
    rr = find_root(dirname)
    if not rr:
        continue
    for p in rr.rglob("*"):
        if p.is_file() and p.suffix.lower() in FILE_EXTS:
            add_candidate(p, source, subject=subject, region=infer_region(p.stem), priority=40)

# Exact SHA-256 deduplication.
for c in candidates:
    c["sha256"] = sha256(c["src_path"])
bysha = defaultdict(list)
for c in candidates:
    bysha[c["sha256"]].append(c)

selected = []
exact_dupes = []
for h, grp in bysha.items():
    grp = sorted(grp, key=lambda x: (x["priority"], -x["size"], str(x["src_path"])))
    keep = grp[0]
    selected.append(keep)
    for d in grp[1:]:
        exact_dupes.append((h, keep, d))

# Conservative PDF semantic dedup: only identical normalized extracted text.
text_seen = {}
semantic_dupes = []
final = []
for c in sorted(selected, key=lambda x: (x["priority"], x["year"], x["subject"], x["title"])):
    if c["ext"] != ".pdf":
        c["pdf_text_sha256"] = ""
        final.append(c)
        continue
    txt = norm_text(pdf_text(c["src_path"]))
    if len(txt) < 500:
        c["pdf_text_sha256"] = ""
        final.append(c)
        continue
    th = hashlib.sha256(txt.encode("utf-8")).hexdigest()
    c["pdf_text_sha256"] = th
    if th in text_seen:
        semantic_dupes.append((th, text_seen[th], c))
    else:
        text_seen[th] = c
        final.append(c)

# Canonical year -> subject layout.
manifest = []
name_counts = Counter()
for c in sorted(final, key=lambda x: (x["year"], x["subject"], x["region"], x["title"])):
    y = str(c["year"])
    sub = sanitize(c["subject"])
    reg = sanitize(c["region"])
    title = sanitize(c["title"])
    base = f"{reg}__{title}{c['ext']}"
    key = (y, sub, base.lower())
    name_counts[key] += 1
    if name_counts[key] > 1:
        base = f"{reg}__{title}__{c['sha256'][:8]}{c['ext']}"
    dst = PAPERS / y / sub / base
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(c["src_path"], dst)
    manifest.append({
        "year": c["year"], "subject": c["subject"], "region": c["region"],
        "paper_type": c["paper_type"], "title": c["title"],
        "format": c["ext"].lstrip("."), "source": c["source"],
        "source_path": str(c["src_path"].relative_to(ROOT)),
        "output_path": str(dst.relative_to(OUT)),
        "sha256": c["sha256"], "size": c["size"], "status": c["status"],
        "pdf_text_sha256": c.get("pdf_text_sha256", ""),
    })

# qingshuo answers/analysis/partials stay separate from complete-paper counts.
if qroot:
    for cat in ("supplements", "partials"):
        src = qroot / "papers" / cat
        if src.exists():
            shutil.copytree(src, OUT / "附属资料" / cat, dirs_exist_ok=True)

# Reconstruct text papers from rainewhk JSONL; it already integrates GAOKAO-Bench + Updates.
rroot = find_root("rainewhk-gaokao")
reconstructed = []
if rroot and (rroot / "dataset").exists():
    records = []
    for p in (rroot / "dataset").rglob("*.jsonl"):
        try:
            with open(p, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        r = json.loads(line)
                    except Exception:
                        continue
                    r["_file"] = str(p.relative_to(rroot))
                    records.append(r)
        except Exception:
            pass

    groups = defaultdict(list)
    for r in records:
        year = r.get("year")
        if isinstance(year, str) and year.isdigit():
            year = int(year)
        subject = r.get("subject") or infer_subject(r.get("_file", ""))
        if not isinstance(year, int) or not subject:
            continue
        subject = SUBJECT_ALIASES.get(str(subject).lower(), subject)
        source_file = r.get("source_file") or ""
        paper = r.get("paper_type") or r.get("category") or ""
        province = r.get("province") or ""
        gkey = (year, subject, source_file or f"{paper}|{province}")
        groups[gkey].append(r)

    qtype_order = {"选择题":1, "多选题":2, "填空题":3, "解答题":4, "主观题":5}
    def sortkey(r):
        rid = str(r.get("id", ""))
        nums = re.findall(r"\d+", rid)
        tail = tuple(int(x) for x in nums[-3:]) if nums else (10**9,)
        return (qtype_order.get(str(r.get("question_type","")), 50), tail, rid)

    for (year, subject, g), rows in sorted(groups.items(), key=lambda x:(x[0][0],x[0][1],x[0][2])):
        rows = sorted(rows, key=sortkey)
        paper = rows[0].get("paper_type") or "未标注卷"
        province = rows[0].get("province") or "全国_未标注"
        sf = rows[0].get("source_file") or g
        title = sanitize(Path(str(sf)).stem if sf else paper)
        d = TEXTS / str(year) / sanitize(subject)
        d.mkdir(parents=True, exist_ok=True)
        stem = f"{sanitize(province)}__{sanitize(paper)}__{title}"
        qpath = d / f"{stem}__题面.txt"
        apath = d / f"{stem}__答案解析.txt"
        head = (
            f"年份：{year}\n科目：{subject}\n卷种：{paper}\n地区：{province}\n"
            f"来源文件：{sf}\n题目记录数：{len(rows)}\n\n"
        )
        with open(qpath, "w", encoding="utf-8") as fq, open(apath, "w", encoding="utf-8") as fa:
            fq.write(head)
            fa.write(head)
            for i, r in enumerate(rows, 1):
                fq.write(f"\n===== 第 {i} 题 =====\n题型：{r.get('question_type','')}\n{r.get('question','')}\n")
                fa.write(f"\n===== 第 {i} 题 =====\n答案：{r.get('answer','')}\n解析：{r.get('analysis','')}\n")
        reconstructed.append({
            "year": year, "subject": subject, "paper": paper, "province": province,
            "source_file": sf, "count": len(rows),
            "question_file": str(qpath.relative_to(OUT)),
            "answer_file": str(apath.relative_to(OUT)),
        })

# Recent reviewed new-gaokao math corpus (2021-2026), preserved verbatim.
troot = find_root("TsubameHata-gaokao_math_corpus")
if troot:
    for subdir in ("corpus", "config", "schemas", "docs"):
        s = troot / subdir
        if s.exists():
            shutil.copytree(s, RAW_STRUCT / "TsubameHata-gaokao_math_corpus" / subdir, dirs_exist_ok=True)

# Reports.
with open(REPORT / "MANIFEST.csv", "w", encoding="utf-8-sig", newline="") as f:
    fields = ["year","subject","region","paper_type","title","format","source","source_path",
              "output_path","sha256","size","status","pdf_text_sha256"]
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(manifest)

with open(REPORT / "RECONSTRUCTED_TEXT_INDEX.csv", "w", encoding="utf-8-sig", newline="") as f:
    fields = ["year","subject","paper","province","source_file","count","question_file","answer_file"]
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(reconstructed)

with open(REPORT / "DUPLICATES_EXACT.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["sha256","kept_source","kept_path","removed_source","removed_path"])
    for h, k, d in exact_dupes:
        w.writerow([h, k["source"], k["src_path"], d["source"], d["src_path"]])

with open(REPORT / "DUPLICATES_PDF_TEXT.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["text_sha256","kept_source","kept_path","removed_source","removed_path"])
    for h, k, d in semantic_dupes:
        w.writerow([h, k["source"], k["src_path"], d["source"], d["src_path"]])

subjects = ["语文","数学","英语","物理","化学","生物","政治","历史","地理","日语","综合理综","综合文综"]
orig = Counter((m["year"], m["subject"]) for m in manifest)
rec = Counter((r["year"], r["subject"]) for r in reconstructed)
years = sorted(set([m["year"] for m in manifest] + [r["year"] for r in reconstructed]))
with open(REPORT / "COVERAGE.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year"] + [f"{s}_原版" for s in subjects] + [f"{s}_重建文本" for s in subjects])
    for y in years:
        w.writerow([y] + [orig[(y, s)] for s in subjects] + [rec[(y, s)] for s in subjects])

if qroot:
    conflict = qroot / "docs" / "candidate-duplicates.md"
    if conflict.exists():
        shutil.copy2(conflict, REPORT / "QINGSHUO_CONFLICTS_PRESERVED.md")

source_counts = Counter(m["source"] for m in manifest)
subject_counts = Counter(m["subject"] for m in manifest)
summary = {
    "input_candidates": len(candidates),
    "after_exact_sha_dedup": len(selected),
    "final_original_papers": len(manifest),
    "exact_duplicates_removed": len(exact_dupes),
    "identical_pdf_text_duplicates_removed": len(semantic_dupes),
    "reconstructed_text_groups": len(reconstructed),
    "original_by_subject": dict(sorted(subject_counts.items())),
    "original_by_source": dict(sorted(source_counts.items())),
    "year_min": min(years) if years else None,
    "year_max": max(years) if years else None,
}
(REPORT / "SUMMARY.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

readme = f"""# 中国历年高考试卷 GitHub 整理包

本包把本次公开 GitHub 来源按 **年份 → 科目** 统一整理，并执行保守去重。

## 目录

- `试卷/`：原始 PDF/DOC/DOCX 完整卷。
- `结构化重建文本/`：由 `rainewhk/gaokao` 的题目级 JSONL 按来源卷重建的题面、答案与解析；这不是原始排版扫描件。
- `结构化语料补充/`：TsubameHata 的 2021–2026 新高考数学审核语料。
- `附属资料/`：qingshuo 中的答案、解析及片段，单独存放，不混作完整试卷。
- `报告/`：完整索引、覆盖矩阵、精确重复、PDF 文本重复与保留冲突。

## 去重规则

1. **SHA-256 完全一致**：只保留一份。
2. PDF 字节不同，但 `pdftotext` 后规范化文本完全一致，且有效文本不少于 500 字符：只保留一份。
3. 仅文件名相似、或文本无法可靠提取：不自动删除。
4. qingshuo 已人工确认存在题干差异的冲突版本全部保留。
5. 不使用 OCR 猜测扫描版试卷内容。

## 来源

- qingshuo/China-Gaokao-Papers-Collection
- deekur/gaokaomath
- deekur/gaokaophysics
- Zaxaerith/GaokaoCHN
- Zaxaerith/GaokaoENG
- Zaxaerith/GaokaoGEO
- rainewhk/gaokao
- OpenLMLab/GAOKAO-Bench（rainewhk 上游，用于来源交叉，不重复拷贝）
- TsubameHata/gaokao_math_corpus

## 完整性说明

这是“公开 GitHub 来源的最大化整理”，**不能等同于教育部官方全国全科无缺口档案**。
历史年份的语文、英语、化学、生物、政治、历史、地理尤其存在公开仓库缺口。
请看 `报告/COVERAGE.csv`，其中分开统计“原版完整卷”和“结构化重建文本”。

原版完整卷：{len(manifest)}
精确重复删除：{len(exact_dupes)}
PDF 规范化文本完全一致重复删除：{len(semantic_dupes)}
结构化重建试卷组：{len(reconstructed)}
"""
(OUT / "README.md").write_text(readme, encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
