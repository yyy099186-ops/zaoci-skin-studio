# 街头二次元可爱风 · 风格指南（Street Anime Kawaii）

> 青春清爽的街头二次元：**白底 + 明亮撞色**（天蓝/薄荷/荧光黄绿/珊瑚橙），软贴纸 + 大眼萌角色。
> **核心铁律：可爱不靠粉，靠明亮通透。** 机读风格包见同目录 `tokens.json` / `style.json` / `meta.json`。

## 一、配色（从《COLOR神明》参考图实取，占比锁死）
| 角色 | 名称 | HEX | 占比 |
|---|---|---|---|
| dominant | 白 + 浅天蓝渐变底 | `#FFFFFF` `#8FD4F5`→`#C4EBFB` | ~50% |
| secondary | 薄荷青 + 珊瑚橙 明快撞色 | `#7FD9C4` `#3DD6D0` `#FF7A5C` `#FF8534` | ~40% |
| accent | 荧光黄绿（只点关键：确认键/勾选/星星） | `#D4FF3F` | ≤10% |
| 角色发色 | 香芋紫（非界面主色） | `#B4A0E8` | 角色 |
| 点缀 | 蜜桃粉（**仅极少量，不主导**） | `#FFB3C7` | 极少 |
| coin | 奶黄杏 | `#FDE0A0` | 点缀 |

## 二、⚠️ 最大的坑：可爱 ≠ 粉
参考图《COLOR神明》的可爱感来自**白底 + 天蓝薄荷荧光绿的明亮通透撞色**，粉只是极少点缀。
**别一想"可爱"就往粉里堆**（这是踩过的坑，Prompt 必须写 `NOT pink-dominated`）。

## 三、AI 出图关键词（喂三谦 gpt-image-2）
**正向**：`street anime kawaii, cute chibi anime character big eyes, bright airy candy colors, sky-blue mint-green acid-lime coral-orange palette, white base, halftone dots, sticker cutout white outline, stars smiley doodles COOL HOT tags, clean bright background, cheerful youthful, NOT pink-dominated`

**负向**：`not dark, not muted, not edgy, NOT pink-heavy, no saccharine pastel pink, no gritty graffiti wall, no dense clutter, not adult, no somber mood, no 3D render, no gloomy, no low-contrast dim`

## 四、角色 / 背景 / 母题
- **角色**：大眼 Q 感 · 圆润软萌（chibi 倾向），发色可用香芋紫/薄荷等亮色，白贴纸描边 + 投影拉景深
- **背景**：明亮纯净 / 柔和渐变（浅天蓝、薄荷青、奶黄），干净、留白、**浅半调（透明度~0.12）铺底**，角色与背景明度拉开
- **母题**：圆润软贴纸、星星、笑脸、圆点、箭头、涂鸦手写字（COOL/HOT/NEW）、滴落液体感顶栏

## 五、字体
中文粗圆体（Baloo 感）+ 白描边 + 浅蓝软投影 + 微倾斜；正文粗体深灰字；强调用荧光绿或橙底白字块。

## 六、适用玩法
休闲 · 消除 · 养成 · 潮流少年少女向。

## 七、界面清单（成套出图）
通用 5 件：主菜单 / 关卡地图 / 核心玩法 / 商店抽卡 / 结算胜利。竖屏 9:16，gpt-image-2 / 2K / high。
（已验证锚点：闯关游戏 4 界面 主菜单/关卡地图/闯关对战/胜利结算）

## 八、三谦出图流程（要点）
1. `get_3000_app_list` 拿 app_id（设计用 105）
2. `3000_generate_image`（model=gpt-image-2, quality=high, image_size=2K, aspect_ratio=9:16），共享风格包写进每张 Prompt
3. `3000_query_generate_async_task_result` 轮询；出图约 1-2 分钟
4. 偶发 pending 超 5 分钟 = 卡任务，**原样重提**即可
5. 若给参考图 → 图生图：先 `3000_get_upload_token` 上传拿 inner_url，生图带 `image=[inner_url]` + `input_fidelity=high`
