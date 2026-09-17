# 官方来源与核实记录

基线核实日：2026-09-17。此文件是检索入口和历史记录，不保证未来仍是最新。网页发布日期与核实日分列；当前无数据不能改成“没有变化”。

| ID | 来源、发布日期 | 本次访问与可支持结论 |
| --- | --- | --- |
| S1 | [Andromeda](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/)，2024-12-02 | 官方工程正文；个性化广告检索及创意规模增长，不是广告主关键词排序公式 |
| S2 | [GEM](https://engineering.fb.com/2025/11/10/ml-applications/metas-generative-ads-model-gem-the-central-brain-accelerating-ads-recommendation-ai-innovation/)，2025-11-10 | 官方正文；广告推荐基础模型及向下游模型传递学习 |
| S3 | [Adaptive Ranking Model](https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/)，2026-03-31 | 官方正文；按请求上下文调整推理，不证明某个词或固定创意数量必胜 |
| S4 | [Meta Blueprint: diversified creative](https://www.facebookblueprint.com/student/path/253130-increase-campaign-performance-with-diversified-creative)，页面未列发布日期 | 公开课程介绍可读；概念、动机、格式多样化；未声称完成登录后课程 |
| S5 | [A/B 测试简介](https://www.facebook.com/business/help/1738164643098669)，页面未列发布日期 | 网页检索遇登录墙，后由 Chrome 原生 UI 读到完整正文；互斥受众、相同预算建议、正式测试优于手动开关 |
| S6 | [A/B 测试最佳实践](https://www.facebook.com/business/help/290009911394576)，页面未列发布日期 | Chrome 原生 UI 正文核实；单变量、受众与预算、至少 7 天建议、最长 30 天、Ads Manager 可创建 1–30 天 |
| S7 | [GEM Training](https://engineering.fb.com/2026/08/03/ml-applications/training-gem-at-llm-scale-meta-ads-recommendation-foundation-model/)，2026-08-03 | 官方正文；训练效率/规模更新，不是新投放预算或 A/B 规则 |
| S8 | [Multi-stage sequence modeling](https://engineering.fb.com/2026/08/05/ml-applications/from-user-sequences-to-scaling-laws-a-multi-stage-architecture-for-metas-ads-ranking/)，2026-08-05 | 官方检索正文；GEM 中序列建模及用户行为表示，不应用来从模特外貌推断购买者属性 |
| S9 | [Google Trends 数据 FAQ](https://support.google.com/trends/answer/4365533?hl=en)，页面未列发布日期 | 官方正文；采样、0–100 归一化、低量/噪声；7 天及以内使用浏览器/设备本地时区 |
| S10 | [搜索词与主题区别](https://support.google.com/trends/answer/17309543)，页面未列发布日期 | 官方正文；词面查询与跨语言主题不能混作一个比较口径 |

## 每次需要按当前情况核实的入口

- [Meta Ad Library](https://www.facebook.com/ads/library/)：可见样本与字段按当时界面记录。
- [广告指南](https://www.facebook.com/business/ads-guide)：版位、字符建议、裁切与呈现；本基线未逐版位验证。
- [隐私与个人属性广告规范](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/)：本次网页返回 429，未把全文标记为已核实；发布广告前核实当前正文。
- [创意多样性文章](https://www.facebook.com/business/news/demystifying-creative-diversification)：本次检索遇登录墙；使用 S4 支持多样性原则，不借第三方转述伪装读过该文。

## 与实操的连接

建议图像、商品、场景与文案保持明确一致，开发不同购买动机的创意，然后以单变量实验验证。此为依据官方系统方向形成的策略建议，不是官方保证，也不是“2026 算法破解公式”。不引用平台整体性能提升数字当成本品牌预期 ROAS。
