#!/usr/bin/env python3
"""Six more Tencent Android titles. Reuse tested selective remote ZIP extraction."""
import ace_range_from_tencent_apks as ace
ace.SOURCES.update({
  "arena":("暗区突围","com.tencent.mf.uam","1.0.167.167","91AEDB7C1EF4046D1D42FF3B7CEE19FD",2083295477),
  "cod":("使命召唤手游","com.tencent.tmgp.cod","1.9.57","E8742B35B8EEECC854B69FD9D5D3BB46",1982730752),
  "lolm":("英雄联盟手游","com.tencent.lolm","7.3.0.2813","9F1AF63FE4EE58D81DEC802FDC032FEC",1755288344),
  "speed":("QQ飞车手游","com.tencent.tmgp.speedmobile","1.59.0.56365","32383943BD993E08F17C71152FE44C1A",2117190715),
  "jcc":("金铲铲之战","com.tencent.jkchess","1.14.35","B19C1357C5A44ADC09CEB1C58A9148EC",1819837872),
  "codev":("无畏契约手游：源能行动","com.tencent.tmgp.codev","1.25.0","1C21E6BD5F10CF77187FED25334CA731",2010248248)
})
if __name__=="__main__": ace.main()
