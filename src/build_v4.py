"""
TRAMARCA. Brand Manual — v4 (Shamusic v6 playbook applied)
==========================================================
58 pages, A4 landscape. Anatomy-aligned to 12 chapters from tramarca.es.

v4 additions vs v3:
- Cover v9 (typographic minimal, no chrome, no mantra on cover)
- Spread 00 "Estado del sistema" (FIEL / PROPUESTA / INVENTADO ledger)
- Personas data-viz (3 client archetypes, stat cards + timeline 24h + watermark)
- 12-chapter anatomy from /anatomia (adds Iconografía, Arquitectura, Movimiento, Extensiones)
- Real pricing 490/990/1990€ + guarantee 50%/14d
- TL;DR V9 "La marca en 10 líneas" closer
- Metastrip !important fix (survives .grain > * bug)
"""
from __future__ import annotations
from pathlib import Path
from toolkit import *
from toolkit import fidelity_badge, stat_tensional, timeline_24h, watermark_number, metastrip

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
OUT  = DIST / "tramarca-v4.html"
PDF  = DIST / "tramarca-v4.pdf"

ASSETS = "assets"

# ══════════════════════════════════════════════════════════════
# 00 APERTURA  (pp 01-05)
# ══════════════════════════════════════════════════════════════

def p01_cover_v9():
    """Cover — logo positivo (negro sobre papel cálido) + hero wax-drop photo + sober rule."""
    body = f"""\
<!-- Warm off-white paper backdrop -->
<div style="position:absolute;inset:0;background:{PAPEL};"></div>

<!-- Hero photograph — right half full bleed -->
<div style="position:absolute;left:50%;top:0;right:0;bottom:0;overflow:hidden;">
  <img src="{ASSETS}/generated/cover-hero.png" style="width:100%;height:100%;object-fit:cover;
    filter:contrast(1.04);" alt="">
</div>

<!-- Subtle vertical rule at halfway line -->
<div style="position:absolute;left:50%;top:0;bottom:0;width:0.5px;background:rgba(12,12,12,0.08);"></div>

<!-- Centered wordmark (positive: negro sobre papel) — left half -->
<div style="position:absolute;left:0;width:50%;top:50%;transform:translateY(-50%);text-align:center;padding:0 16mm;">
  <div style="font-family:{FAM};font-size:78px;font-weight:900;
    color:{NEGRO};letter-spacing:-3px;line-height:0.95;">
    {BRAND}<span style="color:{LACRE};font-size:94px;line-height:1;">.</span>
  </div>
  <div style="width:36mm;height:1px;background:{LACRE};margin:10mm auto 6mm auto;"></div>
  <div style="font-family:{FAM};font-size:15px;font-weight:500;color:{NEGRO};letter-spacing:-0.3px;line-height:1.3;">
    Tu marca,<br>por escrito<span style="color:{LACRE};">.</span>
  </div>
</div>"""
    return page_shell(body, 1, bg=PAPEL, no_furniture=True)


def p02_mantra():
    """p02 — The mantra. Full-page editorial statement, the first thing after the cover."""
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;">
  <div class="eyebrow" style="margin-bottom:4mm;">Apertura · 01</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:42mm;bottom:26mm;
  display:flex;flex-direction:column;justify-content:center;">
  <div style="font-family:{FAM};font-size:82px;font-weight:900;
    color:{NEGRO};line-height:0.95;letter-spacing:-3px;max-width:220mm;">
    Un estudio<br>que solo<br>hace manuales<span style="color:{LACRE};font-size:96px;">.</span>
  </div>
  <div style="width:60px;height:3px;background:{LACRE};margin-top:10mm;margin-bottom:5mm;"></div>
  <div style="font-family:{FAM};font-size:14px;font-weight:400;
    color:{PIEDRA};max-width:180mm;line-height:1.6;">
    No hacemos web, ni campañas, ni packaging, ni ads, ni ocho servicios más diluidos.
    Hacemos una sola cosa y por eso la hacemos con rigor.
  </div>
</div>

{metastrip(2, "00 · Apertura")}"""
    return page_shell(body, 2, bg=PAPEL, no_furniture=True)


def p03_estado_sistema():
    """p03 — 'Cómo leer este manual' — orientation + big photo.
    Contemporary brand manuals open with a reader's guide before content."""
    steps = [
        ("01", "Apertura",      "Portada · mantra · índice. Orienta qué es y de dónde viene."),
        ("02", "Fundamentos",   "Personas, propósito, valores. La base estratégica (cap. II-III)."),
        ("03", "Sistema visual","Logo, tipografía, color, iconografía, fotografía (cap. IV-VIII)."),
        ("04", "Voz y aplicaciones","Cómo habla la marca y dónde vive (cap. IX-X)."),
        ("05", "Governance",    "Arquitectura, versionado, extensiones (cap. XI-XIV)."),
        ("06", "Servicio",      "Tiers, proceso y portfolio (cap. XV-XVI)."),
    ]
    steps_html = ""
    for num, title, desc in steps:
        steps_html += f"""\
<div style="display:grid;grid-template-columns:14mm 42mm 1fr;gap:4mm;
  align-items:baseline;padding:3mm 0;border-bottom:0.5px solid {CENIZA};">
  <span style="font-family:{MONO};font-size:10px;font-weight:700;color:{LACRE};font-variant-numeric:tabular-nums;">{num}</span>
  <span style="font-family:{FAM};font-size:13px;font-weight:700;color:{NEGRO};">{title}<span style="color:{LACRE};">.</span></span>
  <span style="font-family:{FAM};font-size:11px;color:{PIEDRA};line-height:1.5;">{desc}</span>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">Apertura · 02</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:14mm;align-items:stretch;">

  <!-- LEFT: photograph full-height (books on concrete — no visible text) -->
  <div style="overflow:hidden;background:{CARBON};">
    <img src="{ASSETS}/img-06.jpg" style="width:100%;height:100%;object-fit:cover;
      filter:grayscale(10%) contrast(1.05);" alt="">
  </div>

  <!-- RIGHT: guidance -->
  <div style="display:flex;flex-direction:column;">
    {titulo("Cómo leer<br>este manual", 36)}
    <div class="body-text" style="margin-top:3mm;margin-bottom:6mm;">
      Seis bloques, en este orden. Cada capítulo abre con un divider
      y cierra con reglas operativas. Si solo tienes diez minutos,
      salta al TL;DR de la última página.
    </div>
    <div style="margin-bottom:6mm;">{steps_html}</div>
    <div style="margin-top:auto;border-left:3px solid {LACRE};padding-left:10px;">
      <div style="font-family:{FAM};font-size:12px;font-weight:500;color:{NEGRO};line-height:1.5;">
        Lo que no se documenta, se improvisa<span style="color:{LACRE};">.</span>
      </div>
    </div>
  </div>
</div>

{metastrip(3, "00 · Apertura")}"""
    return page_shell(body, 3, bg=PAPEL, no_furniture=True)


def p04_indice():
    """p04 — Index in 2 columns. 17 sections visible side by side."""
    visible = [s for s in SECTIONS[1:-1] if s["r"]]
    mid = (len(visible) + 1) // 2

    def render_col(entries):
        out = ""
        for s in entries:
            out += f"""\
<div style="display:flex;justify-content:space-between;align-items:baseline;
  padding:2.6mm 0;border-bottom:0.5px solid rgba(244,240,235,0.08);">
  <div style="display:flex;gap:4mm;align-items:baseline;">
    <span style="font-family:{MONO};font-size:8px;font-weight:700;color:{LACRE};
      display:inline-block;min-width:14mm;">{s['r']}</span>
    <span style="font-family:{FAM};font-size:12.5px;font-weight:500;color:{PAPEL};">{s['title']}</span>
  </div>
  <span style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.35);
    font-variant-numeric:tabular-nums;">{s['pages'][0]:02d}</span>
</div>"""
        return out

    col_a = render_col(visible[:mid])
    col_b = render_col(visible[mid:])

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow" style="color:{LACRE};">Apertura · 03</div>
  <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.4);
    letter-spacing:2.4px;text-transform:uppercase;">
    {TOTAL} páginas · 17 secciones · 48 componentes
  </div>
</div>

<!-- Title row -->
<div style="position:absolute;left:24mm;right:24mm;top:32mm;display:flex;
  justify-content:space-between;align-items:baseline;gap:16mm;">
  <div>
    <div style="font-family:{FAM};font-size:88px;font-weight:900;
      color:{PAPEL};letter-spacing:-4px;line-height:0.9;">
      Índice<span style="color:{LACRE};font-size:104px;">.</span>
    </div>
    <div style="font-family:{FAM};font-size:12.5px;color:rgba(244,240,235,0.6);
      max-width:120mm;line-height:1.55;margin-top:5mm;">
      Dieciséis capítulos de anatomía + apertura y cierre.
      Cuatro componentes por capítulo. Ni uno de adorno.
    </div>
  </div>
  <div style="width:60px;height:3px;background:{LACRE};flex-shrink:0;margin-top:8mm;"></div>
</div>

<!-- TOC 2 columns -->
<div style="position:absolute;left:24mm;right:24mm;top:92mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;align-items:start;">
  <div>{col_a}</div>
  <div>{col_b}</div>
</div>

<div class="metastrip dark">
  <span>{BRAND}<span style="color:{LACRE};">.</span> · Manual de marca</span>
  <span style="text-transform:uppercase;letter-spacing:2px;">00 · Apertura</span>
  <span style="font-variant-numeric:tabular-nums;">04 / {TOTAL}</span>
</div>"""
    return page_shell(body, 4, bg=NEGRO, dark=True, no_furniture=True)


def p05_colofon():
    """p05 — Manifiesto. Six commitments, editorial. The colofón proper is at p58."""
    items = [
        ("Hacemos",     "una sola cosa: manuales de marca documentados."),
        ("No hacemos",  "web, ads, packaging, branding integral ni ocho servicios más."),
        ("Escribimos",  "cada regla con su razón. Si no podemos explicar por qué, lo quitamos."),
        ("Entregamos",  "en el plazo publicado. Sin excusas, sin estiramientos."),
        ("Documentamos",  "cada decisión. Lo que no está por escrito, no existe."),
        ("Cerramos",    "cada proyecto. Manual entregado, archivos empaquetados, relación terminada."),
    ]
    lines = ""
    for i, (verb, tail) in enumerate(items):
        num = f"{i+1:02d}"
        lines += f"""\
<div style="display:grid;grid-template-columns:14mm 1fr;gap:6mm;
  padding:4mm 0;border-bottom:0.5px solid {CENIZA};align-items:baseline;">
  <span style="font-family:{MONO};font-size:9px;font-weight:700;color:{LACRE};
    font-variant-numeric:tabular-nums;letter-spacing:1.5px;">{num}</span>
  <span style="font-family:{FAM};font-size:16px;color:{NEGRO};line-height:1.45;">
    <span style="font-weight:900;">{verb}</span>
    <span style="color:{PIEDRA};font-weight:400;"> {tail}</span>
  </span>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">Apertura · 04</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:0.9fr 1.2fr;gap:16mm;align-items:start;">
  <div>
    {titulo("Manifiesto", 44)}
    <div class="body-text" style="margin-bottom:6mm;max-width:100mm;">
      Seis compromisos. Uno por línea. Lo que hacemos, lo que no
      hacemos y cómo tratamos cada proyecto. No hay cláusula pequeña.
    </div>
    <div style="border-left:3px solid {LACRE};padding-left:10px;margin-top:8mm;">
      <div class="pq" style="font-size:18px;">
        El trabajo es revisar<span class="p">.</span>
      </div>
      <div style="font-family:{MONO};font-size:7px;color:{PIEDRA};
        letter-spacing:1.5px;margin-top:3mm;text-transform:uppercase;">
        Frase directa de /sobre
      </div>
    </div>
  </div>
  <div>
    <div class="eyebrow" style="margin-bottom:3mm;color:{LACRE};">Seis compromisos</div>
    {lines}
    <div style="font-family:{MONO};font-size:7px;color:{PIEDRA};
      letter-spacing:1.5px;margin-top:6mm;text-transform:uppercase;">
      Colofón editorial → contraportada · p{TOTAL}
    </div>
  </div>
</div>

{metastrip(5, "00 · Apertura")}"""
    return page_shell(body, 5, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# I PROVOCACIÓN  (pp 06-09)
# ══════════════════════════════════════════════════════════════

def p06_provocacion():
    return divider("01", "I", "Provocación", "Por qué este manual existe.", pg=6,
                   img=f"{ASSETS}/generated/div-provocacion.png")


def p07_the_problem():
    """The 90% problem — tramarca.es verbatim stat."""
    body = f"""\
<div style="position:absolute;left:0;top:0;bottom:0;width:45%;overflow:hidden;">
  <img src="{ASSETS}/generated/hero-logos-chaos.png" style="width:100%;height:100%;object-fit:cover;
    filter:grayscale(25%) contrast(1.15);" alt="">
  <div style="position:absolute;inset:0;
    background:linear-gradient(90deg, transparent 50%, {NEGRO} 100%);"></div>
  <div style="position:absolute;left:0;top:0;bottom:0;width:4px;background:{LACRE};"></div>
</div>

<div style="position:absolute;left:45%;top:0;bottom:0;right:0;background:{NEGRO};
  padding:30mm 24mm 24mm 16mm;display:flex;flex-direction:column;justify-content:center;">

  <div style="display:flex;gap:6mm;align-items:baseline;margin-bottom:10mm;">
    <div class="eyebrow" style="color:{LACRE};">I · Provocación</div>
    {fidelity_badge("FIEL", dark=True)}
  </div>

  <div style="font-family:{FAM};font-size:140px;font-weight:900;
    color:{LACRE};line-height:0.9;letter-spacing:-5px;margin-bottom:2mm;
    font-variant-numeric:tabular-nums;">90<span style="font-size:90px;">%</span></div>

  <div style="font-family:{FAM};font-size:22px;font-weight:700;
    color:{PAPEL};line-height:1.3;max-width:140mm;margin-bottom:8mm;">
    De lo que se vende como "manual de marca" en España
    son ocho láminas con logo, paleta y tipografía<span style="color:{LACRE};">.</span>
  </div>
  <div style="width:50px;height:3px;background:{LACRE};margin-bottom:6mm;"></div>
  <div style="font-family:{FAM};font-size:13px;color:{CENIZA};line-height:1.8;max-width:140mm;">
    La mayoría de las marcas existen solo en la cabeza de quien las creó.
    No en un documento. No por escrito. En la cabeza.<br><br>
    Sin reglas escritas, cada persona que toca la marca la interpreta a su manera.
    El resultado es ruido visual. Inconsistencia. Improvisación.
  </div>
</div>

<div class="metastrip dark">
  <span>{BRAND}<span style="color:{LACRE};">.</span> · Manual de marca</span>
  <span style="text-transform:uppercase;letter-spacing:2px;">I · Provocación</span>
  <span style="font-variant-numeric:tabular-nums;">07 / {TOTAL}</span>
</div>"""
    return page_shell(body, 7, bg=NEGRO, dark=True, no_furniture=True)


def p08_nuestra_respuesta():
    """Scope cerrado: tier + plazo + revisiones + método. All FIEL from /precios."""
    pillars = [
        ("Precio cerrado",      "IVA incluido. Publicado.",            "490€ / 990€ / 1.990€"),
        ("Plazo publicado",     "Días laborables, no estimados.",      "5 · 7 · 10 días"),
        ("Proceso cerrado",     "Dos rondas de revisión incluidas.",   "2 rondas"),
        ("Entrega editorial",   "Libro físico, PDF y assets.",         "Sistema completo"),
    ]
    pillars_html = ""
    for i, (title, sub, value) in enumerate(pillars):
        pillars_html += f"""\
<div style="border-top:3px solid {LACRE};padding-top:5mm;">
  <div class="eyebrow" style="margin-bottom:2mm;">0{i+1}</div>
  <div style="font-family:{FAM};font-size:20px;font-weight:900;color:{NEGRO};
    line-height:1.1;margin-bottom:2mm;">{title}<span style="color:{LACRE};">.</span></div>
  <div style="font-family:{FAM};font-size:11px;color:{PIEDRA};line-height:1.5;margin-bottom:4mm;">{sub}</div>
  <div style="font-family:{MONO};font-size:11px;font-weight:700;color:{NEGRO};
    letter-spacing:1px;">{value}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">I · Provocación · 08</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:36mm;bottom:22mm;
  display:flex;flex-direction:column;">
  {titulo("Nuestra respuesta", 42)}
  <div class="body-text" style="margin-top:2mm;margin-bottom:8mm;max-width:200mm;">
    Scope cerrado antes de empezar: tres tiers con entregables publicados,
    plazo de 5/7/10 días laborables, revisión consolidada antes del cierre
    y entrega editorial completa — libro físico, PDF y assets.
  </div>
  <div class="g4" style="gap:10mm;flex:1;">
    {pillars_html}
  </div>
  <div style="border-top:0.5px solid {CENIZA};padding-top:4mm;margin-top:6mm;
    display:flex;justify-content:space-between;align-items:baseline;">
    <div style="font-family:{FAM};font-size:14px;font-weight:700;color:{NEGRO};">
      Lo que ves es lo que pagas<span style="color:{LACRE};">.</span>
    </div>
    <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};letter-spacing:1.5px;text-transform:uppercase;">
      Fuente · tramarca.es/precios
    </div>
  </div>
</div>

{metastrip(8, "I · Provocación")}"""
    return page_shell(body, 8, bg=PAPEL, no_furniture=True)


def p09_comparativa():
    """Agencia / Freelance / Canva / Tramarca comparison — from /precios."""
    cols = [
        ("Agencia tradicional", "6.000€ – 18.000€ + IVA", "Semanas de discovery", "Precio personalizado", "Calidad de agencia"),
        ("Freelance generalista", "800€ – 3.500€",        "Variable",             "Negociado",            "Depende del perfil"),
        ("Canva + logo barato",  "~80€",                  "Instantáneo",          "Plantilla + archivo",  "Básico, sin sistema"),
        ("Tramarca",             "490€ – 1.990€",         "5 – 10 días laborables","Precio fijo publicado","Sistema documentado de calidad"),
    ]
    rows = [
        ("Precio",   [c[1] for c in cols]),
        ("Plazo",    [c[2] for c in cols]),
        ("Scope",    [c[3] for c in cols]),
        ("Calidad",  [c[4] for c in cols]),
    ]

    header = f"""\
<div style="display:grid;grid-template-columns:30mm 1fr 1fr 1fr 1fr;gap:4mm;
  padding-bottom:4mm;border-bottom:1.5px solid {NEGRO};margin-bottom:2mm;">
  <div></div>
  {"".join(f'<div style="font-family:{FAM};font-size:13px;font-weight:900;color:{LACRE if c[0] == "Tramarca" else NEGRO};letter-spacing:-0.3px;">{c[0]}<span style="color:{LACRE};">.</span></div>' for c in cols)}
</div>"""

    rows_html = ""
    for lbl, vals in rows:
        cells = "".join(
            f'<div style="font-family:{FAM};font-size:11px;font-weight:{900 if i == 3 else 400};color:{NEGRO if i == 3 else CARBON};line-height:1.4;">{v}</div>'
            for i, v in enumerate(vals)
        )
        rows_html += f"""\
<div style="display:grid;grid-template-columns:30mm 1fr 1fr 1fr 1fr;gap:4mm;
  padding:4mm 0;border-bottom:0.5px solid {CENIZA};align-items:baseline;">
  <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};
    letter-spacing:1.5px;text-transform:uppercase;">{lbl}</div>
  {cells}
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">I · Provocación · 09</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;">
  {titulo("El mercado, en una tabla", 36)}
  <div class="body-text" style="margin-top:1mm;margin-bottom:6mm;max-width:200mm;">
    Sin ancla, 1.990€ flota. Con ancla, se lee regalado.
    Esta comparativa no es marketing: son los rangos reales de 2026 en España.
  </div>
  {header}
  {rows_html}
  <div style="margin-top:6mm;background:transparent;border-left:3px solid {LACRE};padding:10px 16px;padding-left:14px;
    display:flex;justify-content:space-between;align-items:baseline;">
    <div style="font-family:{FAM};font-size:12px;font-weight:500;color:{NEGRO};">
      Precio cerrado, plazo publicado, sistema documentado<span style="color:{LACRE};">.</span>
    </div>
    <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};">tramarca.es/precios</div>
  </div>
</div>

{metastrip(9, "I · Provocación")}"""
    return page_shell(body, 9, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# II PERSONAS  (pp 10-13) — data-viz layer
# ══════════════════════════════════════════════════════════════

def p10_personas_divider():
    return divider("02", "II", "Personas", "Quién compra. Qué le duele.", pg=10,
                   img=f"{ASSETS}/generated/div-personas.png")


def _persona_page(pg, num, name, role, jtbd, stats, timeline, demog, trigger, tier, quote, section, photo="", friccion="", como_lee=""):
    """Shared persona template — watermark + stats + timeline + quote + optional portrait."""
    stats_html = "".join(stat_tensional(s[0], s[1], s[2], s[3]) for s in stats)

    portrait_html = ""
    if photo:
        portrait_html = f"""\
<div style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;background:{CARBON};">
  <img src="{photo}" style="width:100%;height:100%;object-fit:cover;
    filter:grayscale(15%) contrast(1.05);" alt="">
  <div style="position:absolute;inset:0;
    background:linear-gradient(180deg, rgba(12,12,12,0.78) 0%, rgba(12,12,12,0.15) 35%, rgba(12,12,12,0) 100%);"></div>
  <div style="position:absolute;left:10mm;right:10mm;top:14mm;">
    <div style="font-family:{MONO};font-size:8px;color:{LACRE};letter-spacing:2px;text-transform:uppercase;margin-bottom:2mm;">{role}</div>
    <div style="font-family:{FAM};font-size:28px;font-weight:900;color:{PAPEL};line-height:1;letter-spacing:-1px;">
      {name}<span style="color:{LACRE};">.</span>
    </div>
  </div>
</div>"""

    demog_rows = "".join(
        f"""<div style="display:grid;grid-template-columns:26mm 1fr;gap:3mm;
  padding:1.5mm 0;border-bottom:0.5px solid {CENIZA};">
  <span style="font-family:{MONO};font-size:7px;color:{PIEDRA};
    letter-spacing:1.3px;text-transform:uppercase;">{k}</span>
  <span style="font-family:{FAM};font-size:10px;color:{NEGRO};">{v}</span>
</div>"""
        for k, v in demog
    )

    body = f"""\
{watermark_number(num, right="6mm", top="8mm")}

<!-- LEFT column: full-bleed portrait with name overlay -->
<div style="position:absolute;left:0;top:0;bottom:0;width:45%;">
  {portrait_html if photo else f'<div style="position:absolute;inset:0;background:{CARBON};"></div>'}
</div>

<!-- RIGHT column: all data -->
<div style="position:absolute;left:45%;top:0;bottom:0;right:0;padding:22mm 14mm 22mm 12mm;display:flex;flex-direction:column;z-index:2;">

  <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:5mm;">
    <div class="eyebrow">{section}</div>
    {fidelity_badge("PROPUESTA")}
  </div>

  <div class="eyebrow" style="margin-bottom:2mm;">Job to be done</div>
  <div class="pq" style="font-size:14px;margin-bottom:5mm;">{jtbd}<span class="p">.</span></div>

  <div class="eyebrow" style="margin-bottom:2mm;">Tensión · 3 métricas</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:3mm;margin-bottom:5mm;">
    {stats_html}
  </div>

  <div class="eyebrow" style="margin-bottom:2mm;">Día típico · 24h</div>
  <div style="margin-bottom:5mm;">{timeline}</div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-bottom:4mm;">
    <div>
      <div class="eyebrow" style="margin-bottom:2mm;">Demografía</div>
      {demog_rows}
    </div>
    <div style="display:flex;flex-direction:column;gap:3.5mm;">
      <div style="border-left:3px solid {LACRE};padding-left:8px;">
        <div class="eyebrow" style="margin-bottom:1.5mm;">Trigger</div>
        <div style="font-family:{FAM};font-size:9.5px;color:{NEGRO};line-height:1.4;">{trigger}</div>
      </div>
      <div style="border-left:3px solid {LACRE};padding-left:8px;">
        <div class="eyebrow" style="margin-bottom:1.5mm;">Fricción principal</div>
        <div style="font-family:{FAM};font-size:9.5px;color:{NEGRO};line-height:1.4;">{friccion}</div>
      </div>
      <div style="border-left:3px solid {LACRE};padding-left:8px;">
        <div class="eyebrow" style="margin-bottom:1.5mm;">Cómo lee este manual</div>
        <div style="font-family:{FAM};font-size:9.5px;color:{NEGRO};line-height:1.4;">{como_lee}</div>
      </div>
      <div style="border-left:3px solid {LACRE};padding-left:8px;">
        <div class="eyebrow" style="margin-bottom:1.5mm;">Tier recomendado</div>
        <div style="font-family:{FAM};font-size:15px;font-weight:900;color:{NEGRO};">{tier}<span style="color:{LACRE};">.</span></div>
      </div>
    </div>
  </div>
</div>

{metastrip(pg, section)}"""
    return page_shell(body, pg, bg=PAPEL, no_furniture=True)


def p11_persona_fundadora():
    return _persona_page(
        pg=11, num="01",
        name="Fundadora SaaS solo",
        role="Perfil · A · Bootstrapped B2B",
        jtbd="Necesito que mi marca parezca profesional cuando firmo al primer cliente enterprise",
        stats=[
            ("12", "h",  "Por semana improvisando decks y assets",   70),
            ("3",  "+",  "Fuentes distintas en la misma landing",     80),
            ("0",  "",   "Sistema documentado",                        5),
        ],
        timeline=timeline_24h([
            (7, "Sueño",       CARBON),
            (2, "Producto",    LACRE),
            (4, "Ventas",      NEGRO),
            (2, "Assets",      PIEDRA),
            (3, "Soporte",     CARBON),
            (6, "Off",         PIEDRA_LIGHT),
        ]),
        demog=[
            ("Edad",      "30 – 42"),
            ("Empresa",   "SaaS solo-founder · 1 – 5 fte"),
            ("Ingresos",  "MRR 5k – 50k€"),
            ("Ciudad",    "Madrid · Barcelona · remoto"),
            ("Decisor",   "Ella misma · comité de 1"),
        ],
        trigger="Primera ronda de inversores, demo a cliente enterprise, rebrand post-PMF.",
        friccion="Cada proveedor externo (diseñador freelance, agencia de ads, growth) aplica la marca distinta. Cada landing se reinventa y ninguna coincide.",
        como_lee="De golpe en una tarde. Marca capítulos Voz, Color y Aplicaciones para enviar a cada colaborador antes del brief.",
        tier="Esencial o Profesional",
        quote="Tenemos logo pero cada vez que alguien lo usa sale distinto.",
        section="II · Personas",
        photo=f"{ASSETS}/generated/persona-a-saas.png",
    )


def p12_persona_consultora():
    return _persona_page(
        pg=12, num="02",
        name="Consultora freelance",
        role="Perfil · B · Senior independiente",
        jtbd="Voy a cobrar 3× — necesito que la marca esté a la altura del precio que voy a pedir",
        stats=[
            ("80", "%",  "De freelances operan sin manual propio",  80),
            ("3",  "×",  "Rate target sobre baseline actual",        95),
            ("7",  "d",  "Hasta kickoff si firma este mes",           40),
        ],
        timeline=timeline_24h([
            (7, "Sueño",       CARBON),
            (3, "Comercial",   LACRE),
            (4, "Entrega",     NEGRO),
            (2, "Reuniones",   PIEDRA),
            (3, "Admin",       CARBON),
            (5, "Familia",     PIEDRA_LIGHT),
        ]),
        demog=[
            ("Edad",       "32 – 48"),
            ("Trayectoria","3+ años freelance senior"),
            ("Ingresos",   "4k – 12k€ / mes"),
            ("Ciudad",     "España · LATAM remoto"),
            ("Decisor",    "Ella misma · sin comité"),
        ],
        trigger="Reposicionamiento para subir precios, primer contrato retainer anual, lanzamiento producto propio.",
        friccion="Cada propuesta nueva se maqueta desde cero. La marca personal parece improvisada al lado de los clientes que vende.",
        como_lee="Por capítulos, citando fragmentos en propuestas y emails. Usa Voz, Color y Tipografía a diario.",
        tier="Profesional",
        quote="Queremos parecer profesionales, no improvisados.",
        section="II · Personas",
        photo=f"{ASSETS}/generated/persona-b-freelance.png",
    )


def p13_persona_estudio():
    return _persona_page(
        pg=13, num="03",
        name="Estudio proveedor",
        role="Perfil · C · Agencia white-label",
        jtbd="Necesito un proveedor que produzca manuales para mis clientes sin competir con mi estudio",
        stats=[
            ("12", "k€", "Coste oculto de producir un manual in-house", 70),
            ("2",  "–3", "Manuales / año que podríamos externalizar",    50),
            ("0",  "%",  "Conflicto de canal con Tramarca",               2),
        ],
        timeline=timeline_24h([
            (7, "Sueño",        CARBON),
            (3, "Comercial",    LACRE),
            (5, "Producción",   NEGRO),
            (2, "Clientes",     PIEDRA),
            (2, "Equipo",       CARBON),
            (5, "Off",          PIEDRA_LIGHT),
        ]),
        demog=[
            ("Tamaño",    "Agencia / estudio 5 – 15 fte"),
            ("Servicios", "Web, campañas, producto digital"),
            ("Ingresos",  "200k – 1M€ anual"),
            ("Ciudad",    "Madrid · Barcelona · Valencia"),
            ("Decisor",   "Fundador / socio"),
        ],
        trigger="Cliente pide rebrand completo que el estudio no quiere asumir · white-label margen.",
        friccion="Producir un manual editorial serio cuesta 12k€ internos. Ocupa a 2 seniors 3 semanas sin ingresar más.",
        como_lee="Como referencia de sistema. Lo presenta al cliente como entregable co-branded y cierra factura.",
        tier="Premium",
        quote="No es nuestro core pero el cliente nos lo pide. Lo delegamos con tranquilidad.",
        section="II · Personas",
        photo=f"{ASSETS}/generated/persona-c-partner.png",
    )


# ══════════════════════════════════════════════════════════════
# III FUNDAMENTOS  (pp 14-18)
# ══════════════════════════════════════════════════════════════

def p14_fundamentos():
    return divider("03", "III", "Fundamentos",
                   "Propósito · Visión · Valores · Personalidad", pg=14,
                   img=f"{ASSETS}/generated/div-fundamentos.png")


def p15_proposito_vision():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">III · Fundamentos · 15</div>
  <div style="display:flex;gap:4mm;">
    {fidelity_badge("FIEL")} {fidelity_badge("PROPUESTA")}
  </div>
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;">
  <div style="display:flex;flex-direction:column;">
    <div class="eyebrow" style="margin-bottom:3mm;">Propósito {fidelity_badge("FIEL")}</div>
    <div style="font-family:{FAM};font-size:30px;font-weight:900;
      color:{NEGRO};line-height:1.1;margin-bottom:10mm;letter-spacing:-1px;">
      Que cada marca profesional tenga su sistema por escrito<span style="color:{LACRE};">.</span>
    </div>

    <div class="eyebrow" style="margin-bottom:3mm;">Visión {fidelity_badge("PROPUESTA")}</div>
    <div style="font-family:{FAM};font-size:18px;font-weight:700;
      color:{NEGRO};line-height:1.3;margin-bottom:4mm;">
      Convertir el manual de marca en una categoría productizada en España —
      precio cerrado, plazo publicado, sistema documentado<span style="color:{LACRE};">.</span>
    </div>
    <div class="body-text" style="max-width:110mm;margin-bottom:8mm;">
      Queremos que un fundador compre un manual como compra un dominio:
      scope publicado, coste publicado, entregables publicados.
    </div>

    <div style="margin-top:auto;padding-top:6mm;border-top:0.5px solid {CENIZA};">
      <div class="eyebrow" style="margin-bottom:3mm;">Fundado</div>
      <div style="font-family:{MONO};font-size:10px;color:{PIEDRA};line-height:2;">
        2026 · Madrid · Estudio remoto<br>
        Edición 01 / 01 — primer manual público
      </div>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;">
    <div class="eyebrow" style="margin-bottom:3mm;">Misión {fidelity_badge("PROPUESTA")}</div>
    <div style="font-family:{FAM};font-size:22px;font-weight:900;
      color:{NEGRO};line-height:1.2;margin-bottom:6mm;">
      Producir sistemas de marca completos en 5–10 días<span style="color:{LACRE};">.</span>
    </div>
    <div class="body-text" style="margin-bottom:10mm;max-width:100mm;">
      Identidad visual, voz, personalidad, assets y reglas de uso.
      Un documento. Cada decisión por escrito.
    </div>

    <div style="background:transparent;border-left:3px solid {LACRE};padding:16px 20px;padding-left:14px;margin-bottom:8mm;">
      <div class="eyebrow" style="margin-bottom:4mm;">El trabajo es revisar {fidelity_badge("FIEL")}</div>
      <div style="font-family:{FAM};font-size:14px;font-weight:500;
        color:{NEGRO};line-height:1.5;">
        Por eso el scope está cerrado antes de empezar.
        Lo que no se documenta, se improvisa.
      </div>
    </div>

    <div style="margin-top:auto;padding-top:6mm;border-top:0.5px solid {CENIZA};">
      <div class="eyebrow" style="margin-bottom:3mm;">Por qué ahora</div>
      <div style="font-family:{FAM};font-size:10.5px;color:{CARBON};line-height:1.6;max-width:100mm;">
        El mercado español de branding vende semanas de discovery para
        entregar 8 láminas. Hay espacio para un producto cerrado y honesto.
      </div>
    </div>
  </div>
</div>

{metastrip(15, "III · Fundamentos")}"""
    return page_shell(body, 15, bg=PAPEL, no_furniture=True)


def p16_valores():
    icon_claridad   = f"""<svg viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="{LACRE}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="16" r="9"/><circle cx="16" cy="16" r="3" fill="{LACRE}"/></svg>"""
    icon_honest     = f"""<svg viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="{LACRE}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 10h20M6 16h20M6 22h14"/></svg>"""
    icon_rigor      = f"""<svg viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="{LACRE}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="12" width="22" height="8"/><path d="M9 12v4M13 12v3M17 12v4M21 12v3M25 12v4"/></svg>"""
    icon_foco       = f"""<svg viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="{LACRE}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="16" r="11"/><circle cx="16" cy="16" r="6"/><circle cx="16" cy="16" r="1.5" fill="{LACRE}"/></svg>"""

    vals = [
        ("01", icon_claridad, "Claridad",   "Cada decisión tiene una razón. Si no la tiene, sobra."),
        ("02", icon_honest,   "Honestidad", "Si tu marca tiene un problema, lo decimos. Sin suavizar."),
        ("03", icon_rigor,    "Rigor",      "No hay páginas de relleno. Todo tiene peso."),
        ("04", icon_foco,     "Foco",       "No hacemos web, ni campañas, ni packaging. Una sola cosa."),
    ]
    cards = ""
    for num, icon, name, desc in vals:
        cards += f"""\
<div style="border-top:4px solid {LACRE};padding-top:6mm;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:4mm;">
    <div style="font-family:{MONO};font-size:10px;font-weight:700;color:{LACRE};">{num}</div>
    <div style="flex-shrink:0;">{icon}</div>
  </div>
  <div style="font-family:{FAM};font-size:28px;font-weight:900;
    color:{NEGRO};margin-bottom:4mm;line-height:1;">{name}<span style="color:{LACRE};">.</span></div>
  <div class="body-text" style="font-size:12px;">{desc}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">III · Fundamentos · 16</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:flex;flex-direction:column;">
  {titulo("Valores", 42)}
  <div class="body-text" style="margin-top:2mm;margin-bottom:10mm;max-width:200mm;">
    Cuatro valores. No son poesía corporativa: son filtros de decisión.
    Cuando una pieza no pasa uno de estos cuatro, no sale.
  </div>
  <div class="g4" style="gap:12mm;flex:1;">
    {cards}
  </div>
  <div style="border-top:0.5px solid {CENIZA};padding-top:4mm;margin-top:8mm;">
    <div class="pq" style="max-width:none;">
      Si no podemos explicar por qué, lo quitamos<span class="p">.</span>
    </div>
  </div>
</div>

{metastrip(16, "III · Fundamentos")}"""
    return page_shell(body, 16, bg=PAPEL, no_furniture=True)


def p17_personalidad():
    adjs = [
        ("Directo",    "Sin rodeos. Sin matices innecesarios."),
        ("Provocador", "Cuestiona lo que el mercado da por sentado."),
        ("Seguro",     "No pide permiso. No se disculpa."),
        ("Preciso",    "Cada palabra elegida. Nada sobra."),
        ("Cercano",    'Usa "tú". Habla de igual a igual.'),
    ]
    items = ""
    for i, (adj, desc) in enumerate(adjs, 1):
        items += f"""\
<div style="display:grid;grid-template-columns:12mm 40mm 1fr;gap:4mm;align-items:baseline;
  padding:3mm 0;border-bottom:0.5px solid {CENIZA};">
  <span style="font-family:{MONO};font-size:10px;font-weight:700;color:{LACRE};">{i:02d}</span>
  <span style="font-family:{FAM};font-size:16px;font-weight:900;color:{NEGRO};">{adj}<span style="color:{LACRE};">.</span></span>
  <span style="font-family:{FAM};font-size:11px;color:{CARBON};line-height:1.5;">{desc}</span>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">III · Fundamentos · 17</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1.1fr 1fr;gap:16mm;">
  <div>
    {titulo("Personalidad", 40)}
    <div class="body-text" style="margin-top:2mm;margin-bottom:6mm;max-width:120mm;">
      Cinco adjetivos. Si un copy o una decisión visual no encaja con los cinco,
      no es Tramarca. Es otra cosa.
    </div>
    {items}
  </div>
  <div style="display:flex;flex-direction:column;gap:6mm;">
    <div style="background:{NEGRO};padding:20px 24px;color:{PAPEL};">
      <div class="eyebrow" style="color:{LACRE};margin-bottom:4mm;">Regla de oro</div>
      <div style="font-family:{FAM};font-size:20px;font-weight:700;
        line-height:1.3;">
        Tramarca nombra lo que ya sabes<span style="color:{LACRE};">.</span><br>
        Precio, plazo, scope —
        escritos antes de empezar<span style="color:{LACRE};">.</span>
      </div>
    </div>
    <div style="background:transparent;border-left:3px solid {LACRE};padding:14px 18px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:3mm;">Test de coherencia</div>
      <div class="body-text" style="font-size:11px;">
        Si una frase podría decirla una agencia grande con 20 cuentas,
        no es nuestra. Si podría decirla un freelance barato, tampoco.
        Nuestra voz queda en medio — precisa y sin adjetivos gratis.
      </div>
    </div>
    <div>
      <div class="eyebrow" style="margin-bottom:3mm;">Así sí</div>
      <div style="display:grid;grid-template-columns:1fr;gap:2mm;">
        <div style="display:grid;grid-template-columns:14mm 1fr;gap:4mm;
          padding:2.5mm 0;border-bottom:0.5px solid {CENIZA};align-items:baseline;">
          <span style="font-family:{MONO};font-size:8px;color:{LACRE};letter-spacing:1.4px;text-transform:uppercase;">Voz</span>
          <span style="font-family:{FAM};font-size:11px;color:{CARBON};line-height:1.5;">
            "Un estudio que solo hace manuales."
          </span>
        </div>
        <div style="display:grid;grid-template-columns:14mm 1fr;gap:4mm;
          padding:2.5mm 0;border-bottom:0.5px solid {CENIZA};align-items:baseline;">
          <span style="font-family:{MONO};font-size:8px;color:{LACRE};letter-spacing:1.4px;text-transform:uppercase;">Voz</span>
          <span style="font-family:{FAM};font-size:11px;color:{CARBON};line-height:1.5;">
            "Lo que ves es lo que pagas."
          </span>
        </div>
        <div style="display:grid;grid-template-columns:14mm 1fr;gap:4mm;
          padding:2.5mm 0;align-items:baseline;">
          <span style="font-family:{MONO};font-size:8px;color:{LACRE};letter-spacing:1.4px;text-transform:uppercase;">Voz</span>
          <span style="font-family:{FAM};font-size:11px;color:{CARBON};line-height:1.5;">
            "El trabajo es revisar."
          </span>
        </div>
      </div>
    </div>
  </div>
</div>

{metastrip(17, "III · Fundamentos")}"""
    return page_shell(body, 17, bg=PAPEL, no_furniture=True)


def p18_posicionamiento():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">III · Fundamentos · 18</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1.1fr 1fr;gap:18mm;">
  <div>
    {titulo("Posicionamiento", 36)}
    <div class="body-text" style="margin-top:2mm;margin-bottom:6mm;max-width:120mm;">
      Tramarca es un estudio editorial, no una agencia creativa.
      Producimos sistemas de marca completos — no logos sueltos,
      no slides de branding, no PDFs de tres páginas.
    </div>
    <div style="margin-bottom:6mm;">
      <div class="eyebrow" style="margin-bottom:3mm;">Lo que no somos</div>
      <div style="font-family:{FAM};font-size:14px;font-weight:500;
        color:{PIEDRA};line-height:2;">
        <span class="struck">Una agencia creativa</span><br>
        <span class="struck">Un freelance que hace logos</span><br>
        <span class="struck">Un estudio de diseño generalista</span><br>
        <span class="struck">Un SaaS de plantillas</span>
      </div>
    </div>
    <div class="pq" style="max-width:120mm;">
      No somos una agencia. No somos un freelance. Somos un sistema<span class="p">.</span>
    </div>
  </div>

  <div style="display:flex;flex-direction:column;justify-content:center;">
    <div class="eyebrow" style="margin-bottom:4mm;">Mapa competitivo</div>
    <div style="position:relative;width:100%;aspect-ratio:1/1;
      border-left:1px solid {CENIZA};border-bottom:1px solid {CENIZA};">
      <div style="position:absolute;bottom:-8mm;left:50%;transform:translateX(-50%);
        font-family:{MONO};font-size:7px;color:{PIEDRA};letter-spacing:1px;text-transform:uppercase;">
        Sistema completo →
      </div>
      <div style="position:absolute;left:-12mm;top:50%;transform:rotate(-90deg);transform-origin:left top;
        font-family:{MONO};font-size:7px;color:{PIEDRA};letter-spacing:1px;text-transform:uppercase;">
        Precio cerrado →
      </div>
      <div style="position:absolute;left:15%;bottom:15%;width:8px;height:8px;border-radius:50%;background:{CENIZA};"></div>
      <div style="position:absolute;left:20%;bottom:55%;width:8px;height:8px;border-radius:50%;background:{CENIZA};"></div>
      <div style="position:absolute;left:60%;bottom:22%;width:8px;height:8px;border-radius:50%;background:{CENIZA};"></div>
      <div style="position:absolute;left:68%;bottom:70%;width:8px;height:8px;border-radius:50%;background:{CENIZA};"></div>
      <div style="position:absolute;left:82%;bottom:85%;width:16px;height:16px;border-radius:50%;
        background:{LACRE};box-shadow:0 0 0 5px rgba(196,85,58,0.22);"></div>
      <div style="position:absolute;left:15%;bottom:7%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Fiverr · Canva</div>
      <div style="position:absolute;left:20%;bottom:47%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Freelance</div>
      <div style="position:absolute;left:52%;bottom:14%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Estudio boutique</div>
      <div style="position:absolute;left:58%;bottom:62%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Agencia grande</div>
      <div style="position:absolute;left:66%;bottom:92%;font-family:{FAM};font-size:10px;font-weight:900;color:{LACRE};">TRAMARCA.</div>
    </div>
    <div style="margin-top:10mm;font-family:{MONO};font-size:8px;color:{PIEDRA};letter-spacing:1.2px;text-transform:uppercase;line-height:1.8;">
      Eje X · scope · de logo suelto a sistema completo<br>
      Eje Y · precio · de negociado a publicado
    </div>
  </div>
</div>

{metastrip(18, "III · Fundamentos")}"""
    return page_shell(body, 18, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# IV SISTEMA DE LOGO  (pp 19-23)
# ══════════════════════════════════════════════════════════════

def p19_logo_divider():
    return divider("04", "IV", "Sistema de logo",
                   "Marca · variantes · zona · usos.", pg=19,
                   img=f"{ASSETS}/generated/div-logo-v2.png")


def p20_logo_primary():
    body = f"""\
<div class="noise" style="position:absolute;inset:0;"></div>

<div style="position:absolute;inset:0;
  background:radial-gradient(ellipse at 50% 45%,
    rgba(196,85,58,0.06) 0%, transparent 60%);pointer-events:none;"></div>

<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-52%);
  font-family:{FAM};font-size:400px;font-weight:900;
  color:rgba(244,240,235,0.025);letter-spacing:-12px;
  pointer-events:none;user-select:none;white-space:nowrap;">{BRAND}</div>

<div style="position:absolute;left:50%;top:46%;transform:translate(-50%,-50%);text-align:center;">
  <div style="font-family:{FAM};font-size:96px;font-weight:900;
    color:{PAPEL};letter-spacing:-3px;line-height:1;">
    {BRAND}<span style="color:{LACRE};font-size:120px;position:relative;top:6px;">.</span>
  </div>
</div>

<div style="position:absolute;left:0;right:0;top:62%;height:0.5px;
  background:linear-gradient(90deg, transparent 0%, rgba(244,240,235,0.08) 20%, rgba(244,240,235,0.08) 80%, transparent 100%);"></div>

<div class="vertical-text" style="position:absolute;left:14mm;top:50%;transform:translateY(-50%);">El punto final</div>

<div style="position:absolute;left:24mm;bottom:18mm;">
  <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.4);line-height:2.2;letter-spacing:0.5px;">
    <span style="color:rgba(244,240,235,0.25);">TIPOGRAFÍA</span> Satoshi Black 900<br>
    <span style="color:rgba(244,240,235,0.25);">CONCEPTO</span> El Punto Final<br>
    <span style="color:rgba(244,240,235,0.25);">PUNTO</span> 125% cap-height · Lacre {LACRE}
  </div>
</div>

<div style="position:absolute;right:24mm;top:18mm;display:flex;gap:4mm;align-items:baseline;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.45);letter-spacing:2px;text-transform:uppercase;">
    IV · Sistema de logo
  </span>
  {fidelity_badge("FIEL", dark=True)}
</div>

<div class="metastrip dark">
  <span>{BRAND}<span style="color:{LACRE};">.</span> · Manual de marca</span>
  <span style="text-transform:uppercase;letter-spacing:2px;">IV · Sistema de logo</span>
  <span style="font-variant-numeric:tabular-nums;">20 / {TOTAL}</span>
</div>"""
    return page_shell(body, 20, bg=NEGRO, dark=True, no_furniture=True)


def p21_logo_construccion():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">IV · Sistema de logo · 21</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1.3fr 1fr;gap:16mm;">
  <div>
    {titulo("Construcción", 36)}
    <div style="position:relative;width:100%;height:82mm;margin-top:4mm;
      background:
        repeating-linear-gradient(0deg, transparent, transparent 9.5mm, rgba(181,177,172,0.18) 9.5mm, rgba(181,177,172,0.18) 10mm),
        repeating-linear-gradient(90deg, transparent, transparent 9.5mm, rgba(181,177,172,0.18) 9.5mm, rgba(181,177,172,0.18) 10mm);
      border:0.5px solid {CENIZA};">
      <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">
        <div style="position:relative;">
          <div style="font-family:{FAM};font-size:52px;font-weight:900;
            color:{NEGRO};letter-spacing:-1px;">
            {BRAND}<span style="color:{LACRE};font-size:64px;">.</span>
          </div>
          <div style="position:absolute;top:4px;left:-18mm;right:-18mm;
            border-top:0.5px dashed {LACRE};opacity:0.55;"></div>
          <div style="position:absolute;bottom:6px;left:-18mm;right:-18mm;
            border-top:0.5px dashed {LACRE};opacity:0.55;"></div>
          <div style="position:absolute;top:-6mm;left:-6mm;right:-6mm;bottom:-6mm;
            border:0.5px dashed {CENIZA};"></div>
          <div style="position:absolute;top:-6mm;right:-6mm;
            font-family:{MONO};font-size:7px;color:{PIEDRA};transform:translate(50%,-100%);">X</div>
        </div>
      </div>
    </div>
    <div class="g3" style="margin-top:5mm;gap:6mm;">
      <div>
        <div class="eyebrow" style="margin-bottom:2mm;">Zona de respeto</div>
        <div class="meta">X = ancho del punto. Nada invade esta zona.</div>
      </div>
      <div>
        <div class="eyebrow" style="margin-bottom:2mm;">El punto final</div>
        <div class="meta">125% cap-height · elemento identitario central.</div>
      </div>
      <div>
        <div class="eyebrow" style="margin-bottom:2mm;">Tracking</div>
        <div class="meta">-3px en display · -1px en cuerpo. Nunca positivo.</div>
      </div>
    </div>
  </div>

  <div>
    <div class="eyebrow" style="margin-bottom:6mm;">Tamaños mínimos</div>
    <div style="margin-bottom:8mm;padding-bottom:6mm;border-bottom:0.5px solid {CENIZA};">
      <div style="font-family:{FAM};font-size:26px;font-weight:900;color:{NEGRO};margin-bottom:2mm;">
        {BRAND}<span style="color:{LACRE};font-size:32px;">.</span>
      </div>
      <div class="meta">Digital: mín 80px · Impreso: mín 25mm <span style="color:{LACRE};">OK</span></div>
    </div>
    <div style="margin-bottom:8mm;padding-bottom:6mm;border-bottom:0.5px solid {CENIZA};">
      <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{CENIZA};margin-bottom:2mm;">
        {BRAND}<span style="color:{CENIZA};">.</span>
      </div>
      <div class="meta">Por debajo de 60px / 18mm: usar monograma</div>
    </div>
    <div>
      <div style="font-family:{FAM};font-size:24px;font-weight:900;color:{NEGRO};margin-bottom:2mm;">
        Tm<span style="color:{LACRE};font-size:29px;">.</span>
      </div>
      <div class="meta">Monograma · favicons, avatares, tamaños reducidos</div>
    </div>
    {accent_rule(60, "6mm")}
    <div class="meta" style="margin-top:4mm;">
      El punto siempre en Lacre, independientemente del tamaño.
    </div>
  </div>
</div>

{metastrip(21, "IV · Sistema de logo")}"""
    return page_shell(body, 21, bg=PAPEL, no_furniture=True)


def p22_logo_variantes():
    versions = [
        ("Positivo",        PAPEL, NEGRO, LACRE),
        ("Negativo",        NEGRO, PAPEL, LACRE),
        ("Monocromo",       PAPEL, NEGRO, NEGRO),
        ("Monocromo inv.",  NEGRO, PAPEL, PAPEL),
    ]
    grid = ""
    for label, bg, text, dot in versions:
        border = f"border:1px solid {CENIZA};" if bg == PAPEL else ""
        grid += f"""\
<div>
  <div style="background:{bg};{border}height:52mm;
    display:flex;align-items:center;justify-content:center;">
    <div style="font-family:{FAM};font-size:30px;font-weight:900;color:{text};">
      {BRAND}<span style="color:{dot};font-size:37px;">.</span>
    </div>
  </div>
  <div class="eyebrow" style="margin-top:3mm;">{label}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">IV · Sistema de logo · 22</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    {titulo("Variantes", 40)}
    <div class="g4" style="margin-top:6mm;gap:8mm;">
      {grid}
    </div>
  </div>
  <div>
    {data_block([
        ("Preferencia", "Positivo con punto Lacre · uso principal"),
        ("Monocromo",   "Solo cuando la impresión a color no es posible"),
        ("Regla",       "El punto en Lacre siempre que sea técnicamente posible"),
    ])}
  </div>
</div>

{metastrip(22, "IV · Sistema de logo")}"""
    return page_shell(body, 22, bg=PAPEL, no_furniture=True)


def p23_logo_donts():
    violations = [
        ("No rotar",                "transform:rotate(15deg);",                            LACRE),
        ("No cambiar color del punto","",                                                  "#3366CC"),
        ("No usar sombras",         "filter:drop-shadow(3px 3px 4px rgba(0,0,0,0.4));",    LACRE),
        ("No deformar",             "transform:scaleX(1.4);",                              LACRE),
        ("No sobre fondos complejos","",                                                   LACRE),
        ("No eliminar el punto",    "",                                                    None),
    ]
    grid = ""
    for i, (caption, style, dot_color) in enumerate(violations):
        if i == 4:
            bg_css = f"background:repeating-linear-gradient(45deg,{ARENA},{ARENA} 4px,{CENIZA} 4px,{CENIZA} 8px);"
        else:
            bg_css = f"background:{PAPEL};border:1px solid {CENIZA};"
        mark = BRAND if dot_color is None else f'{BRAND}<span style="color:{dot_color};font-size:22px;">.</span>'
        grid += f"""\
<div>
  <div style="{bg_css}height:50mm;display:flex;align-items:center;justify-content:center;position:relative;">
    <div style="font-family:{FAM};font-size:20px;font-weight:900;color:{NEGRO};{style}">{mark}</div>
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
      font-family:{FAM};font-size:50px;font-weight:900;color:rgba(196,85,58,0.3);">X</div>
  </div>
  <div class="meta" style="margin-top:2mm;">{caption}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">IV · Sistema de logo · 23</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    {titulo("Usos incorrectos", 38)}
    <div class="g3" style="margin-top:4mm;row-gap:6mm;gap:6mm;">
      {grid}
    </div>
  </div>
  <div style="border-left:4px solid {LACRE};padding-left:14px;">
    <div style="font-family:{FAM};font-size:14px;font-weight:500;color:{NEGRO};line-height:1.6;">
      Si no está en esta página, pregunta antes de usarlo<span style="color:{LACRE};">.</span><br>
      La consistencia no es negociable.
    </div>
  </div>
</div>

{metastrip(23, "IV · Sistema de logo")}"""
    return page_shell(body, 23, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# V TIPOGRAFÍA  (pp 24-26)
# ══════════════════════════════════════════════════════════════

def p24_tipo_divider():
    return divider("05", "V", "Tipografía", "Dos familias. Roles claros.", pg=24,
                   img=f"{ASSETS}/generated/div-tipografia.png")


def p25_specimens():
    phrase = "Lo que no se documenta, se improvisa."
    weights = [("Regular 400", 400), ("Medium 500", 500),
               ("Bold 700", 700), ("Black 900", 900)]
    ramp = ""
    for label, w in weights:
        ramp += f"""\
<div style="margin-bottom:3mm;">
  <div class="meta" style="margin-bottom:1mm;">{label}</div>
  <div style="font-family:{FAM};font-size:13px;font-weight:{w};color:{NEGRO};">{phrase}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">V · Tipografía · 25</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1.4fr 1fr;gap:16mm;">
  <div>
    <div style="font-family:{FAM};font-size:72px;font-weight:900;
      color:{NEGRO};line-height:1;margin-bottom:6mm;letter-spacing:-2px;">Satoshi</div>
    <div style="font-family:{FAM};font-size:17px;font-weight:400;
      color:{CARBON};letter-spacing:2px;line-height:1.6;margin-bottom:6mm;">
      A B C D E F G H I J K L M N O P Q R S T U V W X Y Z<br>
      a b c d e f g h i j k l m n o p q r s t u v w x y z<br>
      0 1 2 3 4 5 6 7 8 9
    </div>
    {ramp}
    <div style="margin-top:4mm;padding-top:3mm;border-top:0.5px solid {CENIZA};">
      <div class="meta" style="margin-bottom:1.5mm;">Muestra · Satoshi 400 · 12 px · line-height 1.5</div>
      <div style="font-family:{FAM};font-size:12px;font-weight:400;color:{NEGRO};
        line-height:1.5;max-width:110mm;">
        Tramarca produce manuales de marca por escrito. Cada página de este documento
        es una decisión firmada antes del primer contacto con el cliente: precio,
        plazo, scope, entregable. Un sistema sin libro es un conjunto de gustos.
      </div>
    </div>
    {accent_rule(60, "4mm")}
    <div style="font-family:{MONO};font-size:36px;font-weight:700;
      color:{NEGRO};line-height:1;margin-top:8mm;margin-bottom:4mm;letter-spacing:-0.5px;">IBM Plex Mono</div>
    <div style="font-family:{MONO};font-size:14px;font-weight:400;
      color:{CARBON};letter-spacing:1px;line-height:1.6;">
      A B C D E F G H I J K L M N O P Q R S T U V W X Y Z<br>
      0 1 2 3 4 5 6 7 8 9 ! @ # $ % &amp; * ( ) — . , : ;
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:6mm;">
    {data_block([
        ("Satoshi",  "Fontshare · Indian Type Foundry"),
        ("Clase",    "Geometric sans-serif"),
        ("Uso",      "Títulos, cuerpo, UI · todo"),
        ("Pesos",    "400 · 500 · 700 · 900"),
        ("Carga",    "Self-hosted .woff2 · preload"),
    ])}
    <div style="background:transparent;border-left:3px solid {LACRE};padding:14px 18px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:3mm;">Por qué Satoshi</div>
      <div class="body-text" style="font-size:11px;">
        Geométrica sin ser fría. Legible en cuerpo,
        contundente en display. Un solo tipo que cubre
        toda la jerarquía sin pareja display separada.
      </div>
    </div>
    {data_block([
        ("Plex Mono","Google Fonts · IBM"),
        ("Clase",    "Monospaced"),
        ("Uso",      "Metadata, eyebrows, data, specs"),
        ("Pesos",    "400 · 700"),
        ("Carga",    "next/font/google · preload"),
    ])}
    <div style="background:transparent;border-left:3px solid {LACRE};padding:14px 18px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:3mm;">Por qué Plex Mono</div>
      <div class="body-text" style="font-size:11px;">
        Precisión técnica sin competir con Satoshi.
        Ancho fijo crea alineación vertical natural
        en tablas y data blocks.
      </div>
    </div>
  </div>
</div>

{metastrip(25, "V · Tipografía")}"""
    return page_shell(body, 25, bg=PAPEL, no_furniture=True)


def p26_tipo_jerarquia():
    levels = [
        ("Eyebrow",   "Plex Mono 8px 700",  f'<div class="eyebrow">V · TIPOGRAFÍA</div>'),
        ("Título",    "Satoshi 42px 900",   f'<div style="font-family:{FAM};font-size:28px;font-weight:900;color:{NEGRO};">Sistema tipográfico<span style="color:{LACRE};">.</span></div>'),
        ("Subtítulo", "Satoshi 22px 700",   f'<div style="font-family:{FAM};font-size:18px;font-weight:700;color:{NEGRO};">Jerarquía</div>'),
        ("Cuerpo",    "Satoshi 13px 400",   f'<div class="body-text">Dos familias, cinco niveles, sin cursivas.</div>'),
        ("Metadata",  "Plex Mono 9px 400",  f'<div class="meta">EDICIÓN · PRIMERA EDICIÓN · 2026</div>'),
    ]
    demo = ""
    for name, spec, example in levels:
        demo += f"""\
<div style="padding:3mm 0;border-bottom:0.5px solid {CENIZA};">
  <div class="meta" style="margin-bottom:1mm;color:{PIEDRA};">{name} — {spec}</div>
  {example}
</div>"""

    rules = [
        "Satoshi 900 solo para títulos principales.",
        "IBM Plex Mono solo por debajo de 11px.",
        "Sin cursivas. Solo subtítulo cover.",
        "Énfasis con peso (700) o color (Lacre).",
        "El punto final siempre en Lacre a 120-125%.",
        "Numerales tabulares (tabular-nums) en precios y stats.",
    ]
    rules_html = ""
    for i, r in enumerate(rules, 1):
        rules_html += f"""\
<div style="display:grid;grid-template-columns:10mm 1fr;gap:3mm;margin-bottom:3mm;align-items:baseline;">
  <span style="font-family:{MONO};font-size:11px;font-weight:700;color:{LACRE};font-variant-numeric:tabular-nums;">{i:02d}</span>
  <span style="font-family:{FAM};font-size:12px;font-weight:400;color:{CARBON};line-height:1.4;">{r}</span>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">V · Tipografía · 26</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1.3fr 1fr;gap:18mm;">
  <div style="display:flex;flex-direction:column;justify-content:space-between;">
    <div>
      {titulo("Jerarquía", 36)}
      {demo}
    </div>
    <div style="border-top:0.5px solid {CENIZA};padding-top:4mm;">
      <div class="meta" style="line-height:1.8;">
        Cada nivel tiene un único propósito. Un título nunca se usa como cuerpo.
        Un metadata nunca se usa como subtítulo. La jerarquía es ley.
      </div>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:space-between;">
    <div style="background:transparent;border-left:3px solid {LACRE};padding:20px 24px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:6mm;">Reglas</div>
      {rules_html}
    </div>
    <div style="background:{NEGRO};padding:16px 20px;margin-top:8mm;">
      <div class="eyebrow" style="color:{LACRE};margin-bottom:3mm;">Ejemplo aplicado</div>
      <div style="font-family:{FAM};font-size:22px;font-weight:900;color:{PAPEL};letter-spacing:-0.5px;">
        Título en Satoshi 900<span style="color:{LACRE};font-size:26px;">.</span>
      </div>
      <div style="font-family:{MONO};font-size:9px;color:rgba(244,240,235,0.55);margin-top:2mm;letter-spacing:1px;">
        METADATA EN PLEX MONO 400
      </div>
    </div>
  </div>
</div>

{metastrip(26, "V · Tipografía")}"""
    return page_shell(body, 26, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# VI COLOR  (pp 27-29)
# ══════════════════════════════════════════════════════════════

def p27_color_divider():
    return divider("06", "VI", "Color", "Siete tokens. Un acento.", pg=27,
                   img=f"{ASSETS}/generated/div-color-v2.png")


def p28_color_palette():
    colors = [
        (NEGRO,        "Negro",        PAPEL, "#0C0C0C", "Ink"),
        (CARBON,       "Carbón",       PAPEL, "#1C1C1C", "Dark"),
        (LACRE,        "Lacre",        PAPEL, "#C4553A", "Acento"),
        (PIEDRA,       "Piedra",       PAPEL, "#5E5A57", "Muted AA"),
        (PIEDRA_LIGHT, "Piedra light", NEGRO, "#7A7672", "Decorativo"),
        (CENIZA,       "Ceniza",       NEGRO, "#B5B1AC", "Rules"),
        (ARENA,        "Arena",        NEGRO, "#E4E2DC", "Panels"),
        (PAPEL,        "Papel",        NEGRO, "#F4F0EB", "Background"),
    ]
    stripes = ""
    for bg, name, tc, hex_val, role in colors:
        role_color = "rgba(244,240,235,0.78)" if tc == PAPEL else "rgba(12,12,12,0.78)"
        hex_color  = "rgba(244,240,235,0.88)" if tc == PAPEL else "rgba(12,12,12,0.82)"
        stripes += f"""\
<div style="flex:1;background:{bg};display:flex;flex-direction:column;
  justify-content:flex-end;padding:10mm 4mm;gap:2mm;">
  <div style="font-family:{FAM};font-size:13px;font-weight:900;color:{tc};
    letter-spacing:-0.3px;line-height:1;">{name}</div>
  <div style="font-family:{MONO};font-size:9px;letter-spacing:0.8px;color:{hex_color};
    font-variant-numeric:tabular-nums;line-height:1;">{hex_val}</div>
  <div style="font-family:{MONO};font-size:7.5px;letter-spacing:1.4px;color:{role_color};
    text-transform:uppercase;line-height:1;">{role}</div>
</div>"""

    left = f"""\
<div style="width:100%;height:100%;background:{NEGRO};display:flex;flex-direction:column;
  justify-content:space-between;padding:24mm 22mm 20mm 24mm;box-sizing:border-box;">
  <div>
    <div style="display:flex;gap:4mm;align-items:baseline;margin-bottom:12mm;">
      <div style="font-family:{MONO};font-size:8px;font-weight:700;letter-spacing:3px;
        text-transform:uppercase;color:{LACRE};">VI · Color</div>
      {fidelity_badge("FIEL", dark=True)}
    </div>
    <div style="font-family:{FAM};font-size:60px;font-weight:900;
      color:{PAPEL};letter-spacing:-3px;line-height:0.9;">
      Paleta<br>de color<span style="color:{LACRE};font-size:74px;">.</span>
    </div>
  </div>
  <div>
    <div style="width:40px;height:3px;background:{LACRE};margin-bottom:6mm;"></div>
    <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.55);line-height:2;letter-spacing:1px;">
      8 tokens<br>0 degradados<br>1 acento · Lacre
    </div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:0;top:0;bottom:0;width:34%;z-index:2;">{left}</div>
<div style="position:absolute;left:34%;top:0;bottom:22mm;right:0;display:flex;z-index:1;">{stripes}</div>

<div class="metastrip dark">
  <span>{BRAND}<span style="color:{LACRE};">.</span> · Manual de marca</span>
  <span style="text-transform:uppercase;letter-spacing:2px;">VI · Color</span>
  <span style="font-variant-numeric:tabular-nums;">28 / {TOTAL}</span>
</div>"""
    return page_shell(body, 28, bg=NEGRO, dark=True, no_furniture=True)


def p29_color_combos():
    combos = [
        ("Principal oscuro",    NEGRO, PAPEL,  LACRE, "15.4:1"),
        ("Principal claro",     PAPEL, NEGRO,  LACRE, "15.4:1"),
        ("Acento sobre oscuro", NEGRO, LACRE,  None,  "4.6:1"),
        ("Secundario cálido",   ARENA, CARBON, None,  "10.7:1"),
    ]
    combo_grid = ""
    for label, bg, fg, accent, ratio in combos:
        border = f"border:1px solid {CENIZA};" if bg in [PAPEL, ARENA] else ""
        dot = f'<span style="color:{accent};">.</span>' if accent else ""
        combo_grid += f"""\
<div>
  <div style="background:{bg};{border}height:30mm;
    display:flex;align-items:center;justify-content:center;">
    <span style="font-family:{FAM};font-size:18px;font-weight:700;color:{fg};">Aa{dot}</span>
  </div>
  <div style="display:flex;justify-content:space-between;margin-top:1.5mm;align-items:baseline;">
    <span style="font-family:{FAM};font-size:10px;color:{NEGRO};">{label}</span>
    <span class="meta" style="font-variant-numeric:tabular-nums;">{ratio}</span>
  </div>
</div>"""

    donts = [
        ("Lacre como fondo", f"background:{LACRE};", f"color:{PAPEL};"),
        ("Degradados",       f"background:linear-gradient(135deg,{NEGRO},{LACRE});", f"color:{PAPEL};"),
        ("Múltiples acentos",f"background:{PAPEL};border:1px solid {CENIZA};", f"color:{NEGRO};"),
    ]
    dont_grid = ""
    for title, bg_css, fg_css in donts:
        inner = f'{BRAND}<span style="color:{LACRE};font-size:16px;">.</span>'
        if "ltiples" in title:
            inner = f'{BRAND}<span style="color:#2E6DB4;">.</span><span style="color:#4CAF50;">*</span>'
        dont_grid += f"""\
<div>
  <div style="{bg_css}{fg_css}height:30mm;display:flex;align-items:center;justify-content:center;position:relative;">
    <span style="font-family:{FAM};font-size:14px;font-weight:900;">{inner}</span>
    <div style="position:absolute;top:2mm;right:3mm;font-family:{FAM};font-size:20px;font-weight:900;color:{LACRE};opacity:0.8;">X</div>
  </div>
  <div class="meta" style="margin-top:1.5mm;">{title}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">VI · Color · 29</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;">
  <div>
    {titulo("Combinaciones", 32)}
    <div class="body-text" style="font-size:11px;margin-bottom:4mm;">
      Todas superan WCAG AA (4.5:1) para texto normal.
    </div>
    <div class="g2" style="row-gap:4mm;">
      {combo_grid}
    </div>
  </div>
  <div>
    {titulo("Usos incorrectos", 32)}
    <div class="g3" style="margin-top:4mm;">
      {dont_grid}
    </div>
    <div style="margin-top:6mm;">
      {data_block([
          ("Regla",      "Lacre es acento, nunca fondo"),
          ("Contraste",  "Mín WCAG AA · 4.5:1"),
          ("Degradados", "Prohibidos · colores planos"),
          ("Piedra",     "5E5A57 para texto · 7A7672 decorativo"),
      ])}
    </div>
  </div>
</div>

{metastrip(29, "VI · Color")}"""
    return page_shell(body, 29, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# VII ICONOGRAFÍA  (pp 30-31)
# ══════════════════════════════════════════════════════════════

def p30_icono_divider():
    return divider("07", "VII", "Iconografía",
                   "Trazo · tamaños · colección · do & don'ts.", pg=30,
                   img=f"{ASSETS}/generated/div-iconografia.png")


def p31_icono_sistema():
    # Icon grid — 12 placeholder icons with consistent stroke
    icons_data = [
        ("M4 12 L20 12", "Línea"),
        ("M12 4 L12 20", "Vertical"),
        ("M4 4 L20 20 M20 4 L4 20", "Cruz"),
        ("M4 12 A8 8 0 1 0 20 12 A8 8 0 1 0 4 12", "Círculo"),
        ("M4 4 H20 V20 H4 Z", "Cuadro"),
        ("M12 4 L20 16 L4 16 Z", "Triángulo"),
        ("M4 12 L12 4 L20 12 L12 20 Z", "Rombo"),
        ("M4 8 L12 16 L20 8", "Down"),
        ("M8 4 L16 12 L8 20", "Right"),
        ("M4 16 L10 10 L14 14 L20 4", "Up chart"),
        ("M4 4 H20 M4 12 H20 M4 20 H20", "Lines"),
        ("M4 4 L20 4 L20 12 L12 12 L8 16 L8 12 L4 12 Z", "Bubble"),
    ]
    grid = ""
    for path, label in icons_data:
        grid += f"""\
<div style="display:flex;flex-direction:column;align-items:center;gap:3mm;
  padding:10mm 6mm;border:0.5px solid {CENIZA};background:{PAPEL};">
  <svg width="32" height="32" viewBox="0 0 24 24" fill="none"
    stroke="{NEGRO}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="{path}"/>
  </svg>
  <div class="meta" style="text-align:center;">{label}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">VII · Iconografía · 31</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1.4fr;gap:16mm;">
  <div>
    {titulo("Sistema de trazo", 30)}
    <div class="body-text" style="margin-top:2mm;margin-bottom:6mm;max-width:100mm;">
      Stroke 1.5px, linecap round, linejoin round. Sin relleno.
      El icono usa el token de color del contexto — nunca Lacre salvo
      en estados activos.
    </div>
    {data_block([
        ("Grid",       "24 × 24 px · viewBox 0 0 24 24"),
        ("Stroke",     "1.5 px · uniforme"),
        ("Cap / Join", "Round / Round"),
        ("Relleno",    "Ninguno · solo outline"),
        ("Color",      "Hereda del contexto · nunca Lacre por defecto"),
        ("Tamaños",    "16 · 20 · 24 · 32 px"),
    ])}
    <div style="margin-top:6mm;border-left:3px solid {LACRE};padding-left:12px;">
      <div class="body-text" style="font-size:11px;">
        Si una acción no se puede representar con estas 12 primitivas combinadas,
        se describe en texto. El icono no es decoración.
      </div>
    </div>
  </div>
  <div>
    <div class="eyebrow" style="margin-bottom:4mm;">Colección base · 12 primitivas</div>
    <div style="display:grid;grid-template-columns:repeat(4, 1fr);gap:4mm;">
      {grid}
    </div>
  </div>
</div>

{metastrip(31, "VII · Iconografía")}"""
    return page_shell(body, 31, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# VIII FOTOGRAFÍA  (pp 32-33)
# ══════════════════════════════════════════════════════════════

def p32_foto_divider():
    return divider("08", "VIII", "Fotografía",
                   "Dirección · tratamiento · composición.", pg=32,
                   img=f"{ASSETS}/generated/div-fotografia-v4.png")


def p33_foto_direccion():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">VIII · Fotografía · 33</div>
  <div style="display:flex;gap:3mm;">
    {fidelity_badge("PROPUESTA")} {fidelity_badge("INVENTADO")}
  </div>
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1.3fr;gap:16mm;">
  <div>
    {titulo("Dirección visual", 30)}
    <div class="body-text" style="margin-bottom:6mm;max-width:110mm;">
      Contemporáneo editorial — concreto pulido, steel anodizado,
      papel sin deckle, studio flat light, precisión geométrica.
      Ni nostalgia, ni letterpress, ni golden hour.
    </div>
    {data_block([
        ("Estilo",     "Editorial contemporáneo · Pentagram · Stripe Press"),
        ("Iluminación","Flat studio · ventana norte suave"),
        ("Paleta",     "Neutros fríos + Lacre puntual"),
        ("Tratamiento","Grayscale 15% · contrast 1.08"),
        ("Composición","Grid riguroso · espacios negativos amplios"),
        ("Evitar",     "Golden-hour · sepia · Kinfolk · letterpress"),
    ])}
    <div style="margin-top:6mm;border-left:3px solid {LACRE};padding-left:12px;">
      <div class="body-text" style="font-size:11px;">
        Referencias canónicas: Pentagram monograph, Stripe Press, Gretel,
        Koto, Apartamento 2026, Base Design.
      </div>
    </div>
  </div>
  <div>
    <div class="eyebrow" style="margin-bottom:4mm;">Moodboard · 4 referencias</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5mm;">
      <div style="aspect-ratio:3/2;overflow:hidden;"><img src="{ASSETS}/img-01.jpg" style="width:100%;height:100%;object-fit:cover;filter:grayscale(15%) contrast(1.08);" alt=""></div>
      <div style="aspect-ratio:3/2;overflow:hidden;"><img src="{ASSETS}/img-03.jpg" style="width:100%;height:100%;object-fit:cover;filter:grayscale(15%) contrast(1.08);" alt=""></div>
      <div style="aspect-ratio:3/2;overflow:hidden;"><img src="{ASSETS}/img-05.jpg" style="width:100%;height:100%;object-fit:cover;filter:grayscale(15%) contrast(1.08);" alt=""></div>
      <div style="aspect-ratio:3/2;overflow:hidden;"><img src="{ASSETS}/img-06.jpg" style="width:100%;height:100%;object-fit:cover;filter:grayscale(15%) contrast(1.08);" alt=""></div>
    </div>
    <div class="meta" style="margin-top:4mm;">
      Moodboard de calibración · referencias editoriales, no imágenes finales de marca
    </div>
  </div>
</div>

{metastrip(33, "VIII · Fotografía")}"""
    return page_shell(body, 33, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# IX VOZ Y TONO  (pp 34-36)
# ══════════════════════════════════════════════════════════════

def p34_voz_divider():
    return divider("09", "IX", "Voz y tono",
                   "Principios · registro · glosario.", pg=34,
                   img=f"{ASSETS}/generated/div-voz-v3.png")


def p35_voz_principios():
    principios = [
        ("Claro antes que bonito", "Si una frase necesita un adjetivo, probablemente sobra el adjetivo y falta un sustantivo."),
        ("Directo sin ser seco",   "Usamos 'tú', frases cortas y subordinadas mínimas. Pero no renunciamos al ritmo."),
        ("Concreto sobre vago",    "Precios exactos, plazos en días, métricas sin redondear."),
        ("Nombra lo exacto",       "Precios, plazos, scope. Datos antes que adjetivos."),
    ]
    prin_html = ""
    for i, (title, desc) in enumerate(principios, 1):
        prin_html += f"""\
<div style="padding:4mm 0;border-bottom:0.5px solid {CENIZA};">
  <div style="display:flex;gap:4mm;align-items:baseline;margin-bottom:2mm;">
    <span style="font-family:{MONO};font-size:10px;font-weight:700;color:{LACRE};font-variant-numeric:tabular-nums;">{i:02d}</span>
    <span style="font-family:{FAM};font-size:16px;font-weight:900;color:{NEGRO};">{title}<span style="color:{LACRE};">.</span></span>
  </div>
  <div class="body-text" style="font-size:11px;margin-left:14mm;">{desc}</div>
</div>"""

    tono_rows = [
        ("Landing",   "Provocador",  "Directo, afirmativo, con pulso editorial"),
        ("Propuesta", "Riguroso",    "Datos, rangos, plazos — sin adornos"),
        ("Email",     "Cercano",     "Tú, sin florituras, pero sin perder oficio"),
        ("Manual",    "Declarativo", "Cada regla con su razón, sin hedging"),
        ("Social",    "Afilado",     "Ideas cortas, sin emoji, sin hashtag salvo branded"),
    ]
    tono_html = "".join(
        f"""<div style="display:grid;grid-template-columns:24mm 28mm 1fr;gap:4mm;
  padding:2.6mm 0;border-bottom:0.5px solid {CENIZA};align-items:baseline;">
  <span style="font-family:{MONO};font-size:8px;color:{PIEDRA};letter-spacing:1.3px;text-transform:uppercase;">{canal}</span>
  <span style="font-family:{FAM};font-size:11px;font-weight:700;color:{NEGRO};">{tono}</span>
  <span style="font-family:{FAM};font-size:10.5px;color:{CARBON};line-height:1.4;">{desc}</span>
</div>"""
        for canal, tono, desc in tono_rows
    )

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">IX · Voz y tono · 35</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;">
  <div>
    {titulo("Principios de voz", 32)}
    {prin_html}
  </div>
  <div>
    {titulo("Registro por canal", 32)}
    <div class="body-text" style="font-size:11px;margin-bottom:4mm;">
      La voz no cambia. El tono sí — se ajusta al canal sin perder la personalidad.
    </div>
    {tono_html}
    <div style="margin-top:6mm;background:transparent;border-left:3px solid {LACRE};padding:12px 16px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:2mm;">Test rápido</div>
      <div style="font-family:{FAM};font-size:11px;color:{NEGRO};line-height:1.5;">
        ¿Podría decirlo una agencia grande genérica? Cambia la frase.
        ¿Suena a "growth bro" con emoji? Cambia la frase.
        ¿Hedging con "quizás / a veces / podría"? Reescribe afirmativo.
      </div>
    </div>
  </div>
</div>

{metastrip(35, "IX · Voz y tono")}"""
    return page_shell(body, 35, bg=PAPEL, no_furniture=True)


def p36_voz_vocabulario():
    usamos = [
        ("documentado",  "lo que entregamos — no 'diseñado'"),
        ("sistema",      "más preciso que 'identidad' o 'estilo'"),
        ("editorial",    "producimos un libro, no un PDF suelto"),
        ("publicado",    "precio, plazo, scope — transparentes"),
        ("escrito",      "cada decisión firmada en el manual"),
        ("cerrado",      "scope, plazo y coste definidos antes del kickoff"),
    ]
    evitamos = [
        ("estratégico",     "lo reivindica todo el mundo · vacío"),
        ("impactante",      "adjetivo mendigo · nunca se cumple"),
        ("disruptivo",      "cliché SaaS · borrar"),
        ("excelencia",      "inverso: aspiracional no-descriptivo"),
        ("partner",         "si eres mi proveedor, dilo; 'partner' es eufemismo"),
        ("onboarding",      "usar 'bienvenida' o 'kickoff'"),
        ("a la vanguardia", "adorno de brochure · evitar"),
    ]
    usamos_html = "".join(
        f"""<div style="display:grid;grid-template-columns:32mm 1fr;gap:4mm;
  padding:2.4mm 0;border-bottom:0.5px solid {CENIZA};">
  <span style="font-family:{FAM};font-size:12px;font-weight:700;color:{NEGRO};">{w}</span>
  <span style="font-family:{FAM};font-size:10.5px;color:{PIEDRA};line-height:1.4;">{d}</span>
</div>"""
        for w, d in usamos
    )
    evitamos_html = "".join(
        f"""<div style="display:grid;grid-template-columns:32mm 1fr;gap:4mm;
  padding:2.4mm 0;border-bottom:0.5px solid {CENIZA};">
  <span class="struck" style="font-family:{FAM};font-size:12px;font-weight:500;">{w}</span>
  <span style="font-family:{FAM};font-size:10.5px;color:{PIEDRA};line-height:1.4;">{d}</span>
</div>"""
        for w, d in evitamos
    )

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">IX · Voz y tono · 36</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;">
  <div>
    {titulo("Vocabulario", 34)}
    <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
      Palabras que usamos porque dicen algo preciso.
    </div>
    {usamos_html}
  </div>
  <div>
    {titulo("Frases prohibidas", 34)}
    <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
      Palabras que no usamos porque no dicen nada — o dicen lo contrario.
    </div>
    {evitamos_html}
    <div style="margin-top:6mm;border-left:4px solid {LACRE};padding-left:12px;">
      <div style="font-family:{FAM};font-size:13px;font-weight:500;color:{NEGRO};line-height:1.5;">
        Si una palabra pasaría el corrector automático de cualquier agencia,
        probablemente sobra<span style="color:{LACRE};">.</span>
      </div>
    </div>
  </div>
</div>

{metastrip(36, "IX · Voz y tono")}"""
    return page_shell(body, 36, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# X APLICACIONES  (pp 37-41)
# ══════════════════════════════════════════════════════════════

def p37_apps_divider():
    return divider("10", "X", "Aplicaciones",
                   "Papelería · digital · merch · señalética.", pg=37,
                   img=f"{ASSETS}/generated/div-aplicaciones.png")


def p38_apps_papeleria():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">X · Aplicaciones · 38</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:14mm;">
  <div style="min-width:0;">
    {titulo("Papelería", 34)}
    <div class="body-text" style="margin-bottom:8mm;">
      Tarjeta doble cara · 85 × 55 mm · papel texturizado 350 g · corte recto.
      Una cara wordmark, otra cara datos — nunca ambos en la misma cara.
    </div>

    <!-- Row 1 · Business card front + back -->
    <div style="display:flex;gap:5mm;margin-bottom:3mm;">
      <div class="mockup-shadow" style="background:{NEGRO};width:62mm;height:40mm;
        display:flex;align-items:center;justify-content:center;">
        <div style="font-family:{FAM};font-size:17px;font-weight:900;color:{PAPEL};letter-spacing:-0.5px;">
          {BRAND}<span style="color:{LACRE};font-size:20px;">.</span>
        </div>
      </div>
      <div class="mockup-shadow" style="background:{PAPEL};width:62mm;height:40mm;
        border:0.5px solid {CENIZA};padding:5mm 6mm;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden;">
        <div style="position:absolute;top:-2mm;right:-6mm;width:28mm;height:0.8mm;background:{LACRE};transform:rotate(-28deg);transform-origin:100% 50%;pointer-events:none;"></div>
        <div style="position:absolute;right:5mm;bottom:4mm;width:2.5mm;height:2.5mm;border-radius:50%;background:{LACRE};pointer-events:none;"></div>
        <div>
          <div style="font-family:{FAM};font-size:8px;font-weight:900;color:{NEGRO};">
            Fernando Rojas Pacheco<span style="color:{LACRE};">.</span>
          </div>
          <div style="font-family:{MONO};font-size:5.5px;color:{PIEDRA};margin-top:0.5mm;letter-spacing:1px;text-transform:uppercase;">Fundador</div>
        </div>
        <div style="font-family:{MONO};font-size:5.5px;color:{PIEDRA};line-height:1.6;letter-spacing:0.5px;">
          hola@tramarca.es<br>
          tramarca.es · Madrid
        </div>
      </div>
    </div>
    <div class="meta" style="margin-bottom:5mm;">Tarjeta 85×55 mm · anverso Negro · reverso Papel</div>

    <!-- Row 2 · Letterhead + envelope -->
    <div style="display:flex;gap:5mm;align-items:flex-start;">
      <div class="mockup-shadow" style="background:{PAPEL};width:54mm;height:52mm;
        border:0.5px solid {CENIZA};padding:6mm 5mm;display:flex;flex-direction:column;">
        <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:3mm;">
          <div style="font-family:{FAM};font-size:8px;font-weight:900;color:{NEGRO};">
            {BRAND}<span style="color:{LACRE};">.</span>
          </div>
          <div style="font-family:{MONO};font-size:5px;color:{PIEDRA};letter-spacing:0.8px;">tramarca.es</div>
        </div>
        <div style="width:14mm;height:0.5px;background:{LACRE};margin-bottom:3mm;"></div>
        <div style="font-family:{FAM};font-size:5.5px;color:{CARBON};line-height:1.55;">
          Hola Marta,<br><br>
          Adjunto propuesta Tramarca Profesional. Scope cerrado, plazo 7 días.<br><br>
          — Fernando<span style="color:{LACRE};">.</span>
        </div>
      </div>
      <div class="mockup-shadow" style="background:{PAPEL};width:70mm;height:36mm;
        border:0.5px solid {CENIZA};position:relative;padding:4mm 6mm;display:flex;flex-direction:column;justify-content:space-between;">
        <div style="font-family:{FAM};font-size:7px;font-weight:900;color:{NEGRO};">
          {BRAND}<span style="color:{LACRE};">.</span>
        </div>
        <div style="font-family:{MONO};font-size:5px;color:{PIEDRA};line-height:1.55;letter-spacing:0.4px;">
          Manual de marca · C/ Serrano 88<br>
          28006 Madrid · hola@tramarca.es
        </div>
        <div style="position:absolute;right:6mm;top:50%;transform:translateY(-50%);
          width:5mm;height:5mm;border-radius:50%;background:{LACRE};
          box-shadow:0 0 0 1px rgba(12,12,12,0.08);"></div>
      </div>
    </div>
    <div class="meta" style="margin-top:3mm;">Carta A5 + sobre DL · Papel 120 g · sello Lacre</div>
  </div>

  <div style="display:flex;flex-direction:column;gap:6mm;min-width:0;">
    <div style="border-top:2px solid {NEGRO};padding-top:4mm;">
      <div class="eyebrow" style="margin-bottom:3mm;">Especificaciones</div>
      <div class="db" style="font-size:10px;line-height:2;">
        <div><span class="lbl" style="min-width:70px;">Formato</span> 85 × 55 mm</div>
        <div><span class="lbl" style="min-width:70px;">Papel</span> Fedrigoni Tintoretto 350 g</div>
        <div><span class="lbl" style="min-width:70px;">Anverso</span> Negro · wordmark</div>
        <div><span class="lbl" style="min-width:70px;">Reverso</span> Papel · datos mono</div>
        <div><span class="lbl" style="min-width:70px;">Acabado</span> Corte recto · relieve</div>
        <div><span class="lbl" style="min-width:70px;">Impresión</span> Offset · Lacre 18-1550</div>
      </div>
    </div>
    <div style="border-left:3px solid {LACRE};padding:2mm 0 2mm 10px;">
      <div class="eyebrow" style="margin-bottom:2mm;">Regla</div>
      <div style="font-family:{FAM};font-size:11px;color:{NEGRO};line-height:1.55;">
        Nunca imprimir logo en Lacre plano. Punto en Lacre, siempre.
        Fondo Lacre sólido está prohibido (ver capítulo VI).
      </div>
    </div>
  </div>
</div>

{metastrip(38, "X · Aplicaciones")}"""
    return page_shell(body, 38, bg=PAPEL, no_furniture=True)


def p39_apps_email():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">X · Aplicaciones · 39</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1.3fr 1fr;gap:16mm;">
  <div>
    {titulo("Firma de email", 34)}
    <div class="body-text" style="margin-bottom:6mm;max-width:120mm;">
      Texto plano siempre. Sin imagen incrustada, sin HTML complicado, sin disclaimer largo.
      La firma termina en punto Lacre (vía carácter Unicode o HTML mínimo).
    </div>

    <!-- Email mockup -->
    <div class="mockup-shadow" style="background:{PAPEL};border:0.5px solid {CENIZA};overflow:hidden;">
      <div style="background:{PAPEL};padding:4mm 6mm;border-bottom:0.5px solid {CENIZA};font-family:{MONO};font-size:8px;color:{PIEDRA};letter-spacing:1px;text-transform:uppercase;">
        De · Fernando · Tramarca
      </div>
      <div style="padding:8mm 10mm;">
        <div style="font-family:{FAM};font-size:12px;color:{NEGRO};line-height:1.6;margin-bottom:8mm;">
          Hola Marta,<br><br>
          Gracias por el brief. Te he enviado la propuesta con link de pago.<br>
          Si confirmas hoy, kickoff el jueves y entrega el 28 de abril.<br><br>
          Cualquier duda, contesta a este email.
        </div>
        <div style="padding-top:4mm;border-top:0.5px solid {CENIZA};">
          <div style="font-family:{FAM};font-size:11px;font-weight:900;color:{NEGRO};">
            Fernando Rojas Pacheco<span style="color:{LACRE};">.</span>
          </div>
          <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};margin-top:2mm;line-height:1.7;">
            Tramarca · Manuales de marca por escrito<br>
            hola@tramarca.es · tramarca.es
          </div>
        </div>
      </div>
    </div>
  </div>

  <div style="display:flex;flex-direction:column;gap:5mm;">
    {data_block([
        ("Formato",    "Texto plano · sin imagen"),
        ("Nombre",     "Satoshi 900 · punto Lacre"),
        ("Subcopia",   "Plex Mono · 1 línea studio + contacto"),
        ("Separador",  "Línea 0.5px · Ceniza"),
        ("Long. máx",  "4 líneas · no disclaimer legal"),
        ("Respuesta",  "24 h laborables · publicado"),
    ])}
    <div style="background:{NEGRO};padding:14px 16px;color:{PAPEL};">
      <div class="eyebrow" style="color:{LACRE};margin-bottom:3mm;">Texto pegable</div>
      <pre style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.85);line-height:1.6;white-space:pre-wrap;margin:0;">Fernando Rojas Pacheco.
Tramarca · Manuales de marca por escrito
hola@tramarca.es · tramarca.es</pre>
    </div>
  </div>
</div>

{metastrip(39, "X · Aplicaciones")}"""
    return page_shell(body, 39, bg=PAPEL, no_furniture=True)


def p40_apps_digital():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">X · Aplicaciones · 40</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:14mm;">
  <div>
    {titulo("Web", 30)}
    <div class="body-text" style="margin-bottom:6mm;">
      tramarca.es — stack Next.js 16, Satoshi self-hosted, Tailwind v4.
      Masthead editorial fija, grid 12-col 24 mm márgenes.
    </div>

    <!-- Real screenshot tramarca.es home -->
    <div class="mockup-shadow" style="background:{PAPEL};border:0.5px solid {CENIZA};overflow:hidden;">
      <div class="browser-chrome">
        <div class="browser-dot"></div>
        <div class="browser-dot"></div>
        <div class="browser-dot"></div>
        <div style="font-family:{MONO};font-size:7px;color:{PIEDRA};margin-left:3mm;">tramarca.es</div>
      </div>
      <div style="height:78mm;overflow:hidden;position:relative;">
        <img src="{ASSETS}/tramarca-web-home.jpg"
          style="width:100%;display:block;object-fit:cover;object-position:top center;" alt="Captura tramarca.es">
      </div>
      <div style="padding:2mm 6mm;border-top:0.5px solid {CENIZA};
        font-family:{MONO};font-size:6.5px;color:{PIEDRA};letter-spacing:1.2px;text-transform:uppercase;">
        tramarca.es · captura real
      </div>
    </div>
  </div>

  <div>
    {titulo("Propuesta PDF", 30)}
    <div class="body-text" style="margin-bottom:6mm;">
      Cada lead recibe una propuesta en PDF generada dinámicamente
      con el tier, plazo y link de pago Stripe personalizados.
    </div>

    <!-- Proposal doc mockup (no wrapper frame) -->
    <div class="mockup-shadow doc-mockup" style="background:{PAPEL};border:0.5px solid {CENIZA};padding:8mm 10mm;">
      <div style="display:flex;justify-content:space-between;align-items:baseline;padding-bottom:4mm;border-bottom:0.5px solid {CENIZA};">
        <div style="font-family:{FAM};font-size:11px;font-weight:900;color:{NEGRO};">{BRAND}<span style="color:{LACRE};">.</span></div>
        <div style="font-family:{MONO};font-size:7px;color:{PIEDRA};letter-spacing:1.2px;text-transform:uppercase;">PROP-2026-012</div>
      </div>
      <div style="font-family:{FAM};font-size:22px;font-weight:900;color:{NEGRO};line-height:1;margin-top:6mm;">
        Propuesta<br>Profesional<span style="color:{LACRE};">.</span>
      </div>
      <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};margin-top:3mm;">Cliente · Marta Núñez</div>
      <div style="display:flex;justify-content:space-between;margin-top:8mm;padding-top:4mm;border-top:0.5px solid {CENIZA};">
        <div>
          <div class="meta">IMPORTE</div>
          <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{NEGRO};">990€ IVA incl.</div>
        </div>
        <div>
          <div class="meta">PLAZO</div>
          <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{NEGRO};">7 días laborables</div>
        </div>
      </div>
    </div>
  </div>
</div>

{metastrip(40, "X · Aplicaciones")}"""
    return page_shell(body, 40, bg=PAPEL, no_furniture=True)


def p41_apps_merch_senal():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">X · Aplicaciones · 41</div>
  <div style="display:flex;gap:3mm;">
    {fidelity_badge("PROPUESTA")} {fidelity_badge("INVENTADO")}
  </div>
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:14mm;">
  <div>
    {titulo("Merch", 32)}
    <div class="body-text" style="margin-bottom:6mm;">
      Merch mínimo, funcional — no gadgets. Libro físico del manual
      Premium, carpetilla A4 de entrega, bolsa kraft con sello.
    </div>
    {data_block([
        ("Libro",         "Cosido · tapa Negro · canto Lacre"),
        ("Carpetilla",    "Kraft 300g · sello Tramarca en relieve"),
        ("Bolsa",         "Kraft natural · asa plana · sello troquelado"),
        ("Prohibido",     "Gadgets · tazas · chapas · pins"),
    ])}
    <div style="margin-top:6mm;border-left:3px solid {LACRE};padding-left:10px;">
      <div class="body-text" style="font-size:11px;">
        El libro físico va con el tier Premium (FIEL, publicado en /precios).
        No se imprime para Esencial ni Profesional.
      </div>
    </div>
  </div>

  <div>
    {titulo("Señalética", 32)}
    <div class="body-text" style="margin-bottom:6mm;">
      Tramarca no tiene oficina pública — la señalética es digital.
      Email, dominio, firmas, headers de documento siguen el mismo sistema.
    </div>

    <div style="background:{NEGRO};padding:14px 18px;color:{PAPEL};margin-bottom:5mm;">
      <div class="eyebrow" style="color:{LACRE};margin-bottom:3mm;">Header de documento</div>
      <div style="display:flex;justify-content:space-between;align-items:baseline;padding-bottom:3mm;border-bottom:0.5px solid rgba(244,240,235,0.15);">
        <div style="font-family:{FAM};font-size:14px;font-weight:900;">{BRAND}<span style="color:{LACRE};">.</span></div>
        <div style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.5);letter-spacing:1.5px;text-transform:uppercase;">Manuales de marca · Madrid · 2026</div>
      </div>
    </div>
    <div style="background:transparent;border-left:3px solid {LACRE};padding:12px 16px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:2mm;">Nota</div>
      <div style="font-family:{FAM};font-size:11px;color:{NEGRO};line-height:1.5;">
        Señalética física queda fuera de scope.
        Si abrimos estudio físico, volverá este capítulo.
      </div>
    </div>
  </div>
</div>

{metastrip(41, "X · Aplicaciones")}"""
    return page_shell(body, 41, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# XI ARQUITECTURA DE MARCA  (pp 42-43)
# ══════════════════════════════════════════════════════════════

def p42_arq_divider():
    return divider("11", "XI", "Arquitectura",
                   "Marca ↔ producto · submarcas · endorsement.", pg=42,
                   img=f"{ASSETS}/generated/div-arquitectura.png")


def p43_arq_sistema():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">XI · Arquitectura · 43</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1.1fr;gap:16mm;">
  <div>
    {titulo("Arquitectura", 36)}
    <div class="body-text" style="margin-bottom:6mm;max-width:110mm;">
      Tramarca opera como marca monolítica. Una sola marca madre,
      sin submarcas de producto, sin extensiones, sin sub-brands.
      Los tres tiers son niveles de scope, no marcas.
    </div>
    <!-- Diagram -->
    <div style="background:transparent;border-left:3px solid {LACRE};padding:22px 24px 26px 18px;">
      <div class="eyebrow" style="margin-bottom:10mm;">Modelo · monolítico</div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:8mm;">
        <div style="font-family:{FAM};font-size:58px;font-weight:900;color:{NEGRO};letter-spacing:-2px;line-height:1;">
          TRAMARCA<span style="color:{LACRE};">.</span>
        </div>
        <div style="width:2px;height:18mm;background:{CENIZA};"></div>
        <div style="display:flex;gap:14mm;">
          <div style="font-family:{MONO};font-size:11px;color:{NEGRO};letter-spacing:1.5px;text-transform:uppercase;font-weight:700;">Esencial</div>
          <div style="font-family:{MONO};font-size:11px;color:{NEGRO};letter-spacing:1.5px;text-transform:uppercase;font-weight:700;">Profesional</div>
          <div style="font-family:{MONO};font-size:11px;color:{NEGRO};letter-spacing:1.5px;text-transform:uppercase;font-weight:700;">Premium</div>
        </div>
        <div class="meta" style="margin-top:3mm;">Tres niveles · una sola marca</div>
      </div>
    </div>
  </div>

  <div>
    <div class="eyebrow" style="margin-bottom:4mm;">Reglas de convivencia</div>
    <div style="display:flex;flex-direction:column;gap:3mm;">

      <div style="padding:4mm 0;border-bottom:0.5px solid {CENIZA};">
        <div style="font-family:{FAM};font-size:13px;font-weight:700;color:{NEGRO};margin-bottom:1mm;">Marca ↔ producto {fidelity_badge("PROPUESTA")}</div>
        <div class="body-text" style="font-size:11px;">El "producto" (tier) nunca antecede a Tramarca. Se nombra "Tramarca Esencial", nunca "Esencial by Tramarca".</div>
      </div>

      <div style="padding:4mm 0;border-bottom:0.5px solid {CENIZA};">
        <div style="font-family:{FAM};font-size:13px;font-weight:700;color:{NEGRO};margin-bottom:1mm;">Co-branding {fidelity_badge("PROPUESTA")}</div>
        <div class="body-text" style="font-size:11px;">Permitido solo cuando Tramarca va segunda ("En colaboración con Tramarca."). Nunca al mismo nivel.</div>
      </div>

      <div style="padding:4mm 0;border-bottom:0.5px solid {CENIZA};">
        <div style="font-family:{FAM};font-size:13px;font-weight:700;color:{NEGRO};margin-bottom:1mm;">Submarcas {fidelity_badge("PROPUESTA")}</div>
        <div class="body-text" style="font-size:11px;">Prohibidas. Si surge una línea nueva de servicio, se vuelve al paso 1 y se replantea si es Tramarca o no.</div>
      </div>

      <div style="padding:4mm 0;">
        <div style="font-family:{FAM};font-size:13px;font-weight:700;color:{NEGRO};margin-bottom:1mm;">Endorsement {fidelity_badge("PROPUESTA")}</div>
        <div class="body-text" style="font-size:11px;">Caso Estudio proveedor (Persona C): la agencia firma — Tramarca acredita en el colofón editorial del manual entregado.</div>
      </div>

    </div>

    <div style="margin-top:6mm;border-left:4px solid {LACRE};padding-left:12px;">
      <div style="font-family:{FAM};font-size:13px;font-weight:500;color:{NEGRO};line-height:1.5;">
        Una sola marca. Una sola voz. Un solo punto final<span style="color:{LACRE};">.</span>
      </div>
    </div>
  </div>
</div>

{metastrip(43, "XI · Arquitectura")}"""
    return page_shell(body, 43, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# XII GOVERNANCE  (pp 44-46)
# ══════════════════════════════════════════════════════════════

def p44_gov_divider():
    return divider("12", "XII", "Governance",
                   "Aprobación · versionado · formación.", pg=44,
                   img=f"{ASSETS}/generated/div-governance.png")


def p45_gov_checklist():
    checklist = [
        ("Logo", [
            "Punto en Lacre, no en otro color",
            "Tamaño mínimo cumplido (25 mm / 80 px)",
            "Zona de respeto X alrededor",
            "Variante correcta para el fondo",
        ]),
        ("Tipografía", [
            "Satoshi para display y cuerpo",
            "Plex Mono solo para metadata < 11 px",
            "Sin cursivas salvo subtítulo cover",
            "Tabular-nums en precios y stats",
        ]),
        ("Color", [
            "Contraste mínimo WCAG AA (4.5:1)",
            "Lacre como acento, nunca fondo",
            "Sin degradados · colores planos",
        ]),
        ("Voz", [
            "Sin adjetivos mendigos (impactante · disruptivo)",
            "Frases afirmativas · sin hedging",
            "Tuteo editorial · sin usted",
        ]),
    ]
    blocks = ""
    for title, items in checklist:
        rows = "".join(
            f"""<div style="display:grid;grid-template-columns:6mm 1fr;gap:3mm;padding:1.8mm 0;border-bottom:0.5px solid {CENIZA};align-items:baseline;">
  <div style="width:4mm;height:4mm;border:1px solid {NEGRO};"></div>
  <span style="font-family:{FAM};font-size:11px;color:{CARBON};">{item}</span>
</div>"""
            for item in items
        )
        blocks += f"""<div style="margin-bottom:5mm;">
  <div class="eyebrow" style="margin-bottom:3mm;">{title}</div>
  {rows}
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">XII · Governance · 45</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1.3fr 1fr;gap:16mm;">
  <div>
    {titulo("Checklist de uso", 34)}
    <div class="body-text" style="font-size:11px;margin-bottom:6mm;">
      Antes de publicar cualquier pieza — web, email, doc, post —
      pasa por este checklist. 14 ítems. Si alguno falla, no se publica.
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm;">
      {blocks}
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:5mm;">
    <div>
      <div class="eyebrow" style="margin-bottom:3mm;">Responsables</div>
      {data_block([
          ("Aprobación final", "Fernando Rojas Pacheco · único firmante"),
          ("Revisión interna", "Cualquier miembro del estudio"),
          ("Cliente",          "Aprueba entregables, no reglas"),
          ("Terceros",         "Nunca modifican · solo aplican"),
      ])}
    </div>

    <div style="background:{NEGRO};padding:14px 16px;color:{PAPEL};">
      <div class="eyebrow" style="color:{LACRE};margin-bottom:3mm;">Regla cero</div>
      <div style="font-family:{FAM};font-size:13px;font-weight:500;line-height:1.5;">
        Si una pieza no se puede explicar con alguna regla de este manual,
        la regla que falta se documenta antes de publicar la pieza<span style="color:{LACRE};">.</span>
      </div>
    </div>

    <div style="background:transparent;border-left:3px solid {LACRE};padding:12px 16px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:2mm;">Ciclo</div>
      <div style="font-family:{FAM};font-size:11px;color:{NEGRO};line-height:1.5;">
        Draft · Review interno · Firma Fernando · Publicación.
        Sin excepciones para "urgencias".
      </div>
    </div>
  </div>
</div>

{metastrip(45, "XII · Governance")}"""
    return page_shell(body, 45, bg=PAPEL, no_furniture=True)


def p46_gov_versioning():
    versions = [
        ("v4.0", "2026-04-17", "Anatomy-aligned rebuild. 58pp. Cover v9, personas data-viz, TL;DR V9.", "Actual"),
        ("v3.0", "2026-04-11", "45pp. Añadidos F7/S6/V3/V6/I7/A8/O1/O2/O3/V9.", "Legacy"),
        ("v2.0", "2026-04-08", "34pp brutal. Primera versión editorial cinematográfica.", "Legacy"),
        ("v1.0", "2026-04-01", "Proof of concept · 20pp interno.", "Legacy"),
    ]
    rows = ""
    for tag, date, notes, state in versions:
        rows += f"""\
<div style="display:grid;grid-template-columns:18mm 30mm 1fr 24mm;gap:6mm;
  padding:4mm 0;border-bottom:0.5px solid {CENIZA};align-items:baseline;">
  <span style="font-family:{MONO};font-size:12px;font-weight:700;color:{LACRE};font-variant-numeric:tabular-nums;">{tag}</span>
  <span style="font-family:{MONO};font-size:10px;color:{PIEDRA};font-variant-numeric:tabular-nums;">{date}</span>
  <span style="font-family:{FAM};font-size:11px;color:{CARBON};line-height:1.5;">{notes}</span>
  <span style="font-family:{MONO};font-size:8px;font-weight:700;color:{NEGRO if state == 'Actual' else PIEDRA};
    letter-spacing:1.2px;text-transform:uppercase;">{state}</span>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">XII · Governance · 46</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1.2fr 1fr;gap:16mm;">
  <div>
    {titulo("Versionado", 34)}
    <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
      SemVer editorial. Mayor cuando cambia estructura · menor cuando cambia contenido ·
      patch cuando cambian typos o assets.
    </div>
    {rows}
    <div style="margin-top:6mm;">
      {data_block([
          ("Mayor (X.0.0)", "Cambio de estructura o scope · regenera PDF completo"),
          ("Menor (0.X.0)", "Añade/reemplaza capítulo · regenera sección"),
          ("Patch (0.0.X)", "Typo, asset, corrección · regenera página"),
          ("Cadencia",      "Revisión cada 6 meses · mayor cada 12-18"),
      ])}
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:5mm;">
    <div>
      <div class="eyebrow" style="margin-bottom:3mm;">Formación del equipo</div>
      <div class="body-text" style="font-size:11px;">
        Cualquier persona que toque la marca pasa por este manual antes
        de producir una sola pieza. Bienvenida = leer este PDF
        + checklist del capítulo anterior.
      </div>
    </div>
    <div style="background:transparent;border-left:3px solid {LACRE};padding:14px 18px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:3mm;">Repositorio</div>
      <div style="font-family:{MONO};font-size:9px;color:{PIEDRA};line-height:1.9;letter-spacing:0.5px;">
        github.com/ferrojas93-sketch/brand-manuals<br>
        repo 04-tramarca · branch main<br>
        build: python3 src/build_v4.py<br>
        render: python3 src/render_pdf.py
      </div>
    </div>
    <div style="border-left:4px solid {LACRE};padding-left:12px;">
      <div style="font-family:{FAM};font-size:13px;font-weight:500;color:{NEGRO};line-height:1.5;">
        Cada versión queda archivada<span style="color:{LACRE};">.</span>
        Si un cliente pregunta "¿qué había antes?",
        se responde con el PDF, no con memoria.
      </div>
    </div>
  </div>
</div>

{metastrip(46, "XII · Governance")}"""
    return page_shell(body, 46, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# XIII MARCA EN MOVIMIENTO  (pp 47-48)
# ══════════════════════════════════════════════════════════════

def p47_motion_divider():
    return divider("13", "XIII", "Marca en movimiento",
                   "Motion · microinteracciones · video.", pg=47,
                   img=f"{ASSETS}/generated/div-motion-v2.png")


def p48_motion_sistema():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">XIII · Marca en movimiento · 48</div>
  <div style="display:flex;gap:3mm;">
    {fidelity_badge("PROPUESTA")} {fidelity_badge("INVENTADO")}
  </div>
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:14mm;">

  <div>
    {titulo("Motion del logo", 30)}
    <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
      La marca entra en dos tiempos: wordmark aparece sin animación,
      el punto Lacre aterriza después con un micro-drop.
      Nunca un reveal de izquierda a derecha. Nunca un morph.
    </div>
    {data_block([
        ("Duración total","0.45s · 27 frames @ 60fps"),
        ("Easing",        "cubic-bezier(0.2, 0, 0, 1)"),
        ("Step 1",        "Wordmark fade-in · 0 – 0.30s"),
        ("Step 2",        "Punto drop · 0.30 – 0.45s"),
        ("Loop",          "Sin loop · animación única al cargar"),
        ("Sin",           "Morph · reveal lateral · bounce"),
    ])}
    <div style="margin-top:5mm;border-left:3px solid {LACRE};padding-left:10px;">
      <div class="body-text" style="font-size:11px;">
        Solo en web y en video opener. Nunca en email, doc, PDF.
      </div>
    </div>
  </div>

  <div>
    {titulo("Microinteracciones", 30)}
    <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
      Todos los elementos interactivos (botones, links, inputs) responden en 180ms
      con un cambio mínimo. Ni hover flashy ni transforms ni shadows.
    </div>
    {data_block([
        ("Hover link",    "Color Lacre · 180ms ease-out"),
        ("Focus",         "Outline 3px Lacre · offset 3px"),
        ("Button click",  "Opacity 0.85 · 100ms"),
        ("Drawer open",   "Slide-in right · 260ms"),
        ("Reduced motion","prefers-reduced-motion: reduce · transitions off"),
    ])}

    <div style="margin-top:6mm;background:{NEGRO};padding:14px 16px;color:{PAPEL};">
      <div class="eyebrow" style="color:{LACRE};margin-bottom:3mm;">Video e identidad sonora</div>
      <div style="font-family:{FAM};font-size:11px;line-height:1.5;">
        Identidad sonora fuera de scope 2026. Si producimos video,
        usamos silencio o música instrumental neutral.
        Nunca voice-over corporativo.
      </div>
    </div>

    <div style="margin-top:5mm;font-family:{MONO};font-size:8px;color:{PIEDRA};letter-spacing:1px;text-transform:uppercase;">
      Especificación sin implementación de referencia · revisión 2026 Q4
    </div>
  </div>

</div>

{metastrip(48, "XIII · Marca en movimiento")}"""
    return page_shell(body, 48, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# XIV EXTENSIONES  (pp 49-51)
# ══════════════════════════════════════════════════════════════

def p49_ext_divider():
    return divider("14", "XIV", "Extensiones",
                   "Accesibilidad · digital · territorial · legal.", pg=49,
                   img=f"{ASSETS}/img-04.jpg")


def p50_ext_a11y_digital():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">XIV · Extensiones · 50</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;">
  <div>
    {titulo("Accesibilidad", 30)}
    <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
      WCAG 2.2 AA como mínimo, AAA donde no afecte jerarquía.
      Piedra 5E5A57 es el token oscurecido post-audit 2026-04
      para cumplir ratio 5.2:1 sobre Papel.
    </div>
    {data_block([
        ("Contraste texto",  "Mín AA 4.5:1 · objetivo AAA 7:1"),
        ("Focus visible",    "Outline 3px Lacre · offset 3-4px"),
        ("Touch targets",    "Mín 40 × 40 px mobile"),
        ("Reduced motion",   "Todas transitions desactivables"),
        ("Alt text",         "Todas imágenes · vacío si decorativas"),
        ("Keyboard",         "Navegación completa sin mouse"),
    ])}
    <div style="margin-top:5mm;border-left:3px solid {LACRE};padding-left:10px;">
      <div class="body-text" style="font-size:11px;">
        Accesibilidad no es feature — es parte del sistema base.
        Componente que no pasa AA, se rehace. No se publica.
      </div>
    </div>
  </div>

  <div>
    {titulo("Sistema digital", 30)}
    <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
      Tokens CSS que espejan los tokens de este manual.
      Variable fonts, rem-based, mobile-first.
    </div>
    <div style="background:{NEGRO};padding:12px 14px;color:{PAPEL};">
      <div class="eyebrow" style="color:{LACRE};margin-bottom:3mm;">Tokens CSS</div>
      <pre style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.85);line-height:1.7;white-space:pre-wrap;margin:0;">:root {{
  --color-negro:   #0C0C0C;
  --color-carbon:  #1C1C1C;
  --color-lacre:   #C4553A;
  --color-piedra:  #5E5A57;
  --color-ceniza:  #B5B1AC;
  --color-arena:   #E4E2DC;
  --color-papel:   #F4F0EB;

  --font-sans: 'Satoshi', system-ui;
  --font-mono: 'IBM Plex Mono', monospace;

  --radius: 0;  /* sin radios */
  --focus-ring: 3px solid var(--color-lacre);
}}</pre>
    </div>
    <div style="margin-top:4mm;font-family:{MONO};font-size:8px;color:{PIEDRA};letter-spacing:1px;text-transform:uppercase;">
      tramarca.es · globals.css
    </div>
  </div>
</div>

{metastrip(50, "XIV · Extensiones")}"""
    return page_shell(body, 50, bg=PAPEL, no_furniture=True)


def p51_ext_territorial_legal():
    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">XIV · Extensiones · 51</div>
  {fidelity_badge("PROPUESTA")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;">
  <div>
    {titulo("Territorial", 30)}
    <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
      Tramarca opera en España en castellano. Cuando atendemos LATAM,
      mantenemos castellano ibérico — sin switching a neutro ni inglés.
      La marca es una marca española contemporánea.
    </div>
    {data_block([
        ("Idioma primario", "Castellano · ibérico"),
        ("Secundario",      "Inglés · solo documentación técnica"),
        ("Mercado",         "España · LATAM remoto"),
        ("Moneda",          "EUR · IVA incluido publicado"),
        ("Facturación",     "Fiscal España · IVA 21%"),
        ("Pago",            "Stripe · tarjeta + SEPA"),
    ])}
    <div style="margin-top:5mm;border-left:3px solid {LACRE};padding-left:10px;">
      <div class="body-text" style="font-size:11px;">
        Si un cliente latinoamericano prefiere inglés, se acomoda —
        pero el manual entregado sigue siendo en castellano.
      </div>
    </div>
  </div>

  <div>
    {titulo("Legal", 30)}
    <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
      La marca Tramarca se protege. El manual documenta los usos
      autorizados. Lo que no está aquí, no se puede reclamar.
    </div>
    {data_block([
        ("Titularidad",    "Fernando Rojas Pacheco · Madrid"),
        ("Marca registrada","OEPM · pendiente solicitud Q2 2026"),
        ("Copyright",      "© 2026 Tramarca · todos derechos reservados"),
        ("Licencia uso",   "Propietaria · no reproducible sin autorización"),
        ("Activos",        "Logo, paleta, tipografía = propiedad estudio"),
        ("Clientes",       "Reciben assets con licencia de uso, no propiedad de marca"),
    ])}
    <div style="margin-top:6mm;background:transparent;border-left:3px solid {LACRE};padding:12px 16px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:2mm;">Protección de cliente</div>
      <div style="font-family:{FAM};font-size:11px;color:{NEGRO};line-height:1.5;">
        Cada manual entregado incluye licencia de uso explícita
        para el cliente sobre sus propios activos (no los de Tramarca).
        El cliente recibe fuentes, SVG, tokens — con derechos de uso.
      </div>
    </div>
  </div>
</div>

{metastrip(51, "XIV · Extensiones")}"""
    return page_shell(body, 51, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# XV SERVICIO  (pp 52-55)
# ══════════════════════════════════════════════════════════════

def p52_servicio_divider():
    return divider("15", "XV", "Servicio",
                   "Tiers · proceso · entrega.", pg=52,
                   img=f"{ASSETS}/generated/div-servicio-v2.png")


def p53_tiers_real():
    tiers = [
        ("Esencial", "490€",   "20 – 25 pp",  "5 días",
         "Para quien firma su primer cliente y necesita dejar de improvisar.",
         ["Manual 20-25pp · PDF A4 landscape",
          "Logo: sistema, variantes, clearspace",
          "Paleta cromática (HEX · RGB · CMYK)",
          "Sistema tipográfico base",
          "Grid y construcción del sistema",
          "3 aplicaciones clave · papelería, email, social",
          "Usos correctos e incorrectos del logo",
          "Archivos fuente · SVG + PNG + PDF"], False),
        ("Profesional", "990€", "30 – 40 pp", "7 días",
         "Para el estudio que cobra 3× y necesita parecerlo en cada propuesta.",
         ["Todo lo de Esencial +",
          "Sistema visual extendido · jerarquías",
          "Tono de voz documentado + vocabulario",
          "Guidelines verbales · qué decir/evitar",
          "Guidelines aplicación extendidas",
          "Sistema tipográfico jerárquico H1-H4",
          "Paleta extendida · roles y combinaciones",
          "Plantillas editables en Figma",
          "Archivos fuente completos · SVG/PNG/PDF/Figma"], True),
        ("Premium", "1.990€",  "40 – 50 pp",  "10 días",
         "Para cuando la marca ya factura y el manual es documento legal: lo firma tu dirección, lo consulta tu agencia, lo hereda tu sucesor.",
         ["LIBRO FÍSICO IMPRESO · encuadernado, enviado",
          "Todo lo de Profesional +",
          "Estrategia de marca · arquetipo, posicionamiento",
          "Identidad verbal · naming, tagline, vocabulario",
          "Sistema visual exhaustivo · logo, variantes, usos",
          "Guidelines totales · web, papelería, social, merch",
          "Sistema tipográfico · OpenType features",
          "Paleta completa · 60/30/10 jerarquía",
          "Biblioteca Figma extendida",
          "Dirección para fotografía e imagen",
          "Archivos fuente + assets empaquetados"], False),
    ]
    cols = ""
    for name, price, pages, timeline, outcome, features, highlight in tiers:
        if highlight:
            bg = LACRE
            border = f"border-top:5px solid {PAPEL};"
            title_color = PAPEL
            price_color = PAPEL
            feat_color = "rgba(244,240,235,0.95)"
            feat_border = "rgba(244,240,235,0.22)"
            meta_color = "rgba(244,240,235,0.85)"
            accent_color = PAPEL
            outcome_color = "rgba(244,240,235,0.92)"
        else:
            bg = PAPEL
            border = f"border-top:3px solid {NEGRO};"
            title_color = NEGRO
            price_color = NEGRO
            feat_color = CARBON
            feat_border = "rgba(12,12,12,0.08)"
            meta_color = PIEDRA
            accent_color = LACRE
            outcome_color = CARBON
        feat_html = "".join(
            f'<div style="font-family:{MONO};font-size:8.5px;color:{feat_color};'
            f'padding:2.5px 0;border-bottom:0.5px solid {feat_border};line-height:1.5;">{f}</div>'
            for f in features
        )
        cols += f"""\
<div style="background:{bg};padding:22px 22px 20px 22px;{border}display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    <div style="display:flex;gap:4mm;align-items:baseline;margin-bottom:3mm;">
      <div style="font-family:{FAM};font-size:26px;font-weight:900;letter-spacing:-0.5px;color:{title_color};">
        {name}<span style="color:{accent_color};">.</span>
      </div>
      {'<span style="background:'+NEGRO+';color:'+PAPEL+';font-family:'+MONO+';font-size:6.5px;font-weight:700;letter-spacing:1.2px;padding:2px 6px;text-transform:uppercase;">Recomendado</span>' if highlight else ''}
    </div>
    <div style="font-family:{FAM};font-size:44px;font-weight:900;color:{price_color};line-height:1;
      letter-spacing:-2px;font-variant-numeric:tabular-nums;margin-bottom:2mm;">{price}</div>
    <div style="font-family:{MONO};font-size:8px;color:{meta_color};letter-spacing:1px;margin-bottom:4mm;">
      {pages} · {timeline} laborables · IVA incl.
    </div>
    <div style="font-family:{FAM};font-size:10.5px;color:{outcome_color};line-height:1.45;
      font-style:italic;margin-bottom:5mm;padding-bottom:4mm;border-bottom:0.5px solid {feat_border};">
      {outcome}
    </div>
    <div style="margin-bottom:4mm;">{feat_html}</div>
  </div>
</div>"""

    body = f"""\
<div class="noise" style="position:absolute;inset:0;"></div>
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div style="display:flex;gap:4mm;align-items:baseline;">
    <div style="font-family:{MONO};font-size:8px;font-weight:700;letter-spacing:3px;
      text-transform:uppercase;color:{LACRE};">XV · Servicio · 53</div>
    {fidelity_badge("FIEL", dark=True)}
  </div>
  <div style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.45);">tramarca.es/precios</div>
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:flex;flex-direction:column;gap:6mm;">
  <div style="font-family:{FAM};font-size:42px;font-weight:900;
    color:{PAPEL};letter-spacing:-2px;line-height:1;">
    Tres tiers<span style="color:{LACRE};">.</span>
    Precio cerrado<span style="color:{LACRE};">.</span>
  </div>
  <div class="g3" style="flex:1;gap:6mm;">
    {cols}
  </div>
  <div style="display:flex;justify-content:space-between;align-items:baseline;padding-top:3mm;border-top:0.5px solid rgba(244,240,235,0.15);">
    <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.55);">
      Precios IVA incluido · plazo publicado · 2 rondas de revisión
    </div>
    <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.55);">
      Pago Stripe · tarjeta o SEPA
    </div>
  </div>
</div>

<div class="metastrip dark">
  <span>{BRAND}<span style="color:{LACRE};">.</span> · Manual de marca</span>
  <span style="text-transform:uppercase;letter-spacing:2px;">XV · Servicio</span>
  <span style="font-variant-numeric:tabular-nums;">53 / {TOTAL}</span>
</div>"""
    return page_shell(body, 53, bg=NEGRO, dark=True, no_furniture=True)


def p54_proceso():
    # SVG icons — 24×24 viewBox, stroke 1.5px LACRE, round caps/joins
    ICON_BRIEF = f"""<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="{LACRE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3h8a2 2 0 0 1 2 2v15l-3-2-3 2-3-2-3 2V5a2 2 0 0 1 2-2z"/><path d="M9 7h6M9 10h6M9 13h3"/></svg>"""
    ICON_KICKOFF = f"""<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="{LACRE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/><circle cx="12" cy="12" r="3"/></svg>"""
    ICON_PRODUCT = f"""<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="{LACRE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18M3 12h18M3 18h12"/><circle cx="19" cy="18" r="1.5"/></svg>"""
    ICON_REVIEW  = f"""<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="{LACRE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5L21 21"/><path d="M8 11h6M11 8v6"/></svg>"""
    ICON_DELIVER = f"""<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="{LACRE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7l9-4 9 4v10l-9 4-9-4V7z"/><path d="M3 7l9 4 9-4M12 11v10"/></svg>"""

    steps = [
        ("01", ICON_BRIEF,   "Brief",      "1 – 2 días", "Cliente rellena formulario · nosotros revisamos y enviamos propuesta"),
        ("02", ICON_KICKOFF, "Kickoff",    "48 h",       "Firma de brief · primer pago 50% · arranca el contador del tier"),
        ("03", ICON_PRODUCT, "Producción", "3 – 7 días", "Tramarca construye el sistema completo"),
        ("04", ICON_REVIEW,  "Revisión",   "1 día",      "Ronda 1: feedback consolidado del cliente · corrección · cierre"),
        ("05", ICON_DELIVER, "Entrega",    "Día final",  "PDF + assets + Figma · segundo pago 50% · libro físico si Premium"),
    ]
    timeline = ""
    for i, (num, icon, name, timing, desc) in enumerate(steps):
        last = i == len(steps) - 1
        timeline += f"""\
<div style="display:grid;grid-template-columns:44px 1fr;gap:6mm;{'margin-top:5mm;' if i > 0 else ''}">
  <div style="display:flex;flex-direction:column;align-items:center;">
    <div style="width:42px;height:42px;border:1.5px solid {LACRE};border-radius:50%;
      display:flex;align-items:center;justify-content:center;flex-shrink:0;background:{PAPEL};">
      {icon}
    </div>
    {'<div style="flex:1;width:1px;background:'+CENIZA+';margin-top:2mm;"></div>' if not last else ''}
  </div>
  <div style="padding-top:2mm;">
    <div style="display:flex;align-items:baseline;gap:4mm;margin-bottom:1mm;">
      <span style="font-family:{MONO};font-size:8px;font-weight:700;color:{LACRE};letter-spacing:1.4px;">{num}</span>
      <span style="font-family:{FAM};font-size:18px;font-weight:900;color:{NEGRO};">{name}<span style="color:{LACRE};">.</span></span>
      <span class="meta">{timing}</span>
    </div>
    <div class="body-text" style="font-size:11px;">{desc}</div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">XV · Servicio · 54</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1fr;gap:18mm;">
  <div>
    {titulo("Proceso", 38)}
    <div class="body-text" style="margin-bottom:6mm;max-width:120mm;">
      Cinco pasos. Plazo publicado. Del brief firmado al libro entregado
      en 5, 7 o 10 días laborables. Cada paso tiene duración conocida y
      entregable definido.
    </div>
    {timeline}
  </div>
  <div style="display:flex;flex-direction:column;gap:5mm;">
    <div>
      <div class="eyebrow" style="margin-bottom:3mm;">Plazo por tier</div>
      {data_block([
          ("Esencial",    "5 días laborables · producción 3 + revisión 1 + entrega 1"),
          ("Profesional", "7 días laborables · producción 5 + revisión 1 + entrega 1"),
          ("Premium",     "10 días laborables · producción 7 + revisión 1 + entrega 2"),
      ])}
    </div>
    <div style="background:transparent;border-left:3px solid {LACRE};padding:14px 18px;padding-left:14px;">
      <div class="eyebrow" style="margin-bottom:3mm;">Revisiones</div>
      <div class="body-text" style="font-size:11px;">
        2 rondas incluidas. Cada ronda = un feedback consolidado del cliente,
        no emails sueltos. Tercera ronda sólo si fallo del estudio, no del cliente.
      </div>
    </div>
    <div style="background:{NEGRO};padding:14px 16px;color:{PAPEL};">
      <div class="eyebrow" style="color:{LACRE};margin-bottom:3mm;">Todo por escrito</div>
      <div style="font-family:{FAM};font-size:12px;line-height:1.5;">
        Cada decisión queda documentada en el hilo. El brief está firmado antes de
        empezar — y el manual publicado es la prueba de lo acordado.
      </div>
    </div>
  </div>
</div>

{metastrip(54, "XV · Servicio")}"""
    return page_shell(body, 54, bg=PAPEL, no_furniture=True)


def p55_garantia():
    """Full-bleed editorial hero spread between servicio and portfolio."""
    body = f"""\
<!-- Full-bleed photo -->
<div style="position:absolute;inset:0;background:{NEGRO};">
  <img src="{ASSETS}/img-03.jpg" style="width:100%;height:100%;object-fit:cover;
    opacity:0.72;filter:grayscale(20%) contrast(1.05);" alt="">
</div>

<!-- Gradient overlay for legibility -->
<div style="position:absolute;inset:0;
  background:linear-gradient(135deg, rgba(12,12,12,0.55) 0%, rgba(12,12,12,0.15) 50%, rgba(12,12,12,0.7) 100%);"></div>

<!-- Typography: one-line editorial statement -->
<div style="position:absolute;left:24mm;right:24mm;bottom:38mm;">
  <div style="width:48px;height:3px;background:{LACRE};margin-bottom:10mm;"></div>
  <div style="font-family:{FAM};font-size:42px;font-weight:900;
    color:{PAPEL};line-height:1.05;letter-spacing:-1.5px;max-width:190mm;">
    Medir antes de imprimir<span style="color:{LACRE};">.</span>
  </div>
  <div style="font-family:{FAM};font-size:14px;font-weight:400;font-style:italic;
    color:rgba(244,240,235,0.72);margin-top:5mm;max-width:160mm;line-height:1.5;">
    El manual no es el acto creativo — es la precisión que hace que lo creativo pueda repetirse.
  </div>
</div>

<!-- Top-left page marker -->
<div style="position:absolute;left:24mm;top:22mm;">
  <div class="eyebrow" style="color:rgba(244,240,235,0.55);">XV · Servicio · 55</div>
</div>

{metastrip(55, "XV · Servicio", dark=True)}"""
    return page_shell(body, 55, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# XVI PORTFOLIO  (pp 56)
# ══════════════════════════════════════════════════════════════

def p56_portfolio():
    manuales = [
        ("Anfisbena",     "Profesional",  "43pp", "Moda · ropa",             "Marca de ropa contemporánea. Sistema documentado para identidad visual, voz editorial y papelería comercial.",  f"{ASSETS}/portfolio/logos/anfisbena.png",  "dark"),
        ("Claramel",      "Esencial",     "29pp", "IA personalizada",        "Asistente de IA personalizado. Identidad base, paleta, tipografía y aplicaciones para producto y web.",          f"{ASSETS}/portfolio/logos/claramel.png",   "light"),
        ("Matraz Innova", "Profesional",  "33pp", "Farmacéutica",            "Laboratorio farmacéutico. Sistema visual y verbal para comunicar ciencia a cliente profesional y consumidor final.", f"{ASSETS}/portfolio/logos/matraz.svg",     "dark"),
        ("Shamusic",      "Premium",      "46pp", "Music-tech",              "Plataforma music-tech. Manual Premium completo — estrategia, voz, aplicaciones y governance.",                  f"{ASSETS}/portfolio/logos/shamusic.png",   "dark"),
        ("Tramarca",      "Proprietary",  "58pp", "Meta · este manual",      "Nuestra propia marca aplicada a sí misma. El documento que estás leyendo.",                                       "",                                         "lacre"),
    ]
    cards = ""
    for name, tier, pages, sector, desc, thumb, bg_mode in manuales:
        accent = LACRE if name == "Tramarca" else NEGRO
        tile_bg = {"dark": NEGRO, "light": PAPEL, "lacre": LACRE}[bg_mode]
        tile_border = f"border:0.5px solid {CENIZA};" if bg_mode == "light" else ""
        if thumb:
            thumb_html = (
                f'<div style="width:30mm;height:20mm;background:{tile_bg};display:flex;align-items:center;'
                f'justify-content:center;flex-shrink:0;padding:3mm;{tile_border}">'
                f'<img src="{thumb}" style="max-width:100%;max-height:100%;object-fit:contain;" alt="{name} logo"></div>'
            )
        else:
            thumb_html = (
                f'<div style="width:30mm;height:20mm;background:{LACRE};display:flex;align-items:center;'
                f'justify-content:center;flex-shrink:0;padding:3mm;">'
                f'<span style="font-family:{FAM};font-size:13px;font-weight:900;color:{PAPEL};'
                f'letter-spacing:-0.3px;text-align:center;line-height:1;">'
                f'{name}<span style="color:{PAPEL};">.</span></span></div>'
            )
        cards += f"""\
<div style="padding:4mm 0;border-bottom:0.5px solid {CENIZA};display:grid;grid-template-columns:30mm 1fr;gap:6mm;align-items:center;">
  {thumb_html}
  <div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:1.5mm;">
      <div style="font-family:{FAM};font-size:16px;font-weight:900;color:{accent};">{name}<span style="color:{LACRE};">.</span></div>
      <div style="font-family:{MONO};font-size:7.5px;color:{PIEDRA};letter-spacing:1.5px;text-transform:uppercase;">{tier} · {pages}</div>
    </div>
    <div style="font-family:{MONO};font-size:7.5px;color:{LACRE};letter-spacing:1.2px;text-transform:uppercase;margin-bottom:1.5mm;">{sector}</div>
    <div style="font-family:{FAM};font-size:10.5px;color:{CARBON};line-height:1.45;">{desc}</div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">XVI · Portfolio · 56</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1.4fr;gap:16mm;">
  <div style="display:flex;flex-direction:column;justify-content:space-between;">
    <div>
      {titulo("Portfolio", 42)}
      <div class="body-text" style="margin-top:2mm;max-width:100mm;">
        Cinco manuales publicados. Cero mockups. Cero casos-hipotéticos.
        Si quieres verlos antes de creerte nada, están en tramarca.es/manuales.
      </div>
    </div>
    <div>
      <div style="font-family:{FAM};font-size:72px;font-weight:900;color:{NEGRO};
        line-height:1;letter-spacing:-3px;font-variant-numeric:tabular-nums;">
        05<span style="color:{LACRE};font-size:88px;">.</span>
      </div>
      <div class="meta" style="margin-top:2mm;">Manuales · 209 páginas · 5 sectores</div>
    </div>
  </div>
  <div>
    {cards}
    <div style="margin-top:6mm;font-family:{MONO};font-size:8px;color:{PIEDRA};
      letter-spacing:1.5px;text-transform:uppercase;">
      Datos verificables en tramarca.es/manuales
    </div>
  </div>
</div>

{metastrip(56, "XVI · Portfolio")}"""
    return page_shell(body, 56, bg=PAPEL, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# CIERRE  (pp 57-58) — TL;DR V9 + back cover
# ══════════════════════════════════════════════════════════════

def p57_tldr():
    """V9 TL;DR — the last content page. 10 rules max."""
    rules = [
        "Un estudio que solo hace manuales · no hacemos web, ni campañas, ni packaging.",
        "Precio cerrado · 490 / 990 / 1.990€ IVA incluido · publicado.",
        "Plazo publicado · 5 / 7 / 10 días laborables por tier.",
        "Brief firmado antes del kickoff · sin brief no empezamos.",
        "Entrega editorial · libro físico impreso (Premium), PDF y assets por tier.",
        "Dos rondas de revisión incluidas · proceso cerrado.",
        "Un manual = 16 capítulos / 48 componentes · anatomía publicada.",
        "Dos tipografías · Satoshi + IBM Plex Mono · sin cursivas.",
        "Siete colores + un acento · Lacre solo como punto, nunca fondo.",
        "El trabajo es revisar · lo que no se documenta, se improvisa.",
    ]
    rows = ""
    for i, r in enumerate(rules, 1):
        rows += f"""\
<div style="display:grid;grid-template-columns:14mm 1fr;gap:4mm;
  padding:3.6mm 0;border-bottom:0.5px solid {CENIZA};align-items:baseline;">
  <span style="font-family:{MONO};font-size:12px;font-weight:700;color:{LACRE};font-variant-numeric:tabular-nums;">{i:02d}</span>
  <span style="font-family:{FAM};font-size:13px;font-weight:500;color:{NEGRO};line-height:1.5;">{r}</span>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div class="eyebrow">Cierre · 57</div>
  {fidelity_badge("FIEL")}
</div>

<div style="position:absolute;left:24mm;right:24mm;top:34mm;bottom:22mm;
  display:grid;grid-template-columns:1fr 1.4fr;gap:18mm;">
  <div style="display:flex;flex-direction:column;justify-content:space-between;">
    <div>
      <div class="eyebrow" style="margin-bottom:4mm;">Resumen · 10 reglas</div>
      <div style="font-family:{FAM};font-size:72px;font-weight:900;
        color:{NEGRO};line-height:0.9;letter-spacing:-3px;">
        La marca<br>en 10 líneas<span style="color:{LACRE};">.</span>
      </div>
    </div>
    <div>
      <div class="pq" style="max-width:none;">
        Si no está aquí, probablemente no está en la marca<span class="p">.</span>
      </div>
      <div style="margin-top:6mm;font-family:{MONO};font-size:8px;color:{PIEDRA};letter-spacing:1.5px;text-transform:uppercase;">
        Derivado de las 58 páginas anteriores · sin contenido nuevo
      </div>
    </div>
  </div>
  <div style="align-self:start;">
    {rows}
  </div>
</div>

{metastrip(57, "17 · Cierre")}"""
    return page_shell(body, 57, bg=PAPEL, no_furniture=True)


def p58_back_cover():
    """Back cover — sober, contact-forward, punto final."""
    body = f"""\
<div class="noise-heavy" style="position:absolute;inset:0;"></div>

<!-- Ghost wordmark watermark centered -->
<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  font-family:{FAM};font-size:320px;font-weight:900;
  color:rgba(244,240,235,0.018);letter-spacing:-10px;
  pointer-events:none;user-select:none;white-space:nowrap;">{BRAND}</div>

<div style="position:absolute;left:24mm;top:22mm;right:24mm;display:flex;
  justify-content:space-between;align-items:baseline;">
  <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.45);letter-spacing:2px;text-transform:uppercase;">
    Contraportada
  </div>
  <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{PAPEL};">
    {BRAND}<span style="color:{LACRE};">.</span>
  </div>
</div>

<!-- Central quote -->
<div style="position:absolute;left:24mm;right:24mm;top:50%;transform:translateY(-50%);text-align:center;">
  <div style="font-family:{FAM};font-size:64px;font-weight:900;
    color:{PAPEL};line-height:1;letter-spacing:-2px;">
    Tu marca,<br>por escrito<span style="color:{LACRE};font-size:78px;">.</span>
  </div>
  <div style="width:60px;height:2px;background:{LACRE};margin:12mm auto 8mm auto;"></div>
  <div style="font-family:{FAM};font-size:14px;font-weight:400;font-style:italic;
    color:rgba(244,240,235,0.6);letter-spacing:0.5px;">
    Un estudio que solo hace manuales.
  </div>
</div>

<!-- Colofón editorial (ledger at bottom — cierra el manual) -->
<div style="position:absolute;left:24mm;right:24mm;bottom:18mm;">
  <div style="border-top:0.5px solid rgba(244,240,235,0.18);padding-top:5mm;
    display:grid;grid-template-columns:repeat(4,1fr);gap:6mm;align-items:start;">
    <div>
      <div style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.4);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:2mm;">Contacto</div>
      <div style="font-family:{MONO};font-size:8.5px;color:rgba(244,240,235,0.75);line-height:1.7;">
        hola@tramarca.es<br>
        tramarca.es<br>
        {CITY}
      </div>
    </div>
    <div>
      <div style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.4);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:2mm;">Edición</div>
      <div style="font-family:{MONO};font-size:8.5px;color:rgba(244,240,235,0.75);line-height:1.7;">
        {EDITION}<br>
        {TOTAL} páginas · 17 secciones<br>
        A4 apaisado · 297 × 210 mm
      </div>
    </div>
    <div>
      <div style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.4);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:2mm;">Sistema</div>
      <div style="font-family:{MONO};font-size:8.5px;color:rgba(244,240,235,0.75);line-height:1.7;">
        Satoshi · IBM Plex Mono<br>
        7 tokens + Lacre<br>
        PDF/X-1a · CMYK coated
      </div>
    </div>
    <div style="text-align:right;">
      <div style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.4);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:2mm;">Derechos</div>
      <div style="font-family:{MONO};font-size:8.5px;color:rgba(244,240,235,0.75);line-height:1.7;">
        © 2026 Tramarca<br>
        Todos los derechos reservados<br>
        Impreso en España
      </div>
    </div>
  </div>
</div>"""
    return page_shell(body, 58, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

PAGES = [
    p01_cover_v9,
    p02_mantra,
    p03_estado_sistema,
    p04_indice,
    p05_colofon,
    p06_provocacion,
    p07_the_problem,
    p08_nuestra_respuesta,
    p09_comparativa,
    p10_personas_divider,
    p11_persona_fundadora,
    p12_persona_consultora,
    p13_persona_estudio,
    p14_fundamentos,
    p15_proposito_vision,
    p16_valores,
    p17_personalidad,
    p18_posicionamiento,
    p19_logo_divider,
    p20_logo_primary,
    p21_logo_construccion,
    p22_logo_variantes,
    p23_logo_donts,
    p24_tipo_divider,
    p25_specimens,
    p26_tipo_jerarquia,
    p27_color_divider,
    p28_color_palette,
    p29_color_combos,
    p30_icono_divider,
    p31_icono_sistema,
    p32_foto_divider,
    p33_foto_direccion,
    p34_voz_divider,
    p35_voz_principios,
    p36_voz_vocabulario,
    p37_apps_divider,
    p38_apps_papeleria,
    p39_apps_email,
    p40_apps_digital,
    p41_apps_merch_senal,
    p42_arq_divider,
    p43_arq_sistema,
    p44_gov_divider,
    p45_gov_checklist,
    p46_gov_versioning,
    p47_motion_divider,
    p48_motion_sistema,
    p49_ext_divider,
    p50_ext_a11y_digital,
    p51_ext_territorial_legal,
    p52_servicio_divider,
    p53_tiers_real,
    p54_proceso,
    p55_garantia,
    p56_portfolio,
    p57_tldr,
    p58_back_cover,
]


def main():
    assert len(PAGES) == TOTAL, f"Page count mismatch: {len(PAGES)} functions vs TOTAL={TOTAL}"
    rendered = [p() for p in PAGES]
    html = html_wrap(rendered)
    OUT.write_text(html, encoding="utf-8")
    size_kb = OUT.stat().st_size / 1024
    print(f"HTML generated: {OUT} ({size_kb:.1f} KB · {TOTAL} pages)")


if __name__ == "__main__":
    main()

