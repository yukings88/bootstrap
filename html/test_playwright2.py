import asyncio
from playwright.async_api import async_playwright
import urllib.parse
import time

async def main():
    prompt = "professional photograph of highway noise barrier wall, blue sky, modern road infrastructure"
    url = f"https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={urllib.parse.quote(prompt)}&image_size=landscape_16_9"
    print(f"Testing with longer waits and hard reloads...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        for i in range(15):
            print(f"\nAttempt {i+1}/15 at {time.strftime('%H:%M:%S')}...")
            
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=90000)
                await page.wait_for_timeout(8000)
                
                title = await page.title()
                current_url = page.url
                print(f"Title: {title}")
                print(f"URL end: ...{current_url[-60:]}")
                
                if "default.jpeg" not in current_url and "1832" not in title:
                    print("Got non-default URL! Downloading...")
                    
                    async with page.expect_download(timeout=30000) as download_info:
                        pass
                    
                    import requests
                    resp = requests.get(current_url, timeout=60)
                    from PIL import Image
                    from io import BytesIO
                    img = Image.open(BytesIO(resp.content))
                    w, h = img.size
                    print(f"Downloaded image: {w}x{h}")
                    if w >= 1300 and h >= 700:
                        img.save("/tmp/pw_success.jpg", "JPEG", quality=95)
                        print("SUCCESS!")
                        break
                else:
                    wait_sec = 20 + (i * 2)
                    print(f"Still default. Waiting {wait_sec}s then hard reload...")
                    await page.wait_for_timeout(wait_sec * 1000)
                    
            except Exception as e:
                print(f"Error: {e}")
                await page.wait_for_timeout(15000)
        
        await browser.close()

asyncio.run(main())
