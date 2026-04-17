"""
Render tramarca-v4.html → tramarca-v4.pdf (A4 landscape).
"""
from __future__ import annotations
import asyncio
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "dist" / "tramarca-v4.html"
PDF  = ROOT / "dist" / "tramarca-v4.pdf"


async def render():
    url = HTML.as_uri()
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 990},
                                       device_scale_factor=2)
        await page.goto(url, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.wait_for_timeout(2200)
        await page.pdf(
            path=str(PDF),
            width="297mm",
            height="210mm",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        await browser.close()
    print(f"PDF: {PDF} ({PDF.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    asyncio.run(render())
