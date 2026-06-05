#!/usr/bin/env bash
# Yukings HTML图片路径替换脚本
# 用途：批量将 ./cdn/ 替换为Shoptop素材中心返回的CDN基础URL
# 用法：将 SHOPTOP_CDN_BASE 变量替换为用户从Shoptop素材中心抓取的实际CDN域名，例如
#       https://img.yukings-domain.com  或  https://cdn.shoplazza.com/yukings
#       然后执行本脚本即可一次性更新全部5个HTML文件

SHOPTOP_CDN_BASE="${1:-https://img.yukings-domain.com}"

echo "===================================="
echo "Yukings HTML图片路径批量替换"
echo "目标CDN: $SHOPTOP_CDN_BASE"
echo "===================================="

cd /workspace/html

for f in *.html; do
  count=$(grep -c "./cdn/" "$f" 2>/dev/null || echo 0)
  if [ "$count" -gt 0 ]; then
    sed -i "s|\./cdn/|$SHOPTOP_CDN_BASE/|g" "$f"
    echo "[OK] $f - 替换 $count 处"
  else
    echo "[--] $f - 无需替换"
  fi
done

echo "===================================="
echo "完成。请用浏览器打开html/*.html验证图片已切换为线上CDN。"
