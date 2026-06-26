import asyncio
from playwright.async_api import async_playwright
import urllib.parse

async def main():
    prompt = "professional photograph of highway noise barrier wall, blue sky, modern road infrastructure"
    url = f"https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={urllib.parse.quote(prompt)}&image_size=landscape_16_9"
    print(f"Testing URL: {url[:100]}...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        for i in range(8):
            print(f"\nAttempt {i+1}...")
            await page.goto(url, wait_until="networkidle", timeout=60000)
            await page.wait_for_timeout(5000)
            
            title = await page.title()
            current_url = page.url
            print(f"Title: {title}")
            print(f"Current URL: ...{current_url[-80:]}")
            
            if "default.jpeg" in current_url:
                print(f"Still default placeholder, waiting 18s...")
                await page.wait_for_timeout(18000)
            else:
                print(f"Got different URL! Checking image...")
                await page.screenshot(path="/tmp/pw_test.png")
                await page.wait_for_timeout(2000)
                
                img_elements = await page.query_selector_all("img")
                if img_elements:
                    src = await img_elements[0].get_attribute("src")
                    print(f"Image src: {src}")
                else:
                    body_html = await page.content()
                    if "1368" in body_html and "768" in body_html:
                        print("Found 1368x768 reference!")
                
                import requests
                session = requests.Session()
                resp = session.get(current_url, timeout=60)
                from PIL import Image
                from io import BytesIO
                img = Image.open(BytesIO(resp.content))
                w, h = img.size
                print(f"Downloaded image size: {w}x{h}")
                if w >= 1300 and h >= 700 and w != 1832:
                    img.save("/tmp/pw_success.jpg", "JPEG", quality=95)
                    print("SUCCESS! Image saved.")
                    break
            
        await browser.close()

asyncio.run(main())
