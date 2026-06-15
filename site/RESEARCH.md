# Yukings 20款声屏障产品页 - 需求研究 RESEARCH.md
## 1. 项目基本信息
项目名称：Yukings外贸独立站声屏障产品详情页（20款）
开发工具：TRAE Solo
部署平台：Shoptop B2B外贸模板
页面总量：20个独立产品页，分为5大品类分组
目标用户：海外基建总包、工厂采购、轨道交通集团、市政工程商、海外工程承包商

## 2. 平台约束规则
1. 仅自定义页面 HTML5 / 原生 CSS3 / 原生轻量JS，禁止修改Shoptop底层框架、原生组件。
2. 图片支持懒加载、点击放大，所有资源使用相对路径，适配海外网络访问。
3. 页面必须PC端为主、移动端自适应，长模块支持折叠，参数表移动端横向滚动。

## 3. 视觉&字体强制规范（全局不可修改）
【工业B2B官网 · 欧美高端风格 · 全站统一UI】

1. 技术约束（必须严格遵守）
- 只生成纯静态 HTML5 + 原生 CSS，禁止使用 JavaScript、iframe、embed、script 标签。
- CSS 全部内联在 <head> 的 <style> 中，不使用外部 CSS 文件。
- 所有页面必须响应式，媒体查询断点：1024px / 768px / 480px。
- 编码格式：UTF-8，缩进统一 2 空格。

2. 全局 CSS 变量（全站强制使用，不可修改）
:root {
    --blue: #082457;
    --blue-light: #0d3a8a;
    --blue-dark: #051a3e;
    --orange: #E4662A;
    --orange-light: #f28a55;
    --orange-dark: #c04e18;
    --white: #ffffff;
    --gray-50: #f8f9fb;
    --gray-100: #eef1f6;
    --gray-200: #d8dde8;
    --gray-300: #b4bcd0;
    --gray-500: #6b7a94;
    --gray-700: #3d4f6a;
    --text-primary: #1a1a2e;
    --text-secondary: #4a5568;
    --shadow-sm: 0 1px 3px rgba(8,36,87,0.08);
    --shadow-md: 0 4px 16px rgba(8,36,87,0.10);
    --shadow-lg: 0 8px 32px rgba(8,36,87,0.12);
    --radius: 6px;
    --radius-lg: 12px;
    --max-width: 1200px;
}

3. 命名规范（全站统一）
- 所有 class 必须以 rsb- 开头，采用 BEM 命名法：
  rsb-block、rsb-block__element、rsb-block--modifier
- 示例：rsb-section、rsb-card__title、rsb-btn--primary

4. 排版规范（欧美工业风）
- 全局字体：'Archivo', 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif
- 标题颜色：var(--text-primary)
- 正文颜色：var(--text-secondary)
- 标题加粗，正文常规字重，行高 1.5~1.6

5. 颜色使用规范（严格）
- 主色：var(--blue)（导航、header、大标题背景）
- 强调色：var(--orange)（按钮、分割线、重点文字、hover）
- 背景：白色或 var(--gray-50)
- 卡片背景：white
- 边框：var(--gray-200)

6. 卡片与组件样式（统一）
- 卡片圆角：var(--radius-lg)
- 按钮圆角：var(--radius)
- 卡片阴影：默认 var(--shadow-md)，hover 用 var(--shadow-lg)
- 所有可点击元素（按钮、卡片）hover：
  - translateY(-2px)
  - 阴影加深
  - 图片缩放 1.05（如有图）

7. 布局规范
- 页面内容宽度：max-width: var(--max-width)，水平居中
- Section 上下内边距：桌面 48px 0；平板 36px 0；手机 28px 0
- 栅格：
  ≥1024px：3列/2列
  768-1023px：2列/1列
  ≤480px：1列

8. SEO 与语义化
- 必须包含：OG、Twitter、canonical、hreflang、robots
- 必须加入 JSON-LD：Product、BreadcrumbList、FAQPage、Organization
- 图片必须有 alt、width、height、loading 属性

9. 风格要求（避免 AI 廉价感）
- 大气、简洁、专业、工业风、欧美 B2B 质感
- 不花哨、不渐变堆砌、不夸张动画
- 保持留白、层次清晰、强信任感

## 4. 产品分组与开发批次（按顺序开发）
1. 分组A（批次1）：公路/高速声屏障 1-8款（流量主力、走量款）
2. 分组B（批次2）：工业/厂区声屏障 9-12款（高利润、复购款）
3. 分组C（批次3）：铁路/轨道交通声屏障 13-15款（大单、政企项目）
4. 分组D（批次4）：居民区/市政声屏障 16-18款（景观、民生项目）
5. 分组E（批次5）：定制声屏障+配件 19-20款（高客单、长尾配套）

## 5. 海外采购商核心关注点（内容创作依据）
降噪分贝(NRR/dB)、材质防腐等级、耐候/防水/抗UV性能、国际认证(CE/ISO)、安装难度、批量产能、工程案例、质保年限、定制服务、配套配件。