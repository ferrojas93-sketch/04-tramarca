"""
TRAMARCA. Design System Toolkit v3
====================================
BRUTAL edition. Advanced CSS, visual tension, maximum drama.
Every visual decision lives here — pages only assemble content.
"""
from __future__ import annotations

# ═══════════════════════════════════════════════════════════════
# BRAND TOKENS
# ═══════════════════════════════════════════════════════════════

# Colors — El Punto Final
NEGRO  = "#0C0C0C"
CARBON = "#1C1C1C"
LACRE  = "#C4553A"
PIEDRA = "#7A7672"
CENIZA = "#B5B1AC"
ARENA  = "#E4E2DC"
PAPEL  = "#F4F0EB"

# Typography
FAM = "'Satoshi', -apple-system, system-ui, sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, monospace"

FONT_LINKS = """\
<link rel="preconnect" href="https://api.fontshare.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700,900&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;700&display=swap">"""

# Identity
BRAND      = "TRAMARCA"
DESCRIPTOR = "Tu marca, sin improvisar."
EDITION    = "Primera edición · Abril 2026"
TOTAL      = 45   # v4 — 11 páginas nuevas añadidas (F7/S6/V3/V6/I7/A8/O1/O2/O3/V9 + divider)

# Sections — v3 condensada (34 páginas)
SECTIONS = [
    {"n": "00", "r": "",     "title": "Apertura",           "pages": (1, 2)},
    {"n": "01", "r": "I",    "title": "Provocación",        "pages": (3, 4)},
    {"n": "02", "r": "II",   "title": "Fundamentos",        "pages": (5, 8)},
    {"n": "03", "r": "III",  "title": "Servicio",           "pages": (9, 11)},
    {"n": "04", "r": "IV",   "title": "Identidad visual",   "pages": (12, 16)},
    {"n": "05", "r": "V",    "title": "Color",              "pages": (17, 18)},
    {"n": "06", "r": "VI",   "title": "Tipografía",         "pages": (19, 21)},
    {"n": "07", "r": "VII",  "title": "Voz",                "pages": (22, 24)},
    {"n": "08", "r": "VIII", "title": "Dirección de arte",  "pages": (25, 26)},
    {"n": "09", "r": "IX",   "title": "Aplicaciones",       "pages": (27, 31)},
    {"n": "10", "r": "X",    "title": "Portfolio",           "pages": (32, 32)},
    {"n": "11", "r": "",     "title": "Cierre",             "pages": (33, 34)},
]


# ═══════════════════════════════════════════════════════════════
# GLOBAL CSS — BRUTAL EDITION
# ═══════════════════════════════════════════════════════════════

GLOBAL_CSS = f"""\
:root {{
    --negro:  {NEGRO};
    --carbon: {CARBON};
    --lacre:  {LACRE};
    --piedra: {PIEDRA};
    --ceniza: {CENIZA};
    --arena:  {ARENA};
    --papel:  {PAPEL};
    --fam:    {FAM};
    --mono:   {MONO};
}}

@page {{ size: 297mm 210mm; margin: 0; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ background: #555; }}

.page {{
    width: 297mm;
    height: 210mm;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    margin: 4mm auto;
    box-shadow: 0 4px 24px rgba(0,0,0,0.5);
}}

@media print {{
    body {{ background: white; }}
    .page {{ margin: 0; box-shadow: none; }}
}}

/* ── Typography — dramatic scale ── */
p {{ margin: 0; }}

.titulo {{
    font-family: {FAM};
    font-weight: 900;
    line-height: 1.0;
    color: {NEGRO};
    letter-spacing: -2px;
}}
.titulo .p {{ color: {LACRE}; }}

.body-text {{
    font-family: {FAM};
    font-size: 13px;
    font-weight: 400;
    line-height: 1.7;
    color: {CARBON};
}}

.eyebrow {{
    font-family: {MONO};
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: {LACRE};
}}

.meta {{
    font-family: {MONO};
    font-size: 9px;
    font-weight: 400;
    color: {PIEDRA};
}}

/* ── Pull Quote — bigger, bolder ── */
.pq {{
    font-family: {FAM};
    font-size: 28px;
    font-weight: 900;
    line-height: 1.2;
    color: {NEGRO};
    border-left: 5px solid {LACRE};
    padding-left: 20px;
}}
.pq .p {{ color: {LACRE}; font-size: 130%; }}

/* ── Data Block ── */
.db {{
    font-family: {MONO};
    font-size: 11px;
    line-height: 2.2;
    background: {ARENA};
    padding: 14px 18px;
    border-left: 4px solid {LACRE};
}}
.db .lbl {{
    display: inline-block;
    min-width: 90px;
    color: {PIEDRA};
    font-size: 9px;
    letter-spacing: 1px;
    text-transform: uppercase;
}}

/* ── Struck text ── */
.struck {{
    text-decoration: line-through;
    text-decoration-color: {LACRE};
    text-decoration-thickness: 3px;
    color: {PIEDRA};
}}

/* ── Grid ── */
.g2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8mm; }}
.g3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8mm; }}
.g4 {{ display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 6mm; }}

/* ── Card ── */
.card {{
    background: #fff;
    border: 1px solid rgba(12,12,12,0.08);
    padding: 16px 20px;
}}
.dark-card {{
    background: {NEGRO};
    color: {PAPEL};
    padding: 16px 20px;
}}

/* ── Accent Rule ── */
.ar {{
    width: 80px;
    height: 3px;
    background: {LACRE};
}}

/* ── Photo — with advanced treatments ── */
.photo {{
    overflow: hidden;
    background: {ARENA};
    position: relative;
}}
.photo img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    filter: grayscale(15%) contrast(1.08);
}}
.photo::after {{
    content: '';
    position: absolute;
    inset: 0;
    mix-blend-mode: multiply;
    pointer-events: none;
}}

/* ═══ ADVANCED VISUAL EFFECTS ═══ */

/* ── Diagonal cut ── */
.diagonal-cut {{
    clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
}}
.diagonal-cut-inv {{
    clip-path: polygon(0 15%, 100% 0, 100% 100%, 0 100%);
}}

/* ── Lacre slash — the brand's signature diagonal ── */
.lacre-slash {{
    position: absolute;
    width: 200%;
    height: 4px;
    background: {LACRE};
    transform-origin: center;
    transform: rotate(-12deg);
    pointer-events: none;
}}

/* ── Noise texture overlay (SVG feTurbulence grain) ── */
.noise::before {{
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/%3E%3C/svg%3E");
    background-size: 256px 256px;
    background-repeat: repeat;
    pointer-events: none;
    z-index: 1;
}}
/* ── Heavy noise variant for covers/dividers ── */
.noise-heavy::before {{
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.06'/%3E%3C/svg%3E");
    background-size: 256px 256px;
    background-repeat: repeat;
    pointer-events: none;
    z-index: 1;
}}

/* ── Vignette overlay ── */
.vignette::after {{
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, transparent 50%, rgba(12,12,12,0.4) 100%);
    pointer-events: none;
}}

/* ── Glow accent ── */
.glow-lacre {{
    box-shadow: 0 0 80px 20px rgba(196,85,58,0.15);
}}

/* ── Oversized watermark numbers ── */
.watermark {{
    position: absolute;
    font-family: {FAM};
    font-weight: 900;
    color: rgba(255,255,255,0.04);
    pointer-events: none;
    user-select: none;
    line-height: 0.8;
}}

/* ── Full-bleed image with overlay ── */
.fullbleed {{
    position: absolute;
    inset: 0;
}}
.fullbleed img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
}}
.fullbleed .overlay {{
    position: absolute;
    inset: 0;
    pointer-events: none;
}}

/* ── Perspective mockup ── */
.perspective-card {{
    transform: perspective(800px) rotateY(-8deg) rotateX(4deg);
    box-shadow:
        0 20px 60px rgba(12,12,12,0.3),
        0 8px 20px rgba(12,12,12,0.2);
    transition: transform 0.3s;
}}

/* ── Split page layouts ── */
.split-h {{
    position: absolute;
    inset: 0;
    display: grid;
    grid-template-columns: 1fr 1fr;
}}
.split-h > :first-child {{
    overflow: hidden;
}}
.split-60-40 {{
    position: absolute;
    inset: 0;
    display: grid;
    grid-template-columns: 60% 40%;
}}
.split-40-60 {{
    position: absolute;
    inset: 0;
    display: grid;
    grid-template-columns: 40% 60%;
}}

/* ── Bleed columns — edge-to-edge color blocks ── */
.bleed-left {{
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 50%;
}}
.bleed-right {{
    position: absolute;
    right: 0;
    top: 0;
    bottom: 0;
    width: 50%;
}}

/* ── Floating label ── */
.float-label {{
    position: absolute;
    font-family: {MONO};
    font-size: 7px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: {LACRE};
    writing-mode: vertical-rl;
    text-orientation: mixed;
}}

/* ── Large section number ── */
.section-num {{
    font-family: {FAM};
    font-weight: 900;
    font-size: 280px;
    line-height: 0.8;
    letter-spacing: -10px;
    color: rgba(196,85,58,0.12);
}}

/* ── Thick border accent ── */
.border-lacre-left {{
    border-left: 6px solid {LACRE};
    padding-left: 20px;
}}

/* ── Animated-style gradient slab ── */
.slab-gradient {{
    background: linear-gradient(135deg, {NEGRO} 0%, {CARBON} 40%, rgba(196,85,58,0.15) 100%);
}}

/* ── Color swatch — large and expressive ── */
.swatch {{
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 12px 16px;
    min-height: 60mm;
}}
.swatch .name {{
    font-family: {FAM};
    font-size: 18px;
    font-weight: 900;
}}
.swatch .hex {{
    font-family: {MONO};
    font-size: 10px;
    letter-spacing: 1px;
    opacity: 0.7;
}}

/* ── Mockup shadow system ── */
.mockup-shadow {{
    box-shadow:
        0 25px 50px -12px rgba(12,12,12,0.25),
        0 12px 24px -8px rgba(12,12,12,0.15),
        0 4px 8px rgba(12,12,12,0.1);
}}
.mockup-deep-shadow {{
    box-shadow:
        0 50px 100px -20px rgba(12,12,12,0.4),
        0 25px 50px -12px rgba(12,12,12,0.3),
        0 12px 24px rgba(12,12,12,0.15);
}}

/* ── Invoice / document mockup ── */
.doc-mockup {{
    background: #fff;
    box-shadow:
        0 30px 80px rgba(12,12,12,0.5),
        0 15px 30px rgba(12,12,12,0.3);
    border: 0.5px solid rgba(244,240,235,0.06);
}}

/* ── Browser chrome (email, web) ── */
.browser-chrome {{
    height: 8mm;
    background: {ARENA};
    border: 1px solid {CENIZA};
    border-bottom: none;
    display: flex;
    align-items: center;
    padding: 0 4mm;
    gap: 2mm;
}}
.browser-dot {{
    width: 3mm;
    height: 3mm;
    border-radius: 50%;
    background: {CENIZA};
}}

/* ── Vertical micro text ── */
.vertical-text {{
    writing-mode: vertical-rl;
    text-orientation: mixed;
    font-family: {MONO};
    font-size: 7px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: {LACRE};
}}

/* ── Diagonal lacre bar (reusable) ── */
.lacre-bar {{
    width: 5px;
    background: {LACRE};
}}

/* ── Dark gradient backdrop for mockup pages ── */
.mockup-backdrop {{
    background: linear-gradient(160deg, {CARBON} 0%, {NEGRO} 60%, rgba(196,85,58,0.05) 100%);
}}
"""


# ═══════════════════════════════════════════════════════════════
# PAGE SHELL
# ═══════════════════════════════════════════════════════════════

def page_shell(body: str, pg: int, *,
               section: str = "", bg: str = PAPEL,
               dark: bool = False, no_furniture: bool = False) -> str:
    """Wrap content in a page div with header + 3-part footer."""
    tc = PAPEL if dark else NEGRO
    mc = f"rgba(244,240,235,0.45)" if dark else PIEDRA
    bc = f"rgba(244,240,235,0.12)" if dark else CENIZA

    if no_furniture:
        return f'<div class="page" style="background:{bg};color:{tc};">{body}</div>'

    # Header — light pages with section
    hdr = ""
    if not dark and section:
        hdr = f"""\
<div style="position:absolute;top:18mm;left:24mm;right:24mm;display:flex;justify-content:space-between;align-items:baseline;">
  <span style="font-family:{MONO};font-size:7px;font-weight:400;letter-spacing:2px;text-transform:uppercase;color:{mc};">{section}</span>
  <span style="font-family:{FAM};font-size:9px;font-weight:700;color:{NEGRO};">{BRAND}<span style="color:{LACRE};">.</span></span>
</div>"""

    # Footer — 3-part with border-top
    ftr = f"""\
<div style="position:absolute;bottom:11mm;left:24mm;right:24mm;
  border-top:0.5px solid {bc};padding-top:3mm;
  display:flex;justify-content:space-between;align-items:baseline;
  font-family:{MONO};font-size:7px;color:{mc};letter-spacing:0.5px;">
  <span>{BRAND}<span style="color:{LACRE};">.</span> · Manual de marca</span>
  <span style="text-transform:uppercase;letter-spacing:2px;">{section}</span>
  <span>{pg:02d} / {TOTAL}</span>
</div>"""

    return f'<div class="page" style="background:{bg};color:{tc};">{hdr}{body}{ftr}</div>'


# ═══════════════════════════════════════════════════════════════
# SECTION DIVIDER — CINEMATIC
# ═══════════════════════════════════════════════════════════════

def divider(arabic: str, roman: str, title: str,
            subtitle: str = "", pg: int = 0) -> str:
    """Dark full-bleed section divider — cinematic, asymmetric, brutal."""
    # Giant number bleeds off right edge
    wm = ""
    if arabic and arabic != "00":
        wm = f"""\
<div style="position:absolute;right:-30mm;top:-20mm;
  font-family:{FAM};font-size:800px;font-weight:900;
  color:rgba(244,240,235,0.03);line-height:0.7;
  pointer-events:none;user-select:none;">{arabic}</div>"""

    # Roman numeral as floating vertical label
    eye = ""
    if roman:
        eye = f"""\
<div style="position:absolute;top:20mm;left:14mm;
  font-family:{MONO};font-size:8px;font-weight:700;letter-spacing:3px;
  text-transform:uppercase;color:{LACRE};
  writing-mode:vertical-rl;text-orientation:mixed;">{roman}</div>"""

    # Lacre diagonal slash across the page
    slash = f"""\
<div style="position:absolute;left:-20%;top:60%;
  width:200%;height:3px;background:{LACRE};
  transform:rotate(-8deg);opacity:0.4;"></div>"""

    sub = ""
    if subtitle:
        sub = f"""\
<div style="font-family:{MONO};font-size:11px;font-weight:400;
  color:{CENIZA};margin-top:8mm;letter-spacing:2px;">{subtitle}</div>"""

    # Lacre vertical bar — tall accent
    bar = f'<div style="width:5px;height:40mm;background:{LACRE};margin-bottom:10mm;"></div>'

    content = f"""\
{wm}{eye}{slash}
<div style="position:absolute;left:30mm;bottom:30mm;">
  {bar}
  <div style="font-family:{FAM};font-size:110px;font-weight:900;
    color:{PAPEL};letter-spacing:-4px;line-height:0.9;">
    {title}<span style="color:{LACRE};font-size:140px;">.</span>
  </div>
  {sub}
</div>
<div style="position:absolute;right:30mm;bottom:30mm;text-align:right;">
  <div style="font-family:{MONO};font-size:9px;color:rgba(244,240,235,0.3);letter-spacing:2px;">
    {pg:02d} / {TOTAL}
  </div>
</div>"""

    return page_shell(content, pg, bg=NEGRO, dark=True, no_furniture=True)


# ═══════════════════════════════════════════════════════════════
# CONTENT HELPERS
# ═══════════════════════════════════════════════════════════════

def titulo(text: str, size: int = 42, color: str = NEGRO,
           mb: str = "10mm") -> str:
    """Page title with oversized Lacre period."""
    ps = int(size * 1.25)
    return f"""\
<div class="titulo" style="font-size:{size}px;color:{color};margin-bottom:{mb};letter-spacing:{-2 if size > 30 else 0}px;">
  {text}<span class="p" style="font-size:{ps}px;">.</span>
</div>"""


def pull_quote(text: str, width: str = "260px") -> str:
    """Bold pull quote with Lacre left bar — bigger, bolder."""
    return f"""\
<div class="pq" style="max-width:{width};">{text}<span class="p">.</span></div>"""


def data_block(rows: list[tuple[str, str]]) -> str:
    """IBM Plex Mono data readout on Arena background."""
    lines = "".join(
        f'<div><span class="lbl">{lbl}</span> {val}</div>'
        for lbl, val in rows
    )
    return f'<div class="db">{lines}</div>'


def accent_rule(w: int = 80, mt: str = "8mm") -> str:
    """Lacre horizontal accent line."""
    return f'<div class="ar" style="width:{w}px;margin-top:{mt};"></div>'


def arena_panel(content: str, padding: str = "18px 22px") -> str:
    """Content block on Arena background."""
    return f'<div style="background:{ARENA};padding:{padding};">{content}</div>'


def body_text(text: str, max_w: str = "220mm") -> str:
    """Standard body paragraph."""
    return f'<div class="body-text" style="max-width:{max_w};">{text}</div>'


def photo(src: str, w: str = "100%", h: str = "100%",
          pos: str = "center") -> str:
    """Image container with brand filter."""
    return f"""\
<div class="photo" style="width:{w};height:{h};">
  <img src="{src}" style="object-position:{pos};" alt="">
</div>"""


def photo_bleed(src: str, overlay: str = "", pos: str = "center") -> str:
    """Full-bleed photo with optional dark overlay."""
    ov = ""
    if overlay:
        ov = f'<div class="overlay" style="{overlay}"></div>'
    return f"""\
<div class="fullbleed">
  <img src="{src}" style="object-position:{pos};filter:grayscale(20%) contrast(1.1);" alt="">
  {ov}
</div>"""


def content_area(left: str = "24mm", top: str = "30mm",
                 right: str = "24mm", bottom: str = "20mm") -> tuple[str, str]:
    """Return (open_tag, close_tag) for absolutely-positioned content area."""
    o = f'<div style="position:absolute;left:{left};top:{top};right:{right};bottom:{bottom};">'
    return o, '</div>'


def split_page(left_html: str, right_html: str,
               left_bg: str = NEGRO, right_bg: str = PAPEL,
               ratio: str = "50% 50%") -> str:
    """Two-column split page with independent backgrounds."""
    return f"""\
<div style="position:absolute;inset:0;display:grid;grid-template-columns:{ratio};">
  <div style="background:{left_bg};position:relative;overflow:hidden;">{left_html}</div>
  <div style="background:{right_bg};position:relative;overflow:hidden;">{right_html}</div>
</div>"""


def giant_letter(char: str, size: int = 500, color: str = "rgba(196,85,58,0.08)",
                 right: str = "-40mm", top: str = "-60mm") -> str:
    """Massive decorative letter/number bleed."""
    return f"""\
<div style="position:absolute;right:{right};top:{top};
  font-family:{FAM};font-size:{size}px;font-weight:900;
  color:{color};line-height:0.8;pointer-events:none;user-select:none;">{char}</div>"""


# ═══════════════════════════════════════════════════════════════
# HTML WRAPPER
# ═══════════════════════════════════════════════════════════════

def html_wrap(pages: list[str]) -> str:
    """Full HTML document."""
    return f"""\
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>TRAMARCA. — Manual de marca</title>
{FONT_LINKS}
<style>
{GLOBAL_CSS}
</style>
</head>
<body>
{"".join(pages)}
</body>
</html>"""


def generate_pdf(html_path: str, pdf_path: str) -> None:
    """Generate A4 landscape PDF from HTML using Playwright."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path}", wait_until="networkidle")
        page.wait_for_timeout(2000)  # let fonts load
        page.pdf(
            path=pdf_path,
            format="A4",
            landscape=True,
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()
        import os
        size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"PDF generated: {pdf_path} ({size_mb:.1f} MB)")
