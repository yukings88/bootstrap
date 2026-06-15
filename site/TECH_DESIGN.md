# Yukings 声屏障产品页 TECH_DESIGN.md
## 1. 技术栈选型（适配Shoptop模板）
1. 结构：HTML5 语义化标签（nav/section/footer），UTF-8编码。
2. 样式：原生 CSS3，使用CSS全局变量统一色彩/字体/间距，不引入第三方UI框架。
3. 交互：原生 JavaScript（仅图片放大、模块折叠、悬浮按钮），禁止大型插件。
4. 字体：Archivo 字体（由Shoptop全局引入，页面仅调用字体名）。
5. 图片格式：实景JPG、细节PNG，全部开启懒加载。

## 2. 全局 CSS 变量（所有页面共用，不可修改）
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

## 3. 项目文件结构（严格按照此结构生成）
/yukings-20-Noise-Barrier-Pages
├── public/
│   ├── common.css  # 全局通用样式、CSS变量、模块样式
│   ├── common.js   # 全局通用交互脚本
│   └── global-img/ # 全局通用图标、按钮、边框
├── product-group-A/ # 1-8号HTML文件
├── product-group-B/ # 9-12号HTML文件
├── product-group-C/ # 13-15号HTML文件
├── product-group-D/ # 16-18号HTML文件
├── product-group-E/ # 19-20号HTML文件
└── docs/ # 4份核心文档

## 4. HTML 基础结构规范（单页通用框架）
所有单品HTML文件统一使用语义化标签，结构固定，仅修改内部内容。
页面基础结构：面包屑 → 首屏 → 痛点 → 卖点 → 参数表 → 场景 → 细节 → 安装 → 认证 → 案例 → 定制 → 售后 → 底部FAQ+表单 → 悬浮按钮。

## 5. 代码&平台约束
1. 所有样式统一写入 public/common.css，单品HTML仅保留结构与内容，禁止重复写样式。
2. 所有通用交互写入 public/common.js，单品不新增独立JS代码。
3. 图片路径使用**相对路径**，适配Shoptop图片库。
4. 每个页面独立编写 <title> 标题，格式：[产品英文名] | Yukings Sound Barrier。
5. 代码注释使用英文，简洁规范，class类名采用短横线命名法。