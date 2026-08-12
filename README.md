# 造次 Zaoci · 游戏皮肤工作台

品牌设计组「风格技能 → 成套小游戏 UI 设计方案」的可视化编排器。三栏布局：左（输入 & 参数）/ 中（6 格出图画布）/ 右（Agent 分析）。

> 在线 demo 打开即带一套「蓝发金克丝 × 街头二次元可爱风 · 海岛探宝」的真图 + 真分析数据，展示"跑通后长什么样"。

---

## 这是纯前端（当前状态）

整个站点是**静态资源**，可直接托管到 Vercel / 任意静态服务器。前端负责三件事：

1. **输入**：上传 3 类参考图、填主题/风格/比例/角色一致性等参数。
2. **攒 job**：点「生成」把所有输入收敛成一份 `job.json`（见下方契约）。
3. **展示**：读 `outputs/` 里的真图和真分析并渲染画布 + 右栏。

前端**不会**、也**不能**自己真出图、真取色、真写世界观 —— 那是模型能力，不在浏览器里。

## 前端已留好的后端插口（给开发）

前端所有对后端的调用都是 `fetch('/api/...')`，**失败时自动降级读静态文件**，所以：
- 纯静态部署（无后端）：`/api/*` 全部 404 → 自动回落读 `outputs/*.json`，demo 数据正常显示。
- 开发接后端：实现下面 3 个接口即可，**前端一行不用改**。

| 接口 | 方法 | 作用 | 降级行为（无此接口时） |
|------|------|------|------------------------|
| `/api/save-job` | POST | 接收前端攒好的 `job.json`，触发后端真调三谦出图 + 真分析 | 前端改为**下载 job.json**，人工交 agent 代跑 |
| `/api/outputs` | GET | 返回 `{ cells:{login,level,battle,result,components}, ref_hero, style_id }`，画布据此贴真图 | 降级读 `outputs/manifest.json` |
| `/api/analysis` | GET | 返回品牌色系 / 关键词分析 / 世界观（见 `outputs/analysis.json` schema） | 降级读 `outputs/analysis.json` |

### `job.json` 出参契约（前端点「生成」产出）

```jsonc
{
  "theme": "海岛探宝",
  "mascot": "蓝发朋克少女金克丝",
  "ratio": "16:9",
  "style_id": "street-anime-kawaii",
  "refRoles": {
    "color_dna": { "count": 1, "use": "提取配色 + 品牌 DNA" },
    "graphic":   { "count": 1, "use": "参考图形元素" },
    "play":      { "count": 1, "use": "参考玩法" }
  },
  "analysis_todo": ["brand_palette", "keywords", "worldview"],
  "cells": ["login", "level", "battle", "result", "components"]
}
```

### `outputs/analysis.json` schema（后端真分析回填格式）

```jsonc
{
  "palette":  { "source": "...", "groups": [ { "type": "主色", "colors": [ { "name": "潮汐天蓝", "hex": "#26A0DC", "use": "主角识别色/主视觉" } ] } ] },
  "keywords": { "refs": [ { "label": "① 配色 & 品牌 DNA 参考", "features": ["..."], "application": "..." } ], "summary": "..." },
  "worldview":{ "plans": [ { "name": "潮汐藏珍·逐浪寻宝家", "concept": "...", "visual": "...", "symbol": "...", "slogan": "...", "values": ["..."], "recommend": true } ] }
}
```

## 出图/分析真实闭环（当前无后端时）

1. 设计师在页面上传参考图、填参数、点「生成」→ 下载 `job.json`。
2. 把 `job.json`（含参考图）交给 agent，agent 真调三谦 MCP 出图 + 真看图取色/写世界观。
3. agent 把结果写回 `outputs/`（图片 + `manifest.json` + `analysis.json`）。
4. 刷新页面 → 画布贴真图、右栏显示真分析。

开发把第 2、3 步换成 `/api/save-job` 后端后，即变成网页内点一下自动闭环。

## 目录结构

```
index.html            主体工程（三栏工作台，全部前端逻辑内联）
vercel.json           静态托管配置
outputs/              agent 回填的真图 + manifest.json + analysis.json（demo 数据）
skills/               风格技能包（index.json + 各风格 tokens/style/meta）
server.py             本地开发用的极简后端（Vercel 部署用不到，留作后端参考）
jobs/                 本地 server 存 job 的目录（部署可忽略）
```

## 本地跑（可选，带后端体验完整闭环）

```bash
python3 server.py       # 起本地后端，支持 /api/save-job 存 job
# 浏览器打开 http://localhost:8800
```
