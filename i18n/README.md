# 多语言翻译｜Translations

[简体中文](../README.md) · [English](en/README.md) · [日本語](ja/README.md) · [한국어](ko/README.md) · [繁體中文](zh-Hant/README.md)

本目录保存 MJ 宇宙设定集的各语言版本。中文（简体）是源语言，译文与中文条目一一对应；出现版本差异时以中文条目和[来源记录](../sources/README.md)为准。

This directory hosts the translated editions of the MJ Universe Wiki. Simplified Chinese is the source language. Every translated page mirrors a Chinese page; when versions differ, the Chinese page and its [source records](../sources/README.md) take precedence.

## 语言版本

| 语言 | 入口 | 说明 |
| --- | --- | --- |
| 简体中文（源语言） | [README](../README.md) | 全部条目 |
| English | [README](en/README.md) | 全量镜像 |
| 日本語 | [README](ja/README.md) | 全量ミラー |
| 한국어 | [README](ko/README.md) | 전체 번역 |
| 繁體中文 | [README](zh-Hant/README.md) | 全量鏡像 |

## 翻译原则

1. **不改设定**：译文只做语言转换，不新增、不删减、不把“待核对”写成确定事实。
2. **证据标签保留**：片内设定、作者补充、评论共创、整理推断、原创扩写、待核对等标签逐条保留。
3. **专名统一**：人物名、亲属姓名、宇宙名和模式名以[术语表](GLOSSARY.md)为准；二创姓名保留汉字并附读音或直译。
4. **来源链接直达原文**：`sources/` 下的原片与评论链接在各语言版本中保持不变，并链接回中文来源记录。
5. **版本同步**：中文条目更新后，对应译文在同一个 PR 内跟进；无法同步时在译文顶部标注“基于某次提交”。

## 覆盖状态

| 条目 | English | 日本語 | 한국어 | 繁體中文 |
| --- | --- | --- | --- | --- |
| 主 README | ✅ | ✅ | ✅ | ✅ |
| CONTRIBUTING | ✅ | ✅ | ✅ | ✅ |
| ATTRIBUTION | ✅ | ✅ | ✅ | ✅ |
| 五个目录索引 | ✅ | ✅ | ✅ | ✅ |
| characters/ 人物档案 | 15 / 21 篇 | 索引（详细条目链中文） | 索引（详细条目链中文） | 索引（详细条目链中文） |
| universes/ 宇宙与模式 | 索引 | 索引 | 索引 | 索引 |
| relationships/ · memes/ | 索引 | 索引 | 索引 | 索引 |
| sources/ 来源记录 | 索引 | 索引 | 索引 | 索引 |
| templates/ · docs/ | 中文 | 中文 | 中文 | 中文 |

**翻译基线**：译文基于 `main` 提交 `186901c`（2026-11-11）的条目内容。上游新增的图片规范、6 份人物档案（贾维斯、命运博士、尼克·弗瑞、洛基、超人、卡魔拉）、`docs/MJ_HISTORY.md` 与 R28–R39 来源记录，当前以中文原文链接接入；按「主 README → 目录索引 → 人物档案 → 宇宙与模式 → 来源记录 → 模板与调研笔记」的顺序分批补齐，并同步更新本表。

## 怎样参与翻译

- 新增语言：在 `i18n/` 下新建语言目录，先翻译 README、CONTRIBUTING 与五个索引，再逐篇补条目。
- 修订译文：直接改对应语言的文件；涉及设定含义时同时在 PR 说明中引用中文原文。
- 运行检查：`python3 scripts/check_docs.py`，链接与索引必须通过。
- 术语有争议时先改[术语表](GLOSSARY.md)，再统一替换，不在各语言文件里各自造词。

翻译贡献同样按 [CC BY-SA 4.0](../LICENSE) 共享，署名方式见[署名说明](../ATTRIBUTION.md)。
