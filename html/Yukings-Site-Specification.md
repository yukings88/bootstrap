# Yukings 独立站全站设计规范 (Site-Wide Design Specification)

> **版本**: v1.0 · 2026-06-15
> **维护方**: Yukings · Shenzhen Yukings Industrial Co., Ltd.
> **适用范围**: www.yukings.net 全部静态页面 (7 个 HTML)
> **品牌定位**: 工业 B2B 出口型网站 · 欧美高端风格

---

## 1. 品牌基础信息

| 项目 | 详情 |
|---|---|
| 品牌名 (中) | 双禹王 |
| 品牌名 (英) | **Yukings** |
| 域名 | www.yukings.net |
| 主体公司 | Shenzhen Yukings Industrial Co., Ltd. |
| 成立时间 | 2006 |
| 主营品类 | Noise Barrier / Sound Barrier / Acoustic Barrier |
| 业务模式 | Manufacturer · OEM · ODM · Wholesale |

**核心联系方式** (全站统一，禁止改写)

| 角色 | 渠道 | 联系方式 |
|---|---|---|
| 总机 Tel | — | +86-755-86366707 |
| 邮箱 E-mail | — | weilai04525@163.com |
| 国际销售经理 | Miss Tang | +86 17727812004 (WeChat/WhatsApp) |
| 技术方案工程师 | MR. Yu | +86 13828819804 (WeChat/WhatsApp) |
| 公司地址 | — | Room 1405, Building B2, Yunzhi Tech Park, Guangming District, Shenzhen, Guangdong, China |

---

## 2. 全局 CSS 变量 (Design Tokens)

```css
:root {
  /* 主色系 (深蓝主调) */
  --blue: #082457;
  --blue-light: #0d3a8a;
  --blue-dark: #051a3e;

  /* 强调色 (橙红点缀) */
  --orange: #E4662A;
  --orange-light: #f28a55;
  --orange-dark: #c04e18;

  /* 中性色 */
  --white: #ffffff;
  --gray-50: #f8f9fb;
  --gray-100: #eef1f6;
  --gray-200: #d8dde8;
  --gray-300: #b4bcd0;
  --gray-500: #6b7a94;
  --gray-700: #3d4f6a;
  --text-primary: #1a1a2e;
  --text-secondary: #4a5568;

  /* 阴影层级 */
  --shadow-sm: 0 1px 3px rgba(8, 36, 87, .08);
  --shadow-md: 0 4px 16px rgba(8, 36, 87, .10);
  --shadow-lg: 0 8px 32px rgba(8, 36, 87, .12);

  /* 形状 */
  --radius: 6px;
  --radius-lg: 12px;

  /* 布局 */
  --max-width: 1200px;
}
```

**字体栈 (全站统一)**

```css
font-family: 'Archivo', 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
```

---

## 3. 命名规范 (BEM · rsb- 前缀)

所有 class 必须以 `rsb-` 开头，采用 BEM 命名法:

```html
<!-- Block -->
<div class="rsb-card">...</div>

<!-- Block + Element -->
<div class="rsb-card__title">...</div>

<!-- Block + Modifier -->
<button class="rsb-btn rsb-btn--primary">...</button>
```

**不允许出现**: `mt-3`、`btn-blue`、未加 `rsb-` 前缀的样式类。

---

## 4. 排版系统

| 用途 | 字号 | 字重 | 行高 | 颜色 |
|---|---|---|---|---|
| H1 (Hero) | 60-64px | 800 | 1.05-1.1 | var(--white) / var(--text-primary) |
| H2 (Section) | 38-42px | 700 | 1.15 | var(--text-primary) |
| H3 (Sub) | 18-22px | 700 | 1.3 | var(--text-primary) |
| Body | 15-16.5px | 400 | 1.6-1.7 | var(--text-secondary) |
| Small | 13-14px | 500 | 1.5 | var(--gray-500) |
| Eyebrow | 12-12.5px | 700 | 1 | var(--orange) · letter-spacing: 2.4px · uppercase |

**强调用法**:
- H1 中以 `<span>` 包裹品牌调性词 (italic, var(--orange-light))
- 关键词 (产品名) 用 `<strong>` 加粗, 每页 3-5 处

---

## 5. 间距与栅格

**Section 内边距 (默认)**:
- 桌面 (≥1024px): `96px 0`
- 平板 (768-1023px): `72px 0`
- 手机 (≤480px): `60px 0` / `48px 0`

**卡片内边距**: 桌面 `24px` / 移动 `20px`
**按钮内边距**: 默认 `14px 32px` · sm `9px 20px` · lg `16px 38px`

**栅格断点**:
| 断点 | 列数 | 备注 |
|---|---|---|
| ≥1024px | 3 / 2 / 4 列 | 桌面 |
| 768-1023px | 2 / 1 列 | 平板 |
| ≤480px | 1 列 | 手机 |

**容器最大宽度**: `1200px` · 居中 · 左右 `padding: 0 24px`

---

## 6. 组件库

### 6.1 按钮 (Button)

```html
<button class="rsb-btn rsb-btn--primary">Get a Quote</button>
<button class="rsb-btn rsb-btn--blue">View Details</button>
<button class="rsb-btn rsb-btn--ghost">Learn More</button>
```

| 变体 | 用途 | 默认 → Hover |
|---|---|---|
| `--primary` | 主 CTA · 强调 | var(--orange) → var(--orange-dark) + translateY(-2px) + 橙色阴影 |
| `--blue` | 次要 CTA · 品牌色 | var(--blue) → var(--blue-light) + translateY(-2px) + 蓝色阴影 |
| `--ghost` | 第三级 · 浅色背景场景 | 透明白边 → 反色 |

**通用交互**: 全部按钮 hover 时 `transform: translateY(-2px)`，颜色变深 + 阴影加深。

### 6.2 分割线 (Divider)

```html
<div class="rsb-divider"></div>
```

```css
.rsb-divider {
  width: 50px;
  height: 3px;
  background: var(--orange);
  margin: 14px 0 22px;
  border-radius: 2px;
}
```

**强制规范**: 每页 H1/H2 下方必须有 1 条 `rsb-divider`。

### 6.3 顶部导航 (Top Bar)

```html
<div class="rsb-topbar">
  <div class="rsb-container rsb-topbar__inner">
    <div class="rsb-topbar__links">电话 / 邮箱 / 工时</div>
    <div class="rsb-topbar__links">Ship to / EN 切换</div>
  </div>
</div>
```

- 背景: `var(--blue-dark)`
- 字号: `13px`
- 左: 总机+邮箱+工时
- 右: Ship to + EN/中切换

### 6.4 Header 主导航

7 项固定入口 (顺序强制):
1. Home · `/`
2. Products · `/products.html`
3. Solutions · `/solutions.html`
4. Projects · `/projects.html`
5. Blog · `/blog.html`
6. About · `/about.html`
7. Contact · `/contact.html`

右侧: `Get a Quote` 主按钮 (rsb-btn--primary rsb-btn--sm)

### 6.5 面包屑 (Breadcrumb)

强制每页内嵌 `<header>` 之后:
- Home / 当前页面 (2 段)
- 配色: 灰底 `var(--gray-50)`, 末级 `var(--orange)`

### 6.6 Hero 区

- 桌面 `min-height: 480-600px`
- 背景图: 全屏图 + `linear-gradient(105deg, rgba(5,26,62,.96) 0%, ...)` 蒙版
- 动画: `rsbPan 24s ease-in-out infinite alternate` (scale 1.05 → 1.08 + translateX)
- 必含元素: Eyebrow 标签 · H1 · lede 段 · 主+次按钮 · 可选 Meta 数据条

### 6.7 卡片 (Card)

- 圆角: `var(--radius-lg)` (12px)
- 阴影: 默认 `var(--shadow-md)`, hover `var(--shadow-lg)`
- hover: `translateY(-2px ~ -4px)` + 图片缩放 1.05
- 边框: `1px solid var(--gray-200)` (默认) → `var(--orange-light)` (hover)

### 6.8 Footer

- 背景: `var(--blue-dark)`
- 4 列布局: 品牌简介 / Products / Solutions / Company
- 底部条: 版权 + Privacy/Terms/Sitemap
- 社交图标: LinkedIn / Facebook / YouTube (inline SVG 或文字缩写)

---

## 7. 页面架构清单

| URL | 页面 | 主核心关键词 | 关键词密度 |
|---|---|---|---|
| `/index.html` | 首页 | noise barrier manufacturer | ~3% |
| `/products.html` | 产品中心 | noise barrier | ~2.5% |
| `/solutions.html` | 解决方案 | noise barrier solutions | ~3% |
| `/projects.html` | 工程案例 | noise barrier projects | ~3% |
| `/blog.html` | 博客 | noise barrier blog | ~2% |
| `/about.html` | 关于我们 | noise barrier manufacturer | ~2% |
| `/contact.html` | 联系我们 | noise barrier quote | ~2% |

**通用页面骨架** (按需增删模块):
1. Top Bar
2. Header (sticky)
3. Breadcrumb
4. Hero (大标题 + 主图 + CTA)
5. 主体内容 (动态组合: 编辑式图文 / 时间线 / 规格表 / 案例网格 / FAQ / 团队)
6. CTA 区
7. Footer

---

## 8. SEO 关键词分层 (Yukings 词库)

### 一级核心词根 (1-3 个)
- `noise barrier` / `sound barrier` / `acoustic barrier`

### 材质二级词
- `galvanized steel noise barrier` / `aluminum sound barrier` / `concrete acoustic barrier` / `PC transparent noise barrier`

### 应用场景三级词
- `highway noise barrier` / `railway noise barrier` / `industrial plant acoustic barrier` / `residential noise barrier` / `solar noise barrier`

### 商贸转化词
- `manufacturer` / `supplier` / `custom made` / `OEM` / `wholesale` / `factory`

### 地域长尾词 (GEO)
- `USA noise barrier` / `Canada sound barrier` / `Germany acoustic barrier` / `UK noise barrier` / `Australia sound barrier` / `Southeast Asia noise barrier`

**每页布局规则**:
- 唯一 1 个 H1，必须含主核心词
- H2/H3 自然穿插主词 + 变体词
- 正文每段第一句植入 URL 词根
- 内链锚文本: 优先用产品关键词
- 图片 alt: 必填，格式 `关键词+使用场景`
- 关键词密度: 2%~3%，单页不堆砌

---

## 9. TDK 谷歌收录规范

### Title (≤60 字符)
```
{主核心词}+{1-2个变体词} | Yukings Manufacturer
```
示例: `Railway Noise Barriers | OEM Sound Barrier Manufacturer | Yukings`

### Meta Description (120-155 字符)
```
{主关键词}+{1个长尾}+{工厂优势: CE / ISO9001 / OEM / 24h reply}
```
**禁止**: 关键词堆砌、emoji、中式英语

### hreflang / canonical
每页必须有:
```html
<link rel="canonical" href="https://www.yukings.net/{page}.html">
<link rel="alternate" hreflang="en" href="...">
<link rel="alternate" hreflang="x-default" href="...">
```

### OG / Twitter Card
每个页面必填 `og:title / og:description / og:url / og:image / og:type` + `twitter:card / twitter:title / twitter:description`。

---

## 10. EEAT 权威评分落地

### 资质 (E)
- CE 认证 / ISO 9001:2015 / 国标 GB / 美标 ASTM / 德标 DIN
- 公制 + 英制双单位 (例: `42000 m² / 452,084 sq.ft`)

### 经验 (E)
- 2006 至今, 18+ 年制造经验
- 3.6 M m² 累计交付
- 60+ 出口国别

### 权威 (A)
- 真实工程项目引用 (US / EU / AUS / ASEAN / MENA)
- 第三方检测报告 (EN 14388, ASTM E90, GB/T 19889)

### 信任 (T)
- 公司全名 + 完整地址 + 4 渠道联系方式
- 团队人物 (MR. Yu / Miss Tang) 介绍

---

## 11. JSON-LD 结构化数据 (按页面)

**全站共用 (7 页必备)**:
- `Organization`
- `BreadcrumbList`

**按页补充**:
| 页面 | 必含 Schema |
|---|---|
| Home | + WebSite + FAQPage |
| Products | + ItemList + Product |
| Solutions | + FAQPage |
| Projects | + ItemList (5 案例) + FAQPage |
| Blog | + Blog (9 篇 blogPosting) + FAQPage |
| About | + FAQPage |
| Contact | + ContactPage + FAQPage |

---

## 12. 响应式断点 (强制)

```css
/* 平板 */
@media (max-width: 1024px) { ... }

/* 大手机 */
@media (max-width: 768px) { ... }

/* 小手机 */
@media (max-width: 480px) { ... }
```

**断点行为**:
- 1024: 4 列 → 2 列, 字体缩小 20-30%
- 768: 隐藏 topbar 部分链接, 汉堡菜单出现
- 480: 单列布局, 按钮全宽, 内边距收紧

---

## 13. 动效规范

| 动效类型 | 实现 | 用途 |
|---|---|---|
| `rsbPan` | 24s alternate, scale 1.05→1.08 + translateX | Hero 背景 |
| `rsbPulse` | 2s ease-in-out, opacity 1→.4 | 在线状态圆点 |
| Card hover | translateY(-2/-4px) + 阴影加深 | 全部卡片/按钮 |
| Image hover | transform: scale(1.05), 600ms | 全部图片 |
| Sticky 子导航 | top: 80px, z-index: 30 | 长页面 (solutions/projects) |

**禁止**: 旋转、闪烁、视差过深、3D 倾斜

---

## 14. 内容撰写标准

### FAQ 风格
- 全部使用海外采购原声英文 (避免中式英语)
- 主题: MOQ / 报价 / 质保 / 安装 / 海运 / 认证 / 定制
- 每条 1-3 句, 数字+具体场景

### 文案口吻
- 第二人称 (you/your), 偶尔用 we/our
- 强数据支撑 (例: `15-25 working days`, `8-12 dB(A)`)
- 主动语态, 短句为主
- 避免: 夸张形容词 (revolutionary / cutting-edge) · 套话 · 自我吹捧

### 内链策略
- 正文自然植入 3-5 个同站相关栏目锚文本
- 锚文本使用产品关键词 (例: "railway noise barrier" → `/products.html`)

---

## 15. 图片规范

- Banner 默认尺寸: `1920×520`, 格式 WebP
- 全站 img 必填: `alt` / `width` / `height` / `loading`
- alt 模板: `{主关键词} {材质} {使用场景}`
- 示例: `alt="Galvanized steel noise barrier wall along urban highway"`
- 图片源: `https://www.yukings.net/img/{关键词命名}.webp` (实际部署时)
- 当前阶段使用: `https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?...` 生成占位图

---

## 16. 代码工程规范

### 强制
- 纯静态 HTML5 + 原生 CSS, **禁止 JavaScript** (JSON-LD 除外)
- 禁止 `<iframe>` / `<embed>` / `<script>` (除 `application/ld+json`)
- CSS 写在 `<head>` 的 `<style>` 中
- 缩进 2 空格 · 编码 UTF-8
- 所有可点击元素: cursor pointer + transition

### HTML 语义化
- 必含: `<header>` / `<main>` / `<section>` / `<article>` / `<footer>` / `<nav>` / `<aside>`
- 减少冗余 `<div>`, 利于爬虫抓取
- H 标签层级: 1 H1 → 多个 H2 → H3/H4 (不可跳级)

### 文件归档
```
/workspace/html/
├── index.html
├── products.html
├── solutions.html
├── projects.html
├── blog.html
├── about.html
└── contact.html
```

---

## 17. 合规自检 Checklist

每页生成后必查项:

- [ ] H1 唯一, 含主核心词
- [ ] H2/H3 层级有序
- [ ] OG / Twitter / canonical / hreflang / robots 完整
- [ ] JSON-LD: Organization + BreadcrumbList + 页面专属
- [ ] 所有图片有 alt / width / height / loading
- [ ] 关键词密度 2-3%
- [ ] 无 iframe / embed / script (除 JSON-LD)
- [ ] 4 渠道联系方式统一
- [ ] CSS 变量 + BEM 命名 + 3 档响应式
- [ ] 顶部 7 项导航顺序统一
- [ ] 末级面包屑为橙色

---

## 18. 维护记录

| 日期 | 变更 | 维护人 |
|---|---|---|
| 2026-06-15 | 7 个核心页面 (Home/Products/Solutions/Projects/Blog/About/Contact) 全部交付 v1.0 | Yukings Web Team |
| 待定 | 添加 Manufacturers Page · Distributor Page · News & Press | — |
| 待定 | 国际化版本 (ES / DE / FR / RU / JA) | — |

---

*本规范为 Yukings 独立站全站唯一设计源, 任何页面生成必须严格遵守. 豁免需在指令开头标注【本次忽略建站规则】。*
