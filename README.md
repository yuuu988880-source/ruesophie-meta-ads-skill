# Rue Sophie · Meta 素材测试 Skill

从整套穿搭图片生成有品牌依据的图片文案、广告标题、受众假设和 A/B 测试方案；支持按调用时点核查官方规则、当周趋势及测试复盘。中文工作流，广告语言按市场切换。

## 调用

安装后上传 look 图片，输入：

```text
$ruesophie-meta-ads 根据这套 look 生成品牌文案、广告 title、当周关键词建议和单变量 A/B 测试。
```

完整指令与不依赖 Skills 的主 Prompt：[调用指令](prompts/调用指令.md)。

## 安装

将仓库中的 `skills/ruesophie-meta-ads` 目录放入你的个人 Skills 目录（通常是 `~/.codex/skills/`，自定义环境使用 `$CODEX_HOME/skills/`）。不要覆盖已有品牌配置。若当前会话未显示新技能，在新任务中调用；也可直接要求助手读取所安装目录中的 `SKILL.md`。

复制 `references/brand.example.md` 为 `references/brand.local.md`，填入自己的已确认品牌信息。仓库提供的是公开流程和模板；内部手册、logo、原始照片及 Rue Sophie 专用内部配置不包含在发布内容中。

当前使用者的本地安装可拥有专用配置，公开仓库不声称拥有或转授权品牌原始素材。MIT 许可证只覆盖本仓库新增的 Skill、Prompt 与辅助代码，不授予商标、第三方素材或非公开品牌资料权利。

## 输出

- 逐 look 的可见证据、场景及 2–3 个可验证受众假设。
- 有实质区别的创意方向与完整 Meta 文案字段。
- 只改变一个字段的 A/B 对，及固定设置、主指标、周期和判定规则。
- 分来源的关键词信号：账户表现、广告库样本、搜索代理指标、待验证候选。
- 真实报表复盘；证据不足时明确“无结论”。

## 数据与工具

本 Skill 是助手工作指令，不是持有 Meta 私有数据的 API 产品。图片识别需要视觉工具；实时查询需要网络/浏览器，用户指定 Chrome 时优先用 Chrome；账户报告需要用户已授权的访问或聚合导出。不要求安装第三方付费服务，不内置 token，不自动投放/花费，也不会后台自动每周运行。

未取得可验证数据时不会伪造“Meta 服装 Top 关键词榜”。Google Trends 的相对热度不等于 Meta 转化，Ad Library 的久投广告不等于盈利赢家。衣服照片支持风格/场景假设，不支持精准收入或职业识别。

## 维护

[官方核实记录](skills/ruesophie-meta-ads/references/sources.md) 当前基线为 2026-09-17，涵盖截至 2026 年 8 月已检索到的相关 Meta 工程更新；每次“最新”请求仍需重新查证。A/B 文档也要核实当前账户支持情况。

本地素材和配置受 `.gitignore` 排除。发布时采用明确文件清单，不使用强制添加本地配置。更新公开 Skill 后保留原有 `brand.local.md`。

## 验证

`python3 skills/ruesophie-meta-ads/scripts/check_ab_pair.py examples/ab-pair.json` 可检查两组已列字段是否只改变声明变量，并统计文案长度。它不证明真实投放设置、品牌合规或实验显著性。无第三方运行依赖。

[行为验收案例](evals/cases.md) 提供后续回归任务；这些案例不是已完成真实投放或独立模型测评的声明。
