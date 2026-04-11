"""
TRAMARCA. Brand Manual — v3 Final Build
========================================
34 pages, A4 landscape. Brutal visual direction.
CSS 100%, no external tools for mockups.
"""
from __future__ import annotations
from pathlib import Path
from toolkit import *

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
OUT  = DIST / "tramarca-v3.html"
PDF  = DIST / "tramarca-v3.pdf"


# ══════════════════════════════════════════════════════════════
# 00 APERTURA  (pp. 01-02)
# ══════════════════════════════════════════════════════════════

def p01_cover():
    """Cover — asymmetric wordmark, diagonal lacre slash, noise texture.
    Directly from approved proof v3."""
    body = f"""\
<div class="noise-heavy" style="position:absolute;inset:0;"></div>

<div style="position:absolute;inset:0;
  background:radial-gradient(ellipse at 30% 70%, transparent 30%, rgba(0,0,0,0.5) 100%);
  pointer-events:none;"></div>

{giant_letter("T", 900, "rgba(196,85,58,0.04)", "-60mm", "-80mm")}

<div style="position:absolute;left:-10%;top:55%;
  width:120%;height:4px;background:{LACRE};
  transform:rotate(-6deg);opacity:0.6;"></div>
<div style="position:absolute;left:-10%;top:57%;
  width:120%;height:1px;background:{LACRE};
  transform:rotate(-6deg);opacity:0.3;"></div>

<div style="position:absolute;left:24mm;bottom:38mm;">
  <div style="font-family:{FAM};font-size:160px;font-weight:900;
    color:{PAPEL};letter-spacing:-6px;line-height:0.85;">
    {BRAND}<span style="color:{LACRE};font-size:200px;position:relative;top:10px;">.</span>
  </div>
</div>

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

<div class="vertical-text" style="position:absolute;left:10mm;bottom:40mm;opacity:0.7;">
  Tu marca, sin improvisar
</div>

<div style="position:absolute;right:24mm;bottom:14mm;text-align:right;">
  <div style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.2);letter-spacing:1px;">
    {EDITION}
  </div>
</div>"""
    return page_shell(body, 1, bg=NEGRO, dark=True, no_furniture=True)


def p02_index_colophon():
    """Index + Colophon fused — split layout.
    Left: TOC. Right: colophon data + brand statement."""
    # TOC entries
    toc_entries = ""
    for s in SECTIONS[1:-1]:  # skip Apertura and Cierre
        r = s["r"]
        if not r:
            continue
        toc_entries += f"""\
<div style="display:flex;justify-content:space-between;align-items:baseline;
  padding:3mm 0;border-bottom:0.5px solid rgba(244,240,235,0.08);">
  <div style="display:flex;gap:3mm;align-items:baseline;">
    <span style="font-family:{MONO};font-size:9px;font-weight:700;color:{LACRE};
      display:inline-block;min-width:16mm;">{r}</span>
    <span style="font-family:{FAM};font-size:14px;font-weight:500;color:{PAPEL};">{s['title']}</span>
  </div>
  <span style="font-family:{MONO};font-size:8px;color:{PIEDRA};">{s['pages'][0]:02d}</span>
</div>"""

    left = f"""\
<div style="padding:28mm 20mm 24mm 24mm;height:100%;display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    <div class="eyebrow" style="color:{LACRE};margin-bottom:10mm;">Indice</div>
    <div style="font-family:{FAM};font-size:48px;font-weight:900;
      color:{PAPEL};letter-spacing:-2px;line-height:0.9;margin-bottom:12mm;">
      Contenido<span style="color:{LACRE};font-size:60px;">.</span>
    </div>
    {toc_entries}
  </div>
  <div style="width:40px;height:3px;background:{LACRE};"></div>
</div>"""

    right = f"""\
<div style="padding:28mm 24mm 24mm 20mm;height:100%;display:flex;flex-direction:column;justify-content:space-between;">
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
  <div>
    <div style="border-left:5px solid {LACRE};padding-left:20px;margin-bottom:10mm;">
      <div style="font-family:{FAM};font-size:22px;font-weight:900;
        color:{PAPEL};line-height:1.3;">
        Este documento define que es Tramarca, como se ve,
        como habla y como se aplica<span style="color:{LACRE};font-size:28px;">.</span>
      </div>
    </div>
    <div style="font-family:{FAM};font-size:13px;font-weight:400;
      color:{CENIZA};line-height:1.7;">
      Cada decision esta por escrito. Cada regla tiene una razon.
      Si no podemos explicar por que, lo quitamos.
    </div>
  </div>
</div>"""

    # Lacre vertical separator bar between panels
    body = f"""\
<div style="position:absolute;inset:0;display:grid;grid-template-columns:50% 50%;">
  <div style="background:{NEGRO};position:relative;overflow:hidden;">{left}</div>
  <div style="background:{CARBON};position:relative;overflow:hidden;">
    <div style="position:absolute;left:0;top:10%;bottom:10%;width:3px;background:{LACRE};opacity:0.5;"></div>
    {right}
  </div>
</div>"""
    return page_shell(body, 2, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# I  PROVOCACION  (pp. 03-04)
# ══════════════════════════════════════════════════════════════

def p03_provocacion():
    """Section divider — Provocacion. Cinematic, brutal."""
    return divider("01", "I", "Provocacion",
                   "Por que este manual existe", pg=3)


def p04_the_problem():
    """The problem — dramatic split, photo bleeds into text.
    From approved proof v3."""
    left = f"""\
<img src="assets/img-03.jpg" style="width:100%;height:100%;object-fit:cover;
  filter:grayscale(25%) contrast(1.15);" alt="">
<div style="position:absolute;inset:0;
  background:linear-gradient(90deg, transparent 40%, {NEGRO} 95%);"></div>
<div style="position:absolute;left:0;top:0;bottom:0;width:4px;background:{LACRE};"></div>"""

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
    Tu marca no existe<span style="color:{LACRE};font-size:28px;">.</span><br>
    Existe en tu cabeza<span style="color:{LACRE};font-size:28px;">.</span><br>
    Pero eso no cuenta<span style="color:{LACRE};font-size:28px;">.</span>
  </div>
</div>"""

    body = split_page(left, right, left_bg=NEGRO, right_bg=NEGRO, ratio="45% 55%")

    # Floating furniture
    body += f"""\
<div style="position:absolute;right:24mm;top:18mm;z-index:2;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.3);letter-spacing:2px;text-transform:uppercase;">
    I · Provocacion
  </span>
</div>
<div style="position:absolute;left:24mm;bottom:14mm;z-index:2;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.15);letter-spacing:1px;">
    {BRAND}<span style="color:{LACRE};">.</span> · Manual de marca
  </span>
</div>
<div style="position:absolute;right:24mm;bottom:14mm;z-index:2;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.15);letter-spacing:1px;">
    04 / {TOTAL}
  </span>
</div>"""
    return page_shell(body, 4, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# II FUNDAMENTOS  (pp. 05-08)
# ══════════════════════════════════════════════════════════════

def p05_fundamentos():
    """Section divider — Fundamentos."""
    return divider("02", "II", "Fundamentos",
                   "Quien somos. Que hacemos. Para quien", pg=5)


def p06_vision_values():
    """Vision + Mission + Values fused — split dark/light."""
    left = f"""\
<div style="padding:28mm 16mm 24mm 24mm;height:100%;display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    <div class="eyebrow" style="color:{LACRE};margin-bottom:6mm;">Vision</div>
    <div style="font-family:{FAM};font-size:28px;font-weight:900;
      color:{PAPEL};line-height:1.2;margin-bottom:12mm;">
      Que cada marca profesional tenga su sistema por escrito<span style="color:{LACRE};font-size:34px;">.</span>
    </div>
    <div class="eyebrow" style="color:{LACRE};margin-bottom:6mm;">Mision</div>
    <div style="font-family:{FAM};font-size:20px;font-weight:700;
      color:{PAPEL};line-height:1.3;margin-bottom:6mm;">
      Producimos sistemas de marca completos<span style="color:{LACRE};font-size:24px;">.</span>
    </div>
    <div style="font-family:{FAM};font-size:13px;font-weight:400;
      color:{CENIZA};line-height:1.7;">
      Identidad visual, voz, personalidad, assets y reglas de uso.
      Un documento. Cada decision. Por escrito.
    </div>
  </div>
  <!-- Stationery image — what we produce -->
  <div style="height:38mm;overflow:hidden;margin-bottom:4mm;">
    <img src="assets/branded/stationery-flatlay.jpg" alt="" style="width:100%;height:100%;object-fit:cover;
      filter:brightness(0.85);opacity:0.9;">
  </div>
  <div>
    {accent_rule(60, "0")}
    <div style="font-family:{MONO};font-size:9px;color:{PIEDRA};margin-top:3mm;line-height:2;">
      Fundado 2026 · Espana · Remoto
    </div>
  </div>
</div>"""

    vals = [
        ("01", "Claridad", "Cada decision tiene una razon. Si no la tiene, sobra."),
        ("02", "Honestidad", "Si tu marca tiene un problema, lo senalamos."),
        ("03", "Rigor", "No hay paginas de relleno. Todo tiene peso."),
    ]

    vals_html = ""
    for num, name, desc in vals:
        vals_html += f"""\
<div style="border-top:3px solid {LACRE};padding-top:6mm;margin-bottom:6mm;">
  <div style="font-family:{MONO};font-size:10px;font-weight:700;
    color:{LACRE};margin-bottom:3mm;">{num}</div>
  <div style="font-family:{FAM};font-size:20px;font-weight:900;
    color:{NEGRO};margin-bottom:4mm;">{name}<span style="color:{LACRE};font-size:24px;">.</span></div>
  <div class="body-text" style="font-size:12px;">{desc}</div>
</div>"""

    right = f"""\
<div style="padding:28mm 24mm 24mm 20mm;height:100%;display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    <div class="eyebrow" style="margin-bottom:8mm;">Valores</div>
    {vals_html}
  </div>
  <div style="background:{ARENA};padding:14px 18px;">
    <div style="font-family:{FAM};font-size:14px;font-weight:700;
      color:{NEGRO};line-height:1.4;">
      Cada decision<span style="color:{LACRE};">.</span> Por escrito<span style="color:{LACRE};">.</span>
    </div>
  </div>
</div>"""

    body = split_page(left, right, left_bg=NEGRO, right_bg=PAPEL, ratio="45% 55%")
    return page_shell(body, 6, bg=NEGRO, dark=True, no_furniture=True)


def p07_positioning():
    """Positioning — what we are / what we are not + scatter plot + image."""
    body = f"""\
<div style="position:absolute;left:24mm;top:28mm;right:24mm;bottom:18mm;
  display:grid;grid-template-columns:1.2fr 1fr;gap:14mm;">
  <div>
    {titulo("Posicionamiento", 38)}
    <div class="body-text" style="margin-bottom:8mm;">
      Tramarca produce sistemas de marca completos — no logos sueltos,
      no slides de branding, no PDFs de tres paginas. Un documento que
      cubre identidad visual, voz, personalidad, assets y reglas de uso.
    </div>
    <div style="margin-bottom:6mm;">
      <div class="eyebrow" style="margin-bottom:4mm;">Lo que no somos</div>
      <div style="font-family:{FAM};font-size:15px;font-weight:500;color:{PIEDRA};line-height:2;">
        <span class="struck" style="font-size:15px;">Una agencia creativa</span><br>
        <span class="struck" style="font-size:15px;">Un freelance que hace logos</span><br>
        <span class="struck" style="font-size:15px;">Un estudio de diseno generalista</span>
      </div>
    </div>
    {pull_quote("No somos una agencia. No somos un freelance. Somos un sistema", "300px")}
    <!-- Laptop — digital presence -->
    <div style="height:30mm;overflow:hidden;margin-top:4mm;">
      <img src="assets/branded/laptop-dark.jpg" alt="" style="width:100%;height:100%;object-fit:cover;
        filter:brightness(0.8);">
    </div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <div style="position:relative;width:100%;aspect-ratio:1/1;
      border-left:1px solid {CENIZA};border-bottom:1px solid {CENIZA};">
      <div style="position:absolute;bottom:-8mm;left:50%;transform:translateX(-50%);
        font-family:{MONO};font-size:7px;color:{PIEDRA};letter-spacing:1px;text-transform:uppercase;">
        Sistema completo →
      </div>
      <div style="position:absolute;left:-2mm;top:50%;transform:rotate(-90deg) translateX(-50%);transform-origin:0 0;
        font-family:{MONO};font-size:7px;color:{PIEDRA};letter-spacing:1px;text-transform:uppercase;">
        A medida →
      </div>
      <div style="position:absolute;left:15%;bottom:20%;width:8px;height:8px;border-radius:50%;background:{CENIZA};"></div>
      <div style="position:absolute;left:20%;bottom:55%;width:8px;height:8px;border-radius:50%;background:{CENIZA};"></div>
      <div style="position:absolute;left:60%;bottom:70%;width:8px;height:8px;border-radius:50%;background:{CENIZA};"></div>
      <div style="position:absolute;left:70%;bottom:40%;width:8px;height:8px;border-radius:50%;background:{CENIZA};"></div>
      <div style="position:absolute;left:82%;bottom:85%;width:14px;height:14px;border-radius:50%;
        background:{LACRE};box-shadow:0 0 0 4px rgba(196,85,58,0.25);"></div>
      <div style="position:absolute;left:15%;bottom:12%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Fiverr</div>
      <div style="position:absolute;left:20%;bottom:47%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Freelance</div>
      <div style="position:absolute;left:48%;bottom:72%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Estudio boutique</div>
      <div style="position:absolute;left:58%;bottom:32%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Agencia grande</div>
      <div style="position:absolute;left:72%;bottom:88%;font-family:{FAM};font-size:9px;font-weight:700;color:{LACRE};">{BRAND}.</div>
    </div>
  </div>
</div>"""
    return page_shell(body, 7, section="II · Fundamentos", bg=PAPEL)


def p08_audience_personality():
    """Audience + Personality fused into one page."""
    adjs = [
        ("Directo", "Sin rodeos, sin matices innecesarios."),
        ("Provocador", "Cuestiona lo que el mercado da por sentado."),
        ("Seguro", "No pide permiso. No se disculpa."),
        ("Preciso", "Cada palabra elegida. Nada sobra."),
        ("Cercano", 'Usa "tu". Habla de igual a igual.'),
    ]

    personality_items = ""
    for i, (adj, desc) in enumerate(adjs, 1):
        personality_items += f"""\
<div style="display:flex;gap:3mm;align-items:baseline;">
  <span style="font-family:{MONO};font-size:9px;font-weight:700;color:{LACRE};">{i:02d}</span>
  <span style="font-family:{FAM};font-size:13px;font-weight:700;color:{NEGRO};">{adj}<span style="color:{LACRE};">.</span></span>
  <span style="font-family:{FAM};font-size:11px;color:{PIEDRA};">{desc}</span>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:28mm;right:24mm;bottom:18mm;
  display:grid;grid-template-columns:1fr 1fr;gap:14mm;align-content:start;">
  <div style="display:flex;flex-direction:column;gap:4mm;">
    {titulo("Audiencia", 36)}
    <div class="eyebrow" style="margin-bottom:2mm;">Perfil principal</div>
    <div style="font-family:{FAM};font-size:16px;font-weight:700;
      color:{NEGRO};line-height:1.4;margin-bottom:4mm;">
      Fundadores y directores de empresas pequenas y medianas
      que saben que necesitan orden en su marca<span style="color:{LACRE};font-size:20px;">.</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:3mm;margin-bottom:4mm;">
      <div style="border-left:3px solid {LACRE};padding-left:10px;">
        <div class="body-text" style="font-size:11px;">"Tenemos logo pero cada vez que alguien lo usa sale distinto."</div>
      </div>
      <div style="border-left:3px solid {LACRE};padding-left:10px;">
        <div class="body-text" style="font-size:11px;">"Queremos parecer profesionales, no improvisados."</div>
      </div>
    </div>
    {data_block([
        ("Sector", "Multisector — servicios, hosteleria, tech"),
        ("Tamano", "1–50 empleados"),
        ("Decisor", "CEO / Fundador"),
    ])}
    <!-- Our workspace — branded -->
    <div style="height:34mm;overflow:hidden;margin-top:2mm;">
      <img src="assets/branded/workspace-overhead.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">
    </div>
  </div>
  <div>
    {titulo("Personalidad", 36)}
    <div style="display:flex;flex-direction:column;gap:5mm;margin-bottom:8mm;">
      {personality_items}
    </div>
    <div style="background:{ARENA};padding:16px 20px;">
      <div class="eyebrow" style="margin-bottom:4mm;">Regla de oro</div>
      <div style="font-family:{FAM};font-size:16px;font-weight:700;
        color:{NEGRO};line-height:1.35;">
        Tramarca no convence<span style="color:{LACRE};font-size:20px;">.</span>
        Senala lo que ya sabes
        pero no quieres admitir<span style="color:{LACRE};font-size:20px;">.</span>
      </div>
    </div>
  </div>
</div>"""
    return page_shell(body, 8, section="II · Fundamentos", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# III SERVICIO  (pp. 09-11)
# ══════════════════════════════════════════════════════════════

def p09_servicio():
    """Section divider — Servicio."""
    return divider("03", "III", "Servicio",
                   "Que entregamos. Como trabajamos.", pg=9)


def p10_included_process():
    """What's included + Process fused into one page — split layout."""
    items = [
        ("Identidad visual", "Logotipo, paleta, tipografia, reglas de uso."),
        ("Voz y personalidad", "Tono, vocabulario, ejemplos reales."),
        ("Assets listos", "Archivos en todos los formatos. Plantillas."),
        ("Reglas de uso", "Combinaciones permitidas y prohibidas."),
    ]

    items_html = ""
    for i, (cat, desc) in enumerate(items):
        items_html += f"""\
<div style="border-top:2px solid {LACRE if i == 0 else CENIZA};padding-top:4mm;margin-bottom:4mm;">
  <div class="eyebrow" style="margin-bottom:2mm;">{cat}</div>
  <div class="body-text" style="font-size:11px;">{desc}</div>
</div>"""

    steps = [
        ("01", "Brief", "1–2 dias", "Conversacion inicial. Entendemos donde esta tu marca."),
        ("02", "Produccion", "10–15 dias", "Construimos el sistema completo."),
        ("03", "Revision", "3–5 dias", "Presentamos. Dos rondas incluidas."),
        ("04", "Entrega", "Dia final", "PDF + assets. Listo para usar."),
    ]

    timeline = ""
    for i, (num, name, timing, desc) in enumerate(steps):
        timeline += f"""\
<div style="display:grid;grid-template-columns:28px 1fr;gap:4mm;{'margin-top:4mm;' if i > 0 else ''}">
  <div style="display:flex;flex-direction:column;align-items:center;">
    <div style="width:24px;height:24px;border-radius:50%;background:{LACRE};
      display:flex;align-items:center;justify-content:center;flex-shrink:0;">
      <span style="font-family:{MONO};font-size:9px;font-weight:700;color:{PAPEL};">{num}</span>
    </div>
    {'<div style="flex:1;width:1px;background:%s;margin-top:2mm;"></div>' % CENIZA if i < 3 else ''}
  </div>
  <div>
    <div style="display:flex;align-items:baseline;gap:3mm;margin-bottom:1mm;">
      <span style="font-family:{FAM};font-size:14px;font-weight:900;color:{NEGRO};">{name}<span style="color:{LACRE};">.</span></span>
      <span class="meta">{timing}</span>
    </div>
    <div class="body-text" style="font-size:11px;">{desc}</div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;">
  <div>
    {titulo("Que incluye", 34)}
    {items_html}
    <div style="margin-top:4mm;">
      {pull_quote("Todo en un documento. Pagina a pagina", "100%")}
    </div>
  </div>
  <div style="display:flex;flex-direction:column;">
    {titulo("Proceso", 34)}
    {timeline}
    <div style="margin-top:4mm;background:{ARENA};padding:14px 18px;">
      <div class="eyebrow" style="margin-bottom:3mm;">Sin sorpresas</div>
      <div style="font-family:{FAM};font-size:14px;font-weight:700;
        color:{NEGRO};line-height:1.35;">
        Sabes que recibes, cuando lo recibes
        y cuanto cuesta<span style="color:{LACRE};font-size:18px;">.</span>
      </div>
    </div>
    <!-- The deliverable — open manual -->
    <div style="height:30mm;overflow:hidden;margin-top:4mm;">
      <img src="assets/branded/manual-open.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">
    </div>
  </div>
</div>"""
    return page_shell(body, 10, section="III · Servicio", bg=PAPEL)


def p11_tiers():
    """Scope tiers — 3 columns on dark background for drama."""
    tiers = [
        ("Esencial", "25–30 pp",
         ["Logotipo + variaciones", "Paleta de color", "Tipografia",
          "Reglas de uso basicas", "Assets estandar"],
         False),
        ("Profesional", "35–45 pp",
         ["Todo lo de Esencial +", "Voz y personalidad", "Vocabulario de marca",
          "Aplicaciones principales", "Plantillas editables"],
         True),
        ("Premium", "50+ pp",
         ["Todo lo de Profesional +", "Direccion de arte", "Portfolio de aplicaciones",
          "Mockups y contextos de uso", "Iconografia personalizada"],
         False),
    ]

    cols = ""
    for name, pages, features, highlight in tiers:
        bg = LACRE if highlight else "rgba(244,240,235,0.06)"
        tc = PAPEL
        border = f"border-top:4px solid {PAPEL};" if highlight else f"border-top:2px solid rgba(244,240,235,0.15);"
        feat_html = "".join(
            f'<div style="font-family:{MONO};font-size:11px;color:{CENIZA};'
            f'padding:5px 0;border-bottom:0.5px solid rgba(244,240,235,0.1);">{f}</div>'
            for f in features
        )
        cols += f"""\
<div style="background:{bg};color:{tc};padding:24px 26px;{border}display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    <div style="font-family:{FAM};font-size:32px;font-weight:900;
      margin-bottom:3mm;">{name}<span style="color:{PAPEL if highlight else LACRE};">.</span></div>
    <div style="font-family:{MONO};font-size:11px;color:{CENIZA};margin-bottom:6mm;letter-spacing:1px;">{pages}</div>
    <div style="margin-bottom:5mm;">{feat_html}</div>
  </div>
  {'<div style="font-family:'+FAM+';font-size:11px;font-weight:700;color:'+PAPEL+';margin-top:4mm;opacity:0.7;">Recomendado</div>' if highlight else ''}
</div>"""

    body = f"""\
<div class="noise" style="position:absolute;inset:0;"></div>
<div style="position:absolute;left:24mm;top:28mm;right:24mm;bottom:18mm;
  display:flex;flex-direction:column;gap:6mm;">
  <div style="display:flex;justify-content:space-between;align-items:baseline;">
    <div style="font-family:{FAM};font-size:42px;font-weight:900;
      color:{PAPEL};letter-spacing:-2px;">Alcance<span style="color:{LACRE};font-size:52px;">.</span></div>
    <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};letter-spacing:2px;text-transform:uppercase;">
      III · Servicio
    </div>
  </div>
  <div class="g3" style="flex:1;">
    {cols}
  </div>
  <div style="display:flex;justify-content:space-between;align-items:baseline;">
    <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};">
      Precios personalizados por proyecto.
    </div>
    <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};">
      2 rondas de revision + 30 dias de soporte incluidos.
    </div>
  </div>
</div>"""
    return page_shell(body, 11, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# IV IDENTIDAD VISUAL  (pp. 12-16)
# ══════════════════════════════════════════════════════════════

def p12_identidad():
    """Section divider — Identidad Visual."""
    return divider("04", "IV", "Identidad\nvisual",
                   "Logo, construccion, versiones, usos.", pg=12)


def p13_logo_primary():
    """Logo — the shrine. From approved proof v3."""
    body = f"""\
<div class="noise" style="position:absolute;inset:0;"></div>

<div style="position:absolute;inset:0;
  background:radial-gradient(ellipse at 50% 45%,
    rgba(196,85,58,0.06) 0%, transparent 60%);
  pointer-events:none;"></div>

<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-52%);
  font-family:{FAM};font-size:400px;font-weight:900;
  color:rgba(244,240,235,0.025);letter-spacing:-12px;
  pointer-events:none;user-select:none;white-space:nowrap;">{BRAND}</div>

<div style="position:absolute;left:50%;top:46%;transform:translate(-50%,-50%);text-align:center;">
  <div style="font-family:{FAM};font-size:96px;font-weight:900;
    color:{PAPEL};letter-spacing:-3px;line-height:1;position:relative;">
    {BRAND}<span style="color:{LACRE};font-size:120px;position:relative;top:6px;">.</span>
  </div>
</div>

<div style="position:absolute;left:0;right:0;top:62%;height:0.5px;
  background:linear-gradient(90deg, transparent 0%, rgba(244,240,235,0.08) 20%, rgba(244,240,235,0.08) 80%, transparent 100%);"></div>

<div class="vertical-text" style="position:absolute;left:14mm;top:50%;transform:translateY(-50%);">El punto final</div>

<div style="position:absolute;left:24mm;bottom:18mm;">
  <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.35);line-height:2.4;letter-spacing:0.5px;">
    <span style="color:{PIEDRA};">TIPOGRAFIA</span> Satoshi Black 900<br>
    <span style="color:{PIEDRA};">CONCEPTO</span> El Punto Final<br>
    <span style="color:{PIEDRA};">PUNTO</span> 125% cap-height · Lacre {LACRE}
  </div>
</div>

<div style="position:absolute;right:24mm;top:18mm;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.25);letter-spacing:2px;text-transform:uppercase;">
    IV · Identidad visual
  </span>
</div>
<div style="position:absolute;right:24mm;bottom:18mm;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.2);letter-spacing:1px;">
    13 / {TOTAL}
  </span>
</div>"""
    return page_shell(body, 13, bg=NEGRO, dark=True, no_furniture=True)


def p14_construction_clearspace():
    """Logo construction + clear space + minimum sizes — combined."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.3fr 1fr;gap:16mm;align-content:start;">
  <div>
    {titulo("Construccion", 36)}
    <div style="position:relative;width:100%;height:80mm;margin-top:4mm;
      background:
        repeating-linear-gradient(0deg, transparent, transparent 9.5mm, rgba(181,177,172,0.15) 9.5mm, rgba(181,177,172,0.15) 10mm),
        repeating-linear-gradient(90deg, transparent, transparent 9.5mm, rgba(181,177,172,0.15) 9.5mm, rgba(181,177,172,0.15) 10mm);
      border:0.5px solid {CENIZA};">
      <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">
        <div style="position:relative;">
          <div style="font-family:{FAM};font-size:48px;font-weight:900;
            color:{NEGRO};letter-spacing:-1px;">
            {BRAND}<span style="color:{LACRE};font-size:58px;">.</span>
          </div>
          <div style="position:absolute;top:4px;left:-16mm;right:-16mm;
            border-top:0.5px dashed {LACRE};opacity:0.5;"></div>
          <div style="position:absolute;bottom:6px;left:-16mm;right:-16mm;
            border-top:0.5px dashed {LACRE};opacity:0.5;"></div>
          <div style="position:absolute;top:-6mm;left:-6mm;right:-6mm;bottom:-6mm;
            border:0.5px dashed {CENIZA};"></div>
          <div style="position:absolute;top:-6mm;right:-6mm;
            font-family:{MONO};font-size:7px;color:{PIEDRA};transform:translate(50%,-100%);">X</div>
        </div>
      </div>
    </div>
    <div class="g3" style="margin-top:4mm;">
      <div>
        <div class="eyebrow" style="margin-bottom:2mm;">Area de respeto</div>
        <div class="meta">X = ancho del punto. Nada invade esta zona.</div>
      </div>
      <div>
        <div class="eyebrow" style="margin-bottom:2mm;">El punto final</div>
        <div class="meta">120% cap-height. Elemento identitario central.</div>
      </div>
      <div>
        <div class="eyebrow" style="margin-bottom:2mm;">Tracking</div>
        <div class="meta">-2px en display, -1px en cuerpo. Nunca positivo.</div>
      </div>
    </div>
  </div>
  <div>
    <div class="eyebrow" style="margin-bottom:8mm;">Tamanos minimos</div>
    <div style="margin-bottom:8mm;padding-bottom:8mm;border-bottom:0.5px solid {CENIZA};">
      <div style="font-family:{FAM};font-size:24px;font-weight:900;color:{NEGRO};margin-bottom:2mm;">
        {BRAND}<span style="color:{LACRE};font-size:29px;">.</span>
      </div>
      <div class="meta">Digital: min 80px · Impreso: min 25mm <span style="color:{LACRE};">OK</span></div>
    </div>
    <div style="margin-bottom:8mm;padding-bottom:8mm;border-bottom:0.5px solid {CENIZA};">
      <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{CENIZA};margin-bottom:2mm;">
        {BRAND}<span style="color:{CENIZA};">.</span>
      </div>
      <div class="meta">Por debajo de 60px / 18mm: usar monograma</div>
    </div>
    <div style="margin-bottom:6mm;">
      <div style="font-family:{FAM};font-size:22px;font-weight:900;color:{NEGRO};margin-bottom:2mm;">
        Tm<span style="color:{LACRE};font-size:26px;">.</span>
      </div>
      <div class="meta">Monograma para avatares, favicons, tamanos reducidos</div>
    </div>
    {accent_rule(60, "6mm")}
    <div class="meta" style="margin-top:4mm;">
      El punto siempre en Lacre, independientemente del tamano.
    </div>
    <div style="margin-top:10mm;">
      <div class="eyebrow" style="margin-bottom:3mm;">Favicon</div>
      <div style="width:16mm;height:16mm;border-radius:50%;background:{LACRE};
        display:flex;align-items:center;justify-content:center;">
        <span style="font-family:{FAM};font-size:10px;font-weight:900;color:{PAPEL};">Tm.</span>
      </div>
    </div>
  </div>
</div>"""
    return page_shell(body, 14, section="IV · Identidad visual", bg=PAPEL)


def p15_logo_versions():
    """Logo versions — dark/light + monochrome in 2x2 grid on dark bg."""
    versions = [
        ("Positivo", PAPEL, NEGRO, LACRE),
        ("Negativo", NEGRO, PAPEL, LACRE),
        ("Monocromo", PAPEL, NEGRO, NEGRO),
        ("Monocromo inv.", NEGRO, PAPEL, PAPEL),
    ]

    grid = ""
    for label, bg, text, dot in versions:
        border = f"border:1px solid {CENIZA};" if bg == PAPEL else ""
        grid += f"""\
<div>
  <div style="background:{bg};{border}height:48mm;
    display:flex;align-items:center;justify-content:center;">
    <div style="font-family:{FAM};font-size:28px;font-weight:900;color:{text};">
      {BRAND}<span style="color:{dot};font-size:34px;">.</span>
    </div>
  </div>
  <div class="eyebrow" style="margin-top:3mm;">{label}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:18mm;
  display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    {titulo("Versiones", 38)}
    <div class="g2" style="margin-top:4mm;gap:6mm;">
      {grid}
    </div>
  </div>
  <div>
    {data_block([
        ("Preferencia", "Positivo con punto Lacre (uso principal)"),
        ("Monocromo", "Solo cuando la impresion a color no es posible"),
        ("Regla", "El punto en Lacre siempre que sea tecnicamente posible"),
    ])}
  </div>
</div>"""
    return page_shell(body, 15, section="IV · Identidad visual", bg=PAPEL)


def p16_logo_forbidden():
    """Forbidden uses — 6 violations grid."""
    violations = [
        ("No rotar", "transform:rotate(15deg);", LACRE),
        ("No cambiar color del punto", "", "#3366CC"),
        ("No usar sombras", "filter:drop-shadow(3px 3px 4px rgba(0,0,0,0.4));", LACRE),
        ("No deformar", "transform:scaleX(1.4);", LACRE),
        ("No sobre fondos complejos", "", LACRE),
        ("No eliminar el punto", "", None),
    ]

    grid = ""
    for i, (caption, style, dot_color) in enumerate(violations):
        if i == 4:
            bg_css = f"background:repeating-linear-gradient(45deg,{ARENA},{ARENA} 4px,{CENIZA} 4px,{CENIZA} 8px);"
        else:
            bg_css = f"background:{PAPEL};border:1px solid {CENIZA};"

        mark = "TRAMARCA" if dot_color is None else f'{BRAND}<span style="color:{dot_color};font-size:22px;">.</span>'

        grid += f"""\
<div>
  <div style="{bg_css}height:46mm;display:flex;align-items:center;justify-content:center;position:relative;">
    <div style="font-family:{FAM};font-size:18px;font-weight:900;color:{NEGRO};{style}">
      {mark}
    </div>
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
      font-family:{FAM};font-size:44px;font-weight:900;color:rgba(196,85,58,0.25);">X</div>
  </div>
  <div class="meta" style="margin-top:2mm;">{caption}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    {titulo("Usos incorrectos", 38)}
    <div class="g3" style="margin-top:4mm;row-gap:5mm;">
      {grid}
    </div>
  </div>
  <div style="border-left:3px solid {LACRE};padding-left:12px;">
    <div style="font-family:{FAM};font-size:13px;font-weight:500;color:{NEGRO};line-height:1.6;">
      Si no esta en esta pagina, pregunta antes de usarlo.<br>
      La consistencia no es negociable.
    </div>
  </div>
</div>"""
    return page_shell(body, 16, section="IV · Identidad visual", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# V  COLOR  (pp. 17-18)
# ══════════════════════════════════════════════════════════════

def p17_color_palette():
    """Color palette — split: title left, stripes right. From proof v3."""
    colors = [
        (NEGRO,  "Negro",  PAPEL,  "#0C0C0C"),
        (CARBON, "Carbon", PAPEL,  "#1C1C1C"),
        (LACRE,  "Lacre",  PAPEL,  "#C4553A"),
        (PIEDRA, "Piedra", PAPEL,  "#7A7672"),
        (CENIZA, "Ceniza", NEGRO,  "#B5B1AC"),
        (ARENA,  "Arena",  NEGRO,  "#E4E2DC"),
        (PAPEL,  "Papel",  NEGRO,  "#F4F0EB"),
    ]

    stripes = ""
    for bg, name, tc, hex_val in colors:
        stripes += f"""\
<div style="flex:1;background:{bg};display:flex;flex-direction:column;
  justify-content:flex-end;padding:8mm 3mm;">
  <div style="font-family:{FAM};font-size:13px;font-weight:900;color:{tc};
    margin-bottom:2mm;">{name}</div>
  <div style="font-family:{MONO};font-size:7px;letter-spacing:1px;color:{tc};opacity:0.6;">
    {hex_val}</div>
</div>"""

    left = f"""\
<div style="width:35%;background:{NEGRO};display:flex;flex-direction:column;
  justify-content:space-between;padding:24mm 24mm 20mm 24mm;flex-shrink:0;">
  <div>
    <div style="font-family:{MONO};font-size:8px;font-weight:700;letter-spacing:3px;
      text-transform:uppercase;color:{LACRE};margin-bottom:12mm;">V · Color</div>
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
</div>"""
    return page_shell(body, 17, bg=NEGRO, dark=True, no_furniture=True)


def p18_color_combos_donts():
    """Color combos + don'ts on one page — split layout."""
    combos = [
        ("Principal oscuro",    NEGRO, PAPEL,  LACRE, "15.4:1"),
        ("Principal claro",     PAPEL, NEGRO,  LACRE, "15.4:1"),
        ("Acento sobre oscuro", NEGRO, LACRE,  None,  "4.6:1"),
        ("Secundario calido",   ARENA, CARBON, None,  "10.7:1"),
    ]

    combo_grid = ""
    for label, bg, fg, accent, ratio in combos:
        border = f"border:1px solid {CENIZA};" if bg in [PAPEL, ARENA] else ""
        dot = f'<span style="color:{accent};">.</span>' if accent else ""
        combo_grid += f"""\
<div>
  <div style="background:{bg};{border}height:26mm;
    display:flex;align-items:center;justify-content:center;">
    <span style="font-family:{FAM};font-size:14px;font-weight:700;color:{fg};">Aa{dot}</span>
  </div>
  <div style="display:flex;justify-content:space-between;margin-top:1mm;">
    <span style="font-family:{FAM};font-size:9px;color:{NEGRO};">{label}</span>
    <span class="meta">{ratio}</span>
  </div>
</div>"""

    donts = [
        ("Lacre como fondo", f"background:{LACRE};", f"color:{PAPEL};"),
        ("Degradados", f"background:linear-gradient(135deg,{NEGRO},{LACRE});", f"color:{PAPEL};"),
        ("Multiples acentos", f"background:{PAPEL};border:1px solid {CENIZA};", f"color:{NEGRO};"),
    ]

    dont_grid = ""
    for title, bg_css, fg_css in donts:
        inner = f'{BRAND}<span style="color:{LACRE};font-size:16px;">.</span>'
        if "Multiples" in title:
            inner = f'{BRAND}<span style="color:#2E6DB4;">.</span><span style="color:#4CAF50;">*</span>'
        dont_grid += f"""\
<div>
  <div style="{bg_css}{fg_css}height:26mm;display:flex;align-items:center;justify-content:center;position:relative;">
    <span style="font-family:{FAM};font-size:13px;font-weight:900;">{inner}</span>
    <div style="position:absolute;top:2mm;right:3mm;font-family:{FAM};font-size:18px;font-weight:900;color:{LACRE};opacity:0.8;">X</div>
  </div>
  <div class="meta" style="margin-top:1mm;">{title}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;">
  <div>
    {titulo("Combinaciones", 34)}
    <div class="body-text" style="font-size:11px;margin-bottom:4mm;">
      Todas superan WCAG AA (4.5:1) para texto normal.
    </div>
    <div class="g2" style="row-gap:4mm;">
      {combo_grid}
    </div>
  </div>
  <div>
    {titulo("Usos incorrectos", 34)}
    <div class="g3" style="margin-top:4mm;">
      {dont_grid}
    </div>
    <div style="margin-top:6mm;">
      {data_block([
          ("Regla", "Lacre es acento, nunca fondo"),
          ("Contraste", "Min WCAG AA (4.5:1)"),
          ("Degradados", "Prohibidos. Colores planos."),
      ])}
    </div>
  </div>
</div>"""
    return page_shell(body, 18, section="V · Color", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# VI TIPOGRAFIA  (pp. 19-21)
# ══════════════════════════════════════════════════════════════

def p19_tipografia():
    """Section divider — Tipografia."""
    return divider("06", "VI", "Tipografia",
                   "Dos familias. Roles claros.", pg=19)


def p20_specimens():
    """Type specimens — Satoshi + Plex Mono together on one page."""
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
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.4fr 1fr;gap:16mm;">
  <div>
    <div style="font-family:{FAM};font-size:56px;font-weight:900;
      color:{NEGRO};line-height:1;margin-bottom:6mm;">Satoshi</div>
    <div style="font-family:{FAM};font-size:16px;font-weight:400;
      color:{CARBON};letter-spacing:2px;line-height:1.6;margin-bottom:6mm;">
      A B C D E F G H I J K L M N O P Q R S T U V W X Y Z<br>
      a b c d e f g h i j k l m n o p q r s t u v w x y z<br>
      0 1 2 3 4 5 6 7 8 9
    </div>
    {ramp}
    {accent_rule(60, "6mm")}
    <div style="font-family:{MONO};font-size:32px;font-weight:700;
      color:{NEGRO};line-height:1;margin-top:8mm;margin-bottom:4mm;">IBM Plex Mono</div>
    <div style="font-family:{MONO};font-size:14px;font-weight:400;
      color:{CARBON};letter-spacing:1px;line-height:1.6;">
      A B C D E F G H I J K L M N O P Q R S T U V W X Y Z<br>
      0 1 2 3 4 5 6 7 8 9 ! @ # $ % &amp; * ( ) — . , : ;
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:6mm;">
    {data_block([
        ("Satoshi", "Fontshare (Indian Type Foundry)"),
        ("Clase", "Geometric sans-serif"),
        ("Uso", "Titulos, cuerpo, UI, todo"),
        ("Pesos", "400 · 500 · 700 · 900"),
    ])}
    <div style="background:{ARENA};padding:14px 18px;">
      <div class="eyebrow" style="margin-bottom:3mm;">Por que Satoshi</div>
      <div class="body-text" style="font-size:11px;">
        Geometrica sin ser fria. Legible en cuerpo,
        contundente en display. Un solo tipo que cubre
        toda la jerarquia.
      </div>
    </div>
    {data_block([
        ("Plex Mono", "Google Fonts (IBM)"),
        ("Clase", "Monospaced"),
        ("Uso", "Metadata, specs, eyebrows, data"),
        ("Pesos", "400 · 700"),
    ])}
    <div style="background:{ARENA};padding:14px 18px;">
      <div class="eyebrow" style="margin-bottom:3mm;">Por que Plex Mono</div>
      <div class="body-text" style="font-size:11px;">
        Precision tecnica sin competir con Satoshi.
        Ancho fijo crea alineacion vertical natural.
      </div>
    </div>
  </div>
</div>"""
    return page_shell(body, 20, section="VI · Tipografia", bg=PAPEL)


def p21_type_hierarchy():
    """Type hierarchy + rules."""
    levels = [
        ("Eyebrow", "Plex Mono 8px 700", f'<div class="eyebrow">V · PALETA DE COLOR</div>'),
        ("Titulo", "Satoshi 42px 900", f'<div style="font-family:{FAM};font-size:28px;font-weight:900;color:{NEGRO};">Sistema de color<span style="color:{LACRE};">.</span></div>'),
        ("Subtitulo", "Satoshi 22px 700", f'<div style="font-family:{FAM};font-size:18px;font-weight:700;color:{NEGRO};">Combinaciones</div>'),
        ("Cuerpo", "Satoshi 13px 400", f'<div class="body-text">Negro y Papel son los dominantes.</div>'),
        ("Metadata", "Plex Mono 9px 400", f'<div class="meta">EDICION — Primera edicion · Abril 2026</div>'),
    ]

    demo = ""
    for name, spec, example in levels:
        demo += f"""\
<div style="padding:3mm 0;border-bottom:0.5px solid {CENIZA};">
  <div class="meta" style="margin-bottom:1mm;color:{PIEDRA};">{name} — {spec}</div>
  {example}
</div>"""

    rules = [
        "Satoshi 900 solo para titulos principales.",
        "IBM Plex Mono solo por debajo de 11px.",
        "Sin cursivas. Nunca.",
        "Enfasis con peso (700) o color (Lacre).",
        "El punto final siempre en Lacre al 120%.",
    ]
    rules_html = ""
    for i, r in enumerate(rules, 1):
        rules_html += f"""\
<div style="display:flex;gap:3mm;align-items:baseline;margin-bottom:3mm;">
  <span style="font-family:{MONO};font-size:11px;font-weight:700;color:{LACRE};">{i:02d}</span>
  <span style="font-family:{FAM};font-size:12px;font-weight:400;color:{CARBON};">{r}</span>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.3fr 1fr;gap:20mm;">
  <div style="display:flex;flex-direction:column;justify-content:space-between;">
    <div>
      {titulo("Jerarquia tipografica", 34)}
      {demo}
    </div>
    <div style="border-top:0.5px solid {CENIZA};padding-top:4mm;">
      <div class="meta" style="line-height:1.8;">
        Cada nivel tiene un unico proposito. Un titulo nunca se usa como cuerpo.<br>
        Un metadata nunca se usa como subtitulo. La jerarquia es ley.
      </div>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:space-between;">
    <div style="background:{ARENA};padding:20px 24px;">
      <div class="eyebrow" style="margin-bottom:6mm;">Reglas</div>
      {rules_html}
    </div>
    {accent_rule(60, "8mm")}
    <div class="meta" style="margin-top:4mm;">
      Dos familias. Roles claros. Sin excepciones.
    </div>
    <div style="background:{NEGRO};padding:16px 20px;margin-top:6mm;">
      <div style="font-family:{MONO};font-size:8px;font-weight:700;color:{LACRE};
        letter-spacing:2px;text-transform:uppercase;margin-bottom:3mm;">Ejemplo aplicado</div>
      <div style="font-family:{FAM};font-size:22px;font-weight:900;color:{PAPEL};letter-spacing:-0.5px;">
        Titulo en Satoshi 900<span style="color:{LACRE};font-size:26px;">.</span>
      </div>
      <div style="font-family:{MONO};font-size:9px;color:{CENIZA};margin-top:2mm;">
        METADATA EN PLEX MONO 400
      </div>
    </div>
  </div>
</div>"""
    return page_shell(body, 21, section="VI · Tipografia", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# VII VOZ  (pp. 22-24)
# ══════════════════════════════════════════════════════════════

def p22_voz():
    """Section divider — Voz."""
    return divider("07", "VII", "Voz",
                   "Como habla Tramarca.", pg=22)


def p23_voice_principles_tone():
    """Voice principles + tone examples — fused."""
    principles = [
        ("Frases cortas. Una idea por frase.", '"Producimos manuales de marca."'),
        ("Punto final siempre.", '"Tu marca necesita reglas."'),
        ("Preguntas que incomodan.", '"Tu equipo sabe que colores usar? Seguro?"'),
        ("Nunca exclamaciones.", '"Funciona." No: "Funciona increiblemente!"'),
        ('Tuteo siempre.', '"Tu marca", nunca "su marca".'),
    ]

    items = ""
    for i, (principle, example) in enumerate(principles, 1):
        items += f"""\
<div style="padding:3mm 0;border-bottom:0.5px solid {CENIZA};">
  <div style="display:flex;gap:3mm;align-items:baseline;">
    <span style="font-family:{MONO};font-size:10px;font-weight:700;color:{LACRE};">{i:02d}</span>
    <span style="font-family:{FAM};font-size:13px;font-weight:700;color:{NEGRO};">{principle}</span>
  </div>
  <div style="margin-left:7mm;font-family:{FAM};font-size:11px;color:{PIEDRA};margin-top:1mm;">{example}</div>
</div>"""

    examples = [
        ("Web hero",
         "Que hay tras tu marca?",
         "Descubre el poder transformador de una identidad de marca coherente!"),
        ("Email de contacto",
         "Gracias por escribir. Te cuento rapido que hacemos.",
         "Nos alegra enormemente recibir tu mensaje!"),
    ]

    tone_rows = ""
    for context, yes, no in examples:
        tone_rows += f"""\
<div style="margin-bottom:4mm;">
  <div class="eyebrow" style="margin-bottom:2mm;">{context}</div>
  <div class="g2" style="gap:4mm;">
    <div>
      <div style="font-family:{FAM};font-size:9px;font-weight:700;color:{NEGRO};margin-bottom:1mm;">Asi si</div>
      <div class="body-text" style="font-size:11px;">"{yes}"</div>
    </div>
    <div>
      <div class="struck" style="font-family:{FAM};font-size:9px;font-weight:700;margin-bottom:1mm;">Asi no</div>
      <div style="font-family:{FAM};font-size:11px;color:{PIEDRA};line-height:1.6;">"{no}"</div>
    </div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.2fr 1fr;gap:16mm;">
  <div>
    {titulo("Principios de voz", 34)}
    {items}
  </div>
  <div style="display:flex;flex-direction:column;justify-content:space-between;">
    <div>
      {titulo("Tono", 34)}
      {tone_rows}
    </div>
    {pull_quote("Si suena corporativo, reescribelo. Si suena a Tramarca, punto final", "100%")}
  </div>
</div>"""
    return page_shell(body, 23, section="VII · Voz", bg=PAPEL)


def p24_vocabulary():
    """Vocabulary — use vs never use."""
    use_words = ["documentar", "por escrito", "reglas", "decision", "sistema",
                 "construir", "producir", "cada pagina", "claro", "directo"]
    never_words = ["branding 360", "holistico", "sinergia", "storytelling",
                   "disruptivo", "hacer magia", "conceptualizar", "co-crear",
                   "universo de marca", "lovemark"]

    use_html = "".join(
        f'<div style="padding:2.5mm 0;border-bottom:0.5px solid {CENIZA};'
        f'font-family:{FAM};font-size:16px;font-weight:500;color:{NEGRO};">{w}</div>'
        for w in use_words
    )
    never_html = "".join(
        f'<div class="struck" style="padding:2.5mm 0;border-bottom:0.5px solid {CENIZA};'
        f'font-family:{FAM};font-size:16px;font-weight:500;">{w}</div>'
        for w in never_words
    )

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1fr 1fr;gap:24mm;">
  <div>
    {titulo("Usamos", 38)}
    {use_html}
  </div>
  <div>
    <div class="titulo" style="font-size:38px;color:{PIEDRA};margin-bottom:10mm;">
      Nunca usamos<span class="p" style="font-size:45px;">.</span>
    </div>
    {never_html}
  </div>
</div>
<div style="position:absolute;bottom:16mm;left:24mm;">
  <div class="meta">Si una frase necesita mas de 15 palabras, reescribela.</div>
</div>"""
    return page_shell(body, 24, section="VII · Voz", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# VIII DIRECCION DE ARTE  (pp. 25-26)
# ══════════════════════════════════════════════════════════════

def p25_arte():
    """Section divider — Direccion de arte with background photo."""
    body = f"""\
<div class="noise-heavy" style="position:absolute;inset:0;"></div>

<!-- Background photo: open brand manual -->
<div style="position:absolute;right:0;top:0;width:50%;height:100%;overflow:hidden;opacity:0.3;">
  <img src="assets/img-07.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">
  <div style="position:absolute;inset:0;background:linear-gradient(to right, {NEGRO} 0%, transparent 40%);"></div>
</div>

{giant_letter("08", 800, "rgba(244,240,235,0.025)", "40%", "-50mm")}

<div style="position:absolute;left:24mm;bottom:40mm;">
  <div style="font-family:{MONO};font-size:10px;font-weight:700;
    color:{LACRE};letter-spacing:4px;margin-bottom:6mm;">VIII</div>
  <div style="font-family:{FAM};font-size:110px;font-weight:900;
    color:{PAPEL};letter-spacing:-5px;line-height:0.9;">
    Direccion<br>de arte<span style="color:{LACRE};font-size:130px;">.</span>
  </div>
  <div style="font-family:{FAM};font-size:14px;font-weight:400;
    color:{CENIZA};margin-top:8mm;">Fotografia, layout, composicion.</div>
</div>

<div style="position:absolute;right:24mm;bottom:28mm;width:4px;height:45mm;background:{LACRE};"></div>"""
    return page_shell(body, 25, bg=NEGRO, dark=True, no_furniture=True)


def p26_photography():
    """Photography direction — 4 image grid + specs + logo watermark."""
    body = f"""\
<div style="position:absolute;left:24mm;top:28mm;right:24mm;bottom:18mm;
  display:flex;flex-direction:column;gap:4mm;">

  <!-- Header with logo -->
  <div style="display:flex;justify-content:space-between;align-items:flex-start;">
    {titulo("Direccion fotografica", 36)}
    <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{NEGRO};letter-spacing:-0.5px;
      padding-top:6mm;">
      {BRAND}<span style="color:{LACRE};font-size:18px;">.</span>
    </div>
  </div>

  <!-- 5 image grid — branded scenes + editorial -->
  <div style="display:grid;grid-template-columns:1.2fr 0.8fr 1fr;grid-template-rows:1fr 1fr;gap:3mm;flex:1;">
    <div style="grid-row:span 2;overflow:hidden;">
      <img src="assets/branded/stationery-flatlay.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div style="overflow:hidden;">
      <img src="assets/branded/workspace-overhead.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div style="overflow:hidden;">
      <img src="assets/img-03.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div style="overflow:hidden;">
      <img src="assets/branded/laptop-dark.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div style="overflow:hidden;">
      <img src="assets/img-04.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">
    </div>
  </div>

  <!-- Specs grid -->
  <div style="display:grid;grid-template-columns:repeat(4, 1fr);gap:6mm;
    background:{ARENA};padding:4mm 5mm;">
    <div>
      <div style="font-family:{MONO};font-size:9px;font-weight:700;color:{LACRE};
        letter-spacing:2px;text-transform:uppercase;margin-bottom:2mm;">Estilo</div>
      <div style="font-family:{FAM};font-size:12px;color:{NEGRO};line-height:1.5;">
        Editorial, desaturada, luz lateral. Nunca stock generico.</div>
    </div>
    <div>
      <div style="font-family:{MONO};font-size:9px;font-weight:700;color:{LACRE};
        letter-spacing:2px;text-transform:uppercase;margin-bottom:2mm;">Color</div>
      <div style="font-family:{FAM};font-size:12px;color:{NEGRO};line-height:1.5;">
        Dominan neutros. Lacre como detalle unico (&lt;5%).</div>
    </div>
    <div>
      <div style="font-family:{MONO};font-size:9px;font-weight:700;color:{LACRE};
        letter-spacing:2px;text-transform:uppercase;margin-bottom:2mm;">Sujetos</div>
      <div style="font-family:{FAM};font-size:12px;color:{NEGRO};line-height:1.5;">
        Precision, pantallas, teclados, superficies oscuras.</div>
    </div>
    <div>
      <div style="font-family:{MONO};font-size:9px;font-weight:700;color:{LACRE};
        letter-spacing:2px;text-transform:uppercase;margin-bottom:2mm;">Prohibido</div>
      <div style="font-family:{FAM};font-size:12px;color:{NEGRO};line-height:1.5;">
        Stock, caras, sonrisas, fondos degradados, flat icons.</div>
    </div>
  </div>
</div>"""
    return page_shell(body, 26, section="VIII · Direccion de arte", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# IX APLICACIONES  (pp. 27-31)
# ══════════════════════════════════════════════════════════════

def p27_aplicaciones():
    """Section divider — Aplicaciones with stationery flat-lay background."""
    body = f"""\
<div class="noise-heavy" style="position:absolute;inset:0;"></div>

<!-- Full-bleed stationery photograph -->
<div style="position:absolute;inset:0;overflow:hidden;">
  <img src="assets/branded/stationery-flatlay.jpg" alt=""
    style="width:100%;height:100%;object-fit:cover;filter:brightness(0.35);opacity:0.85;">
</div>

<!-- Gradient overlay for text readability -->
<div style="position:absolute;inset:0;
  background:linear-gradient(135deg, rgba(12,12,12,0.9) 0%, rgba(12,12,12,0.4) 50%, rgba(12,12,12,0.7) 100%);"></div>

{giant_letter("09", 800, "rgba(244,240,235,0.03)", "40%", "-50mm")}

<div style="position:absolute;left:24mm;bottom:40mm;">
  <div style="font-family:{MONO};font-size:10px;font-weight:700;
    color:{LACRE};letter-spacing:4px;margin-bottom:6mm;">IX</div>
  <div style="font-family:{FAM};font-size:110px;font-weight:900;
    color:{PAPEL};letter-spacing:-5px;line-height:0.9;">
    Aplicaciones<span style="color:{LACRE};font-size:130px;">.</span>
  </div>
  <div style="font-family:{FAM};font-size:14px;font-weight:400;
    color:{CENIZA};margin-top:8mm;">Tarjeta, email, factura, redes, propuesta.</div>
</div>

<div style="position:absolute;right:24mm;bottom:28mm;width:4px;height:45mm;background:{LACRE};"></div>
<div style="position:absolute;right:24mm;bottom:18mm;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.3);">27 / {TOTAL}</span>
</div>"""
    return page_shell(body, 27, bg=NEGRO, dark=True, no_furniture=True)


def p28_business_card():
    """Business card — full-bleed stationery photo + CSS card mockups overlaid."""
    body = f"""\
<!-- Full-bleed stationery photo as background -->
<div style="position:absolute;inset:0;overflow:hidden;">
  <img src="assets/branded/stationery-flatlay.jpg" alt=""
    style="width:100%;height:100%;object-fit:cover;filter:brightness(0.55);">
</div>
<div class="noise" style="position:absolute;inset:0;"></div>

<!-- Gradient for text zone -->
<div style="position:absolute;inset:0;
  background:linear-gradient(to right, rgba(12,12,12,0.85) 0%, rgba(12,12,12,0.3) 40%, transparent 70%);"></div>

<!-- Left: title + specs -->
<div style="position:absolute;left:24mm;top:24mm;">
  <div class="eyebrow" style="color:{LACRE};">IX · Aplicaciones</div>
</div>
<div style="position:absolute;left:24mm;top:36mm;">
  {titulo("Tarjeta de<br>visita", 42, PAPEL, "0")}
</div>

<div style="position:absolute;left:24mm;bottom:40mm;max-width:90mm;">
  <div style="font-family:{MONO};font-size:9px;color:rgba(244,240,235,0.5);line-height:2.6;">
    <span style="color:{PIEDRA};">TAMANO</span> 85 x 55 mm<br>
    <span style="color:{PIEDRA};">PAPEL</span> 400g cotton uncoated<br>
    <span style="color:{PIEDRA};">TINTA</span> Negro mate + Lacre hot foil<br>
    <span style="color:{PIEDRA};">ACABADO</span> Cantos tintados en Lacre
  </div>
</div>

<!-- CSS mockup: FRONT (top card, on light Papel background for contrast) -->
<div style="position:absolute;right:50mm;top:26mm;
  width:110mm;height:68mm;background:{PAPEL};
  box-shadow:0 20px 60px rgba(0,0,0,0.5),0 8px 20px rgba(0,0,0,0.3);">
  <div style="height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;">
    <div style="font-family:{FAM};font-size:26px;font-weight:900;color:{NEGRO};letter-spacing:-1px;">
      {BRAND}<span style="color:{LACRE};font-size:32px;">.</span>
    </div>
    <div style="font-family:{MONO};font-size:9px;color:{PIEDRA};margin-top:5mm;letter-spacing:2px;text-transform:uppercase;">
      Tu marca, sin improvisar
    </div>
  </div>
  <div style="position:absolute;bottom:0;left:0;right:0;height:3px;background:{LACRE};"></div>
  <div style="position:absolute;top:5mm;left:7mm;">
    <span style="font-family:{MONO};font-size:7px;color:{CENIZA};letter-spacing:2px;text-transform:uppercase;">Anverso</span>
  </div>
</div>

<!-- CSS mockup: BACK (below, dark, with full brand treatment) -->
<div style="position:absolute;right:30mm;bottom:30mm;
  width:110mm;height:68mm;background:{NEGRO};
  box-shadow:0 20px 60px rgba(0,0,0,0.5);
  border:0.5px solid rgba(244,240,235,0.08);">
  <!-- Lacre accent line top -->
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{LACRE};"></div>
  <div style="padding:8mm 9mm;height:100%;display:flex;flex-direction:column;justify-content:space-between;">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;">
      <div>
        <div style="font-family:{FAM};font-size:16px;font-weight:700;color:{PAPEL};">Fernando Rojas</div>
        <div style="font-family:{FAM};font-size:10px;color:{PIEDRA};margin-top:2mm;">Director</div>
      </div>
      <div style="font-family:{FAM};font-size:12px;font-weight:900;color:{PAPEL};opacity:0.3;">
        {BRAND}<span style="color:{LACRE};font-size:15px;">.</span>
      </div>
    </div>
    <div>
      <div style="width:20mm;height:1px;background:{LACRE};margin-bottom:4mm;"></div>
      <div style="font-family:{MONO};font-size:9px;color:{CENIZA};line-height:2.4;">
        hola@tramarca.es<br>tramarca.es<br>+34 600 000 000
      </div>
    </div>
  </div>
  <div style="position:absolute;top:5mm;right:9mm;">
    <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.3);letter-spacing:2px;text-transform:uppercase;">Reverso</span>
  </div>
</div>

<div style="position:absolute;right:24mm;bottom:18mm;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.2);">28 / {TOTAL}</span>
</div>"""
    return page_shell(body, 28, bg=NEGRO, dark=True, no_furniture=True)


def p29_email_signature():
    """Email + signature — cinematic spread with laptop photo background."""
    body = f"""\
<!-- Full-bleed laptop photo -->
<div style="position:absolute;inset:0;overflow:hidden;">
  <img src="assets/branded/laptop-dark.jpg" alt=""
    style="width:100%;height:100%;object-fit:cover;filter:brightness(0.4);">
</div>
<div class="noise" style="position:absolute;inset:0;"></div>

<!-- Gradient for left text zone -->
<div style="position:absolute;inset:0;
  background:linear-gradient(to right, rgba(12,12,12,0.9) 0%, rgba(12,12,12,0.6) 45%, transparent 80%);"></div>

<!-- Title -->
<div style="position:absolute;left:24mm;top:24mm;">
  <div class="eyebrow" style="color:{LACRE};">IX · Aplicaciones</div>
</div>
<div style="position:absolute;left:24mm;top:36mm;">
  {titulo("Email y<br>firma", 42, PAPEL, "0")}
</div>

<!-- Email mockup floating on the right — straight, no rotation -->
<div style="position:absolute;right:30mm;top:50%;transform:translateY(-50%);
  width:150mm;background:white;padding:10mm 14mm;
  box-shadow:0 30px 80px rgba(0,0,0,0.5),0 10px 30px rgba(0,0,0,0.3);">
  <!-- Browser chrome -->
  <div style="position:absolute;top:-8mm;left:0;right:0;height:8mm;background:#2C2C2C;
    display:flex;align-items:center;padding-left:4mm;gap:2mm;">
    <div style="width:3mm;height:3mm;border-radius:50%;background:#FF5F56;"></div>
    <div style="width:3mm;height:3mm;border-radius:50%;background:#FFBD2E;"></div>
    <div style="width:3mm;height:3mm;border-radius:50%;background:#27C93F;"></div>
  </div>
  <div style="font-family:{FAM};font-size:12px;font-weight:400;
    color:{PIEDRA};line-height:1.8;margin-bottom:8mm;">
    Gracias por escribir. Te cuento rapido que hacemos y que no.<br>
    Hablamos cuando quieras.
  </div>
  <div style="width:70mm;height:1px;background:{CENIZA};margin-bottom:5mm;"></div>
  <div style="display:flex;align-items:baseline;gap:3mm;">
    <div style="font-family:{FAM};font-size:13px;font-weight:600;color:{NEGRO};">
      Fernando Rojas</div>
    <span style="color:{LACRE};font-weight:900;font-size:16px;">.</span>
    <div style="font-family:{FAM};font-size:13px;font-weight:600;color:{NEGRO};">Tramarca</div>
  </div>
  <div style="font-family:{MONO};font-size:9px;color:{PIEDRA};margin-top:2mm;">
    {DESCRIPTOR} — tramarca.es
  </div>
</div>

<!-- Rules at bottom left -->
<div style="position:absolute;left:24mm;bottom:24mm;max-width:100mm;">
  <div style="display:flex;gap:6mm;">
    <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.4);line-height:1.8;">
      Sin imagenes incrustadas<br>Sin citas inspiracionales<br>Sin banners promocionales
    </div>
    <div style="width:1px;background:rgba(244,240,235,0.1);"></div>
    <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.4);line-height:1.8;">
      Firma: Nombre · Punto · Marca<br>Tono directo, sin adornos<br>Respuesta &lt; 24h laborables
    </div>
  </div>
</div>

<div style="position:absolute;right:24mm;bottom:18mm;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.2);">29 / {TOTAL}</span>
</div>"""
    return page_shell(body, 29, bg=NEGRO, dark=True, no_furniture=True)


def p30_invoice():
    """Invoice — letterhead photo background + floating CSS invoice."""
    body = f"""\
<!-- Full-bleed letterhead photo -->
<div style="position:absolute;inset:0;overflow:hidden;">
  <img src="assets/branded/letterhead-held.jpg" alt=""
    style="width:100%;height:100%;object-fit:cover;filter:brightness(0.35);">
</div>
<div class="noise" style="position:absolute;inset:0;"></div>

<div style="position:absolute;inset:0;
  background:linear-gradient(to right, rgba(12,12,12,0.9) 0%, rgba(12,12,12,0.5) 50%, rgba(12,12,12,0.7) 100%);"></div>

<!-- Title left -->
<div style="position:absolute;left:24mm;top:24mm;">
  <div class="eyebrow" style="color:{LACRE};">IX · Aplicaciones</div>
</div>
<div style="position:absolute;left:24mm;top:36mm;">
  {titulo("Factura", 48, PAPEL, "0")}
</div>

<!-- Floating invoice document — straight, centered -->
<div style="position:absolute;left:50%;top:50%;transform:translate(-42%,-48%);
  width:140mm;background:white;padding:10mm 12mm;
  box-shadow:0 30px 80px rgba(0,0,0,0.5),0 10px 30px rgba(0,0,0,0.3);">
  <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6mm;">
    <div style="font-family:{FAM};font-size:18px;font-weight:900;color:{NEGRO};">
      {BRAND}<span style="color:{LACRE};">.</span>
    </div>
    <div style="font-family:{MONO};font-size:9px;color:{PIEDRA};letter-spacing:1px;">FAC-2026-001</div>
  </div>
  <div style="width:100%;height:1px;background:{CENIZA};margin-bottom:5mm;"></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8mm;margin-bottom:5mm;">
    <div>
      <div style="font-family:{MONO};font-size:7px;color:{PIEDRA};text-transform:uppercase;letter-spacing:1px;margin-bottom:2mm;">De</div>
      <div style="font-family:{FAM};font-size:10px;color:{NEGRO};line-height:1.7;">Tramarca<br>Fernando Rojas<br>hola@tramarca.es</div>
    </div>
    <div>
      <div style="font-family:{MONO};font-size:7px;color:{PIEDRA};text-transform:uppercase;letter-spacing:1px;margin-bottom:2mm;">Para</div>
      <div style="font-family:{FAM};font-size:10px;color:{NEGRO};line-height:1.7;">Empresa S.L.<br>Calle Ejemplo 1<br>28001 Madrid</div>
    </div>
  </div>
  <div style="background:{ARENA};padding:3mm 4mm;margin-bottom:3mm;">
    <div style="display:flex;justify-content:space-between;font-family:{MONO};font-size:7px;color:{PIEDRA};text-transform:uppercase;letter-spacing:1px;">
      <span>Concepto</span><span>Importe</span>
    </div>
  </div>
  <div style="padding:3mm 4mm;border-bottom:1px solid {CENIZA};display:flex;justify-content:space-between;">
    <div style="font-family:{FAM};font-size:11px;color:{NEGRO};">Manual de marca — Profesional</div>
    <div style="font-family:{MONO};font-size:11px;color:{NEGRO};">2.500,00 EUR</div>
  </div>
  <div style="padding:3mm 4mm;border-bottom:1px solid {CENIZA};display:flex;justify-content:space-between;">
    <div style="font-family:{FAM};font-size:10px;color:{PIEDRA};">IVA (21%)</div>
    <div style="font-family:{MONO};font-size:10px;color:{PIEDRA};">525,00 EUR</div>
  </div>
  <div style="padding:4mm 4mm;display:flex;justify-content:space-between;background:{NEGRO};margin-top:3mm;">
    <div style="font-family:{FAM};font-size:12px;font-weight:700;color:{PAPEL};">Total</div>
    <div style="font-family:{MONO};font-size:12px;font-weight:700;color:{PAPEL};">3.025,00 EUR</div>
  </div>
  <div style="margin-top:4mm;font-family:{MONO};font-size:7px;color:{PIEDRA};line-height:1.8;">
    Pago: transferencia bancaria · Vencimiento: 15 dias
  </div>
</div>

<!-- Specs bottom left -->
<div style="position:absolute;left:24mm;bottom:20mm;">
  <div style="font-family:{MONO};font-size:8px;color:rgba(244,240,235,0.4);line-height:2.2;">
    <span style="color:{PIEDRA};">FORMATO</span> A4 vertical ·
    <span style="color:{PIEDRA};">FACTURACION</span> Holded ·
    <span style="color:{PIEDRA};">PAGO</span> Transferencia + Stripe
  </div>
</div>
<div style="position:absolute;right:24mm;bottom:18mm;">
  <span style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.2);">30 / {TOTAL}</span>
</div>"""
    return page_shell(body, 30, bg=NEGRO, dark=True, no_furniture=True)


def p31_social_proposal():
    """Social media — cinematic phone mockup + proposal document."""
    body = f"""\
<!-- Split: dark left (social) / light right (propuesta) -->
<div style="position:absolute;inset:0;display:grid;grid-template-columns:50% 50%;">

  <!-- LEFT: Social with phone photo -->
  <div style="position:relative;background:{NEGRO};overflow:hidden;">
    <div class="noise" style="position:absolute;inset:0;"></div>
    <!-- Phone photo -->
    <div style="position:absolute;inset:0;overflow:hidden;opacity:0.7;">
      <img src="assets/branded/phone-social.jpg" alt=""
        style="width:100%;height:100%;object-fit:cover;filter:brightness(0.6);">
    </div>
    <div style="position:absolute;inset:0;
      background:linear-gradient(to bottom, rgba(12,12,12,0.7) 0%, rgba(12,12,12,0.3) 40%, rgba(12,12,12,0.8) 100%);"></div>

    <div style="position:absolute;left:16mm;top:24mm;">
      <div class="eyebrow" style="color:{LACRE};">IX · Aplicaciones</div>
      <div style="font-family:{FAM};font-size:36px;font-weight:900;
        color:{PAPEL};letter-spacing:-1.5px;margin-top:4mm;">
        Redes<br>sociales<span style="color:{LACRE};font-size:44px;">.</span>
      </div>
    </div>

    <div style="position:absolute;left:16mm;bottom:24mm;right:16mm;">
      <div style="display:flex;align-items:center;gap:3mm;margin-bottom:4mm;">
        <div style="width:10mm;height:10mm;border-radius:50%;background:{LACRE};
          display:flex;align-items:center;justify-content:center;">
          <span style="font-family:{FAM};font-size:6px;font-weight:900;color:{PAPEL};">Tm.</span>
        </div>
        <div>
          <div style="font-family:{FAM};font-size:10px;font-weight:700;color:{PAPEL};">@tramarca</div>
          <div style="font-family:{MONO};font-size:7px;color:{PIEDRA};margin-top:1mm;">LinkedIn · Instagram</div>
        </div>
      </div>
      <div style="font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.35);line-height:1.8;">
        Fondo oscuro o fondo papel. Nunca degradados.<br>
        Nunca mas de 15 palabras por post.<br>
        Punto Lacre como unico acento de color.
      </div>
    </div>
  </div>

  <!-- RIGHT: Propuesta on light -->
  <div style="position:relative;background:{PAPEL};padding:24mm 20mm 18mm 20mm;
    display:flex;flex-direction:column;gap:5mm;">
    <div style="font-family:{FAM};font-size:36px;font-weight:900;
      color:{NEGRO};letter-spacing:-1.5px;">
      Propuesta<span style="color:{LACRE};font-size:44px;">.</span>
    </div>

    <div style="background:white;border:1px solid {CENIZA};padding:10mm 12mm;
      box-shadow:0 8px 30px rgba(0,0,0,0.08);flex:1;">
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:4mm;">
        <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{NEGRO};">
          {BRAND}<span style="color:{LACRE};">.</span></div>
        <div class="meta">PROP-2026-001</div>
      </div>
      <div style="width:100%;height:1px;background:{CENIZA};margin-bottom:4mm;"></div>
      <div style="font-family:{FAM};font-size:18px;font-weight:900;color:{NEGRO};margin-bottom:3mm;">
        Propuesta para Empresa<span style="color:{LACRE};font-size:22px;">.</span>
      </div>
      <div class="body-text" style="font-size:11px;margin-bottom:5mm;">
        Alcance, proceso y condiciones. Sin rodeos.
      </div>
      {data_block([
          ("Alcance", "Profesional"),
          ("Plazo", "4 semanas"),
          ("Revisiones", "2 rondas"),
      ])}
      <div style="margin-top:5mm;padding-top:4mm;border-top:1px solid {CENIZA};">
        <div style="font-family:{FAM};font-size:11px;font-weight:700;color:{NEGRO};line-height:1.5;">
          Sin slides. Sin filosofia<span style="color:{LACRE};">.</span><br>
          Solo que, como, cuando y cuanto<span style="color:{LACRE};">.</span>
        </div>
      </div>
    </div>

    <div style="font-family:{MONO};font-size:7px;color:{PIEDRA};text-align:right;">
      31 / {TOTAL}
    </div>
  </div>
</div>"""
    return page_shell(body, 31, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# X  PORTFOLIO  (p. 32)
# ══════════════════════════════════════════════════════════════

def p32_portfolio():
    """Portfolio — horizontal strips, one per project, large images."""
    cases = [
        ("Anfisbena", "Knitwear de autor · Madrid", "43 pp",
         "assets/portfolio/anfisbena-cover.png", "assets/portfolio/anfisbena-p08.png"),
        ("Claramel", "App Android · Mexico", "29 pp",
         "assets/portfolio/claramel-cover.png", "assets/portfolio/claramel-p07.png"),
        ("Matraz Innova", "Farmaceutica · Espana", "33 pp",
         "assets/portfolio/matraz-cover.png", "assets/portfolio/matraz-p06.png"),
    ]

    rows = ""
    for name, sector, pages, cover, spread in cases:
        rows += f"""\
<div style="display:grid;grid-template-columns:100mm 1fr;gap:5mm;align-items:start;">
  <!-- Two images side by side -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm;">
    <div style="height:44mm;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.15);">
      <img src="{cover}" alt="" style="width:100%;height:100%;object-fit:cover;object-position:top;">
    </div>
    <div style="height:44mm;overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
      <img src="{spread}" alt="" style="width:100%;height:100%;object-fit:cover;object-position:top;">
    </div>
  </div>
  <!-- Info -->
  <div style="padding-top:2mm;">
    <div style="font-family:{FAM};font-size:22px;font-weight:900;color:{NEGRO};letter-spacing:-0.5px;">
      {name}<span style="color:{LACRE};font-size:26px;">.</span>
    </div>
    <div style="font-family:{FAM};font-size:12px;color:{PIEDRA};margin-top:2mm;">{sector}</div>
    <div style="font-family:{MONO};font-size:9px;color:{CENIZA};margin-top:2mm;">{pages}</div>
    <div style="width:16mm;height:2px;background:{LACRE};margin-top:3mm;"></div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:26mm;right:24mm;bottom:18mm;
  display:flex;flex-direction:column;justify-content:space-between;">

  <div>
    <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:2mm;">
      {titulo("Portfolio", 42)}
      <div style="font-family:{FAM};font-size:12px;font-weight:900;color:{NEGRO};letter-spacing:-0.3px;">
        {BRAND}<span style="color:{LACRE};font-size:15px;">.</span>
      </div>
    </div>
    <div class="body-text" style="margin-bottom:6mm;">
      Tres manuales entregados. Tres marcas con sistema por escrito.
    </div>

    <div style="display:flex;flex-direction:column;gap:5mm;">
      {rows}
    </div>
  </div>

  <div style="padding-top:4mm;border-top:2px solid {NEGRO};">
    <div style="font-family:{FAM};font-size:16px;font-weight:900;color:{NEGRO};line-height:1.3;">
      No mostramos maquetas<span style="color:{LACRE};">.</span>
      Mostramos manuales reales, entregados, en uso<span style="color:{LACRE};">.</span>
    </div>
  </div>
</div>"""
    return page_shell(body, 32, section="X · Portfolio", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# CIERRE  (pp. 33-34)
# ══════════════════════════════════════════════════════════════

def p33_contact():
    """Contact page — split dark with Lacre droplet image."""
    left = f"""\
<div style="padding:28mm 16mm 24mm 24mm;height:100%;display:flex;flex-direction:column;justify-content:space-between;">
  <div>
    <div style="font-family:{FAM};font-size:48px;font-weight:900;
      color:{PAPEL};letter-spacing:-2px;line-height:1.0;margin-bottom:10mm;">
      Que hay tras<br>tu marca<span style="color:{LACRE};font-size:60px;">?</span>
    </div>
    <div style="font-family:{FAM};font-size:16px;font-weight:400;
      color:{CENIZA};line-height:1.7;max-width:110mm;">
      Si has llegado hasta aqui, ya sabes que la improvisacion
      no es estrategia. Hablemos.
    </div>
  </div>
  <!-- Lacre droplet image -->
  <div style="height:50mm;overflow:hidden;">
    <img src="assets/img-08.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">
  </div>
</div>"""

    right = f"""\
<div style="padding:28mm 24mm 24mm 20mm;height:100%;display:flex;flex-direction:column;justify-content:center;">
  <div style="font-family:{MONO};font-size:12px;line-height:3.2;color:{CENIZA};">
    <div><span style="display:inline-block;min-width:22mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">Email</span>hola@tramarca.es</div>
    <div><span style="display:inline-block;min-width:22mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">Web</span>tramarca.es</div>
    <div><span style="display:inline-block;min-width:22mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">LinkedIn</span>Tramarca</div>
    <div><span style="display:inline-block;min-width:22mm;color:{PIEDRA};font-size:8px;letter-spacing:1px;text-transform:uppercase;">Instagram</span>@tramarca</div>
  </div>
  <div style="margin-top:12mm;">
    <div style="font-family:{FAM};font-size:14px;font-weight:700;
      color:{PAPEL};border-left:4px solid {LACRE};padding-left:14px;line-height:1.4;">
      Primer paso: un email. Sin compromiso.<br>
      Te decimos si podemos ayudarte. Sin rodeos.
    </div>
  </div>
</div>"""

    body = split_page(left, right, left_bg=NEGRO, right_bg=CARBON, ratio="55% 45%")
    return page_shell(body, 33, bg=NEGRO, dark=True, no_furniture=True)


def p34_back_cover():
    """Back cover — minimal, dark, the final period."""
    body = f"""\
<div class="noise-heavy" style="position:absolute;inset:0;"></div>

<!-- Subtle vignette -->
<div style="position:absolute;inset:0;
  background:radial-gradient(ellipse at 50% 45%, transparent 30%, rgba(0,0,0,0.5) 100%);
  pointer-events:none;"></div>

<!-- Geometric Lacre circle — the punto final as abstract mark -->
<div style="position:absolute;left:50%;top:42%;transform:translate(-50%,-50%);
  width:60mm;height:60mm;border-radius:50%;
  background:radial-gradient(circle, rgba(196,85,58,0.12) 0%, rgba(196,85,58,0.03) 60%, transparent 80%);
  pointer-events:none;"></div>

<!-- Wordmark centered -->
<div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);text-align:center;">
  <div style="font-family:{FAM};font-size:56px;font-weight:900;
    color:{PAPEL};letter-spacing:-2px;">
    {BRAND}<span style="color:{LACRE};font-size:70px;position:relative;top:4px;">.</span>
  </div>
  <div style="font-family:{MONO};font-size:9px;font-weight:400;
    letter-spacing:5px;color:rgba(244,240,235,0.3);margin-top:8mm;text-transform:uppercase;">
    {DESCRIPTOR}
  </div>
</div>

<!-- Thin diagonal slash — echoes the cover -->
<div style="position:absolute;left:-10%;top:68%;
  width:120%;height:1px;background:{LACRE};
  transform:rotate(-6deg);opacity:0.2;"></div>

<div style="position:absolute;bottom:14mm;left:24mm;right:24mm;
  display:flex;justify-content:space-between;align-items:baseline;
  font-family:{MONO};font-size:7px;color:rgba(244,240,235,0.2);">
  <span>tramarca.es</span>
  <span>hola@tramarca.es</span>
  <span>{EDITION}</span>
</div>"""
    return page_shell(body, 34, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════

def build():
    pages = [
        # 00 Apertura
        p01_cover(),               # 01
        p02_index_colophon(),      # 02
        # I Provocacion
        p03_provocacion(),         # 03
        p04_the_problem(),         # 04
        # II Fundamentos
        p05_fundamentos(),         # 05
        p06_vision_values(),       # 06
        p07_positioning(),         # 07
        p08_audience_personality(),# 08
        # III Servicio
        p09_servicio(),            # 09
        p10_included_process(),    # 10
        p11_tiers(),               # 11
        # IV Identidad visual
        p12_identidad(),           # 12
        p13_logo_primary(),        # 13
        p14_construction_clearspace(), # 14
        p15_logo_versions(),       # 15
        p16_logo_forbidden(),      # 16
        # V Color
        p17_color_palette(),       # 17
        p18_color_combos_donts(),  # 18
        # VI Tipografia
        p19_tipografia(),          # 19
        p20_specimens(),           # 20
        p21_type_hierarchy(),      # 21
        # VII Voz
        p22_voz(),                 # 22
        p23_voice_principles_tone(), # 23
        p24_vocabulary(),          # 24
        # VIII Direccion de arte
        p25_arte(),                # 25
        p26_photography(),         # 26
        # IX Aplicaciones
        p27_aplicaciones(),        # 27
        p28_business_card(),       # 28
        p29_email_signature(),     # 29
        p30_invoice(),             # 30
        p31_social_proposal(),     # 31
        # X Portfolio
        p32_portfolio(),           # 32
        # Cierre
        p33_contact(),             # 33
        p34_back_cover(),          # 34
    ]

    assert len(pages) == TOTAL, f"Expected {TOTAL} pages, got {len(pages)}"

    DIST.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html_wrap(pages), encoding="utf-8")
    print(f"Built {len(pages)} pages -> {OUT}")


if __name__ == "__main__":
    build()
