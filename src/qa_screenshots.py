"""
Capture per-page PNG screenshots for visual-qa review.
Output: dist/qa/p01.png ... p58.png
"""
from __future__ import annotations
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "dist" / "tramarca-v4.html"
QA   = ROOT / "dist" / "qa"
QA.mkdir(parents=True, exist_ok=True)

# Claude multi-image reads reject >2000px. `.page` CSS es 297×210mm → DSR=2
# produce ~2246×1588. Capturamos con nitidez y downscalamos a 1990px máx.
MAX_EDGE = 1990


async def shoot():
    url = HTML.as_uri()
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 990},
                                       device_scale_factor=2)
        await page.goto(url, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.wait_for_timeout(1500)

        pages = await page.locator(".page").count()
        for i in range(pages):
            el = page.locator(".page").nth(i)
            await el.scroll_into_view_if_needed()
            await page.wait_for_timeout(120)
            out = QA / f"p{i+1:02d}.png"
            await el.screenshot(path=str(out))
            im = Image.open(out)
            if max(im.size) > MAX_EDGE:
                im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
                im.save(out, optimize=True)
        await browser.close()
    print(f"QA shots written: {pages} → {QA} (max edge {MAX_EDGE}px)")


if __name__ == "__main__":
    asyncio.run(shoot())
