# Yukings 独立站 · 项目交付包 (Project Deliverables)

> **版本**: v1.0 · 2026-06-15
> **域名**: https://www.yukings.net
> **类型**: 纯静态 HTML5 站点 (零 JS, 零依赖)

## 📦 文件清单

| # | 文件 | 类型 | 大小 | 用途 |
|---|---|---|---|---|
| 1 | `index.html` | 首页 | 49.9 KB | 品牌门面 / 流量入口 |
| 2 | `products.html` | 产品中心 | 60.3 KB | 5 大品类 + 规格表 |
| 3 | `solutions.html` | 解决方案 | 63.2 KB | 5 大场景 + 6 步交付流程 |
| 4 | `projects.html` | 工程案例 | 60.1 KB | 真实项目 + 客户证言 |
| 5 | `blog.html` | 博客 | 62.9 KB | 9 篇文章 + Newsletter |
| 6 | `about.html` | 关于我们 | 39.9 KB | 公司故事 + 工厂 + 资质 |
| 7 | `contact.html` | 联系我们 | 40.5 KB | 4 渠道 + 表单 + FAQ |
| 8 | `Yukings-Site-Specification.md` | 规范文档 | 13.1 KB | 全站设计规范 |
| 9 | `sitemap.xml` | SEO 站点地图 | — | 谷歌收录 |
| 10 | `robots.txt` | 爬虫协议 | — | 搜索引擎抓取规则 |

**总计**: 7 个 HTML 页面 + 3 个项目资产 = 10 个文件

## 🌐 站点地图 (Sitemap)

```
Home (/) — 品牌门面
├─ Products (/products.html) — 5 大品类
│  ├─ Railway Noise Barriers
│  ├─ Highway Noise Barriers
│  ├─ Solar Noise Barriers
│  ├─ Industrial Noise Barriers
│  └─ Residential Noise Barriers
├─ Solutions (/solutions.html) — 5 大场景
│  ├─ Railway Noise Reduction
│  ├─ Highway Noise Control
│  ├─ Industrial Factory Noise Barriers
│  ├─ Residential Community Noise Protection
│  └─ Solar & Energy Noise Barrier Solutions
├─ Projects (/projects.html) — 5 类工程
├─ Blog (/blog.html) — 3 大内容流
├─ About (/about.html) — 公司信息
└─ Contact (/contact.html) — 4 渠道联系
```

## 🔑 核心关键词分布

| 页面 | 主核心词 | 密度 | H1 包含 |
|---|---|---|---|
| Home | noise barrier manufacturer | ~3% | ✅ |
| Products | noise barrier | ~2.5% | ✅ |
| Solutions | noise barrier solutions | ~3% | ✅ |
| Projects | noise barrier projects | ~3% | ✅ |
| Blog | noise barrier blog | ~2% | ✅ |
| About | noise barrier manufacturer | ~2% | ✅ |
| Contact | noise barrier quote | ~2% | ✅ |

## 🎨 设计系统

- **主色**: 深蓝 `#082457`
- **强调色**: 橙红 `#E4662A`
- **字体**: `Archivo, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`
- **BEM 命名**: `rsb-block__element--modifier`
- **响应式**: 1024px / 768px / 480px 三档

详细规范见 `Yukings-Site-Specification.md`。

## 📞 联系方式 (全站统一)

- **Tel**: +86-755-86366707
- **E-mail**: weilai04525@163.com
- **Miss Tang** (Sales): +86 17727812004
- **MR. Yu** (Engineer): +86 13828819804
- **Address**: Room 1405, Building B2, Yunzhi Tech Park, Guangming District, Shenzhen, Guangdong, China

## ✅ 部署前 Checklist

- [ ] 将所有 HTML 部署到 `https://www.yukings.net/` 根目录
- [ ] 替换 `trae-api-cn.mchost.guru` 占位图为正式 CDN 图片 (`https://www.yukings.net/img/...`)
- [ ] 上传 `sitemap.xml` 至根目录
- [ ] 上传 `robots.txt` 至根目录
- [ ] 提交 sitemap 至 Google Search Console + Bing Webmaster
- [ ] 配置 7 个页面的 OG 图 (`/img/yukings-*-og.webp`)
- [ ] 配置 SSL 证书 (HTTPS 强制)
- [ ] 启用 Gzip / Brotli 压缩
- [ ] 配置 CDN 加速 (建议 Cloudflare 或阿里云国际)
- [ ] 部署后 24-48h 内验证 Google 索引

## 🛠 技术栈

- **HTML5**: 语义化标签 (`<header>`, `<main>`, `<section>`, `<article>`, `<footer>`)
- **CSS**: 内联 `<style>`, 零外部依赖
- **JS**: 零 (仅 JSON-LD 结构化数据)
- **字体**: Google Fonts (Archivo)
- **图片**: WebP 格式优先, 提供 alt/width/height/loading
- **图标**: Inline SVG 或文字缩写 (零图标库)

## 📈 SEO 状态

- ✅ 每页唯一 H1
- ✅ 完整 TDK (Title/Description/Keywords)
- ✅ OG + Twitter Card
- ✅ canonical + hreflang
- ✅ JSON-LD: Organization + BreadcrumbList + 页面专属
- ✅ 内链 3-5 处 / 页
- ✅ sitemap.xml + robots.txt
- ⏳ 待补: 各页面 OG 配图

## 🌍 国际化路线 (规划中)

- v1.0 (当前): English
- v1.1 (规划): Spanish (拉美)
- v1.2 (规划): German (德语区)
- v1.3 (规划): French (法语区)
- v1.4 (规划): Russian (俄语区)
- v1.5 (规划): Japanese (日本)

---

**项目所有权**: Shenzhen Yukings Industrial Co., Ltd. © 2006-2026
