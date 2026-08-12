# 符文之境魔幻史诗像素风 · 风格指南

> 一句话：**符文之地魔幻史诗风（西方高幻想）× 像素渲染层**——以「宝石青蓝符文光 × 深海蓝黑冷石基底 × 烫金封套」构成的高幻想小游戏 UI，气质是"克制的史诗华丽"。
> 本风格是**组合技产物**：DNA 层继承自英雄联盟符文之地的设计语言，渲染层换成像素。锚点：LoL: Wild Rift 界面（DNA 底座）；游戏本体《符文之境 RUNE REALM》。
> **模型路由：像素风必走 nano pro（gemini-3-pro-image-preview）**，gpt-image-2 出像素会糊。

## 1. 配色表（角色 / 名称 / HEX / 占比）
| 角色 | 名称 | HEX | 占比 |
|---|---|---|---|
| dominant | 深海军蓝 | `#0E1E2E` `#16283A` | ~55% |
| dominant | 冷石灰岩灰 | `#3E4A52` | ~15% |
| secondary | 符文宝石青蓝 | `#2FB6E8` `#5FD4F5` | ~15% |
| accent | 烫金 / 暖金 | `#C8A24A` `#E8C874` | **≤8%** |
| accent | 紫水晶魔法 | `#8A5BC8` | ~3% |
| accent | 草木绿（仅场景） | `#6FBF7A` | ~4% |

> ⚠️ **强调色不篡位**：青蓝最抢眼但真正铺面的是深蓝黑；金色是"点睛"不是"铺面"，压到 8% 以内。绝不满屏金/满屏青。

## 2. 三大标志物（抓住能还原 80%）
1. **宝石青蓝发光符文环 / 传送门**（外辉光，像素用 dithered halo + halftone 抖动做，不用高斯模糊）
2. **烫金厚描边纹章封套**（段位卷轴 / 翼章 / 按钮镶边——金只点关键）
3. **深海蓝黑 × 冷石灰岩基底 + 电影级景深**（暗、冷、克制、有距离感）

## 3. AI 关键词
**正向**：crisp medium pixel art, cel-shading outlines, Runeterra high-fantasy, epic cold mysterious noble restrained-luxury, gemstone rune cyan glow, forged-metal + natural-rock, cinematic cold dark lighting + cyan fill + gold rim, dithered pixel glow
**负向**：8-bit retro / tiny sprite / minecraft voxel / smooth painterly / 3d render / blurry mushy pixels / gold flooding / **double image / ghosting text / mixed-color lit stars / duplicated rune rings / plain rounded rectangle button / flat-edge rectangle button**
**竖版必带**：NO phone mockup / device frame / bezel / screen border

## 4. 角色 / 背景 / 母题
- **角色（关键铁律）**：给了参考图必须**图生图锁角色**（image=inner_url + input_fidelity=high + do not redesign），**默认取参考图最中心角色**当主角，逐张复用同一 inner_url + 写死特征清单。绝不用文字编角色。本 case 主角=盖伦（深蓝银白金边甲 / 无披风 / 络腮胡 / 巨剑）。
- **主角色分配**：不是每张都堆主角。**关卡地图/选关页做无人纯地景+建筑地标**；主角集中在首页/战斗/结算。
- **背景**：深蓝黑冷石基底，克制不花，让主体和 UI 跳出来；有主角处拉景深压暗背景。
- **母题**：符文能量环、烫金纹章封套、六边形/菱形能量宝石、峡谷建筑地标（法师塔/城堡/罗马柱/传送门遗迹）、光柱光束。**同一母题一个界面只出现一次**（如符文环别叠两圈）。

## 5. 字体
- 中文标题：像素金渐变浮雕 + **单层**深色描边 + 青色外发光；英文副标 = 金色衬线，字距拉开，高度 ≈ 中文 1/3。
- 正文：像素体浅色 `#EAF2FA`；数字/强调：青色 `#2FB6E8` 带柔光；危险标签：`#E24B4A`。
- ⚠️ 标题字务必**单层干净**，防重影/穿帮，逐字核对防 typo。

## 6. 适用玩法
闯关小游戏 / 动作割草 / roguelike / 卡牌养成 / 塔防 / RPG 冒险。

## 7. 界面清单（成套出图，本案 6 件）
游戏首页(Logo+开始游戏) / 关卡地图(无人建筑地景) / 核心战斗(主角放符文能量打怪) / 通关结算(胜利+星级+奖励) / 商店(道具卡+抽卡) / 主菜单大厅(可选)。
**UI 组件全套统一**：主按钮=chamfer 六边形+菱形端帽（保留 LoL 几何 DNA，**统一 ≠ 简化成圆角矩形**）；关卡节点/资源 pill/道具格/HP条/头像框全 chamfer 切角。

## 8. 三谦出图流程要点
1. `get_3000_app_list` → app_id=105
2. 有角色参考图：先 `3000_get_upload_token` → base64 POST uploadMaterial 拿 inner_url
3. `3000_generate_image`：**model_name=gemini-3-pro-image-preview**（nano pro）/ 9:16 / 2K；有角色则带 `image=[inner_url]` + `input_fidelity=high`
4. prompt = style.json 的 unified_component_spec + art_direction + color_instruction + character_lock + negative_prompt 拼成共享包 + 本界面内容
5. 提交后 sleep 90s 轮询；超 5 分钟 pending 原样重提
6. 下载校验尺寸（1536×2752）→ **人眼验收 6 项 bug**：角色一致/按钮 chamfer/文字无重影/星星同色/符文环不重叠/金不泛滥

## 9. 锚点样张
`references/samples/` 存《符文之境》定稿 6 张 + 盖伦角色参考图，作为一致性锚点。
