# Yukings声屏障Shoptop独立站页面生成规范（永久全局生效）

> 豁免规则：用户在指令开头标注【本次忽略建站规则】，本套规则全部失效。

---

## 一、页面架构规范（动态自定义，不固定模块）

1. 摒弃固定5模块模板，按照页面属性：栏目页/单品页/工程案例页/资讯页/FAQ聚合页动态组合页面结构；
   可选模块：通栏Banner、品牌简介、产品分类卡片、技术参数表格、工程项目案例、资质证书、OEM定制说明、安装说明、采购FAQ、工厂实力展示，按需增删。
2. HTML优先使用`<header><main><section><article>`语义标签，精简冗余DIV，利于谷歌爬虫抓取，提升收录。
3. **差异化强制要求**：每一页必须根据自身业务属性、场景、品类、用途，独立设计专属页面架构、模块顺序、内容侧重点、图文排布，禁止统一模板、禁止结构雷同、禁止模块一致。同类页面也要做到布局差异化、内容差异化、板块取舍差异化。

---

## 二、URL命名 + 关键词绑定规则（全站SEO骨架）

### 1. URL格式
全小写、英文横杠-分隔
- 栏目页：`/xxx-noise-barrier`
- 国别细分页：`/country-xxx-noise-barrier`
- 单品详情页：`/material-scene-noise-barrier`
- 案例页：`/project-xxx-noise-barrier-case`

### 2. 关键词绑定逻辑
- ① 页面URL词根 = 本页唯一核心关键词
- ② H1标题和URL词根完全对应
- ③ Title、Meta Description围绕词根拓展1~3个业务长尾
- ④ 正文首段第一句自然植入URL核心词根

### 3. 分层关键词库（仅选用和当前页面匹配词汇，禁止全量堆砌）
- **一级核心词根**：noise barrier、sound barrier、acoustic barrier
- **材质二级词**：galvanized steel / aluminum / concrete / PC transparent noise barrier
- **应用场景三级词**：highway / railway / industrial plant / residential acoustic barrier
- **GEO地域词**：USA、Canada、Germany、UK、Australia、Southeast Asia 搭配产品词
- **商贸转化词**：manufacturer、supplier、custom made、OEM、wholesale

---

## 三、TDK谷歌收录硬性规范

1. **Title**：字符≤60，格式：页面核心关键词+产品属性 | Yukings Manufacturer
2. **Meta Description**：120~155字符，主关键词+1~2个长尾词+工厂优势（CE certified、ISO9001、custom design、short lead time），杜绝关键词堆砌。

---

## 四、页面站内SEO落地细则

1. **H标签**：每页唯一1个H1；H2用于板块大标题、H3用于单品/分项内容，标签层级有序不跳级；页面关键词整体密度控制2%~3%；重点产品参数、品名适当`<strong>`加粗（每页3~5处）。
2. **图片规范**：Banner默认尺寸1920*520、格式WebP；全部img标签必填`alt=页面关键词+使用场景`；图片src统一域名：`https://yukings-domain.com/img/关键词命名.webp`。
3. **内链优化**：页面正文自然植入3~5个同站相关栏目锚文本内链，锚文本使用产品关键词。

---

## 五、EEAT权威评分落地（按页面属性选择性植入）

1. **资质内容**：按需写入CE、ISO9001、国标GB、美标ASTM、德标DIN，产品参数同时标注公制+英制双单位。
2. **权威背书**：匹配页面品类插入对应公路/铁路/厂区真实工程案例、工厂产能、出口国别履历（US/EU/AUS等）。
3. **FAQ撰写标准**：全部采用海外采购原生英文提问，围绕MOQ、报价、质保、安装、海运周期、认证定制，规避中式英文。

---

## 六、GEO地域优化布局（适配谷歌AI Overview、本地搜索收录）

1. 交易词、属性词、国别长尾词分层散布在H3、段落、FAQ；
2. 欧美市场页面侧重CE、检测报告、工程项目；东南亚/中东页面突出MOQ、性价比、防腐耐用、交期；
3. 品牌全平台信息统一：官网、社媒、B2B店铺品牌名、地址、联系方式保持一致。

---

## 七、结构化数据Schema（富摘要收录必备）

1. 栏目/常规页/FAQ区块强制嵌入**FAQPage JSON-LD**，脚本放置`<head>`内，问答文本与页面可见FAQ完全一致；
2. 单品详情页按需补充**Product结构化数据**（品名、材质、产地、认证）；
3. 案例页放弃FAQPage，改用**Article JSON-LD**，填写项目落地地点、完工时间、项目简述。

### Schema类型自动匹配规则
- Product（产品页）→ FAQPage
- Solution（解决方案页）→ FAQPage
- Case（工程案例页）→ Article

---

## 八、品牌视觉·色调&字体强制规范（全页面统一）

1. **整体风格**：简约高端工业风，强化版面结构感、秩序感，参考 schuette-aluminium.de 德系高端工业外贸极简风格、大留白、规整栅格、专业B2B视觉气质。
2. **固定配色**：
   - 主深蓝 `#082457`
   - 点缀橙红 `#E4662A`
   - 页面基底 `#FFFFFF` 白色背景
   - 标题重点文字：`#E4662A`
   - 按钮/强调高亮：`#082457`
   - 正文常规：`#333333`
3. **字体规则**：全页面所有标签行内style统一书写 `font-family:"Archivo",sans-serif`；依靠字号、字重（font-weight）区分信息层级，不随意更换字体，字号整站协调统一。

---

## 九、Shoptop代码输出强制规范

1. 全部CSS样式写在标签内 `inline style=""`，禁止独立`<style>`标签、外链CSS、`@import`；页面整体100%自适应容器，避免宽度溢出错位。
2. 禁用`<script>`、`<iframe>`、`<embed>`等脚本标签，只生成纯静态HTML代码。
3. 输出内容：仅纯净HTML源码，剔除多余说明文字、注释、Markdown、无效空行，代码可直接复制进 MechHub 自定义HTML组件。
4. 文件归档：生成代码通过Filesystem保存至 `./html/页面URL文件名.html`。

---

## 十、生成前置流程

页面编写前启用 **Sequential-Thinking** 分步执行：
1. 确认页面类型
2. 敲定URL & 核心关键词
3. 规划页面架构
4. 代码编写
5. SEO + EEAT + 视觉规范合规自检
6. 输出最终源码

---

## 十一、页面类型与专属架构参考

### Product 产品页
- 钢材屏障类：交通场景Banner → 产品核心优势 → 材质工艺拆解 → 多规格参数表格 → 公路适配型号 → 抗风载/抗老化性能 → 施工安装说明 → 场景实拍 → FAQ
- 透明板类：城市景观Banner → 透光降噪双重优势 → 板材性能解析 → 抗冲击/耐候参数 → 景观适配场景 → 美观+安全双重说明 → 安装细节 → FAQ

### Solution 解决方案页
- 民生降噪类：城市噪音痛点Banner → 三类场景噪音危害分析 → 校园/医院/住宅差异化降噪难点 → 针对性治理方案体系 → 场景分区治理策略 → 适配产品选型逻辑 → 民用降噪标准EEAT佐证 → FAQ
- 工业降噪类：工厂工况噪音场景Banner → 工业设备噪音源拆解 → 车间降噪技术逻辑 → 分区降噪方案 → 防腐耐温工业适配优势 → 工程项目落地标准 → 工厂降噪验收规范 → FAQ

### Case 工程案例页
- 项目实景Banner → 项目概况 & 地点GEO信息 → 现场降噪难题 → 项目定制方案 → 选用材质参数 → 标准适配（ASTM/DIN等）→ 施工过程简述 → 竣工效果实测 → 项目总结 & 相关产品内链

---

## 十二、强制规范自检清单（生成完毕前必查）

- [ ] URL词根与H1完全对应
- [ ] Title ≤ 60字符，Meta Description 120~155字符
- [ ] 每页唯一1个H1
- [ ] 关键词密度 2%~3%
- [ ] `<strong>`加粗 3~5处
- [ ] 所有img含alt属性
- [ ] 正文含 3~5 个同站锚文本内链
- [ ] 嵌入正确Schema（FAQPage/Article）
- [ ] 字体统一 `font-family:"Archivo",sans-serif`
- [ ] 配色严格遵守 #082457 / #E4662A / #FFFFFF / #333333
- [ ] 全部CSS内联，无`<style>`/`<script>`/`<iframe>`
- [ ] 文件保存至 `./html/对应url.html`
