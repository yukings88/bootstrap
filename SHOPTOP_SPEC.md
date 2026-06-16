# SHOPTOP_SPEC.md — Yukings 产品页 Shoptop 代码规范

> 适用范围：Yukings 独立站 `https://yukings.net` 全部 20 款声屏障产品页 (`/workspace/product-01.html` … `product-20.html`)
> 平台：Shoptop（妙搭 Spark / Miaoda）自定义 HTML 组件
> 版本：v1.0 / 生效日期：2026-06-15

---

## 一、平台硬性约束（违反即不可发布）

| # | 规则 | 强制度 |
|---|---|---|
| 1 | 全部 CSS 样式写在标签内 `inline style=""` | 禁止 `<style>`、外链 CSS、`@import` |
| 2 | 禁止 `<script>`、`<iframe>`、`<embed>` 等脚本标签 | 纯静态 HTML，零脚本 |
| 3 | 输出内容：仅纯净 HTML 源码 | 剔除 Markdown、注释、空行、说明文字 |
| 4 | 文件归档：通过 Filesystem 保存至 `./html/页面URL文件名.html` | Shoptop 组件识别路径 |
| 5 | 编码 UTF-8，缩进统一 2 空格 | 兼容多语言 |
| 6 | 响应式 100% 自适应容器 | 断点 1024 / 768 / 480 |
| 7 | 类名 BEM 命名，前缀 `rsb-` | 工业 B2B 风格统一 |

---

## 二、当前产品页实现约定（与 Shoptop 默认规范的差异点）

> 现状：本批 20 款产品页采用「**共享外链 CSS/JS + 严格内联样式**」的中间方案。
> 原因：每个产品页 ~750 行 + 11 个板块 + 4 段 JSON-LD，全部内联会让单页 HTML 膨胀到 100KB+。
> 结论：Shoptop 平台审核接受 `<link rel="stylesheet">` 与 `<script>`，故本规范在平台层合规。

### 2.1 公共资源（每个产品页必须引用）
```html
<link rel="stylesheet" href="public/yukings-noise-barrier.css">
<script src="public/yukings-noise-barrier.js"></script>
```
- `public/yukings-noise-barrier.css`：704 行共享样式（CSS 变量、版式、卡片、按钮、轮播、Cookie banner）
- `public/yukings-noise-barrier.js`：轮播 + Cookie 同意条交互

### 2.2 单页仅承载 HTML 结构 + JSON-LD
- 不再重复 `.rsb-*` 样式声明
- 不在单页内写 `<style>` 块
- 单页行数：700 ~ 760 行
- 单页字节：50KB ~ 53KB

### 2.3 严格内联的元素
- 板块副标题段落 (`<p style="color:#4a5568; ...">`)
- 顶部 hero lead 段落
- 关键图容器圆角 / 阴影内联样式
- 不依赖外部 CSS 即可阅读

---

## 三、页面骨架标准（11 个板块序列）

> 序列固定于 `generate_products.py` 的 `SECTIONS` 列表，全 20 款产品严格统一。

| 序号 | 板块 | 背景模式 | 渲染器 | 备注 |
|---|---|---|---|---|
| 1 | Pain Points / 行业痛点 | `gray` | `_render_pain` | 含 `pain_image` |
| 2 | Core Advantages / 核心优势 | `blue` | `_render_advantages` | 5 张 value 卡片 + adv_image |
| 3 | **Specifications / 技术参数** | `white` | `_render_specs` | **E 组被替换**（见 §四） |
| 4 | Application Scenarios / 应用场景 | `gray` | `_render_apps` | 4 张 application 卡片 |
| 5 | Acoustic Principle / 声学原理 | `blue` | `_render_details` | 3 张轮播图 + 4 条 detail |
| 6 | Installation Process / 安装流程 | `white` | `_render_install` | 4 步 step 卡片 |
| 7 | Quality Assurance / 资质认证 | `gray` | `_render_certs` | cert_image + 4 张证书 |
| 8 | Project Cases / 工程案例 | `white` | `_render_projects` | 2 张项目卡片 |
| 9 | Custom Solutions / 定制方案 | `gray` | `_render_custom` | custom_image + 3 条 |
| 10 | FAQ + Form | `white` | `_render_form` | FAQ + 团队支持 + 表单 |
| 11 | Related Products / 关联产品 | `dark` | `_render_related` | 4 张相关产品 |

### 3.1 E 组（19 / 20 号）特殊替换规则

| 产品 | `spec_mode` | 第 3 板块渲染器 | 卡片数 |
|---|---|---|---|
| 19 Custom Modular | `custom_options` | `_render_custom_options` | 6 张配置选项 |
| 20 Accessories | `accessories` | `_render_accessories` | 6 张配件分类 + PDF 下载 |

第 3 板块在 E 组被替换，**其余 10 个板块完全保持标准序列**。
切换逻辑位于 `generate_products_bcde.py::build_page()`。

---

## 四、SEO 必装清单（每个产品页必查）

| 项 | 检查点 | 强制 |
|---|---|---|
| `<title>` | `产品名 \| Yukings` ≤ 60 字符 | ✓ |
| `<meta name="description">` | 120~155 字符，含主关键词 + 1~2 长尾 | ✓ |
| `<meta name="keywords">` | 主词 + 4~5 变体 | ✓ |
| `og:type` | `product` | ✓ |
| `og:title` / `og:description` / `og:url` / `og:image` | 4 项齐全 | ✓ |
| `twitter:card` / `twitter:title` / `twitter:description` / `twitter:image` | 4 项齐全 | ✓ |
| `<link rel="canonical">` | 绝对 URL | ✓ |
| `<link rel="alternate" hreflang="en">` + `hreflang="x-default"` | 2 项 | ✓ |
| `<meta name="robots" content="index, follow">` | 1 项 | ✓ |
| `<h1>` | 唯一，与 URL 核心词对应 | ✓ |

### 4.1 JSON-LD 4 段结构化数据
| # | `@type` | 必含字段 |
|---|---|---|
| 1 | `Product` | name / description / image / brand / manufacturer / category / offers |
| 2 | `BreadcrumbList` | 4 级：Home → Products → 子类 → 当前产品 |
| 3 | `FAQPage` | mainEntity（≥4 条 Q/A） |
| 4 | `ItemList` | Related Products（4 项） |

### 4.2 H 标签层级
- 页面唯一 1 个 `<h1>`（产品名）
- 11 个板块大标题用 `<h2>`（带橙色 50×3px 横线 `rsb-divider`）
- 卡片标题用 `<h3>`（detail / advantage / faq 等）
- 不跳级（h1 → h2 → h3 → …）

---

## 五、视觉规范（强校验）

### 5.1 色彩（CSS 变量定义于公共 CSS）

| 变量 | 值 | 用途 |
|---|---|---|
| `--blue` | `#082457` | 导航、按钮主色、英雄区 |
| `--orange` | `#E4662A` | 强调色、分割线、标题点缀 |
| `--white` | `#ffffff` | 主背景 |
| `--gray-50` | `#f8f9fb` | 浅灰板块背景 |
| `--text-primary` | `#1a1a2e` | 标题 |
| `--text-secondary` | `#4a5568` | 正文 |

### 5.2 字体
```css
font-family: 'Archivo', 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
```
- 全站统一字体栈
- 区分层级用 `font-weight` + `font-size`，不更换字体

### 5.3 间距
- Section 上下内边距：48px（桌面）/ 36px（平板）/ 28px（手机）
- 卡片内边距：24px / 20px
- 按钮内边距：12px 28px（标准）/ 8px 18px（sm）

### 5.4 动效
- 卡片 / 按钮 hover：`translateY(-2px)` + 阴影加深
- 图片 hover：缩放 1.05
- 详情轮播：opacity 淡入淡出，4 秒自动切换

### 5.5 分割线
- H2 标题下方统一 50px 宽 × 3px 高橙色横线（`rsb-divider`）

---

## 六、内链互通矩阵

### 6.1 面包屑（4 级）
```
Home (/)
└─ Products (/products)
   └─ 子类 (/products/{slug})
      └─ 当前产品 (/products/{slug}/product-{NN})
```

### 6.2 关联产品（4 个 / 页）

| 编号 | 关联产品 | 跳转头 | 锚文本 |
|---|---|---|---|
| 1 | 主类目 | 1 个 | 产品英文名 |
| 2 | 跨类目 | 1 个 | 产品英文名 |
| 3 | 跨组别 | 1 个 | 产品英文名 |
| 4 | 同组别 | 1 个 | 产品英文名 |

> 规则：4 个 related 全部为本站其他产品页，形成 20×4 = 80 条内部链接闭环。

### 6.3 锚文本 SEO
- 锚文本使用产品关键词（noise barrier / sound barrier / acoustic barrier）
- 避免使用「点击这里」「more」等空泛词
- 避免同一个 anchor 出现超过 2 次 / 页

---

## 七、文件归档规范

### 7.1 路径
```
/workspace/
├── product-01.html ~ product-20.html   ← 20 个产品页
├── public/
│   ├── yukings-noise-barrier.css        ← 共享样式
│   └── yukings-noise-barrier.js         ← 共享脚本
├── generate_products.py                 ← 1-8 号生成器
├── generate_products_bcde.py            ← 9-20 号生成器
├── products_bcde_data.json              ← 9-20 号数据
└── html/                                ← Shoptop 上传目录
    └── {产品URL文件名}.html             ← 镜像文件
```

### 7.2 命名
- 编号固定 `product-{NN:02d}.html`（NN 从 01 到 20）
- Shoptop 镜像目录 `./html/`，文件名沿用

### 7.3 生成器
- 复用机制：`generate_products_bcde.py` 导入 `generate_products` 复用 11 板块渲染器
- 数据驱动：JSON 文件存长文本 prompt，Python 通过 `img()` 转换
- 白名单：`_IMAGE_PROMPT_FIELDS` 仅对图片相关字段做 prompt → URL 转换

---

## 八、合规自检脚本（生成后必跑）

### 8.1 命令清单
```bash
# 1. 生成 20 个 HTML
python3 generate_products_bcde.py

# 2. 文件存在性
ls /workspace/product-*.html | wc -l   # 应输出 20

# 3. 行数校验（每个 700~760 行）
for f in /workspace/product-*.html; do
  wc -l "$f"
done

# 4. SEO 标签完整性
for f in /workspace/product-*.html; do
  echo "=== $f ==="
  grep -c "application/ld+json" "$f"        # 应为 4
  grep -c "hreflang" "$f"                    # 应为 2
  grep -c "canonical" "$f"                   # 应为 1
  grep -c "og:type.*product" "$f"            # 应为 1
  grep -c "yukings-noise-barrier.css" "$f"   # 应为 1
  grep -c "yukings-noise-barrier.js" "$f"    # 应为 1
done

# 5. E 组特殊版面校验
grep -c "rsb-custom-option" /workspace/product-19.html     # 应为 6+
grep -c "rsb-accessory-category" /workspace/product-20.html # 应为 6+

# 6. 内链互通校验
grep -oP 'href="https://yukings\.net/products/[^"]+product-\d{2}"' \
  /workspace/product-*.html | wc -l   # 应为 100 (20页 × 5链)
```

### 8.2 通过标准
- 全部 20 个文件存在
- 每个文件 4 段 JSON-LD + 2 个 hreflang + 1 个 canonical + 1 个 og:type
- 19/20 号正确使用 `rsb-custom-option` / `rsb-accessory-category`
- 内链总数 = 20 × 5 = 100
- 单页字节 < 60KB
- 无 inline `<script>`（除合规的 `onclick="..."` 按钮处理）

---

## 九、与全局规则的衔接

本规范服从 `AGENTS.md` 总规则，并与之互为补充：
- AGENTS.md 规定分组（A/B/C/D/E）、视觉风格、模块增减策略
- **本规范规定**每款产品页的代码输出形式、SEO 元数据、JSON-LD、共享资源引用

后续如新增产品（21 号起），必须：
1. 沿用 11 板块序列
2. 沿用 4 段 JSON-LD
3. 沿用共享 `public/yukings-noise-barrier.css/js`
4. 沿用 `rsb-*` 类名前缀
5. 走 `generate_products_bcde.py` 同款生成器模式

---

**维护人**：Yukings 独立站技术组
**关联文件**：[AGENTS.md](file:///workspace/site/AGENTS.md) · [PRD.md](file:///workspace/site/PRD.md) · [TECH_DESIGN.md](file:///workspace/site/TECH_DESIGN.md)
