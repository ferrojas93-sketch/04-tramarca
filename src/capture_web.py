"""
Capture real screenshot of tramarca.es home → assets/tramarca-web-home.jpg.
"""
from __future__ import annotations
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT  = ROOT / "dist" / "assets" / "tramarca-web-home.jpg"
OUT.parent.mkdir(parents=True, exist_ok=True)


async def shoot():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 900},
                                       device_scale_factor=2)
        await page.goto("https://tramarca.es", wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(1500)
        tmp = OUT.with_suffix(".png")
        await page.screenshot(path=str(tmp), full_page=False)
        await browser.close()

    im = Image.open(tmp)
    if max(im.size) > 1800:
        im.thumbnail((1800, 1800), Image.LANCZOS)
    im.convert("RGB").save(OUT, quality=85, optimize=True)
    tmp.unlink()
    print(f"Web shot: {OUT} · {im.size}")


if __name__ == "__main__":
    asyncio.run(shoot())
