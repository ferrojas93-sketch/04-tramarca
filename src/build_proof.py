"""
TRAMARCA. Brand Manual — PROOF OF CONCEPT v3
==============================================
6 pages to validate the brutal visual direction.
"""
from __future__ import annotations
from pathlib import Path
from toolkit import *

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
OUT  = DIST / "tramarca-proof.html"


# ══════════════════════════════════════════════════════════════
# P01 — COVER: Asymmetric, massive, tense
# ══════════════════════════════════════════════════════════════

def p01_cover():
    """Cover — asymmetric wordmark, diagonal lacre slash, noise texture."""
    body = f"""\
<!-- Noise texture -->
<div class="noise" style="position:absolute;inset:0;"></div>

<!-- Vignette -->
<div style="position:absolute;inset:0;
  background:radial-gradient(ellipse at 30% 70%, transparent 30%, rgba(0,0,0,0.5) 100%);
  pointer-events:none;"></div>

<!-- Giant T watermark bleeding off top-right -->
<div style="position:absolute;right:-60mm;top:-80mm;
  font-family:{FAM};font-size:900px;font-weight:900;
  color:rgba(196,85,58,0.04);line-height:0.7;
  pointer-events:none;user-select:none;">T</div>

<!-- Diagonal lacre slash -->
<div style="position:absolute;left:-10%;top:55%;
  width:120%;height:4px;background:{LACRE};
  transform:rotate(-6deg);opacity:0.6;"></div>

<!-- Second thinner slash -->
<div style="position:absolute;left:-10%;top:57%;
  width:120%;height:1px;background:{LACRE};
  transform:rotate(-6deg);opacity:0.3;"></div>

<!-- Main wordmark — pushed to bottom-left, HUGE -->
<div style="position:absolute;left:24mm;bottom:38mm;">
  <div style="font-family:{FAM};font-size:160px;font-weight:900;
    color:{PAPEL};letter-spacing:-6px;line-height:0.85;">
    {BRAND}<span style="color:{LACRE};font-size:200px;position:relative;top:10px;">.</span>
  </div>
</div>

<!-- Descriptor — right-aligned, high up -->
<div style="position:absolute;right:24mm;top:24mm;text-align:right;">
  <div style="font-family:{MONO};font-size:9px;font-weight:400;
    letter-spacing:4px;color:rgba(244,240,235,0.4);text-transform:uppercase;">
    Manual de marca
  </div>
  <div style="font-family:{MONO};font-size:9px;font-weight:400;
    letter-spacing:4px;color:rgba(244,240,235,0.25);text-transform:uppercase;margin-top:3mm;">
    2026
  </div>
</div>

<!-- Vertical label on left edge -->
<div style="position:absolute;left:10mm;bottom:40mm;
  font-family:{MONO};font-size:7px;font-weight:700;letter-spacing:3px;
  text-transform:uppercase;color:{LACRE};
  writing-mode:vertical-rl;text-orientation:mixed;opacity:0.7;">
  Tu marca, sin improvisar
</div>

<!-- Bottom right — edition data micro -->
<div style="position:absolute;right:24mm;bottom:14mm;text-align:right;">
  <div style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.2);letter-spacing:1px;">
    {EDITION}
  </div>
</div>"""
    return page_shell(body, 1, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# P02 — COLOPHON: Split dark/darker with data
# ══════════════════════════════════════════════════════════════

def p02_colophon():
    """Colophon — split layout, left technical data, right brand statement."""
    left = f"""\
<div style="padding:24mm 20mm 24mm 24mm;height:100%;display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    <div class="eyebrow" style="color:{LACRE};margin-bottom:10mm;">Colofon</div>
    <div style="font-family:{MONO};font-size:10px;line-height:2.8;color:{CENIZA};">
      <div><span style="display:inline-block;min-width:28mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">Edicion</span>{EDITION}</div>
      <div><span style="display:inline-block;min-width:28mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">Disenado por</span>Tramarca</div>
      <div><span style="display:inline-block;min-width:28mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">Paginas</span>{TOTAL}</div>
      <div><span style="display:inline-block;min-width:28mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">Tipografias</span>Satoshi + IBM Plex Mono</div>
      <div><span style="display:inline-block;min-width:28mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">Colores</span>7</div>
      <div><span style="display:inline-block;min-width:28mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">Formato</span>A4 apaisado · 297 x 210 mm</div>
    </div>
  </div>
  <div style="width:40px;height:3px;background:{LACRE};"></div>
</div>"""

    right = f"""\
<div style="padding:24mm 24mm 24mm 20mm;height:100%;display:flex;flex-direction:column;justify-content:center;">
  <div style="border-left:5px solid {LACRE};padding-left:20px;">
    <div style="font-family:{FAM};font-size:24px;font-weight:900;
      color:{PAPEL};line-height:1.3;margin-bottom:8mm;">
      Este documento define que es Tramarca, como se ve,
      como habla y como se aplica<span style="color:{LACRE};font-size:30px;">.</span>
    </div>
    <div style="font-family:{FAM};font-size:14px;font-weight:400;
      color:{CENIZA};line-height:1.7;">
      Cada decision esta por escrito. Cada regla tiene una razon.
      Si no podemos explicar por que, lo quitamos.
    </div>
  </div>
</div>"""

    body = split_page(left, right, left_bg=NEGRO, right_bg=CARBON, ratio="45% 55%")
    return page_shell(body, 2, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# P04 — PROVOCACION DIVIDER: Cinematic
# ══════════════════════════════════════════════════════════════

def p04_provocacion():
    """Section divider — Provocacion. Cinematic, brutal."""
    return divider("01", "I", "Provocacion",
                   "Por que este manual existe", pg=4)


# ══════════════════════════════════════════════════════════════
# P18 — LOGO: The shrine
# ══════════════════════════════════════════════════════════════

def p18_logo_primary():
    """Logo presentation — the brand's sacred object. Dramatic, architectural."""
    body = f"""\
<!-- Noise texture -->
<div class="noise" style="position:absolute;inset:0;"></div>

<!-- Subtle radial glow from center -->
<div style="position:absolute;inset:0;
  background:radial-gradient(ellipse at 50% 45%,
    rgba(196,85,58,0.06) 0%, transparent 60%);
  pointer-events:none;"></div>

<!-- Ghost watermark — massive behind the logo -->
<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-52%);
  font-family:{FAM};font-size:400px;font-weight:900;
  color:rgba(244,240,235,0.025);letter-spacing:-12px;
  pointer-events:none;user-select:none;white-space:nowrap;">{BRAND}</div>

<!-- Primary wordmark — centered, massive, clean -->
<div style="position:absolute;left:50%;top:46%;transform:translate(-50%,-50%);text-align:center;">
  <!-- The wordmark -->
  <div style="font-family:{FAM};font-size:96px;font-weight:900;
    color:{PAPEL};letter-spacing:-3px;line-height:1;position:relative;">
    {BRAND}<span style="color:{LACRE};font-size:120px;position:relative;top:6px;">.</span>
  </div>
</div>

<!-- Thin horizontal line across the page at golden ratio -->
<div style="position:absolute;left:0;right:0;top:62%;height:0.5px;
  background:linear-gradient(90deg, transparent 0%, rgba(244,240,235,0.08) 20%, rgba(244,240,235,0.08) 80%, transparent 100%);"></div>

<!-- Concept label — vertical left -->
<div style="position:absolute;left:14mm;top:50%;transform:translateY(-50%);
  font-family:{MONO};font-size:7px;font-weight:700;letter-spacing:3px;
  text-transform:uppercase;color:{LACRE};
  writing-mode:vertical-rl;text-orientation:mixed;">El punto final</div>

<!-- Technical specs — bottom left, minimal -->
<div style="position:absolute;left:24mm;bottom:18mm;">
  <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.35);line-height:2.4;letter-spacing:0.5px;">
    <span style="color:{PIEDRA};">TIPOGRAFIA</span> Satoshi Black 900<br>
    <span style="color:{PIEDRA};">CONCEPTO</span> El Punto Final<br>
    <span style="color:{PIEDRA};">PUNTO</span> 125% cap-height · Lacre {LACRE}
  </div>
</div>

<!-- Section label — top right -->
<div style="position:absolute;right:24mm;top:18mm;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.25);letter-spacing:2px;text-transform:uppercase;">
    IV · Identidad visual
  </span>
</div>

<!-- Page number — bottom right -->
<div style="position:absolute;right:24mm;bottom:18mm;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.2);letter-spacing:1px;">
    18 / {TOTAL}
  </span>
</div>"""
    return page_shell(body, 18, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# P25 — COLOR PALETTE: Full-bleed swatches
# ══════════════════════════════════════════════════════════════

def p25_color():
    """Color palette — split layout: title on left dark panel, stripes on right."""
    colors = [
        (NEGRO,  "Negro",  PAPEL,  "#0C0C0C"),
        (CARBON, "Carbón", PAPEL,  "#1C1C1C"),
        (LACRE,  "Lacre",  PAPEL,  "#C4553A"),
        (PIEDRA, "Piedra", PAPEL,  "#7A7672"),
        (CENIZA, "Ceniza", NEGRO,  "#B5B1AC"),
        (ARENA,  "Arena",  NEGRO,  "#E4E2DC"),
        (PAPEL,  "Papel",  NEGRO,  "#F4F0EB"),
    ]

    # Right side: 7 vertical stripes, each with name + hex, NO overlapping text
    stripes = ""
    for i, (bg, name, tc, hex_val) in enumerate(colors):
        stripes += f"""\
<div style="flex:1;background:{bg};display:flex;flex-direction:column;
  justify-content:flex-end;padding:8mm 3mm;">
  <div style="font-family:{FAM};font-size:13px;font-weight:900;color:{tc};
    margin-bottom:2mm;">{name}</div>
  <div style="font-family:{MONO};font-size:7px;letter-spacing:1px;color:{tc};opacity:0.6;">
    {hex_val}</div>
</div>"""

    # Left panel: title + section label, completely separate from stripes
    left = f"""\
<div style="width:35%;background:{NEGRO};display:flex;flex-direction:column;
  justify-content:space-between;padding:24mm 24mm 20mm 24mm;flex-shrink:0;">
  <div>
    <div style="font-family:{MONO};font-size:8px;font-weight:700;letter-spacing:3px;
      text-transform:uppercase;color:{LACRE};margin-bottom:12mm;">V · Paleta de color</div>
    <div style="font-family:{FAM};font-size:64px;font-weight:900;
      color:{PAPEL};letter-spacing:-3px;line-height:0.9;">
      Paleta<br>de color<span style="color:{LACRE};font-size:80px;">.</span>
    </div>
  </div>
  <div>
    <div style="width:40px;height:3px;background:{LACRE};margin-bottom:6mm;"></div>
    <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};line-height:2;">
      7 colores<br>0 degradados<br>1 acento
    </div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;inset:0;display:flex;">
  {left}
  <div style="flex:1;display:flex;">{stripes}</div>
</div>
"""
    return page_shell(body, 25, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# P43 — BUSINESS CARD: Premium mockup with depth
# ══════════════════════════════════════════════════════════════

def p43_business_card():
    """Business card — premium 3D mockup with shadow and perspective."""
    body = f"""\
<!-- Dark background with subtle gradient -->
<div style="position:absolute;inset:0;
  background:linear-gradient(160deg, {CARBON} 0%, {NEGRO} 60%, rgba(196,85,58,0.05) 100%);"></div>

<!-- Noise -->
<div class="noise" style="position:absolute;inset:0;"></div>

<!-- Subtle spotlight from top-right -->
<div style="position:absolute;inset:0;
  background:radial-gradient(ellipse at 70% 20%, rgba(244,240,235,0.04) 0%, transparent 50%);"></div>

<!-- Section label -->
<div style="position:absolute;left:24mm;top:20mm;">
  <div class="eyebrow">IX · Aplicaciones</div>
</div>
<div style="position:absolute;left:24mm;top:30mm;">
  {titulo("Tarjeta de visita", 44, PAPEL, "0")}
</div>

<!-- Card stack — front card with perspective -->
<div style="position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);">
  <!-- Back card — slightly rotated, behind -->
  <div style="position:absolute;left:30mm;top:8mm;
    width:85mm;height:55mm;background:{CARBON};
    transform:rotate(6deg);
    box-shadow:0 20px 60px rgba(0,0,0,0.4);
    border:0.5px solid rgba(244,240,235,0.05);">
    <!-- Back content — contact info -->
    <div style="padding:8mm;height:100%;display:flex;flex-direction:column;justify-content:space-between;">
      <div>
        <div style="font-family:{FAM};font-size:11px;font-weight:700;color:{PAPEL};">Fernando Rojas</div>
        <div style="font-family:{FAM};font-size:8px;color:{PIEDRA};margin-top:2mm;">Director</div>
      </div>
      <div style="font-family:{MONO};font-size:7px;color:{CENIZA};line-height:2;">
        hola@tramarca.es<br>
        tramarca.es<br>
        +34 600 000 000
      </div>
    </div>
  </div>

  <!-- Front card — main, prominent -->
  <div style="position:relative;
    width:85mm;height:55mm;background:{NEGRO};
    transform:rotate(-3deg);
    box-shadow:
      0 30px 80px rgba(0,0,0,0.5),
      0 15px 30px rgba(0,0,0,0.3),
      0 5px 10px rgba(0,0,0,0.2);
    border:0.5px solid rgba(244,240,235,0.06);">
    <!-- Front content — logo centered -->
    <div style="height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;">
      <div style="font-family:{FAM};font-size:18px;font-weight:900;color:{PAPEL};letter-spacing:-0.5px;">
        {BRAND}<span style="color:{LACRE};font-size:22px;">.</span>
      </div>
      <div style="font-family:{MONO};font-size:6px;color:{PIEDRA};margin-top:3mm;letter-spacing:2px;text-transform:uppercase;">
        Tu marca, sin improvisar
      </div>
    </div>
    <!-- Subtle Lacre line at bottom -->
    <div style="position:absolute;bottom:0;left:0;right:0;height:2px;background:{LACRE};"></div>
  </div>
</div>

<!-- Specs — bottom left -->
<div style="position:absolute;left:24mm;bottom:18mm;">
  <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.35);line-height:2.4;letter-spacing:0.5px;">
    <span style="color:{PIEDRA};">TAMANO</span> 85 x 55 mm<br>
    <span style="color:{PIEDRA};">PAPEL</span> 400g cotton uncoated<br>
    <span style="color:{PIEDRA};">TINTA</span> Negro mate + Lacre hot foil
  </div>
</div>

<!-- Page number -->
<div style="position:absolute;right:24mm;bottom:18mm;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.2);letter-spacing:1px;">
    43 / {TOTAL}
  </span>
</div>"""
    return page_shell(body, 43, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# P05 — THE PROBLEM: Split page with photo bleed
# ══════════════════════════════════════════════════════════════

def p05_the_problem():
    """The problem — dramatic split, photo bleeds into text."""
    left = f"""\
<!-- Full bleed photo -->
<img src="assets/img-03.jpg" style="width:100%;height:100%;object-fit:cover;
  filter:grayscale(25%) contrast(1.15);" alt="">
<!-- Dark gradient overlay from right -->
<div style="position:absolute;inset:0;
  background:linear-gradient(90deg, transparent 40%, {NEGRO} 95%);"></div>
<!-- Lacre accent line on left edge -->
<div style="position:absolute;left:0;top:0;bottom:0;width:4px;background:{LACRE};"></div>
"""

    right = f"""\
<div style="padding:28mm 24mm 24mm 16mm;height:100%;display:flex;flex-direction:column;justify-content:center;">
  <div style="font-family:{FAM};font-size:44px;font-weight:900;
    color:{PAPEL};line-height:1.05;letter-spacing:-2px;margin-bottom:10mm;">
    Lo que no se<br>documenta,<br>
    <span style="font-weight:400;color:{PIEDRA};">se improvisa</span><span style="color:{LACRE};font-size:56px;">.</span>
  </div>
  <div style="font-family:{FAM};font-size:13px;font-weight:400;
    color:{CENIZA};line-height:1.8;max-width:120mm;margin-bottom:10mm;">
    La mayoria de las marcas existen solo en la cabeza de quien las creo.
    No en un documento. No por escrito. En la cabeza.<br><br>
    Sin reglas escritas, cada persona que toca la marca la interpreta
    a su manera. El resultado es ruido visual. Inconsistencia. Improvisacion.
  </div>
  <div style="width:50px;height:3px;background:{LACRE};margin-bottom:8mm;"></div>
  <div style="font-family:{FAM};font-size:20px;font-weight:700;
    color:{PAPEL};line-height:1.3;border-left:4px solid {LACRE};padding-left:16px;">
    Tu marca no existe<span style="color:{LACRE};font-size:24px;">.</span><br>
    Existe en tu cabeza<span style="color:{LACRE};font-size:24px;">.</span><br>
    Pero eso no cuenta<span style="color:{LACRE};font-size:24px;">.</span>
  </div>
</div>
"""

    body = split_page(left, right, left_bg=NEGRO, right_bg=NEGRO, ratio="45% 55%")

    # Eyebrow on top
    body += f"""\
<div style="position:absolute;right:24mm;top:18mm;z-index:2;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.3);letter-spacing:2px;text-transform:uppercase;">
    I · Provocacion
  </span>
</div>
<div style="position:absolute;left:24mm;bottom:14mm;z-index:2;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.15);letter-spacing:1px;">
    TRAMARCA<span style="color:{LACRE};">.</span> · Manual de marca
  </span>
</div>
<div style="position:absolute;right:24mm;bottom:14mm;z-index:2;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.15);letter-spacing:1px;">
    05 / {TOTAL}
  </span>
</div>"""
    return page_shell(body, 5, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════

def build():
    pages = [
        p01_cover(),
        p02_colophon(),
        p04_provocacion(),
        p05_the_problem(),
        p18_logo_primary(),
        p25_color(),
        p43_business_card(),
    ]

    DIST.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html_wrap(pages), encoding="utf-8")
    print(f"✓ Built {len(pages)} proof pages → {OUT}")


if __name__ == "__main__":
    build()
