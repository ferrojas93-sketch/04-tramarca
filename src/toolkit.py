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
# PIEDRA darkened 2026-04 post WCAG AA audit (ratio 3.6→5.2)
NEGRO        = "#0C0C0C"
CARBON       = "#1C1C1C"
LACRE        = "#C4553A"
PIEDRA       = "#5E5A57"  # AA compliant for text
PIEDRA_LIGHT = "#7A7672"  # decorative only, non-text
CENIZA       = "#B5B1AC"
ARENA        = "#E4E2DC"
PAPEL        = "#F4F0EB"

# Typography
FAM = "'Satoshi', -apple-system, system-ui, sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, monospace"

FONT_LINKS = """\
<link rel="preconnect" href="https://api.fontshare.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700,900&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;700&display=swap">"""

# Identity — v4 aligned to tramarca.es /sobre + /home
BRAND      = "TRAMARCA"
DESCRIPTOR = "Un estudio que solo hace manuales."  # /sobre H1
TAGLINE    = "Tu marca, por escrito."               # /home H1
EDITION    = "Primera edición · 2026"
MASTHEAD   = "Manuales de marca · Por escrito · Desde 2026"
CITY       = "Madrid · España"
TOTAL      = 58   # v4 — anatomy-aligned to 12 chapters + personas data-viz + TL;DR

# Sections — v4 aligned to tramarca.es /anatomia 12 chapters + editorial frame
SECTIONS = [
    {"n": "00",  "r": "",      "title": "Apertura",             "pages": (1, 5),   "fid": "FIEL"},
    {"n": "01",  "r": "I",     "title": "Provocación",          "pages": (6, 9),   "fid": "FIEL"},
    {"n": "02",  "r": "II",    "title": "Personas",             "pages": (10, 13), "fid": "PROPUESTA"},
    {"n": "03",  "r": "III",   "title": "Fundamentos",          "pages": (14, 18), "fid": "PROPUESTA"},
    {"n": "04",  "r": "IV",    "title": "Sistema de logo",      "pages": (19, 23), "fid": "PROPUESTA"},
    {"n": "05",  "r": "V",     "title": "Tipografía",           "pages": (24, 26), "fid": "FIEL"},
    {"n": "06",  "r": "VI",    "title": "Color",                "pages": (27, 29), "fid": "FIEL"},
    {"n": "07",  "r": "VII",   "title": "Iconografía",          "pages": (30, 31), "fid": "PROPUESTA"},
    {"n": "08",  "r": "VIII",  "title": "Fotografía",           "pages": (32, 33), "fid": "PROPUESTA"},
    {"n": "09",  "r": "IX",    "title": "Voz y tono",           "pages": (34, 36), "fid": "PROPUESTA"},
    {"n": "10",  "r": "X",     "title": "Aplicaciones",         "pages": (37, 41), "fid": "PROPUESTA"},
    {"n": "11",  "r": "XI",    "title": "Arquitectura",         "pages": (42, 43), "fid": "PROPUESTA"},
    {"n": "12",  "r": "XII",   "title": "Governance",           "pages": (44, 46), "fid": "PROPUESTA"},
    {"n": "13",  "r": "XIII",  "title": "Marca en movimiento",  "pages": (47, 48), "fid": "INVENTADO"},
    {"n": "14",  "r": "XIV",   "title": "Extensiones",          "pages": (49, 51), "fid": "PROPUESTA"},
    {"n": "15",  "r": "XV",    "title": "Servicio",             "pages": (52, 55), "fid": "FIEL"},
    {"n": "16",  "r": "XVI",   "title": "Portfolio",            "pages": (56, 56), "fid": "FIEL"},
    {"n": "17",  "r": "",      "title": "Cierre",               "pages": (57, 58), "fid": "FIEL"},
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
    padding: 6px 0 6px 14px;
    border-left: 3px solid {LACRE};
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

/* ── Mockup frame system (no box-shadow — Chromium renders it as solid grey rectangle in PDF print).
       Use borders only. ── */
.mockup-shadow {{
    border: 0.5px solid {CENIZA};
}}
.mockup-deep-shadow {{
    border: 0.75px solid {CENIZA};
}}

/* ── Invoice / document mockup ── */
.doc-mockup {{
    background: {PAPEL};
    border: 0.5px solid {CENIZA};
}}

/* ── Browser chrome (email, web) — minimal editorial, no grey fill ── */
.browser-chrome {{
    height: 7mm;
    background: {PAPEL};
    border: 0.5px solid {CENIZA};
    border-bottom: 0.5px solid {CENIZA};
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

/* ═══ v4 additions — Shamusic v6 playbook patterns ═══ */

/* ── Fidelity badge — FIEL / PROPUESTA / INVENTADO ── */
.badge-fidelidad {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-family: {MONO};
    font-size: 6.5px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    padding: 2px 6px;
    border-radius: 2px;
    line-height: 1.2;
}}
.badge-fiel       {{ background: rgba(12,12,12,0.08); color: {NEGRO}; }}
.badge-propuesta  {{ background: rgba(196,85,58,0.15); color: {LACRE}; border: 0.5px solid {LACRE}; }}
.badge-inventado  {{ background: rgba(122,118,114,0.15); color: {PIEDRA}; border: 0.5px dashed {PIEDRA}; }}
/* Dark-page variants */
.badge-fiel-dark      {{ background: rgba(244,240,235,0.1); color: {PAPEL}; }}
.badge-propuesta-dark {{ background: rgba(196,85,58,0.25); color: {PAPEL}; border: 0.5px solid {LACRE}; }}

/* ── Stat card tensional (personas data-viz) ── */
.stat-tensional {{
    min-height: 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 4mm 5mm 3mm 5mm;
    background: rgba(12,12,12,0.04);
    border-left: 3px solid {LACRE};
    position: relative;
}}
.stat-tensional .big {{
    font-family: {FAM};
    font-size: 38px;
    font-weight: 900;
    line-height: 0.9;
    color: {NEGRO};
    letter-spacing: -1px;
    font-variant-numeric: tabular-nums;
}}
.stat-tensional .big .unit {{
    font-size: 22px;
    color: {LACRE};
    letter-spacing: 0;
}}
.stat-tensional .label {{
    font-family: {MONO};
    font-size: 7px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: {PIEDRA};
    line-height: 1.3;
    margin-top: 2mm;
}}
.stat-tensional .bar {{
    height: 2px;
    background: {CENIZA};
    margin: 3mm 0 1mm 0;
    position: relative;
}}
.stat-tensional .bar::before {{
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    background: {LACRE};
}}

/* ── Number watermark outline (persona pages) ── */
.watermark-outline {{
    position: absolute;
    font-family: {FAM};
    font-weight: 900;
    font-size: 140pt;
    line-height: 0.78;
    color: transparent;
    -webkit-text-stroke: 1px {CENIZA};
    pointer-events: none;
    user-select: none;
    z-index: 0;
}}

/* ── Timeline 24h horizontal bar ── */
.timeline-24h {{
    display: flex;
    width: 100%;
    height: 10mm;
    border: 0.5px solid {CENIZA};
    position: relative;
    font-family: {MONO};
    font-size: 6.5px;
    letter-spacing: 0.5px;
}}
.timeline-24h .block {{
    display: flex;
    align-items: center;
    justify-content: center;
    color: {PAPEL};
    text-transform: uppercase;
    font-weight: 700;
    border-right: 0.5px solid rgba(244,240,235,0.15);
    overflow: hidden;
    white-space: nowrap;
}}
.timeline-24h .block:last-child {{ border-right: none; }}
.timeline-24h .tick {{
    position: absolute;
    top: 100%;
    font-family: {MONO};
    font-size: 6.5px;
    color: {PIEDRA};
    transform: translateX(-50%);
    margin-top: 1mm;
    font-variant-numeric: tabular-nums;
}}

/* ── Metastrip hard-lock (survives .grain > * override bug) ── */
.metastrip {{
    position: absolute !important;
    z-index: 99 !important;
    bottom: 11mm;
    left: 24mm;
    right: 24mm;
    border-top: 0.5px solid {CENIZA};
    padding-top: 3mm;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-family: {MONO};
    font-size: 7px;
    color: {PIEDRA};
    letter-spacing: 0.5px;
}}
.metastrip.dark {{
    border-top-color: rgba(244,240,235,0.12);
    color: rgba(244,240,235,0.45);
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
            subtitle: str = "", pg: int = 0, img: str = "") -> str:
    """Dark full-bleed section divider — cinematic, asymmetric, brutal.
    Optional image backdrop: opacity 0.32 + diagonal midnight gradient overlay."""
    # Photographic backdrop layer — prominent, full-bleed (Shamusic style)
    photo = ""
    if img:
        photo = f"""\
<div style="position:absolute;inset:0;overflow:hidden;background:{NEGRO};">
  <img src="{img}" style="width:100%;height:100%;object-fit:cover;
    opacity:0.92;filter:grayscale(22%) contrast(1.08) brightness(0.78);" alt="">
</div>
<div style="position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(12,12,12,0.15) 0%,rgba(12,12,12,0) 30%,rgba(12,12,12,0.2) 55%,rgba(12,12,12,0.88) 100%);
  pointer-events:none;"></div>"""

    # Giant number bleeds off right edge
    wm = ""
    if arabic and arabic != "00":
        wm = f"""\
<div style="position:absolute;right:-30mm;top:-20mm;
  font-family:{FAM};font-size:800px;font-weight:900;
  color:rgba(244,240,235,0.035);line-height:0.7;
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
{photo}{wm}{eye}{slash}
<div style="position:absolute;left:30mm;bottom:30mm;">
  {bar}
  <div style="font-family:{FAM};font-size:110px;font-weight:900;
    color:{PAPEL};letter-spacing:-4px;line-height:0.9;">
    {title}<span style="color:{LACRE};font-size:140px;">.</span>
  </div>
  {sub}
</div>
<div style="position:absolute;right:30mm;bottom:30mm;text-align:right;">
  <div style="font-family:{MONO};font-size:9px;color:rgba(244,240,235,0.35);letter-spacing:2px;">
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
    return f'<div style="background:transparent;border-left:3px solid {LACRE};padding:{padding};padding-left:14px;">{content}</div>'


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


def fidelity_badge(kind: str, *, dark: bool = False) -> str:
    """Fidelity tag — disabled per feedback 2026-04-17. Now returns empty string."""
    return ""


def stat_tensional(big: str, unit: str, label: str, fill_pct: int = 60) -> str:
    """Tension stat card — big number + unit + label + bar indicator."""
    return f"""\
<div class="stat-tensional">
  <div class="big">{big}<span class="unit">{unit}</span></div>
  <div class="bar" style="--fill:{fill_pct}%;">
    <style>.stat-tensional .bar::before {{ width: var(--fill); }}</style>
  </div>
  <div class="label">{label}</div>
</div>"""


def timeline_24h(blocks: list[tuple[int, str, str, str]]) -> str:
    """24h horizontal timeline. blocks: [(hours, label, bg, fg?), ...].
    hours must sum to 24."""
    total = sum(h for h, *_ in blocks)
    if total != 24:
        # normalize defensively
        total = 24
    segs = []
    cursor = 0
    ticks = []
    for h, lbl, bg, *rest in blocks:
        pct = h / 24 * 100
        fg = rest[0] if rest else PAPEL
        show_label = h >= 4
        segs.append(
            f'<div class="block" style="width:{pct}%;background:{bg};color:{fg};">'
            f'{lbl if show_label else ""}</div>'
        )
        cursor += h
        ticks.append((cursor, cursor))
    tick_html = "".join(
        f'<span class="tick" style="left:{c/24*100}%;">{c:02d}:00</span>'
        for c, _ in ticks[:-1]
    )
    return f'<div class="timeline-24h" style="margin-bottom:6mm;">{"".join(segs)}{tick_html}</div>'


def watermark_number(num: str, *, right: str = "18mm", top: str = "30mm") -> str:
    """Outline number watermark for persona pages (220pt Satoshi Black outline)."""
    return f"""\
<div class="watermark-outline" style="right:{right};top:{top};">{num}</div>"""


def metastrip(pg: int, section: str = "", *, dark: bool = False) -> str:
    """Always-on metastrip — foot-of-page chrome.
    Uses .metastrip class with !important to survive .grain > * override bug."""
    cls = "metastrip dark" if dark else "metastrip"
    mc = f"rgba(244,240,235,0.45)" if dark else PIEDRA
    return f"""\
<div class="{cls}">
  <span>{BRAND}<span style="color:{LACRE};">.</span> · Manual de marca</span>
  <span style="text-transform:uppercase;letter-spacing:2px;">{section}</span>
  <span>{pg:02d} / {TOTAL}</span>
</div>"""


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
