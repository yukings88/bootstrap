#!/usr/bin/env python3
"""Generate Yukings full static site (28 pages) per v1.0 specification."""
import os, html

OUT = "/workspace/html"
os.makedirs(OUT, exist_ok=True)

# -------- Shared CSS (unified master system) --------
SHARED_CSS = r"""
:root{
  --blue:#082457;--blue-light:#0d3a8a;--blue-dark:#051a3e;
  --orange:#E4662A;--orange-light:#f28a55;--orange-dark:#c04e18;
  --white:#ffffff;--gray-50:#f8f9fb;--gray-100:#eef1f6;
  --gray-200:#d8dde8;--gray-300:#b4bcd0;--gray-500:#6b7a94;
  --gray-700:#3d4f6a;--text-primary:#1a1a2e;--text-secondary:#4a5568;
  --shadow-sm:0 1px 3px rgba(8,36,87,.08);
  --shadow-md:0 4px 16px rgba(8,36,87,.10);
  --shadow-lg:0 8px 32px rgba(8,36,87,.12);
  --radius:6px;--radius-lg:12px;--max-width:1200px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Archivo','Segoe UI','Roboto','Helvetica Neue',Arial,sans-serif;color:var(--text-secondary);line-height:1.65;background:var(--white);-webkit-font-smoothing:antialiased;font-size:15.5px}
img{max-width:100%;display:block;transition:transform .6s ease}
img:hover{transform:scale(1.05)}
a{color:inherit;text-decoration:none;transition:color .25s ease,opacity .25s ease}
h1,h2,h3,h4,h5,h6{font-family:'Archivo',sans-serif;color:var(--text-primary);font-weight:700;line-height:1.2;letter-spacing:-.3px}
.rsb-container{max-width:var(--max-width);margin:0 auto;padding:0 24px;width:100%}
.rsb-divider{width:50px;height:3px;background:var(--orange);margin:14px 0 22px;border-radius:2px}
.rsb-divider--center{margin-left:auto;margin-right:auto}
.rsb-eyebrow{display:inline-block;color:var(--orange);font-weight:700;font-size:12.5px;letter-spacing:2.4px;text-transform:uppercase;margin-bottom:10px}

/* Top bar */
.rsb-topbar{background:var(--blue-dark);color:var(--gray-200);font-size:13px;padding:9px 0}
.rsb-topbar__inner{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}
.rsb-topbar a{color:var(--gray-200);display:inline-flex;align-items:center;gap:6px}
.rsb-topbar a:hover{color:var(--orange-light)}
.rsb-topbar__links{display:flex;gap:18px;flex-wrap:wrap}

/* Header / Main nav */
.rsb-header{background:var(--white);box-shadow:var(--shadow-sm);position:sticky;top:0;z-index:50}
.rsb-header__inner{display:flex;align-items:center;justify-content:space-between;height:80px;gap:18px}
.rsb-logo{display:flex;align-items:center;gap:12px;font-weight:800;font-size:22px;color:var(--blue);letter-spacing:.5px}
.rsb-logo__mark{width:42px;height:42px;background:linear-gradient(135deg,var(--blue) 0%,var(--blue-light) 100%);color:var(--white);display:flex;align-items:center;justify-content:center;border-radius:8px;font-weight:800;font-size:20px;position:relative;box-shadow:0 4px 14px rgba(8,36,87,.18);cursor:pointer;transition:transform .3s ease}
.rsb-logo__mark:hover{transform:translateY(-2px)}
.rsb-logo__mark::after{content:"";position:absolute;right:-4px;bottom:-4px;width:14px;height:14px;background:var(--orange);border-radius:50%;border:2px solid var(--white)}
.rsb-logo__name{display:flex;flex-direction:column;line-height:1.05}
.rsb-logo__name small{font-size:10px;font-weight:500;color:var(--gray-500);letter-spacing:1.4px;text-transform:uppercase}
.rsb-nav{display:flex;align-items:center;gap:2px;flex-wrap:wrap}
.rsb-nav__item{padding:10px 14px;font-size:14px;font-weight:600;color:var(--text-primary);border-radius:var(--radius);position:relative;cursor:pointer}
.rsb-nav__item:hover{color:var(--orange);background:var(--gray-50)}
.rsb-nav__item--active{color:var(--orange)}

/* Buttons */
.rsb-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:14px 32px;font-family:'Archivo',sans-serif;font-weight:600;font-size:14.5px;border-radius:var(--radius);border:none;cursor:pointer;transition:all .3s ease;letter-spacing:.3px;text-decoration:none;color:var(--white);text-align:center;white-space:nowrap}
.rsb-btn--primary{background:var(--orange);color:var(--white)}
.rsb-btn--primary:hover{background:var(--orange-dark);transform:translateY(-2px);box-shadow:0 8px 22px rgba(228,102,42,.4)}
.rsb-btn--ghost{background:transparent;color:var(--white);border:1.5px solid rgba(255,255,255,.55)}
.rsb-btn--ghost:hover{background:var(--white);color:var(--blue);transform:translateY(-2px);border-color:var(--white)}
.rsb-btn--blue{background:var(--blue);color:var(--white)}
.rsb-btn--blue:hover{background:var(--blue-light);transform:translateY(-2px);box-shadow:0 8px 22px rgba(8,36,87,.3)}
.rsb-btn--ghost-alt{background:transparent;color:var(--blue);border:1.5px solid var(--blue)}
.rsb-btn--ghost-alt:hover{background:var(--blue);color:var(--white);transform:translateY(-2px)}
.rsb-btn--sm{padding:9px 20px;font-size:13px}
.rsb-btn--lg{padding:16px 38px;font-size:15.5px}
.rsb-btn--block{width:100%}

/* Breadcrumb */
.rsb-breadcrumb{background:var(--gray-50);padding:14px 0;border-bottom:1px solid var(--gray-200)}
.rsb-breadcrumb__list{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--gray-500);flex-wrap:wrap;list-style:none;padding:0}
.rsb-breadcrumb__list a{color:var(--gray-700);font-weight:500}
.rsb-breadcrumb__list a:hover{color:var(--orange)}
.rsb-breadcrumb__sep{color:var(--gray-300)}
.rsb-breadcrumb__list li:last-child span,.rsb-breadcrumb__current{color:var(--orange);font-weight:600}

/* Hero */
.rsb-hero{position:relative;min-height:560px;color:var(--white);overflow:hidden;background:var(--blue-dark);display:flex;align-items:center;padding:90px 0 80px}
.rsb-hero__bg{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0;animation:rsbPan 24s ease-in-out infinite alternate}
@keyframes rsbPan{0%{transform:scale(1.04) translateX(0)}100%{transform:scale(1.07) translateX(-1.2%)}}
.rsb-hero::after{content:"";position:absolute;inset:0;background:linear-gradient(105deg,rgba(5,26,62,.96) 0%,rgba(5,26,62,.72) 50%,rgba(5,26,62,.35) 100%);z-index:1}
.rsb-hero__content{position:relative;z-index:2;max-width:820px}
.rsb-hero__eyebrow{display:inline-flex;align-items:center;gap:10px;padding:6px 16px;background:rgba(228,102,42,.18);border:1px solid rgba(228,102,42,.4);color:var(--orange-light);border-radius:50px;font-size:12px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:24px}
.rsb-hero__eyebrow::before{content:"";width:6px;height:6px;background:var(--orange);border-radius:50%;animation:rsbPulse 2s ease-in-out infinite}
@keyframes rsbPulse{0%,100%{opacity:1}50%{opacity:.4}}
.rsb-hero h1{color:var(--white);font-size:62px;line-height:1.08;margin-bottom:22px;letter-spacing:-1px;font-weight:800}
.rsb-hero h1 span{color:var(--orange-light);font-style:italic;font-weight:600}
.rsb-hero p.lede{font-size:18px;color:rgba(255,255,255,.88);max-width:680px;margin-bottom:34px;line-height:1.7}
.rsb-hero__actions{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:48px}
.rsb-hero__quick{display:flex;flex-wrap:wrap;gap:10px;padding-top:24px;border-top:1px solid rgba(255,255,255,.18)}
.rsb-hero__chip{padding:8px 16px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);color:var(--white);border-radius:50px;font-size:13px;font-weight:500;letter-spacing:.3px;transition:all .3s ease}
.rsb-hero__chip:hover{background:var(--orange);border-color:var(--orange);color:var(--white);transform:translateY(-2px)}
.rsb-hero__stats{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:48px;padding-top:32px;border-top:1px solid rgba(255,255,255,.18)}
.rsb-hero__stat strong{display:block;color:var(--orange-light);font-size:32px;font-weight:800;margin-bottom:4px;letter-spacing:-.5px}
.rsb-hero__stat span{font-size:12px;color:rgba(255,255,255,.7);letter-spacing:.5px;text-transform:uppercase;font-weight:500}

/* Section base */
.rsb-section{padding:96px 0;scroll-margin-top:120px}
.rsb-section--gray{background:var(--gray-50)}
.rsb-section--blue{background:linear-gradient(135deg,var(--blue) 0%,var(--blue-dark) 100%);color:var(--white)}
.rsb-section--blue h2,.rsb-section--blue h3{color:var(--white)}
.rsb-section--blue p{color:rgba(255,255,255,.8)}
.rsb-section--blue .rsb-divider{background:var(--orange)}
.rsb-section__head{max-width:760px;margin:0 auto 60px;text-align:center}
.rsb-section__head .rsb-divider{margin:14px auto 22px}
.rsb-section__head h2{font-size:42px;margin-bottom:14px;line-height:1.15}
.rsb-section__head p{font-size:16.5px;color:var(--text-secondary);line-height:1.7;max-width:640px;margin:0 auto}

/* Card grid */
.rsb-grid{display:grid;gap:24px}
.rsb-grid--3{grid-template-columns:repeat(3,1fr)}
.rsb-grid--4{grid-template-columns:repeat(4,1fr)}
.rsb-grid--2{grid-template-columns:repeat(2,1fr)}

.rsb-card{background:var(--white);border:1px solid var(--gray-200);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);transition:all .35s ease;cursor:pointer;display:flex;flex-direction:column}
.rsb-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg);border-color:var(--orange-light)}
.rsb-card__media{position:relative;aspect-ratio:16/10;background:var(--gray-200);overflow:hidden}
.rsb-card__img{width:100%;height:100%;background-size:cover;background-position:center;transition:transform .6s ease}
.rsb-card:hover .rsb-card__img{transform:scale(1.05)}
.rsb-card__tag{position:absolute;top:16px;left:16px;background:var(--orange);color:var(--white);padding:6px 14px;border-radius:50px;font-size:11.5px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;z-index:2;box-shadow:0 4px 12px rgba(228,102,42,.4)}
.rsb-card__body{padding:24px;flex:1;display:flex;flex-direction:column}
.rsb-card__meta{font-size:12.5px;color:var(--orange);font-weight:700;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px}
.rsb-card__title{font-size:20px;margin-bottom:10px;color:var(--text-primary);font-weight:700;line-height:1.3}
.rsb-card__text{font-size:14.5px;color:var(--text-secondary);line-height:1.6;margin-bottom:18px;flex:1}
.rsb-card__link{color:var(--blue);font-weight:700;font-size:14px;cursor:pointer}
.rsb-card__link:hover{color:var(--orange)}

/* Editorial split blocks */
.rsb-split{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;margin-bottom:80px}
.rsb-split:last-child{margin-bottom:0}
.rsb-split--reverse{direction:rtl}
.rsb-split--reverse > *{direction:ltr}
.rsb-split__media{position:relative;aspect-ratio:4/3;border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-md);background:var(--gray-200)}
.rsb-split__img{width:100%;height:100%;background-size:cover;background-position:center;transition:transform .8s ease}
.rsb-split__media:hover .rsb-split__img{transform:scale(1.05)}
.rsb-split__eyebrow{color:var(--orange);font-weight:700;font-size:12.5px;letter-spacing:2.4px;text-transform:uppercase;margin-bottom:14px;display:block}
.rsb-split__body h2{font-size:36px;margin-bottom:14px;line-height:1.2}
.rsb-split__body > p{font-size:16px;line-height:1.7;margin-bottom:20px}
.rsb-split__list{list-style:none;padding:0;margin:0 0 26px}
.rsb-split__list li{padding:10px 0 10px 26px;position:relative;font-size:15px;border-bottom:1px dashed var(--gray-200)}
.rsb-split__list li::before{content:"\2713";position:absolute;left:0;top:10px;color:var(--orange);font-weight:800;font-size:16px}
.rsb-split__actions{display:flex;gap:12px;flex-wrap:wrap}

/* Spec table */
.rsb-tablewrap{background:var(--white);border:1px solid var(--gray-200);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);margin-bottom:30px}
.rsb-tablewrap:last-child{margin-bottom:0}
.rsb-table{width:100%;border-collapse:collapse;font-size:14px}
.rsb-table thead{background:var(--blue-dark);color:var(--white)}
.rsb-table th{text-align:left;padding:16px 20px;font-weight:700;font-size:13px;letter-spacing:.5px;text-transform:uppercase;border-right:1px solid rgba(255,255,255,.1)}
.rsb-table th:last-child{border-right:none}
.rsb-table th:first-child{background:var(--blue);width:24%}
.rsb-table td{padding:16px 20px;border-bottom:1px solid var(--gray-100);color:var(--text-secondary);vertical-align:top;line-height:1.6}
.rsb-table tbody tr:last-child td{border-bottom:none}
.rsb-table td:first-child{font-weight:700;color:var(--text-primary);background:var(--gray-50);border-right:1px solid var(--gray-200)}
.rsb-table strong{color:var(--text-primary)}
.rsb-table .rsb-tag{display:inline-block;background:rgba(228,102,42,.08);color:var(--orange);padding:3px 10px;border-radius:50px;font-size:11.5px;font-weight:600;margin:2px 4px 2px 0;letter-spacing:.3px}

/* Stat counters */
.rsb-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.rsb-stat{background:var(--white);border:1px solid var(--gray-200);border-radius:var(--radius-lg);padding:28px 24px;text-align:center;box-shadow:var(--shadow-sm);transition:all .35s ease}
.rsb-stat:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--orange-light)}
.rsb-stat strong{display:block;font-size:40px;color:var(--blue);font-weight:800;margin-bottom:6px;letter-spacing:-.5px}
.rsb-stat strong em{color:var(--orange);font-style:normal}
.rsb-stat span{font-size:13.5px;color:var(--text-secondary);font-weight:500;letter-spacing:.3px}

/* Feature / capability */
.rsb-features{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.rsb-feature{background:var(--white);padding:28px 24px;border-radius:var(--radius-lg);border:1px solid var(--gray-200);box-shadow:var(--shadow-sm);transition:all .35s ease}
.rsb-feature:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--orange-light)}
.rsb-feature__icon{width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,rgba(228,102,42,.12),rgba(228,102,42,.04));color:var(--orange);display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:800;margin-bottom:18px;font-style:normal;border:1px solid rgba(228,102,42,.25);transition:all .35s ease}
.rsb-feature:hover .rsb-feature__icon{background:var(--orange);color:var(--white);border-color:var(--orange)}
.rsb-feature h3{font-size:18px;margin-bottom:10px;color:var(--text-primary)}
.rsb-feature p{font-size:14px;color:var(--text-secondary);line-height:1.65}

/* FAQ */
.rsb-faq{max-width:920px;margin:0 auto;display:grid;gap:14px}
.rsb-faq__item{border:1px solid var(--gray-200);border-radius:var(--radius-lg);background:var(--white);padding:22px 26px;transition:all .3s ease}
.rsb-faq__item:hover{border-color:var(--orange);box-shadow:var(--shadow-sm)}
.rsb-faq__q{font-size:16px;font-weight:700;color:var(--text-primary);margin-bottom:8px;display:flex;align-items:flex-start;gap:12px}
.rsb-faq__q::before{content:"Q";flex-shrink:0;width:28px;height:28px;background:var(--orange);color:var(--white);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;margin-top:-2px}
.rsb-faq__a{font-size:14.5px;color:var(--text-secondary);line-height:1.7;padding-left:40px}

/* CTA */
.rsb-cta{position:relative;padding:110px 0;background:linear-gradient(105deg,rgba(5,26,62,.96) 0%,rgba(5,26,62,.82) 100%),var(--blue-dark);background-size:cover,cover;background-position:center,center;color:var(--white);text-align:center}
.rsb-cta__inner{position:relative;z-index:2;max-width:820px;margin:0 auto}
.rsb-cta__inner .rsb-eyebrow{color:var(--orange-light);margin-bottom:14px}
.rsb-cta h2{color:var(--white);font-size:46px;margin-bottom:18px;line-height:1.15}
.rsb-cta h2 span{color:var(--orange-light);font-style:italic;font-weight:600}
.rsb-cta p{font-size:17px;color:rgba(255,255,255,.85);line-height:1.7;margin-bottom:32px;max-width:640px;margin-left:auto;margin-right:auto}
.rsb-cta__actions{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-bottom:48px}
.rsb-cta__contacts{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;padding-top:42px;border-top:1px solid rgba(255,255,255,.18);text-align:left;max-width:1024px;margin:0 auto}
.rsb-cta__contact{display:flex;align-items:center;gap:14px}
.rsb-cta__contact i{width:48px;height:48px;background:rgba(228,102,42,.18);border:1px solid rgba(228,102,42,.4);color:var(--orange-light);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;font-style:normal;flex-shrink:0;transition:all .3s ease}
.rsb-cta__contact:hover i{background:var(--orange);color:var(--white);border-color:var(--orange);transform:scale(1.05)}
.rsb-cta__contact strong{display:block;color:rgba(255,255,255,.65);font-size:12px;font-weight:500;letter-spacing:1px;margin-bottom:4px;text-transform:uppercase}
.rsb-cta__contact span{font-size:14.5px;color:var(--white);font-weight:600}

/* Inquiry form (static) */
.rsb-form{max-width:820px;margin:0 auto;background:var(--white);border-radius:var(--radius-lg);padding:40px;border:1px solid var(--gray-200);box-shadow:var(--shadow-md)}
.rsb-form--dark{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.18);color:var(--white)}
.rsb-form h3{font-size:24px;margin-bottom:10px;text-align:center}
.rsb-form--dark h3{color:var(--white)}
.rsb-form > p{text-align:center;margin-bottom:28px;font-size:15px}
.rsb-form__grid{display:grid;grid-template-columns:1fr 1fr;gap:14px 18px;margin-bottom:18px}
.rsb-form__field{display:flex;flex-direction:column;gap:6px;text-align:left}
.rsb-form__field--full{grid-column:1/-1}
.rsb-form__field label{font-size:12.5px;color:var(--gray-700);font-weight:600;letter-spacing:.5px;text-transform:uppercase}
.rsb-form--dark .rsb-form__field label{color:rgba(255,255,255,.75)}
.rsb-form__field input,.rsb-form__field select,.rsb-form__field textarea{padding:12px 14px;background:var(--white);border:1px solid var(--gray-200);border-radius:var(--radius);color:var(--text-primary);font-family:inherit;font-size:14px;transition:all .25s ease}
.rsb-form--dark .rsb-form__field input,.rsb-form--dark .rsb-form__field select,.rsb-form--dark .rsb-form__field textarea{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.25);color:var(--white)}
.rsb-form--dark .rsb-form__field input::placeholder,.rsb-form--dark .rsb-form__field textarea::placeholder{color:rgba(255,255,255,.45)}
.rsb-form__field input:focus,.rsb-form__field select:focus,.rsb-form__field textarea:focus{outline:none;border-color:var(--orange)}
.rsb-form__field textarea{min-height:120px;resize:vertical;line-height:1.6}
.rsb-form__submit{display:block;width:100%;margin-top:10px}

/* Footer */
.rsb-footer{background:var(--blue-dark);color:rgba(255,255,255,.72);padding:72px 0 0;font-size:14.5px}
.rsb-footer__grid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1.2fr;gap:48px;padding-bottom:48px}
.rsb-footer h4{color:var(--white);font-size:16px;margin-bottom:20px;letter-spacing:.5px;font-weight:700;position:relative;padding-bottom:12px}
.rsb-footer h4::after{content:"";position:absolute;left:0;bottom:0;width:30px;height:2px;background:var(--orange);border-radius:2px}
.rsb-footer__about p{color:rgba(255,255,255,.68);line-height:1.7;margin-bottom:12px;font-size:14px}
.rsb-footer__logo{margin-bottom:18px;display:flex;align-items:center;gap:12px;color:var(--white);font-weight:800;font-size:21px}
.rsb-footer ul{list-style:none;padding:0}
.rsb-footer ul li{margin-bottom:10px}
.rsb-footer ul li a{color:rgba(255,255,255,.65);transition:color .25s ease,padding-left .25s ease;display:inline-flex;align-items:center;gap:6px;font-size:14px}
.rsb-footer ul li a::before{content:"\2192";color:var(--orange);opacity:0;transition:opacity .25s ease,margin-right .25s ease;margin-right:-10px}
.rsb-footer ul li a:hover{color:var(--orange-light);padding-left:4px}
.rsb-footer ul li a:hover::before{opacity:1;margin-right:0}
.rsb-footer__contact li{display:flex;gap:10px;align-items:flex-start;margin-bottom:14px;color:rgba(255,255,255,.7);line-height:1.6;font-size:14px}
.rsb-footer__contact li i{color:var(--orange);flex-shrink:0;margin-top:3px;font-style:normal;font-weight:700}
.rsb-footer__bottom{padding:22px 0;border-top:1px solid rgba(255,255,255,.1);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;font-size:13px;color:rgba(255,255,255,.55)}
.rsb-footer__social{display:flex;gap:14px}
.rsb-footer__social a{color:rgba(255,255,255,.65);font-weight:600;font-size:13px}
.rsb-footer__social a:hover{color:var(--orange-light)}

/* Cookie bar */
.rsb-cookie{position:fixed;bottom:20px;left:20px;right:20px;max-width:520px;margin:0 auto;background:var(--blue-dark);border:1px solid var(--orange);border-radius:var(--radius-lg);padding:20px 22px;color:var(--white);box-shadow:var(--shadow-lg);z-index:200;font-size:13.5px;line-height:1.55;display:flex;align-items:center;gap:14px}
.rsb-cookie p{flex:1;color:rgba(255,255,255,.9)}
.rsb-cookie p a{color:var(--orange-light);font-weight:600;text-decoration:underline}
.rsb-cookie button{padding:10px 20px;background:var(--orange);color:var(--white);border:none;border-radius:var(--radius);font-weight:700;font-size:13px;cursor:pointer;transition:background .25s ease;flex-shrink:0}
.rsb-cookie button:hover{background:var(--orange-dark)}

/* Legal doc styling */
.rsb-legal{max-width:920px;margin:0 auto}
.rsb-legal h2{font-size:26px;margin:40px 0 14px;color:var(--blue)}
.rsb-legal h3{font-size:20px;margin:28px 0 10px;color:var(--text-primary)}
.rsb-legal p{font-size:15.5px;color:var(--text-secondary);line-height:1.75;margin-bottom:14px}
.rsb-legal ul{padding-left:24px;margin-bottom:16px}
.rsb-legal ul li{margin-bottom:8px;font-size:15px;color:var(--text-secondary);line-height:1.7;list-style:disc}

/* Team */
.rsb-team{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.rsb-team__member{background:var(--white);border:1px solid var(--gray-200);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);transition:all .35s ease;text-align:center}
.rsb-team__member:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--orange-light)}
.rsb-team__photo{aspect-ratio:4/5;background:linear-gradient(135deg,var(--blue) 0%,var(--blue-dark) 100%);position:relative;overflow:hidden}
.rsb-team__photo-content{width:100%;height:100%;background-size:cover;background-position:center;transition:transform .6s ease}
.rsb-team__member:hover .rsb-team__photo-content{transform:scale(1.05)}
.rsb-team__body{padding:28px 22px}
.rsb-team__name{font-size:20px;color:var(--text-primary);font-weight:700;margin-bottom:4px}
.rsb-team__role{font-size:13px;color:var(--orange);font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px}
.rsb-team__bio{font-size:14px;color:var(--text-secondary);line-height:1.7;margin-bottom:16px}
.rsb-team__contact{font-size:13px;color:var(--gray-700)}
.rsb-team__contact i{color:var(--orange);font-style:normal;font-weight:700}

/* Timeline */
.rsb-timeline{position:relative;padding-left:40px}
.rsb-timeline::before{content:"";position:absolute;left:10px;top:0;bottom:0;width:2px;background:linear-gradient(180deg,var(--orange) 0%,var(--blue) 100%)}
.rsb-timeline__item{position:relative;margin-bottom:32px}
.rsb-timeline__item::before{content:"";position:absolute;left:-36px;top:6px;width:16px;height:16px;background:var(--white);border:3px solid var(--orange);border-radius:50%;box-shadow:0 0 0 4px rgba(228,102,42,.15)}
.rsb-timeline__year{display:inline-block;color:var(--orange);font-weight:800;font-size:14px;letter-spacing:1.2px;margin-bottom:6px;background:rgba(228,102,42,.08);padding:4px 12px;border-radius:50px}
.rsb-timeline__title{font-size:18px;color:var(--text-primary);font-weight:700;margin-bottom:6px}
.rsb-timeline__text{font-size:14.5px;color:var(--text-secondary);line-height:1.7}

/* Certification */
.rsb-certs{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.rsb-cert{background:var(--white);border:1px solid var(--gray-200);border-radius:var(--radius-lg);padding:28px 22px;text-align:center;box-shadow:var(--shadow-sm);transition:all .35s ease}
.rsb-cert:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--orange-light)}
.rsb-cert__badge{width:68px;height:68px;margin:0 auto 16px;border-radius:50%;background:linear-gradient(135deg,var(--blue) 0%,var(--blue-light) 100%);display:flex;align-items:center;justify-content:center;color:var(--white);font-size:22px;font-weight:800;letter-spacing:.5px;box-shadow:0 8px 20px rgba(8,36,87,.18);position:relative}
.rsb-cert__badge::after{content:"";position:absolute;inset:-6px;border-radius:50%;border:2px dashed rgba(228,102,42,.45);animation:rsbPulse 2s ease-in-out infinite}
.rsb-cert h3{font-size:15px;color:var(--text-primary);margin-bottom:6px;font-weight:700}
.rsb-cert p{font-size:12.5px;color:var(--gray-500);letter-spacing:.3px;line-height:1.5}

/* Blog article */
.rsb-article{background:var(--white);border:1px solid var(--gray-200);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);transition:all .35s ease}
.rsb-article:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--orange-light)}
.rsb-article__media{aspect-ratio:16/9;position:relative;background:var(--gray-200);overflow:hidden}
.rsb-article__img{width:100%;height:100%;background-size:cover;background-position:center;transition:transform .6s ease}
.rsb-article:hover .rsb-article__img{transform:scale(1.05)}
.rsb-article__category{position:absolute;top:16px;left:16px;background:var(--orange);color:var(--white);padding:6px 14px;border-radius:50px;font-size:11.5px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;z-index:2}
.rsb-article__body{padding:26px}
.rsb-article__meta{font-size:12.5px;color:var(--gray-500);margin-bottom:10px;letter-spacing:.3px}
.rsb-article__title{font-size:20px;color:var(--text-primary);font-weight:700;margin-bottom:10px;line-height:1.35}
.rsb-article__excerpt{font-size:14.5px;color:var(--text-secondary);line-height:1.7;margin-bottom:18px}

/* Chips / tags */
.rsb-chips{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}
.rsb-chip{padding:8px 16px;background:rgba(8,36,87,.05);color:var(--blue);border:1px solid rgba(8,36,87,.1);border-radius:50px;font-size:13px;font-weight:600;cursor:pointer;transition:all .25s ease}
.rsb-chip:hover{background:var(--orange);color:var(--white);border-color:var(--orange);transform:translateY(-2px)}

/* Responsive */
@media (max-width:1024px){
  .rsb-hero h1{font-size:46px}
  .rsb-section__head h2{font-size:32px}
  .rsb-section{padding:72px 0}
  .rsb-split,.rsb-split--reverse{grid-template-columns:1fr;gap:36px;margin-bottom:60px;direction:ltr}
  .rsb-split__body h2{font-size:28px}
  .rsb-grid--3,.rsb-grid--4,.rsb-features,.rsb-stats,.rsb-certs{grid-template-columns:repeat(2,1fr)}
  .rsb-team{grid-template-columns:repeat(2,1fr)}
  .rsb-hero__stats,.rsb-cta__contacts{grid-template-columns:repeat(2,1fr)}
  .rsb-footer__grid{grid-template-columns:1fr 1fr;gap:36px}
  .rsb-table{font-size:13px}
  .rsb-table th,.rsb-table td{padding:12px 14px}
  .rsb-form__grid{grid-template-columns:1fr}
}
@media (max-width:768px){
  .rsb-nav{display:none}
  .rsb-hero{min-height:auto;padding:70px 0 60px}
  .rsb-hero h1{font-size:34px}
  .rsb-hero p.lede{font-size:15.5px}
  .rsb-hero__actions .rsb-btn{width:100%}
  .rsb-section{padding:60px 0}
  .rsb-section__head{margin-bottom:42px}
  .rsb-section__head h2,.rsb-cta h2{font-size:28px}
  .rsb-grid--3,.rsb-grid--4,.rsb-features,.rsb-stats,.rsb-certs,.rsb-team,.rsb-grid--2{grid-template-columns:1fr}
  .rsb-hero__stats,.rsb-cta__contacts{grid-template-columns:1fr 1fr;gap:14px}
  .rsb-cta{padding:70px 0}
  .rsb-footer__grid{grid-template-columns:1fr}
  .rsb-table thead{display:none}
  .rsb-table,.rsb-table tbody,.rsb-table tr,.rsb-table td{display:block;width:100%}
  .rsb-table tr{margin-bottom:14px;border:1px solid var(--gray-200);border-radius:var(--radius-lg);overflow:hidden}
  .rsb-table td{padding:10px 16px;border-bottom:none}
  .rsb-table td:first-child{background:var(--blue);color:var(--white);border-right:none;font-size:13px;letter-spacing:.5px;text-transform:uppercase}
  .rsb-cookie{flex-direction:column;align-items:stretch;gap:12px;text-align:center;left:10px;right:10px;padding:16px}
  .rsb-cookie button{width:100%}
  .rsb-topbar__links{gap:10px;font-size:12px}
  .rsb-form{padding:26px}
}
@media (max-width:480px){
  .rsb-container{padding:0 16px}
  .rsb-hero h1{font-size:30px}
  .rsb-section__head h2,.rsb-cta h2{font-size:24px}
  .rsb-btn--lg{padding:14px 24px;font-size:14px;width:100%}
  .rsb-header__inner{height:70px}
  .rsb-logo{font-size:18px}
}
"""

# -------- Shared helpers --------
NAV_ORDER = [
    ("Home", "index.html"),
    ("Products", "products.html"),
    ("Solutions", "solutions.html"),
    ("Projects", "projects.html"),
    ("Blog", "blog.html"),
    ("FAQs", "faqs.html"),
    ("About Us", "about.html"),
    ("Get Quote", "get-quote.html"),
    ("Contact Us", "contact.html"),
]

def topbar():
    return f"""<div class="rsb-topbar" style="font-family:'Archivo',sans-serif">
  <div class="rsb-container">
    <div class="rsb-topbar__inner">
      <div class="rsb-topbar__links">
        <a href="tel:+8675586366707" aria-label="Call Yukings sales"><span aria-hidden="true">&#9742;</span> +86-755-86366707</a>
        <a href="mailto:weilai04525@163.com" aria-label="Email Yukings"><span aria-hidden="true">&#9993;</span> weilai04525@163.com</a>
        <span><span aria-hidden="true">&#9881;</span> Mon-Sat 8:30-18:30 (Beijing Time)</span>
      </div>
      <div class="rsb-topbar__links">
        <a href="faqs.html" aria-label="FAQs">FAQs</a>
        <a href="get-quote.html" aria-label="Request a quote">Request a Quote &rarr;</a>
        <span><span aria-hidden="true">&#127758;</span> EN / Ship to Worldwide</span>
      </div>
    </div>
  </div>
</div>"""

def header(active_file):
    nav = ""
    for name, f in NAV_ORDER:
        cls = "rsb-nav__item rsb-nav__item--active" if f == active_file else "rsb-nav__item"
        nav += f'<a href="{f}" class="{cls}">{name}</a>'
    return f"""<header class="rsb-header" style="font-family:'Archivo',sans-serif">
  <div class="rsb-container">
    <div class="rsb-header__inner">
      <a href="index.html" class="rsb-logo" aria-label="Yukings home">
        <span class="rsb-logo__mark">Y</span>
        <span class="rsb-logo__name">Yukings<small>Noise Barrier Manufacturer</small></span>
      </a>
      <nav class="rsb-nav" aria-label="Primary">{nav}</nav>
      <a href="get-quote.html" class="rsb-btn rsb-btn--primary rsb-btn--sm">Get a Quote</a>
    </div>
  </div>
</header>"""

def breadcrumb(items):
    """items: list of (label, href_or_None). last item is orange current page."""
    parts = []
    for i, (label, href) in enumerate(items):
        is_last = i == len(items) - 1
        if is_last:
            parts.append(f'<li><span class="rsb-breadcrumb__current">{html.escape(label)}</span></li>')
        else:
            parts.append(f'<li><a href="{href}">{html.escape(label)}</a></li>')
            parts.append('<li class="rsb-breadcrumb__sep">/</li>')
    return f"""<nav class="rsb-breadcrumb" aria-label="Breadcrumb" style="font-family:'Archivo',sans-serif">
  <div class="rsb-container">
    <ol class="rsb-breadcrumb__list">{"".join(parts)}</ol>
  </div>
</nav>"""

def hero(title, span_word, lede, bg_prompt, chips=None, actions=None, stats=None):
    if chips is None:
        chips = ["ISO 9001 / CE Certified", "18+ Years OEM Experience", "42,000 m\u00b2 Factory", "60+ Export Countries"]
    if actions is None:
        actions = [("primary", "Request a Free Quote", "get-quote.html"), ("ghost", "Browse Our Products", "products.html")]
    bg = f"url('https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={bg_prompt}&image_size=landscape_16_9')"
    actions_html = ""
    for style, label, href in actions:
        actions_html += f'<a href="{href}" class="rsb-btn rsb-btn--{style} rsb-btn--lg">{label}</a>'
    chips_html = "".join(f'<span class="rsb-hero__chip">{c}</span>' for c in chips)
    stats_html = ""
    if stats:
        items = "".join(f'<div class="rsb-hero__stat"><strong>{s[0]}</strong><span>{s[1]}</span></div>' for s in stats)
        stats_html = f'<div class="rsb-hero__stats">{items}</div>'
    title_html = title.replace("__SPAN__", f"<span>{span_word}</span>")
    return f"""<section class="rsb-hero" aria-labelledby="hero-title" style="font-family:'Archivo',sans-serif">
  <div class="rsb-hero__bg" style="background-image:{bg}" role="img" aria-label="{html.escape(span_word)} noise barrier hero"></div>
  <div class="rsb-container">
    <div class="rsb-hero__content">
      <span class="rsb-hero__eyebrow">Yukings \u00b7 Noise Barrier Manufacturer Since 2006</span>
      <h1 id="hero-title">{title_html}</h1>
      <p class="lede">{lede}</p>
      <div class="rsb-hero__actions">{actions_html}</div>
      <div class="rsb-hero__quick" aria-label="Highlights">{chips_html}</div>
      {stats_html}
    </div>
  </div>
</section>"""

def section_head(eyebrow, title, desc):
    return f"""<div class="rsb-section__head">
  <span class="rsb-eyebrow">{eyebrow}</span>
  <h2>{title}</h2>
  <div class="rsb-divider rsb-divider--center"></div>
  <p>{desc}</p>
</div>"""

def footer():
    return f"""<footer class="rsb-footer" style="font-family:'Archivo',sans-serif">
  <div class="rsb-container">
    <div class="rsb-footer__grid">
      <div class="rsb-footer__about">
        <div class="rsb-footer__logo"><span class="rsb-logo__mark">Y</span><span>Yukings</span></div>
        <p>Shenzhen Yukings Industrial Co., Ltd. is a professional manufacturer of noise barriers, sound walls and acoustic barriers. 42,000 m\u00b2 (452,084 sq.ft) factory, 18+ years OEM experience, ISO 9001 / ISO 14001 / CE certified. Exported to 60+ countries across North America, Europe, Australia, Southeast Asia and the Middle East.</p>
        <p>Room 1405, Building B2, Yunzhi Tech Park, Guangming District, Shenzhen, Guangdong, China</p>
      </div>
      <div>
        <h4>Products</h4>
        <ul>
          <li><a href="railway-noise-barriers.html">Railway Noise Barriers</a></li>
          <li><a href="highway-noise-barriers.html">Highway Noise Barriers</a></li>
          <li><a href="solar-noise-barriers.html">Solar Noise Barriers</a></li>
          <li><a href="industrial-noise-barriers.html">Industrial Noise Barriers</a></li>
          <li><a href="residential-noise-barriers.html">Residential Noise Barriers</a></li>
          <li><a href="products.html">All Product Lines</a></li>
        </ul>
      </div>
      <div>
        <h4>Solutions &amp; Projects</h4>
        <ul>
          <li><a href="railway-noise-reduction.html">Railway Noise Reduction</a></li>
          <li><a href="highway-noise-control.html">Highway Noise Control</a></li>
          <li><a href="industrial-factory-noise-barriers.html">Industrial Factory Solutions</a></li>
          <li><a href="residential-community-noise-protection.html">Residential Community Protection</a></li>
          <li><a href="solar-energy-noise-barrier-solutions.html">PV / Solar Noise Barriers</a></li>
          <li><a href="projects.html">Project Case Studies</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact Yukings</h4>
        <ul class="rsb-footer__contact">
          <li><i>&#9742;</i><span>Tel: +86-755-86366707</span></li>
          <li><i>&#9993;</i><span>Email: weilai04525@163.com</span></li>
          <li><i>&#9990;</i><span>Miss Tang (Sales): +86 17727812004</span></li>
          <li><i>&#9990;</i><span>Mr. Yu (Engineering): +86 13828819804</span></li>
          <li><i>&#9881;</i><span>Mon-Sat 8:30-18:30 Beijing Time</span></li>
        </ul>
      </div>
    </div>
    <div class="rsb-footer__bottom">
      <span>&copy; 2006-2026 Shenzhen Yukings Industrial Co., Ltd. All rights reserved. Noise Barrier Manufacturer. ISO 9001 \u00b7 ISO 14001 \u00b7 CE \u00b7 EN 14388 Certified.</span>
      <div class="rsb-footer__social">
        <a href="contact.html" aria-label="Contact">Contact</a>
        <a href="privacy-policy.html" aria-label="Privacy Policy">Privacy</a>
        <a href="terms-of-service.html" aria-label="Terms of Service">Terms</a>
        <a href="faqs.html" aria-label="FAQs">FAQs</a>
        <span>LinkedIn \u00b7 Facebook \u00b7 YouTube \u00b7 Instagram</span>
      </div>
    </div>
  </div>
</footer>"""

def cookie_bar():
    return f"""<div class="rsb-cookie" role="dialog" aria-label="Cookie consent">
  <p>Yukings.net uses cookies to improve your browsing experience and analyze anonymized traffic. By continuing to use this site you agree to our <a href="privacy-policy.html">privacy policy</a> and <a href="terms-of-service.html">terms</a>.</p>
  <button type="button">Accept</button>
</div>"""

def close_page():
    return f"""{cookie_bar()}
</body>
</html>"""

def write_page(filename, html_text):
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_text)
    print(f"  [wrote] {path} ({len(html_text)} chars)")

# -------- Page records (simplified model, but still with good data) --------

def page_head(title, description, canonical, extra_json_ld=None, extra_meta=None):
    keywords_html = extra_meta or ""
    og_url = f"https://www.yukings.net/{canonical}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="noise barrier, sound barrier, acoustic barrier, galvanized steel noise barrier, aluminum noise barrier, concrete sound wall, PC transparent noise barrier, highway noise barrier, railway noise barrier, industrial noise control, residential acoustic fence, solar noise barrier, Yukings manufacturer, OEM noise barrier, China noise barrier factory">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Shenzhen Yukings Industrial Co., Ltd.">
<link rel="canonical" href="{og_url}">
<link rel="alternate" hreflang="en" href="{og_url}">
<link rel="alternate" hreflang="x-default" href="{og_url}">

<meta property="og:type" content="website">
<meta property="og:title" content="{title.split('|')[0].strip()} | Yukings">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{og_url}">
<meta property="og:site_name" content="Yukings - Noise Barrier Manufacturer">
<meta property="og:image" content="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=modern%20industrial%20noise%20barrier%20factory%20site%20aerial&image_size=landscape_16_9">
<meta property="og:locale" content="en_US">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title.split('|')[0].strip()} | Yukings">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=modern%20industrial%20noise%20barrier%20factory%20site%20aerial&image_size=landscape_16_9">
{keywords_html}

<style>{SHARED_CSS}</style>

<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"Shenzhen Yukings Industrial Co., Ltd.","alternateName":"Yukings","url":"https://www.yukings.net","logo":"https://www.yukings.net/img/yukings-logo.svg","image":"https://www.yukings.net/img/yukings-factory.webp","description":"Noise barrier manufacturer based in Shenzhen, China. 18+ years of OEM experience, 42,000 m\u00b2 factory, ISO 9001/14001/45001 and CE certified.","foundingDate":"2006","foundingLocation":"Shenzhen, Guangdong, China","hasOfferCatalog":{{"@type":"OfferCatalog","name":"Yukings Noise Barrier Catalog","itemListElement":["Railway Noise Barriers","Highway Noise Barriers","Industrial Noise Barriers","Residential Noise Barriers","Solar Noise Barriers"]}},"slogan":"Engineered Acoustic Barriers for a Quieter World","telephone":"+86-755-86366707","email":"weilai04525@163.com","address":{{"@type":"PostalAddress","streetAddress":"Room 1405, Building B2, Yunzhi Tech Park, Guangming District","addressLocality":"Shenzhen","addressRegion":"Guangdong","postalCode":"518106","addressCountry":"CN"}},"geo":{{"@type":"GeoCoordinates","latitude":22.7673,"longitude":113.9696}},"sameAs":["https://www.linkedin.com/company/yukings","https://www.facebook.com/yukings","https://www.youtube.com/@yukings"],"contactPoint":[{{"@type":"ContactPoint","telephone":"+86-755-86366707","contactType":"customer service","availableLanguage":["English","Chinese"]}}]}}
</script>

<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.yukings.net/index.html"}]}}
</script>

{extra_json_ld or ""}

</head>
<body>
{topbar()}
{header(canonical)}
"""

def cta_section(title, subtitle):
    return f"""<section class="rsb-cta" style="font-family:'Archivo',sans-serif">
  <div class="rsb-container">
    <div class="rsb-cta__inner">
      <span class="rsb-eyebrow">Ready to Take the Next Step?</span>
      <h2>{title} <span>yukings</span> team today.</h2>
      <p>{subtitle}</p>
      <div class="rsb-cta__actions">
        <a href="get-quote.html" class="rsb-btn rsb-btn--primary rsb-btn--lg">Get a Free Project Quote</a>
        <a href="contact.html" class="rsb-btn rsb-btn--ghost rsb-btn--lg">Contact Our Engineers</a>
      </div>
      <div class="rsb-cta__contacts">
        <div class="rsb-cta__contact"><i>&#9742;</i><div><strong>Tel</strong><span>+86-755-86366707</span></div></div>
        <div class="rsb-cta__contact"><i>&#9993;</i><div><strong>Email</strong><span>weilai04525@163.com</span></div></div>
        <div class="rsb-cta__contact"><i>&#9990;</i><div><strong>Miss Tang (Sales)</strong><span>+86 17727812004</span></div></div>
        <div class="rsb-cta__contact"><i>&#9990;</i><div><strong>Mr. Yu (Engineering)</strong><span>+86 13828819804</span></div></div>
      </div>
    </div>
  </div>
</section>"""

def faq_section(faq_items):
    items = "".join(f'<div class="rsb-faq__item"><div class="rsb-faq__q">{q}</div><div class="rsb-faq__a">{a}</div></div>' for q,a in faq_items)
    return f"""<section class="rsb-section rsb-section--gray" style="font-family:'Archivo',sans-serif">
  <div class="rsb-container">
    {section_head("Frequently Asked Questions", "Answers to the questions we hear most often", "Explore answers to common questions about our noise barrier products, certifications, lead times, OEM customization and logistics. Our team responds to detailed inquiries within 24 hours.")}
    <div class="rsb-faq">{items}</div>
  </div>
</section>"""

def stat_section(stats, eyebrow="At a Glance", title="Manufacturing capacity, quality data and export footprint", desc="Numbers matter in industrial procurement. Here is a transparent overview of Yukings capacity, certifications, experience and global reach to support your due diligence."):
    items = "".join(f'<div class="rsb-stat"><strong>{s[0]}</strong><span>{s[1]}</span></div>' for s in stats)
    return f"""<section class="rsb-section" style="font-family:'Archivo',sans-serif">
  <div class="rsb-container">
    {section_head(eyebrow, title, desc)}
    <div class="rsb-stats">{items}</div>
  </div>
</section>"""

def feature_section(features):
    items = "".join(f'<div class="rsb-feature"><i class="rsb-feature__icon">{f[0]}</i><h3>{f[1]}</h3><p>{f[2]}</p></div>' for f in features)
    return f"""<div class="rsb-features">{items}</div>"""

def card(card_title, meta, text, link_label, href, prompt, tag):
    return f"""<div class="rsb-card">
  <div class="rsb-card__media">
    <div class="rsb-card__img" style="background-image:url('https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={prompt}&image_size=landscape_16_9')" role="img" aria-label="{html.escape(card_title)}"></div>
    <span class="rsb-card__tag">{tag}</span>
  </div>
  <div class="rsb-card__body">
    <span class="rsb-card__meta">{meta}</span>
    <h3 class="rsb-card__title">{card_title}</h3>
    <p class="rsb-card__text">{text}</p>
    <a href="{href}" class="rsb-card__link">{link_label} &rarr;</a>
  </div>
</div>"""

def split_block(prompt, eyebrow, heading, paragraphs, bullets, actions=None, reverse=False):
    """Editorial split: image + text body."""
    rev = " rsb-split--reverse" if reverse else ""
    li = "".join(f"<li>{b}</li>" for b in bullets)
    para = "".join(f"<p>{p}</p>" for p in paragraphs)
    act = ""
    if actions:
        act = f'<div class="rsb-split__actions">{"".join(f"<a href=\"{a[2]}\" class=\"rsb-btn rsb-btn--{a[0]}\">{a[1]}</a>" for a in actions)}</div>'
    return f"""<div class="rsb-split{rev}">
  <div class="rsb-split__media"><div class="rsb-split__img" style="background-image:url('https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={prompt}&image_size=landscape_4_3')" role="img" aria-label="{html.escape(heading)}"></div></div>
  <div class="rsb-split__body">
    <span class="rsb-split__eyebrow">{eyebrow}</span>
    <h2>{heading}</h2>
    <div class="rsb-divider"></div>
    {para}
    <ul class="rsb-split__list">{li}</ul>
    {act}
  </div>
</div>"""

def specs_table(spec_title, headers, rows):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body_rows = ""
    for r in rows:
        body_rows += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return f"""<div class="rsb-tablewrap">
  <div style="padding:14px