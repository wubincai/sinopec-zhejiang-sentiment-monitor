#!/usr/bin/env python3
"""生成一轮中国石化浙江石油舆情监控的搜索词组合。

只生成查询词，不做爬取、不发请求。
用法：python3 queries.py
"""
subjects = ["中国石化浙江石油", "浙江石油"]
groups = {
    "A 安全质量": ["漏油 爆炸 起火 事故", "油品质量 不合格 掺水", "缺斤少两 计量作弊"],
    "B 服务投诉": ["投诉 维权 12315", "加油站 服务差 退款"],
    "C 价格政策": ["涨价 优惠取消", "断供 缺油 价格欺诈"],
    "D 经营合规": ["立案 处罚 通报", "停业整顿 环保处罚"],
}
for s in subjects:
    print(f"主体单独查: {s}")
for name, terms in groups.items():
    for t in terms:
        print(f"{name}: 中国石化浙江石油 {t}")
