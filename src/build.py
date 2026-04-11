"""
TRAMARCA. Brand Manual — Rebuild v2
====================================
51 pages, A4 landscape. Built on the toolkit design system.
"""
from __future__ import annotations
from pathlib import Path
from toolkit import *

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
OUT  = DIST / "tramarca-brand-manual.html"


# ══════════════════════════════════════════════════════════════
# 00 APERTURA  (pp. 01-03)
# ══════════════════════════════════════════════════════════════

def p01_cover():
    """Cover — black void, massive wordmark, oversized punto."""
    body = f"""\
<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-54%);text-align:center;">
  <div style="font-family:{FAM};font-size:140px;font-weight:900;
    color:{PAPEL};letter-spacing:-4px;line-height:1;">
    {BRAND}<span style="color:{LACRE};font-size:180px;position:relative;top:8px;">.</span>
  </div>
  <div style="font-family:{MONO};font-size:10px;font-weight:400;
    letter-spacing:6px;color:{CENIZA};margin-top:14mm;text-transform:uppercase;">
    Tu marca, sin improvisar
  </div>
</div>
<div style="position:absolute;bottom:14mm;left:24mm;right:24mm;
  display:flex;justify-content:space-between;align-items:baseline;
  font-family:{MONO};font-size:8px;color:{PIEDRA};">
  <span>Manual de marca</span>
  <span style="letter-spacing:2px;">2026</span>
</div>"""
    return page_shell(body, 1, bg=NEGRO, dark=True, no_furniture=True)


def p02_colophon():
    """Colophon — technical data + brand statement."""
    body = f"""\
<div style="position:absolute;top:28mm;left:30mm;right:30mm;bottom:18mm;
  display:grid;grid-template-columns:1fr 1.4fr;gap:40mm;align-content:start;">
  <!-- Left: colophon data -->
  <div>
    <div class="eyebrow" style="margin-bottom:8mm;">Colofón</div>
    {data_block([
        ("Edición", EDITION),
        ("Diseñado por", "Tramarca"),
        ("Páginas", str(TOTAL)),
        ("Tipografías", "Satoshi (Fontshare), IBM Plex Mono (Google)"),
        ("Colores", "7"),
        ("Formato", "A4 apaisado, 297 × 210 mm"),
        ("Producido con", "Python + Playwright + Chromium"),
    ])}
  </div>
  <!-- Right: brand statement -->
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <div style="font-family:{FAM};font-size:18px;font-weight:400;
      color:{CENIZA};line-height:1.8;">
      Este documento define qué es Tramarca, cómo se ve, cómo habla
      y cómo se aplica. Cada decisión está por escrito.
      Cada regla tiene una razón.
    </div>
    {accent_rule(80, "14mm")}
    <div style="font-family:{FAM};font-size:14px;font-weight:500;
      color:{PIEDRA};margin-top:10mm;line-height:1.7;">
      Si no podemos explicar por qué, lo quitamos.
    </div>
  </div>
</div>"""
    return page_shell(body, 2, bg=CARBON, dark=True, section="Colofón")


def p03_toc():
    """Table of contents — two-column grid."""
    left = SECTIONS[1:7]   # I–VI
    right = SECTIONS[7:]   # VII–X + Cierre

    def entry(s):
        r = s["r"]
        lbl = f'<span style="font-family:{MONO};font-weight:700;color:{LACRE};font-size:10px;display:inline-block;min-width:28px;">{r}</span>' if r else '<span style="display:inline-block;min-width:28px;"></span>'
        return f"""\
<div style="display:flex;justify-content:space-between;align-items:baseline;
  margin-bottom:5mm;padding-bottom:5mm;border-bottom:0.5px solid {CENIZA};">
  <div>{lbl}<span style="font-family:{FAM};font-size:15px;font-weight:500;
    color:{NEGRO};">{s['title']}</span></div>
  <span class="meta">{s['pages'][0]:02d}</span>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;">
  {titulo("Índice", 42)}
</div>
<div style="position:absolute;left:24mm;top:62mm;right:24mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;">
  <div>{"".join(entry(s) for s in left)}</div>
  <div>{"".join(entry(s) for s in right)}</div>
</div>"""
    return page_shell(body, 3, section="Índice", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# I  PROVOCACIÓN  (pp. 04-06)
# ══════════════════════════════════════════════════════════════

def p04_provocacion():
    """Section divider — Provocación."""
    return divider("1", "I", "Provocación",
                   "Por qué este manual existe", pg=4)


def p05_the_problem():
    """The problem — Lo que no se documenta, se improvisa."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.3fr 1fr;gap:12mm;">
  <!-- Left: text -->
  <div style="display:flex;flex-direction:column;justify-content:space-between;">
    <div>
      <div style="font-family:{FAM};font-size:38px;font-weight:900;
        color:{NEGRO};line-height:1.15;letter-spacing:-1px;margin-bottom:10mm;">
        Lo que no se<br>documenta,<br>
        <span style="font-weight:400;color:{PIEDRA};">se improvisa</span><span style="color:{LACRE};font-size:46px;">.</span>
      </div>
      <div class="body-text" style="max-width:130mm;">
        <p style="margin-bottom:6mm;">
          La mayoría de las marcas existen solo en la cabeza de quien las creó.
          No en un documento. No por escrito. En la cabeza.
        </p>
        <p style="margin-bottom:6mm;">
          Sin reglas escritas, cada persona que toca la marca la interpreta
          a su manera. Tu imprenta elige un azul. Tu community manager elige otro tono.
          Tu equipo reinventa la rueda cada lunes.
        </p>
        <p>
          El resultado es ruido visual. Inconsistencia. Improvisación.
        </p>
      </div>
    </div>
    {accent_rule()}
  </div>
  <!-- Right: pull quote + image -->
  <div style="display:flex;flex-direction:column;justify-content:space-between;">
    <div class="photo" style="width:100%;height:55%;overflow:hidden;">
      <img src="assets/img-03.jpg" style="object-position:center;width:100%;height:100%;object-fit:cover;
        filter:grayscale(15%) contrast(1.08);" alt="">
    </div>
    <div style="text-align:right;margin-top:auto;padding-top:8mm;">
      <div style="font-family:{FAM};font-size:24px;font-weight:700;
        color:{NEGRO};line-height:1.35;">
        Tu marca no existe<span style="color:{LACRE};font-size:29px;">.</span><br>
        Existe en tu cabeza<span style="color:{LACRE};font-size:29px;">.</span><br>
        Pero eso no cuenta<span style="color:{LACRE};font-size:29px;">.</span>
      </div>
      {accent_rule(60, "6mm")}
    </div>
  </div>
</div>"""
    return page_shell(body, 5, section="I · Provocación", bg=PAPEL)


def p06_the_answer():
    """The answer — Un sistema de marca."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;">
  {titulo("Un sistema de marca", 38)}
  <div class="body-text" style="max-width:220mm;margin-bottom:8mm;">
    <p style="margin-bottom:6mm;">
      Un sistema de marca no es un logo. No es un PDF de tres páginas
      que alguien hizo hace dos años. Es el conjunto completo de reglas
      — visuales y verbales — que protege tu marca de la improvisación.
    </p>
    <p>
      Identidad visual. Voz. Personalidad. Assets. Reglas de uso.
      Todo en un documento. Página a página. Decisión a decisión.
    </p>
  </div>
</div>
<!-- Bottom image strip -->
<div style="position:absolute;bottom:0;left:0;right:0;height:75mm;overflow:hidden;">
  <img src="assets/img-10.jpg" style="width:100%;height:100%;object-fit:cover;
    object-position:center 40%;filter:grayscale(25%) contrast(1.1);opacity:0.9;" alt="">
  <div style="position:absolute;top:0;left:0;right:0;height:100%;
    background:linear-gradient({PAPEL} 0%, transparent 50%);"></div>
  <div style="position:absolute;bottom:18mm;left:24mm;right:24mm;
    display:flex;justify-content:space-between;align-items:flex-end;">
    <div style="font-family:{FAM};font-size:14px;font-weight:500;
      color:{PAPEL};text-shadow:0 1px 4px rgba(0,0,0,0.6);">
      Eso es lo que hacemos en Tramarca. Ponerlo por escrito.
    </div>
    <div style="font-family:{MONO};font-size:9px;color:rgba(244,240,235,0.6);
      text-shadow:0 1px 3px rgba(0,0,0,0.5);">
      tramarca.es
    </div>
  </div>
</div>"""
    return page_shell(body, 6, section="I · Provocación", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# II FUNDAMENTOS  (pp. 07-12)
# ══════════════════════════════════════════════════════════════

def p07_fundamentos():
    """Section divider — Fundamentos."""
    return divider("2", "II", "Fundamentos",
                   "Quién somos. Qué hacemos. Para quién", pg=7)


def p08_vision_mission():
    """Vision and Mission with data strip."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;grid-template-rows:auto 1fr auto;">
  <!-- Title spans both columns -->
  <div style="grid-column:1/-1;">
    {titulo("Visión y misión", 38)}
  </div>
  <!-- Vision -->
  <div>
    <div class="eyebrow" style="margin-bottom:5mm;">Visión</div>
    <div style="font-family:{FAM};font-size:20px;font-weight:700;
      color:{NEGRO};line-height:1.4;">
      Que cada marca profesional tenga su sistema por escrito<span style="color:{LACRE};font-size:24px;">.</span>
    </div>
  </div>
  <!-- Mission -->
  <div>
    <div class="eyebrow" style="margin-bottom:5mm;">Misión</div>
    <div style="font-family:{FAM};font-size:20px;font-weight:700;
      color:{NEGRO};line-height:1.4;margin-bottom:8mm;">
      Producimos sistemas de marca completos<span style="color:{LACRE};font-size:24px;">.</span>
    </div>
    <div class="body-text">
      Identidad visual, voz, personalidad, assets y reglas de uso.
      Un documento. Cada decisión. Por escrito.
    </div>
  </div>
  <!-- Pull quote spans both columns -->
  <div style="grid-column:1/-1;align-self:end;">
    {accent_rule(60, "0")}
    <div style="margin-top:5mm;">
      {pull_quote("Cada decisión. Por escrito", "400px")}
    </div>
  </div>
  <!-- Data strip spans both columns -->
  <div style="grid-column:1/-1;align-self:end;">
    {data_block([
        ("Fundado", "2026"),
        ("Ubicación", "España"),
        ("Formato", "Remoto"),
        ("Especialidad", "Sistemas de marca completos"),
    ])}
  </div>
</div>"""
    return page_shell(body, 8, section="II · Fundamentos", bg=PAPEL)


def p09_values():
    """Values — 3 values in grid."""
    vals = [
        ("01", "Claridad", "Cada decisión tiene una razón. Si no la tiene, sobra. No añadimos nada que no podamos justificar en una frase."),
        ("02", "Honestidad", "Decimos lo que pensamos. Si tu marca tiene un problema, lo señalamos. No cobramos por decirte lo que quieres oír."),
        ("03", "Rigor", "Cada página del manual pasa por el mismo estándar. No hay páginas de relleno. No hay secciones vacías. Todo tiene peso."),
    ]

    cards = ""
    for num, name, desc in vals:
        cards += f"""\
<div style="border-top:3px solid {LACRE};padding-top:8mm;">
  <div style="font-family:{MONO};font-size:10px;font-weight:700;
    color:{LACRE};margin-bottom:4mm;">{num}</div>
  <div style="font-family:{FAM};font-size:22px;font-weight:900;
    color:{NEGRO};margin-bottom:6mm;">{name}<span style="color:{LACRE};font-size:26px;">.</span></div>
  <div class="body-text">{desc}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;">
  {titulo("Valores", 38)}
</div>
<div style="position:absolute;left:24mm;top:62mm;right:24mm;bottom:20mm;">
  <div class="g3" style="height:100%;align-content:start;">
    {cards}
  </div>
</div>"""
    return page_shell(body, 9, section="II · Fundamentos", bg=PAPEL)


def p10_positioning():
    """Positioning — what we are / what we are not + scatter plot."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.2fr 1fr;gap:16mm;">
  <!-- Left: positioning text -->
  <div>
    {titulo("Posicionamiento", 38)}
    <div class="body-text" style="margin-bottom:8mm;">
      Tramarca produce sistemas de marca completos — no logos sueltos,
      no slides de branding, no PDFs de tres páginas. Un documento que
      cubre identidad visual, voz, personalidad, assets y reglas de uso.
    </div>
    <div style="margin-bottom:6mm;">
      <div class="eyebrow" style="margin-bottom:4mm;">Lo que no somos</div>
      <div style="font-family:{FAM};font-size:15px;font-weight:500;color:{PIEDRA};line-height:2;">
        <span class="struck" style="font-size:15px;">Una agencia creativa</span><br>
        <span class="struck" style="font-size:15px;">Un freelance que hace logos</span><br>
        <span class="struck" style="font-size:15px;">Un estudio de diseño generalista</span>
      </div>
    </div>
    {pull_quote("No somos una agencia. No somos un freelance. Somos un sistema", "300px")}
  </div>
  <!-- Right: positioning scatter plot -->
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <div style="position:relative;width:100%;aspect-ratio:1/1;
      border-left:1px solid {CENIZA};border-bottom:1px solid {CENIZA};">
      <!-- Axes labels -->
      <div style="position:absolute;bottom:-8mm;left:50%;transform:translateX(-50%);
        font-family:{MONO};font-size:7px;color:{PIEDRA};letter-spacing:1px;text-transform:uppercase;">
        Sistema completo →
      </div>
      <div style="position:absolute;left:-2mm;top:50%;transform:rotate(-90deg) translateX(-50%);transform-origin:0 0;
        font-family:{MONO};font-size:7px;color:{PIEDRA};letter-spacing:1px;text-transform:uppercase;">
        A medida →
      </div>
      <!-- Competitor dots -->
      <div style="position:absolute;left:15%;bottom:20%;width:8px;height:8px;border-radius:50%;background:{CENIZA};" title="Fiverr"></div>
      <div style="position:absolute;left:20%;bottom:55%;width:8px;height:8px;border-radius:50%;background:{CENIZA};" title="Freelance"></div>
      <div style="position:absolute;left:60%;bottom:70%;width:8px;height:8px;border-radius:50%;background:{CENIZA};" title="Estudio boutique"></div>
      <div style="position:absolute;left:70%;bottom:40%;width:8px;height:8px;border-radius:50%;background:{CENIZA};" title="Agencia grande"></div>
      <!-- Tramarca — top-right -->
      <div style="position:absolute;left:82%;bottom:85%;width:14px;height:14px;border-radius:50%;
        background:{LACRE};box-shadow:0 0 0 4px rgba(196,85,58,0.25);"></div>
      <!-- Labels -->
      <div style="position:absolute;left:15%;bottom:12%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Fiverr</div>
      <div style="position:absolute;left:20%;bottom:47%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Freelance</div>
      <div style="position:absolute;left:48%;bottom:72%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Estudio boutique</div>
      <div style="position:absolute;left:58%;bottom:32%;font-family:{MONO};font-size:7px;color:{PIEDRA};">Agencia grande</div>
      <div style="position:absolute;left:72%;bottom:88%;font-family:{FAM};font-size:9px;font-weight:700;color:{LACRE};">TRAMARCA.</div>
    </div>
  </div>
</div>"""
    return page_shell(body, 10, section="II · Fundamentos", bg=PAPEL)


def p11_audience():
    """Target audience — who we serve."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1fr 1fr;gap:16mm;align-content:start;">
  <div style="grid-column:1/-1;">
    {titulo("Audiencia", 38)}
  </div>
  <div>
    <div class="eyebrow" style="margin-bottom:4mm;">Perfil principal</div>
    <div style="font-family:{FAM};font-size:18px;font-weight:700;
      color:{NEGRO};line-height:1.4;margin-bottom:6mm;">
      Fundadores y directores de empresas pequeñas y medianas
      que saben que necesitan orden en su marca<span style="color:{LACRE};font-size:22px;">.</span>
    </div>
    <div class="body-text">
      No buscan un logo. Ya tienen uno. Buscan el sistema que les falta:
      las reglas, los assets, el documento que dice qué sí y qué no.
      Están cansados de improvisar.
    </div>
  </div>
  <div>
    <div class="eyebrow" style="margin-bottom:4mm;">Señales de compra</div>
    <div style="display:flex;flex-direction:column;gap:4mm;">
      <div style="border-left:3px solid {LACRE};padding-left:12px;">
        <div class="body-text">"Tenemos logo pero cada vez que alguien lo usa sale distinto."</div>
      </div>
      <div style="border-left:3px solid {LACRE};padding-left:12px;">
        <div class="body-text">"Necesitamos un manual de marca pero no sabemos por dónde empezar."</div>
      </div>
      <div style="border-left:3px solid {LACRE};padding-left:12px;">
        <div class="body-text">"Queremos parecer profesionales, no improvisados."</div>
      </div>
    </div>
  </div>
  <!-- Data strip -->
  <div style="grid-column:1/-1;margin-top:4mm;">
    {data_block([
        ("Sector", "Multisector — servicios profesionales, hostelería, moda, tech"),
        ("Tamaño", "1–50 empleados"),
        ("Decisor", "CEO / Fundador / Director de marketing"),
        ("Presupuesto", "Inversión media: 1.500–4.500 €"),
    ])}
  </div>
</div>"""
    return page_shell(body, 11, section="II · Fundamentos", bg=PAPEL)


def p12_personality():
    """Brand personality — 5 adjectives + golden rule."""
    adjs = [
        ("Directo", "Dice lo que piensa. Sin rodeos, sin matices innecesarios."),
        ("Provocador", "Cuestiona lo que el mercado da por sentado."),
        ("Seguro", "No pide permiso. No se disculpa."),
        ("Preciso", "Cada palabra elegida. Nada sobra."),
        ("Cercano", 'Usa "tú". Habla de igual a igual.'),
    ]

    items = ""
    for i, (adj, desc) in enumerate(adjs, 1):
        items += f"""\
<div style="border-top:2px solid {LACRE if i == 1 else CENIZA};padding-top:5mm;">
  <div style="display:flex;gap:4mm;align-items:baseline;margin-bottom:3mm;">
    <span style="font-family:{MONO};font-size:10px;font-weight:700;color:{LACRE};">0{i}</span>
    <span style="font-family:{FAM};font-size:18px;font-weight:900;color:{NEGRO};">{adj}<span style="color:{LACRE};">.</span></span>
  </div>
  <div class="body-text">{desc}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.4fr 1fr;gap:16mm;">
  <div>
    {titulo("Personalidad", 38)}
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm 12mm;margin-top:2mm;">
      {items}
    </div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <div style="background:{ARENA};padding:24px 28px;">
      <div class="eyebrow" style="margin-bottom:8mm;">Regla de oro</div>
      <div style="font-family:{FAM};font-size:22px;font-weight:700;
        color:{NEGRO};line-height:1.35;">
        Tramarca no convence<span style="color:{LACRE};font-size:26px;">.</span>
        Tramarca señala lo que ya sabes
        pero no quieres admitir<span style="color:{LACRE};font-size:26px;">.</span>
      </div>
      {accent_rule(60, "10mm")}
      <div class="meta" style="margin-top:6mm;">
        Si suena duro, es que va bien. Si suena corporativo, hay que reescribir.
      </div>
    </div>
  </div>
</div>"""
    return page_shell(body, 12, section="II · Fundamentos", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# 03 SERVICIO  (pp. 13-16)
# ══════════════════════════════════════════════════════════════

def p13_servicio():
    """Section divider — Servicio."""
    return divider("03", "III", "Servicio",
                   "Qué entregamos. Cómo trabajamos.", pg=13)


def p14_whats_included():
    """What a brand system includes — 4-item grid."""
    items = [
        ("Identidad visual",
         "Logotipo, paleta, tipografía, iconografía.",
         "No solo qué es, sino cómo se usa y cómo no."),
        ("Voz y personalidad",
         "Tono, vocabulario, ejemplos reales.",
         "Para que tu marca suene igual la escriba quien la escriba."),
        ("Assets listos para usar",
         "Archivos en todos los formatos.",
         "Plantillas, firmas de email, aplicaciones reales."),
        ("Reglas de uso",
         "Espacios, tamaños mínimos, fondos.",
         "Combinaciones permitidas y prohibidas. Sin ambigüedad."),
    ]

    cards = ""
    for i, (cat, what, why) in enumerate(items):
        cards += f"""\
<div style="border-top:2px solid {LACRE if i == 0 else CENIZA};padding-top:5mm;">
  <div class="eyebrow" style="margin-bottom:3mm;">{cat}</div>
  <div style="font-family:{FAM};font-size:15px;font-weight:700;
    color:{NEGRO};line-height:1.4;margin-bottom:3mm;">{what}</div>
  <div class="body-text" style="font-size:12px;">{why}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1fr 1fr;gap:10mm;align-content:start;">
  <div style="grid-column:1/-1;">
    {titulo("Lo que incluye un sistema de marca", 36)}
  </div>
  {cards}
  <div style="grid-column:1/-1;margin-top:4mm;">
    {pull_quote("Todo en un documento. Página a página. Decisión a decisión", "100%")}
  </div>
</div>"""
    return page_shell(body, 14, section="III · Servicio", bg=PAPEL)


def p15_process():
    """Process timeline — 4 steps with connecting line."""
    steps = [
        ("01", "1–2 días", "Brief",
         "Conversación inicial. Entendemos dónde está tu marca ahora y qué necesita."),
        ("02", "10–15 días", "Producción",
         "Construimos el sistema completo. Sin reuniones intermedias innecesarias."),
        ("03", "3–5 días", "Revisión",
         "Presentamos. Dos rondas de revisión incluidas en todos los planes."),
        ("04", "Día final", "Entrega",
         "Manual final en PDF + assets en todos los formatos. Listo para usar."),
    ]

    timeline = ""
    for i, (num, timing, name, desc) in enumerate(steps):
        timeline += f"""\
<div style="display:grid;grid-template-columns:36px 1fr;gap:5mm;
  {'padding-top:6mm;' if i > 0 else ''}">
  <div style="display:flex;flex-direction:column;align-items:center;">
    <div style="width:32px;height:32px;border-radius:50%;background:{LACRE};
      display:flex;align-items:center;justify-content:center;flex-shrink:0;">
      <span style="font-family:{MONO};font-size:11px;font-weight:700;color:{PAPEL};">{num}</span>
    </div>
    {'<div style="flex:1;width:1px;background:%s;margin-top:3mm;"></div>' % CENIZA if i < 3 else ''}
  </div>
  <div>
    <div style="display:flex;align-items:baseline;gap:4mm;margin-bottom:2mm;">
      <span style="font-family:{FAM};font-size:18px;font-weight:900;color:{NEGRO};">{name}<span style="color:{LACRE};">.</span></span>
      <span class="meta">{timing}</span>
    </div>
    <div class="body-text">{desc}</div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.3fr 1fr;gap:20mm;align-content:start;">
  <div>
    {titulo("Proceso", 42)}
    <div style="margin-top:4mm;">
      {timeline}
    </div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;gap:10mm;">
    <div style="background:{ARENA};padding:24px 28px;">
      <div class="eyebrow" style="margin-bottom:6mm;">Sin sorpresas</div>
      <div style="font-family:{FAM};font-size:20px;font-weight:700;
        color:{NEGRO};line-height:1.35;">
        Sabes qué recibes, cuándo lo recibes
        y cuánto cuesta<span style="color:{LACRE};font-size:24px;">.</span>
        Antes de empezar<span style="color:{LACRE};font-size:24px;">.</span>
      </div>
    </div>
    {data_block([
        ("Formato", "PDF interactivo + assets originales"),
        ("Revisiones", "2 rondas incluidas"),
        ("Soporte", "30 días post-entrega"),
    ])}
  </div>
</div>"""
    return page_shell(body, 15, section="III · Servicio", bg=PAPEL)


def p16_scope_tiers():
    """Scope tiers — 3 columns (Esencial / Profesional / Premium)."""
    tiers = [
        ("Esencial", "25–30 páginas",
         ["Logotipo + variaciones", "Paleta de color", "Tipografía",
          "Reglas de uso básicas", "Assets en formatos estándar"],
         "Para marcas nuevas que necesitan partir con sistema."),
        ("Profesional", "35–45 páginas",
         ["Todo lo de Esencial +", "Voz y personalidad", "Vocabulario de marca",
          "Aplicaciones principales", "Plantillas editables"],
         "Para marcas en crecimiento que necesitan coherencia."),
        ("Premium", "50+ páginas",
         ["Todo lo de Profesional +", "Dirección de arte", "Portfolio de aplicaciones",
          "Mockups y contextos de uso", "Iconografía personalizada"],
         "Para marcas que exigen el estándar más alto."),
    ]

    cols = ""
    for i, (name, pages, features, desc) in enumerate(tiers):
        is_pro = (i == 1)
        bg = NEGRO if is_pro else "transparent"
        tc = PAPEL if is_pro else NEGRO
        mc = CENIZA if is_pro else PIEDRA
        border = f"border-top:3px solid {LACRE};" if is_pro else f"border-top:1px solid {CENIZA};"
        feat_html = "".join(
            f'<div style="font-family:{MONO};font-size:9px;color:{mc};'
            f'padding:3px 0;border-bottom:0.5px solid {"rgba(244,240,235,0.1)" if is_pro else ARENA};">{f}</div>'
            for f in features
        )
        cols += f"""\
<div style="background:{bg};color:{tc};padding:20px 22px;{border}">
  <div style="font-family:{FAM};font-size:22px;font-weight:900;
    margin-bottom:2mm;">{name}<span style="color:{LACRE};">.</span></div>
  <div class="meta" style="color:{mc};margin-bottom:5mm;">{pages}</div>
  <div style="margin-bottom:5mm;">{feat_html}</div>
  <div style="font-family:{FAM};font-size:11px;font-weight:400;
    color:{mc};line-height:1.5;">{desc}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:flex;flex-direction:column;gap:8mm;">
  {titulo("Alcance", 42)}
  <div class="g3" style="flex:1;">
    {cols}
  </div>
  <div style="display:flex;justify-content:space-between;align-items:baseline;">
    <div class="meta">Precios y presupuestos personalizados por proyecto.</div>
    <div class="meta">Todos los planes incluyen 2 rondas de revisión + 30 días de soporte.</div>
  </div>
</div>"""
    return page_shell(body, 16, section="III · Servicio", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# 04 IDENTIDAD VISUAL  (pp. 17-24)
# ══════════════════════════════════════════════════════════════

def p17_identidad():
    """Section divider — Identidad Visual."""
    return divider("04", "IV", "Identidad visual",
                   "Logo, construcción, versiones, usos.", pg=17)


def p18_logo_primary():
    """Logo primary — massive wordmark presentation."""
    body = f"""\
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;">
  <div style="text-align:center;">
    <!-- Watermark -->
    <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
      font-family:{FAM};font-size:320px;font-weight:900;color:rgba(12,12,12,0.03);
      letter-spacing:-8px;pointer-events:none;user-select:none;">{BRAND}</div>
    <!-- Primary wordmark -->
    <div style="font-family:{FAM};font-size:72px;font-weight:900;
      color:{NEGRO};letter-spacing:-2px;position:relative;">
      {BRAND}<span style="color:{LACRE};font-size:90px;position:relative;top:4px;">.</span>
    </div>
    <div style="font-family:{MONO};font-size:10px;color:{PIEDRA};
      letter-spacing:4px;margin-top:8mm;text-transform:uppercase;">{DESCRIPTOR}</div>
  </div>
</div>
<!-- Tech specs -->
<div style="position:absolute;right:24mm;top:30mm;">
  {data_block([
      ("Tipografía", "Satoshi Black (900)"),
      ("Concepto", "El Punto Final"),
      ("Elementos", "8 caracteres + punto"),
      ("Punto", "120% cap-height, Lacre"),
  ])}
</div>"""
    return page_shell(body, 18, section="IV · Identidad visual", bg=PAPEL)


def p19_logo_construction():
    """Logo construction grid with technical annotations."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;">
  {titulo("Construcción", 38)}
  <!-- Construction area with grid -->
  <div style="position:relative;width:100%;height:100mm;margin-top:6mm;
    background:
      repeating-linear-gradient(0deg, transparent, transparent 9.5mm, rgba(181,177,172,0.15) 9.5mm, rgba(181,177,172,0.15) 10mm),
      repeating-linear-gradient(90deg, transparent, transparent 9.5mm, rgba(181,177,172,0.15) 9.5mm, rgba(181,177,172,0.15) 10mm);
    border:0.5px solid {CENIZA};">
    <!-- Wordmark centered -->
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">
      <div style="position:relative;">
        <div style="font-family:{FAM};font-size:56px;font-weight:900;
          color:{NEGRO};letter-spacing:-1px;">
          {BRAND}<span style="color:{LACRE};font-size:67px;">.</span>
        </div>
        <!-- Cap-height line -->
        <div style="position:absolute;top:6px;left:-20mm;right:-20mm;
          border-top:0.5px dashed {LACRE};opacity:0.5;"></div>
        <!-- Baseline -->
        <div style="position:absolute;bottom:8px;left:-20mm;right:-20mm;
          border-top:0.5px dashed {LACRE};opacity:0.5;"></div>
        <!-- Clear space box -->
        <div style="position:absolute;top:-8mm;left:-8mm;right:-8mm;bottom:-8mm;
          border:0.5px dashed {CENIZA};"></div>
        <!-- X annotations -->
        <div style="position:absolute;top:-8mm;right:-8mm;
          font-family:{MONO};font-size:7px;color:{PIEDRA};transform:translate(50%,-100%);">X</div>
        <div style="position:absolute;bottom:-8mm;left:-8mm;
          font-family:{MONO};font-size:7px;color:{PIEDRA};transform:translate(-50%,100%);">X</div>
      </div>
    </div>
  </div>
  <!-- Annotations row -->
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8mm;margin-top:6mm;">
    <div>
      <div class="eyebrow" style="margin-bottom:2mm;">Área de respeto</div>
      <div class="meta">X = ancho del punto. Ningún elemento externo debe invadir esta zona.</div>
    </div>
    <div>
      <div class="eyebrow" style="margin-bottom:2mm;">El punto final</div>
      <div class="meta">El punto se renderiza al 120% de la cap-height. Es el elemento identitario central.</div>
    </div>
    <div>
      <div class="eyebrow" style="margin-bottom:2mm;">Tracking</div>
      <div class="meta">Letter-spacing: -2px en display (≥48px), -1px en cuerpo. Nunca positivo.</div>
    </div>
  </div>
</div>"""
    return page_shell(body, 19, section="IV · Identidad visual", bg=PAPEL)


def p20_clearspace():
    """Clear space and minimum sizes."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.2fr 1fr;gap:20mm;align-content:start;">
  <div>
    {titulo("Área de respeto", 36)}
    <div class="body-text" style="margin-bottom:8mm;">
      El espacio libre alrededor del logotipo garantiza legibilidad e impacto.
      Ningún elemento — texto, imagen, borde — puede entrar en esta zona.
    </div>
    <!-- Clear space demo -->
    <div style="position:relative;background:{ARENA};padding:20mm;display:inline-block;">
      <div style="border:1px dashed {CENIZA};padding:10mm 12mm;position:relative;">
        <div style="font-family:{FAM};font-size:32px;font-weight:900;color:{NEGRO};">
          {BRAND}<span style="color:{LACRE};font-size:38px;">.</span>
        </div>
        <!-- X markers -->
        <div style="position:absolute;top:1mm;left:50%;font-family:{MONO};font-size:7px;color:{LACRE};">X</div>
        <div style="position:absolute;bottom:1mm;left:50%;font-family:{MONO};font-size:7px;color:{LACRE};">X</div>
        <div style="position:absolute;left:1mm;top:50%;font-family:{MONO};font-size:7px;color:{LACRE};">X</div>
        <div style="position:absolute;right:1mm;top:50%;font-family:{MONO};font-size:7px;color:{LACRE};">X</div>
      </div>
    </div>
  </div>
  <div>
    <div class="eyebrow" style="margin-bottom:8mm;">Tamaños mínimos</div>
    <!-- Good size -->
    <div style="margin-bottom:8mm;padding-bottom:8mm;border-bottom:0.5px solid {CENIZA};">
      <div style="font-family:{FAM};font-size:24px;font-weight:900;color:{NEGRO};margin-bottom:2mm;">
        {BRAND}<span style="color:{LACRE};font-size:29px;">.</span>
      </div>
      <div class="meta">Digital: mínimo 80px de ancho · Impreso: mínimo 25mm <span style="color:{LACRE};">✓</span></div>
    </div>
    <!-- Too small -->
    <div style="margin-bottom:8mm;padding-bottom:8mm;border-bottom:0.5px solid {CENIZA};">
      <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{CENIZA};margin-bottom:2mm;">
        {BRAND}<span style="color:{CENIZA};">.</span>
      </div>
      <div class="meta">Por debajo de 60px / 18mm: usar monograma <span style="color:{LACRE};">✗</span></div>
    </div>
    <!-- Monogram -->
    <div style="margin-bottom:6mm;">
      <div style="font-family:{FAM};font-size:22px;font-weight:900;color:{NEGRO};margin-bottom:2mm;">
        Tm<span style="color:{LACRE};font-size:26px;">.</span>
      </div>
      <div class="meta">Monograma para avatares, favicons y tamaños reducidos <span style="color:{LACRE};">✓</span></div>
    </div>
    {accent_rule(60, "6mm")}
    <div class="meta" style="margin-top:4mm;">
      El punto siempre se mantiene en Lacre, independientemente del tamaño.
    </div>
  </div>
</div>"""
    return page_shell(body, 20, section="IV · Identidad visual", bg=PAPEL)


def p21_logo_dark():
    """Logo on dark backgrounds — split page Negro/Carbon."""
    body = f"""\
<!-- Top: Negro -->
<div style="position:absolute;top:0;left:0;right:0;height:50%;background:{NEGRO};
  display:flex;align-items:center;padding:0 30mm;">
  <div style="flex:1;">
    <div style="font-family:{FAM};font-size:42px;font-weight:900;color:{PAPEL};">
      {BRAND}<span style="color:{LACRE};font-size:50px;">.</span>
    </div>
  </div>
  <div>
    <div style="font-family:{FAM};font-size:26px;font-weight:900;color:{PAPEL};">
      Tm<span style="color:{LACRE};">.</span>
    </div>
  </div>
</div>
<!-- Bottom: Carbon -->
<div style="position:absolute;top:50%;left:0;right:0;height:50%;background:{CARBON};
  display:flex;align-items:center;padding:0 30mm;">
  <div style="flex:1;">
    <div style="font-family:{FAM};font-size:42px;font-weight:900;color:{PAPEL};">
      {BRAND}<span style="color:{LACRE};font-size:50px;">.</span>
    </div>
  </div>
  <div>
    <div style="font-family:{FAM};font-size:26px;font-weight:900;color:{PAPEL};">
      Tm<span style="color:{LACRE};">.</span>
    </div>
  </div>
</div>
<!-- Annotation strip -->
<div style="position:absolute;bottom:0;left:0;right:0;
  background:{NEGRO};padding:4mm 30mm;
  border-top:0.5px solid rgba(244,240,235,0.12);">
  <div style="display:flex;justify-content:space-between;">
    <div style="font-family:{MONO};font-size:8px;color:{CENIZA};">
      Sobre fondos oscuros: logotipo en Papel (#F4F0EB). El punto siempre en Lacre.
    </div>
    <div style="font-family:{MONO};font-size:8px;color:{PIEDRA};">
      Negro {NEGRO} · Carbón {CARBON}
    </div>
  </div>
</div>"""
    return page_shell(body, 21, bg=NEGRO, dark=True, no_furniture=True)


def p22_logo_versions():
    """Monochrome and special versions — 2x2 grid."""
    versions = [
        ("Positivo", PAPEL, NEGRO, LACRE, True),
        ("Negativo", NEGRO, PAPEL, LACRE, False),
        ("Monocromo", PAPEL, NEGRO, NEGRO, True),
        ("Monocromo invertido", NEGRO, PAPEL, PAPEL, False),
    ]

    grid = ""
    for label, bg, text, dot, border in versions:
        brd = f"border:1px solid {CENIZA};" if border else ""
        grid += f"""\
<div>
  <div style="background:{bg};{brd}height:55mm;
    display:flex;align-items:center;justify-content:center;">
    <div style="font-family:{FAM};font-size:32px;font-weight:900;color:{text};">
      {BRAND}<span style="color:{dot};font-size:38px;">.</span>
    </div>
  </div>
  <div class="eyebrow" style="margin-top:3mm;">{label}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;">
  {titulo("Versiones", 38)}
  <div class="g2" style="margin-top:6mm;">
    {grid}
  </div>
  <div style="margin-top:6mm;">
    {data_block([
        ("Preferencia", "Positivo con punto Lacre (uso principal)"),
        ("Monocromo", "Solo cuando la impresión a color no es posible"),
        ("Regla", "El punto se mantiene en Lacre siempre que sea técnicamente posible"),
    ])}
  </div>
</div>"""
    return page_shell(body, 22, section="IV · Identidad visual", bg=PAPEL)


def p23_logo_forbidden():
    """Forbidden logo uses — 6 violations in 3x2 grid."""
    violations = [
        ("No rotar", "transform:rotate(15deg);", LACRE),
        ("No cambiar color del punto", "", "#3366CC"),
        ("No usar sombras", "filter:drop-shadow(3px 3px 4px rgba(0,0,0,0.4));", LACRE),
        ("No deformar", "transform:scaleX(1.4);", LACRE),
        ("No usar sobre fondos complejos", "", LACRE),
        ("No eliminar el punto", "", None),
    ]

    grid = ""
    for i, (caption, style, dot_color) in enumerate(violations):
        if i == 4:  # busy background
            bg_css = f"background:repeating-linear-gradient(45deg,{ARENA},{ARENA} 4px,{CENIZA} 4px,{CENIZA} 8px);"
        else:
            bg_css = f"background:{PAPEL};border:1px solid {CENIZA};"

        mark_text = "TRAMARCA" if dot_color is None else f'{BRAND}<span style="color:{dot_color};font-size:24px;">.</span>'

        grid += f"""\
<div>
  <div style="{bg_css}height:40mm;display:flex;align-items:center;justify-content:center;position:relative;">
    <div style="font-family:{FAM};font-size:20px;font-weight:900;color:{NEGRO};{style}">
      {mark_text}
    </div>
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
      font-family:{FAM};font-size:52px;font-weight:900;color:rgba(196,85,58,0.25);">✗</div>
  </div>
  <div class="meta" style="margin-top:2mm;">{caption}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;">
  {titulo("Usos incorrectos", 38)}
  <div class="g3" style="margin-top:4mm;row-gap:6mm;">
    {grid}
  </div>
</div>"""
    return page_shell(body, 23, section="IV · Identidad visual", bg=PAPEL)


def p24_logo_context():
    """Logo in context — 3 mockups + image."""
    contexts = [
        ("Tarjeta de visita", "Logo invertido sobre fondo oscuro",
         NEGRO, PAPEL, False),
        ("Cabecera de documento", "Logo estándar sobre fondo claro",
         PAPEL, NEGRO, True),
        ("Avatar redes sociales", "Monograma Tm. en círculo",
         NEGRO, PAPEL, False),
    ]

    slots = ""
    for i, (title, desc, bg, fg, border) in enumerate(contexts):
        brd = f"border:1px solid {CENIZA};" if border else ""
        if i == 2:  # monogram avatar
            logo = f"""\
<div style="width:32mm;height:32mm;border-radius:50%;background:{bg};
  display:flex;align-items:center;justify-content:center;">
  <span style="font-family:{FAM};font-size:18px;font-weight:900;color:{fg};">Tm<span style="color:{LACRE};">.</span></span>
</div>"""
        else:
            logo = f'<div style="font-family:{FAM};font-size:20px;font-weight:900;color:{fg};">{BRAND}<span style="color:{LACRE};font-size:24px;">.</span></div>'

        slots += f"""\
<div>
  <div style="background:{bg};{brd}height:50mm;
    display:flex;align-items:center;justify-content:center;">{logo}</div>
  <div style="margin-top:3mm;">
    <div style="font-family:{FAM};font-size:12px;font-weight:700;color:{NEGRO};margin-bottom:1mm;">{title}</div>
    <div class="meta">{desc}</div>
  </div>
</div>"""

    # Fourth slot: image
    slots += f"""\
<div>
  <div class="photo" style="height:50mm;">
    <img src="assets/img-04.jpg" alt="">
  </div>
  <div style="margin-top:3mm;">
    <div style="font-family:{FAM};font-size:12px;font-weight:700;color:{NEGRO};margin-bottom:1mm;">En contexto</div>
    <div class="meta">Aplicación real sobre material</div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;">
  {titulo("Logo en contexto", 38)}
  <div class="g4" style="margin-top:6mm;">
    {slots}
  </div>
  <div style="margin-top:6mm;">
    {pull_quote("El logo no decora. El logo certifica", "100%")}
  </div>
</div>"""
    return page_shell(body, 24, section="IV · Identidad visual", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# 05 PALETA DE COLOR  (pp. 25-28)
# ══════════════════════════════════════════════════════════════

def p25_color():
    """Section divider — Paleta de Color."""
    return divider("05", "V", "Paleta de color",
                   "7 colores. Una sola regla: el acento es uno.", pg=25)


def p26_color_system():
    """Color system — 7 swatches strip + role explanation."""
    colors = [
        ("Negro",  NEGRO,  "Dominante oscuro. Texto, fondos, autoridad."),
        ("Carbón", CARBON, "Secundario oscuro. Fondos alternativos."),
        ("Lacre",  LACRE,  "Único acento. El punto, la barra, la marca."),
        ("Piedra", PIEDRA, "Texto secundario. Metadata, captions."),
        ("Ceniza", CENIZA, "Bordes, separadores, elementos UI."),
        ("Arena",  ARENA,  "Fondos cálidos. Paneles de contenido."),
        ("Papel",  PAPEL,  "Fondo principal. Espacio, aire, respiro."),
    ]

    swatches = ""
    for name, hex_val, role in colors:
        tc = PAPEL if hex_val in [NEGRO, CARBON, LACRE, PIEDRA] else NEGRO
        border = f"border:1px solid {CENIZA};" if hex_val == PAPEL else ""
        swatches += f"""\
<div style="background:{hex_val};{border}padding:14px 16px;display:flex;flex-direction:column;justify-content:space-between;">
  <div style="font-family:{FAM};font-size:13px;font-weight:700;color:{tc};">{name}</div>
  <div>
    <div style="font-family:{MONO};font-size:8px;color:{tc};opacity:0.7;">{hex_val}</div>
    <div style="font-family:{FAM};font-size:9px;color:{tc};opacity:0.7;margin-top:2px;">{role}</div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:flex;flex-direction:column;gap:6mm;">
  {titulo("Sistema de color", 42)}
  <div class="body-text" style="margin-bottom:2mm;">
    Negro y Papel son los dominantes. Lacre es el único acento.
    Todo lo demás es neutro. Sin excepciones.
  </div>
  <!-- Color strip -->
  <div style="display:grid;grid-template-columns:1fr 1fr 0.7fr 1fr 1fr 1fr 1fr;gap:2px;flex:1;">
    {swatches}
  </div>
  {pull_quote("Cuando todo es acento, nada destaca. Por eso Lacre es uno", "100%")}
</div>"""
    return page_shell(body, 26, section="V · Paleta de color", bg=PAPEL)


def p27_color_combos():
    """Color combinations with WCAG ratios — 3x2 grid."""
    combos = [
        ("Principal oscuro",    NEGRO, PAPEL,  LACRE, "15.4:1"),
        ("Principal claro",     PAPEL, NEGRO,  LACRE, "15.4:1"),
        ("Secundario cálido",   ARENA, CARBON, None,  "10.7:1"),
        ("Secundario oscuro",   CARBON, CENIZA, LACRE, "6.2:1"),
        ("Acento sobre oscuro", NEGRO, LACRE,  None,  "4.6:1"),
        ("Acento sobre claro",  PAPEL, LACRE,  None,  "4.3:1"),
    ]

    grid = ""
    for label, bg, fg, accent, ratio in combos:
        border = f"border:1px solid {CENIZA};" if bg in [PAPEL, ARENA] else ""
        dot = f'<span style="color:{accent};">.</span>' if accent else ""
        grid += f"""\
<div>
  <div style="background:{bg};{border}height:38mm;
    display:flex;align-items:center;justify-content:center;">
    <span style="font-family:{FAM};font-size:16px;font-weight:700;color:{fg};">Aa{dot}</span>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:2mm;">
    <span style="font-family:{FAM};font-size:10px;font-weight:500;color:{NEGRO};">{label}</span>
    <span class="meta">{ratio}</span>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;">
  {titulo("Combinaciones", 38)}
  <div class="body-text" style="margin-bottom:6mm;">
    Todas las combinaciones principales superan WCAG AA (4.5:1) para texto normal.
  </div>
  <div class="g3" style="row-gap:8mm;">
    {grid}
  </div>
</div>"""
    return page_shell(body, 27, section="V · Paleta de color", bg=PAPEL)


def p28_color_donts():
    """Incorrect color uses — 2x2 grid."""
    donts = [
        ("Lacre como fondo",
         f"background:{LACRE};", f"color:{PAPEL};",
         "Demasiado acento. Lacre es un detalle, no un fondo."),
        ("Piedra sobre Arena",
         f"background:{ARENA};", f"color:{PIEDRA};",
         "Contraste insuficiente. No supera WCAG AA."),
        ("Múltiples acentos",
         f"background:{PAPEL};border:1px solid {CENIZA};", f"color:{NEGRO};",
         "Solo Lacre. Nunca azul, verde ni otro color."),
        ("Degradados",
         f"background:linear-gradient(135deg,{NEGRO},{LACRE});", f"color:{PAPEL};",
         "Sin degradados. Colores planos siempre."),
    ]

    grid = ""
    for i, (title, bg_css, fg_css, caption) in enumerate(donts):
        inner = f'{BRAND}<span style="color:{LACRE};font-size:18px;">.</span>'
        if "Múltiples" in title:
            inner = f'{BRAND}<span style="color:#2E6DB4;">.</span><span style="color:#4CAF50;margin-left:2px;">●</span>'
        grid += f"""\
<div>
  <div style="{bg_css}{fg_css}height:42mm;display:flex;align-items:center;justify-content:center;position:relative;">
    <span style="font-family:{FAM};font-size:15px;font-weight:900;">{inner}</span>
    <div style="position:absolute;top:3mm;right:4mm;font-family:{FAM};font-size:20px;font-weight:900;color:{LACRE};opacity:0.8;">✗</div>
  </div>
  <div style="margin-top:2mm;">
    <div style="font-family:{FAM};font-size:10px;font-weight:700;color:{NEGRO};margin-bottom:1mm;">{title}</div>
    <div class="meta">{caption}</div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;">
  {titulo("Usos incorrectos", 38)}
  <div class="g2" style="margin-top:4mm;row-gap:8mm;">
    {grid}
  </div>
  <div style="margin-top:6mm;">
    {data_block([
        ("Regla", "Lacre es acento, nunca fondo ni dominante"),
        ("Contraste", "Mínimo WCAG AA (4.5:1) para todo texto"),
        ("Degradados", "Prohibidos. Colores planos siempre"),
    ])}
  </div>
</div>"""
    return page_shell(body, 28, section="V · Paleta de color", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# 06 TIPOGRAFÍA  (pp. 29-32)
# ══════════════════════════════════════════════════════════════

def p29_tipografia():
    """Section divider — Tipografía."""
    return divider("06", "VI", "Tipografía",
                   "Dos familias. Roles claros.", pg=29)


def p30_specimen_satoshi():
    """Type specimen — Satoshi."""
    phrase = "Lo que no se documenta, se improvisa."
    weights = [("Regular 400", 400), ("Medium 500", 500),
               ("Bold 700", 700), ("Black 900", 900)]

    ramp = ""
    for label, w in weights:
        ramp += f"""\
<div style="margin-bottom:4mm;">
  <div class="meta" style="margin-bottom:1mm;">{label}</div>
  <div style="font-family:{FAM};font-size:14px;font-weight:{w};color:{NEGRO};">{phrase}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.6fr 1fr;gap:20mm;">
  <div>
    <!-- Large name -->
    <div style="font-family:{FAM};font-size:64px;font-weight:900;
      color:{NEGRO};line-height:1;margin-bottom:8mm;">Satoshi</div>
    <!-- Alphabet -->
    <div style="font-family:{FAM};font-size:18px;font-weight:400;
      color:{CARBON};letter-spacing:2px;line-height:1.6;margin-bottom:8mm;">
      A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z<br>
      a b c d e f g h i j k l m n ñ o p q r s t u v w x y z<br>
      0 1 2 3 4 5 6 7 8 9
    </div>
    <!-- Weight ramp -->
    {ramp}
  </div>
  <div>
    {data_block([
        ("Source", "Fontshare (Indian Type Foundry)"),
        ("Clase", "Geometric sans-serif"),
        ("Uso", "Títulos, cuerpo, UI, todo"),
        ("Pesos", "400 · 500 · 700 · 900"),
    ])}
    <div style="margin-top:8mm;background:{ARENA};padding:18px 22px;">
      <div class="eyebrow" style="margin-bottom:4mm;">Por qué Satoshi</div>
      <div class="body-text" style="font-size:12px;">
        Geométrica sin ser fría. Legible en cuerpo,
        contundente en display. Un solo tipo que cubre
        toda la jerarquía sin recurrir a una segunda sans.
      </div>
    </div>
  </div>
</div>"""
    return page_shell(body, 30, section="VI · Tipografía", bg=PAPEL)


def p31_specimen_plex():
    """Type specimen — IBM Plex Mono."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.6fr 1fr;gap:20mm;">
  <div>
    <div style="font-family:{MONO};font-size:42px;font-weight:700;
      color:{NEGRO};line-height:1;margin-bottom:8mm;">IBM Plex Mono</div>
    <!-- Character set -->
    <div style="font-family:{MONO};font-size:15px;font-weight:400;
      color:{CARBON};letter-spacing:1px;line-height:1.7;margin-bottom:8mm;">
      A B C D E F G H I J K L M<br>
      N Ñ O P Q R S T U V W X Y Z<br>
      0 1 2 3 4 5 6 7 8 9<br>
      ! @ # $ % &amp; * ( ) — . , : ;
    </div>
    <!-- Weight comparison -->
    <div style="margin-bottom:4mm;">
      <div class="meta" style="margin-bottom:1mm;">Regular 400</div>
      <div style="font-family:{MONO};font-size:14px;font-weight:400;color:{NEGRO};">Tu marca, sin improvisar.</div>
    </div>
    <div style="margin-bottom:6mm;">
      <div class="meta" style="margin-bottom:1mm;">Bold 700</div>
      <div style="font-family:{MONO};font-size:14px;font-weight:700;color:{NEGRO};">Tu marca, sin improvisar.</div>
    </div>
    <!-- Usage example -->
    <div class="eyebrow" style="margin-bottom:3mm;">Ejemplo de uso</div>
    {data_block([
        ("Edición", "Primera edición"),
        ("Fecha", "Abril 2026"),
        ("Páginas", "51"),
        ("Formato", "A4 apaisado"),
    ])}
  </div>
  <div>
    {data_block([
        ("Source", "Google Fonts (IBM)"),
        ("Clase", "Monospaced"),
        ("Uso", "Metadata, specs, eyebrows, data"),
        ("Pesos", "400 · 700"),
    ])}
    <div style="margin-top:8mm;background:{ARENA};padding:18px 22px;">
      <div class="eyebrow" style="margin-bottom:4mm;">Por qué Plex Mono</div>
      <div class="body-text" style="font-size:12px;">
        Aporta precisión técnica sin competir con Satoshi.
        Su ancho fijo crea alineación vertical natural en
        tablas de datos y especificaciones.
      </div>
    </div>
  </div>
</div>"""
    return page_shell(body, 31, section="VI · Tipografía", bg=PAPEL)


def p32_type_hierarchy():
    """Type hierarchy demonstration + rules."""
    levels = [
        ("Eyebrow", f"{MONO}, 8px, 700", "letter-spacing:3px;text-transform:uppercase;",
         f'<div class="eyebrow">V · PALETA DE COLOR</div>'),
        ("Título", f"{FAM}, 42px, 900", "",
         f'<div style="font-family:{FAM};font-size:32px;font-weight:900;color:{NEGRO};">Sistema de color<span style="color:{LACRE};">.</span></div>'),
        ("Subtítulo", f"{FAM}, 22px, 700", "",
         f'<div style="font-family:{FAM};font-size:20px;font-weight:700;color:{NEGRO};">Combinaciones</div>'),
        ("Cuerpo", f"{FAM}, 13px, 400", "",
         f'<div class="body-text">Negro y Papel son los dominantes. Lacre es el único acento.</div>'),
        ("Metadata", f"{MONO}, 9px, 400", "",
         f'<div class="meta">EDICIÓN — Primera edición · Abril 2026</div>'),
    ]

    demo = ""
    for name, spec, _, example in levels:
        demo += f"""\
<div style="padding:4mm 0;border-bottom:0.5px solid {CENIZA};">
  <div class="meta" style="margin-bottom:2mm;color:{PIEDRA};">{name} — {spec}</div>
  {example}
</div>"""

    rules = [
        "Satoshi 900 solo para títulos principales.",
        "IBM Plex Mono solo por debajo de 11px.",
        "Sin cursivas. Nunca.",
        "Énfasis con peso (700) o color (Lacre).",
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
  <div>
    {titulo("Jerarquía tipográfica", 36)}
    {demo}
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <div style="background:{ARENA};padding:24px 28px;">
      <div class="eyebrow" style="margin-bottom:6mm;">Reglas</div>
      {rules_html}
    </div>
    {accent_rule(60, "8mm")}
    <div class="meta" style="margin-top:4mm;">
      Dos familias. Roles claros. Sin excepciones.
    </div>
  </div>
</div>"""
    return page_shell(body, 32, section="VI · Tipografía", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# 07 VOZ Y PERSONALIDAD  (pp. 33-37)
# ══════════════════════════════════════════════════════════════

def p33_voz():
    """Section divider — Voz y personalidad."""
    return divider("07", "VII", "Voz y personalidad",
                   "Cómo habla Tramarca.", pg=33)


def p34_voice_principles():
    """5 voice principles with numbered list + pull quote."""
    principles = [
        ("Frases cortas. Una idea por frase.",
         '"Producimos manuales de marca." No: "Nos dedicamos a la producción integral de sistemas de identidad visual."'),
        ("Punto final siempre. No puntos suspensivos.",
         '"Tu marca necesita reglas." No: "Tu marca necesita reglas..."'),
        ("Preguntas retóricas que incomodan.",
         '"¿Tu equipo sabe qué colores usar? ¿Seguro?"'),
        ("Nunca exclamaciones. La convicción no necesita volumen.",
         '"Funciona." No: "¡Funciona increíblemente bien!"'),
        ('Tuteo siempre. "Tu marca", nunca "su marca".',
         '"¿Qué hay tras tu marca?" No: "¿Qué hay tras su marca?"'),
    ]

    items = ""
    for i, (principle, example) in enumerate(principles, 1):
        items += f"""\
<div style="margin-bottom:6mm;padding-bottom:6mm;border-bottom:0.5px solid {CENIZA};">
  <div style="display:flex;gap:3mm;align-items:baseline;margin-bottom:2mm;">
    <span style="font-family:{MONO};font-size:12px;font-weight:700;color:{LACRE};">{i:02d}</span>
    <span style="font-family:{FAM};font-size:14px;font-weight:700;color:{NEGRO};">{principle}</span>
  </div>
  <div style="margin-left:9mm;font-family:{FAM};font-size:12px;font-weight:400;
    color:{CARBON};line-height:1.6;">{example}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.4fr 1fr;gap:20mm;">
  <div>
    {titulo("Principios de voz", 38)}
    {items}
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;">
    {pull_quote("Si suena corporativo, reescríbelo. Si suena a todo el mundo, reescríbelo. Si suena a Tramarca, punto final", "100%")}
    {accent_rule(60, "10mm")}
  </div>
</div>"""
    return page_shell(body, 34, section="VII · Voz y personalidad", bg=PAPEL)


def p35_vocabulary():
    """Vocabulary — words we use vs. never use."""
    use_words = ["documentar", "por escrito", "reglas", "decisión", "sistema",
                 "construir", "producir", "cada página", "claro", "directo",
                 "manual", "identidad", "profesional"]
    never_words = ["branding 360", "holístico", "sinergia", "storytelling",
                   "disruptivo", "hacer magia", "conceptualizar", "co-crear",
                   "universo de marca", "lovemark"]

    use_html = "".join(
        f'<div style="padding:3mm 0;border-bottom:0.5px solid {CENIZA};'
        f'font-family:{FAM};font-size:14px;font-weight:500;color:{NEGRO};">{w}</div>'
        for w in use_words
    )
    never_html = "".join(
        f'<div class="struck" style="padding:3mm 0;border-bottom:0.5px solid {CENIZA};'
        f'font-family:{FAM};font-size:14px;font-weight:500;">{w}</div>'
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
    <div class="titulo" style="font-size:38px;color:{PIEDRA};margin-bottom:10mm;letter-spacing:0px;">
      Nunca usamos<span class="p" style="font-size:45px;">.</span>
    </div>
    {never_html}
  </div>
</div>
<div style="position:absolute;bottom:16mm;left:24mm;">
  <div class="meta">Si una frase necesita más de 15 palabras, reescríbela.</div>
</div>"""
    return page_shell(body, 35, section="VII · Voz y personalidad", bg=PAPEL)


def p36_tone_examples():
    """Tone examples — 3 contexts with right/wrong."""
    examples = [
        ("Web hero",
         "¿Qué hay tras tu marca?",
         "¡Descubre el poder transformador de una identidad de marca coherente!"),
        ("Email de contacto",
         "Gracias por escribir. Te cuento rápido qué hacemos y qué no.",
         "¡Nos alegra enormemente recibir tu mensaje! Estamos deseando embarcarnos juntos en este emocionante viaje."),
        ("Respuesta a objeción",
         "No lo necesitas. Si estás cómodo con que cada persona que toca tu marca la interprete a su manera, no lo necesitas.",
         "¡Entendemos tu preocupación! Nuestro servicio integral de branding 360 te ayudará a potenciar sinergias..."),
    ]

    rows = ""
    for context, yes, no in examples:
        rows += f"""\
<div style="padding:5mm 0;border-bottom:0.5px solid {CENIZA};">
  <div class="eyebrow" style="margin-bottom:4mm;">{context}</div>
  <div class="g2">
    <div>
      <div style="font-family:{FAM};font-size:10px;font-weight:700;color:{NEGRO};margin-bottom:2mm;">Así sí</div>
      <div class="body-text" style="font-size:12px;">"{yes}"</div>
    </div>
    <div>
      <div class="struck" style="font-family:{FAM};font-size:10px;font-weight:700;margin-bottom:2mm;">Así no</div>
      <div style="font-family:{FAM};font-size:12px;font-weight:400;color:{PIEDRA};line-height:1.7;">"{no}"</div>
    </div>
  </div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;">
  {titulo("Ejemplos de tono", 38)}
  {rows}
</div>"""
    return page_shell(body, 36, section="VII · Voz y personalidad", bg=PAPEL)


def p37_voice_card():
    """Brand voice reference card — summary on Arena background."""
    keywords = "Directo &ensp;/&ensp; Provocador &ensp;/&ensp; Seguro &ensp;/&ensp; Preciso &ensp;/&ensp; Cercano"

    body = f"""\
<div style="position:absolute;inset:0;background:{ARENA};
  display:flex;align-items:center;justify-content:center;">
  <div style="width:210mm;background:{PAPEL};
    box-shadow:0 2px 24px rgba(0,0,0,0.06);padding:18mm 24mm;position:relative;">
    <div class="eyebrow" style="margin-bottom:8mm;">Tarjeta de voz de marca</div>
    <div style="font-family:{FAM};font-size:20px;font-weight:700;
      color:{NEGRO};line-height:1.4;margin-bottom:8mm;">
      Tramarca no convence<span style="color:{LACRE};font-size:24px;">.</span>
      Señala lo que ya sabes pero no quieres admitir<span style="color:{LACRE};font-size:24px;">.</span>
    </div>
    <div style="font-family:{FAM};font-size:15px;font-weight:500;
      color:{LACRE};margin-bottom:8mm;letter-spacing:1px;">{keywords}</div>
    <div style="width:100%;height:0.5px;background:{CENIZA};margin-bottom:6mm;"></div>
    <div class="body-text" style="margin-bottom:3mm;">
      Formato: frases cortas, punto siempre, sin exclamaciones, sin cursivas.
    </div>
    <div class="body-text">Tú, nunca usted.</div>
    <!-- Monogram watermark -->
    <div style="position:absolute;bottom:14mm;right:20mm;
      font-family:{FAM};font-size:32px;font-weight:900;color:{CENIZA};opacity:0.25;">
      Tm<span style="color:{LACRE};opacity:0.4;">.</span>
    </div>
  </div>
</div>"""
    return page_shell(body, 37, section="VII · Voz y personalidad", bg=ARENA, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# 08 DIRECCIÓN DE ARTE  (pp. 38-41)
# ══════════════════════════════════════════════════════════════

def p38_arte():
    """Section divider — Dirección de arte."""
    return divider("08", "VIII", "Dirección de arte",
                   "Fotografía, layout, composición.", pg=38)


def p39_photography():
    """Photography direction — 2 images + 3-column specs."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:flex;flex-direction:column;gap:6mm;">
  {titulo("Fotografía", 42)}
  <!-- Two editorial images -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm;flex:1;">
    <div class="photo" style="height:100%;">
      <img src="assets/img-01.jpg" alt="">
    </div>
    <div class="photo" style="height:100%;">
      <img src="assets/img-02.jpg" alt="">
    </div>
  </div>
  <!-- 3-column specs -->
  <div class="g3">
    <div>
      <div class="eyebrow" style="margin-bottom:2mm;">Estilo</div>
      <div class="body-text" style="font-size:11px;">Editorial, desaturada, luz lateral controlada. Nunca stock genérico.</div>
    </div>
    <div>
      <div class="eyebrow" style="margin-bottom:2mm;">Color</div>
      <div class="body-text" style="font-size:11px;">Dominan neutros de la paleta. Lacre aparece como detalle único.</div>
    </div>
    <div>
      <div class="eyebrow" style="margin-bottom:2mm;">Sujetos</div>
      <div class="body-text" style="font-size:11px;">Instrumentos de precisión, pantallas, teclados, herramientas técnicas. Nunca caras.</div>
    </div>
  </div>
  <div class="meta">Anti-referencias: stock corporativo, personas sonriendo a cámara, fondos degradados, iconografía flat.</div>
</div>"""
    return page_shell(body, 39, section="VIII · Dirección de arte", bg=PAPEL)


def p40_layout_grid():
    """Layout grid system — 6-column diagram."""
    cols = "".join(f'<div style="border:1px solid {CENIZA};opacity:0.3;"></div>' for _ in range(6))

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:flex;flex-direction:column;gap:6mm;">
  {titulo("Retícula", 42)}
  <!-- Grid diagram -->
  <div style="flex:1;border:1px solid {CENIZA};position:relative;background:{PAPEL};">
    <!-- Margin guides -->
    <div style="position:absolute;top:0;left:0;width:20mm;height:100%;border-right:1px dashed {LACRE};opacity:0.25;"></div>
    <div style="position:absolute;top:0;right:0;width:20mm;height:100%;border-left:1px dashed {LACRE};opacity:0.25;"></div>
    <div style="position:absolute;top:0;left:0;width:100%;height:15mm;border-bottom:1px dashed {LACRE};opacity:0.25;"></div>
    <div style="position:absolute;bottom:0;left:0;width:100%;height:12mm;border-top:1px dashed {LACRE};opacity:0.25;"></div>
    <!-- 6-column grid -->
    <div style="position:absolute;top:15mm;bottom:12mm;left:20mm;right:20mm;
      display:grid;grid-template-columns:repeat(6,1fr);gap:8mm;">
      {cols}
    </div>
    <!-- Labels -->
    <div style="position:absolute;top:3mm;left:6mm;font-family:{MONO};font-size:7px;color:{LACRE};">24mm</div>
    <div style="position:absolute;top:3mm;right:6mm;font-family:{MONO};font-size:7px;color:{LACRE};">24mm</div>
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
      font-family:{MONO};font-size:9px;color:{PIEDRA};">6 columnas · 8mm gutters</div>
  </div>
  {data_block([
      ("Formato", "A4 apaisado (297 × 210mm)"),
      ("Márgenes", "24mm laterales · 28mm top · 20mm bottom"),
      ("Columnas", "6 columnas con 8mm gutters"),
      ("Baseline", "8mm grid baseline"),
  ])}
</div>"""
    return page_shell(body, 40, section="VIII · Dirección de arte", bg=PAPEL)


def p41_art_proof():
    """Art direction proof — 3 mockup images."""
    mockups = [
        ("img-07.jpg", "Manual impreso, flat-lay"),
        ("img-05.jpg", "Tarjeta de visita"),
        ("img-09.jpg", "Pantalla con tramarca.es"),
    ]

    grid = ""
    for img, caption in mockups:
        grid += f"""\
<div>
  <div class="photo" style="height:80mm;">
    <img src="assets/{img}" alt="">
  </div>
  <div class="meta" style="margin-top:2mm;">{caption}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:flex;flex-direction:column;gap:6mm;">
  {titulo("Dirección visual en contexto", 36)}
  <div class="g3" style="flex:1;">
    {grid}
  </div>
  {pull_quote("La imagen no ilustra. La imagen certifica el tono", "100%")}
</div>"""
    return page_shell(body, 41, section="VIII · Dirección de arte", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# 09 APLICACIONES  (pp. 42-47)
# ══════════════════════════════════════════════════════════════

def p42_aplicaciones():
    """Section divider — Aplicaciones."""
    return divider("09", "IX", "Aplicaciones",
                   "Tarjeta, email, redes, propuesta, web.", pg=42)


def p43_business_card():
    """Business card — photo + CSS mockup specs."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.4fr 1fr;gap:16mm;align-content:start;">
  <div>
    {titulo("Tarjeta de visita", 38)}
    <!-- Photo of cards -->
    <div class="photo" style="height:90mm;margin-top:4mm;">
      <img src="assets/img-05.jpg" alt="">
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:6mm;">
    <div class="eyebrow">Especificaciones</div>
    <!-- Front mini -->
    <div style="background:{NEGRO};padding:6mm 8mm;display:flex;flex-direction:column;
      align-items:center;justify-content:center;height:35mm;">
      <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{PAPEL};">
        {BRAND}<span style="color:{LACRE};">.</span>
      </div>
      <div style="font-family:{FAM};font-size:7px;color:{PIEDRA};margin-top:2mm;">Sistemas de marca.</div>
    </div>
    <div class="meta">Frontal — Satoshi 900, Papel sobre Negro</div>
    <!-- Back mini -->
    <div style="background:{PAPEL};border:1px solid {CENIZA};padding:5mm 7mm;
      display:flex;flex-direction:column;justify-content:space-between;height:35mm;">
      <div>
        <div style="font-family:{FAM};font-size:9px;font-weight:500;color:{NEGRO};">Fernando Rojas</div>
        <div style="font-family:{FAM};font-size:7px;color:{PIEDRA};margin-top:1mm;">Director</div>
      </div>
      <div style="font-family:{MONO};font-size:7px;color:{NEGRO};line-height:1.8;">
        tramarca.es · hola@tramarca.es
      </div>
    </div>
    <div class="meta">Reverso — Satoshi 500 + IBM Plex Mono 400</div>
    {data_block([("Tamaño", "85 × 55 mm"), ("Papel", "400g cotton"), ("Tinta", "Negro mate")])}
  </div>
</div>"""
    return page_shell(body, 43, section="IX · Aplicaciones", bg=PAPEL)


def p44_email_signature():
    """Email signature mockup."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:flex;flex-direction:column;gap:6mm;">
  {titulo("Firma de email", 38)}
  <!-- Faux email window -->
  <div style="flex:1;">
    <!-- Window chrome -->
    <div style="height:8mm;background:{ARENA};border:1px solid {CENIZA};
      border-bottom:none;display:flex;align-items:center;padding:0 4mm;gap:2mm;">
      <div style="width:3mm;height:3mm;border-radius:50%;background:{CENIZA};"></div>
      <div style="width:3mm;height:3mm;border-radius:50%;background:{CENIZA};"></div>
      <div style="width:3mm;height:3mm;border-radius:50%;background:{CENIZA};"></div>
    </div>
    <!-- Email body -->
    <div style="background:white;border:1px solid {CENIZA};padding:10mm 14mm;">
      <div style="font-family:{FAM};font-size:12px;font-weight:400;
        color:{PIEDRA};line-height:1.7;margin-bottom:8mm;max-width:180mm;">
        Gracias por escribir. Te cuento rápido qué hacemos y qué no.<br>
        Hablamos cuando quieras.
      </div>
      <div style="width:60mm;height:0.5px;background:{CENIZA};margin-bottom:5mm;"></div>
      <div style="font-family:{FAM};font-size:12px;font-weight:500;color:{NEGRO};">
        Fernando Rojas <span style="color:{LACRE};font-weight:700;font-size:14px;">.</span> Tramarca
      </div>
      <div style="font-family:{MONO};font-size:9px;color:{PIEDRA};margin-top:2mm;">
        {DESCRIPTOR} — tramarca.es
      </div>
    </div>
  </div>
  <div class="g3">
    <div class="meta">Sin imágenes incrustadas.</div>
    <div class="meta">Sin citas inspiracionales.</div>
    <div class="meta">Sin banners promocionales.</div>
  </div>
</div>"""
    return page_shell(body, 44, section="IX · Aplicaciones", bg=PAPEL)


def p45_social_media():
    """Social media — 3 square post mockups."""
    posts = [
        (NEGRO, PAPEL, f'¿Tu equipo sabe qué colores usar<span style="color:{LACRE};">?</span><br>¿Seguro<span style="color:{LACRE};">?</span>',
         "Post tipo: pregunta provocadora"),
        (ARENA, NEGRO, f'<div class="eyebrow" style="margin-bottom:3mm;">ARTÍCULO</div>'
         f'<div style="font-family:{FAM};font-size:16px;font-weight:900;line-height:1.3;">'
         f'Por qué tu manual<br>de marca caduca<span style="color:{LACRE};">.</span></div>',
         "Post tipo: carrusel / artículo"),
        (PAPEL, NEGRO, f'Lo que no se documenta, se improvisa<span style="color:{LACRE};">.</span>',
         "Post tipo: frase mínima"),
    ]

    grid = ""
    for bg, fg, content, caption in posts:
        border = f"border:1px solid {CENIZA};" if bg in [PAPEL, ARENA] else ""
        grid += f"""\
<div>
  <div style="background:{bg};{border}aspect-ratio:1/1;
    display:flex;align-items:center;justify-content:center;padding:8mm;">
    <div style="font-family:{FAM};font-size:14px;font-weight:700;
      color:{fg};text-align:center;line-height:1.5;">{content}</div>
  </div>
  <div class="meta" style="margin-top:2mm;">{caption}</div>
</div>"""

    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:flex;flex-direction:column;gap:6mm;">
  {titulo("Redes sociales", 38)}
  <div class="g3" style="flex:1;">
    {grid}
  </div>
  <div style="display:flex;align-items:center;gap:3mm;">
    <div style="width:10mm;height:10mm;border-radius:50%;background:{LACRE};
      display:flex;align-items:center;justify-content:center;">
      <span style="font-family:{FAM};font-size:7px;font-weight:900;color:{PAPEL};">Tm.</span>
    </div>
    <div>
      <div style="font-family:{FAM};font-size:10px;font-weight:700;color:{NEGRO};">@tramarca</div>
      <div class="meta">Sistemas de marca. Lo que no se documenta, se improvisa.</div>
    </div>
  </div>
</div>"""
    return page_shell(body, 45, section="IX · Aplicaciones", bg=PAPEL)


def p46_proposal():
    """Proposal document mockup."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.3fr 1fr;gap:16mm;align-content:start;">
  <div>
    {titulo("Propuesta", 38)}
    <!-- Proposal card -->
    <div style="background:white;border:1px solid {CENIZA};padding:12mm 14mm;
      box-shadow:0 2px 8px rgba(0,0,0,0.04);">
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6mm;">
        <div style="font-family:{FAM};font-size:14px;font-weight:900;color:{NEGRO};">
          {BRAND}<span style="color:{LACRE};">.</span></div>
        <div class="meta">PROP-2026-001</div>
      </div>
      <div style="width:100%;height:0.5px;background:{CENIZA};margin-bottom:5mm;"></div>
      <div style="font-family:{FAM};font-size:20px;font-weight:900;color:{NEGRO};margin-bottom:4mm;">
        Propuesta para Empresa<span style="color:{LACRE};font-size:24px;">.</span>
      </div>
      <div class="body-text" style="font-size:11px;margin-bottom:5mm;max-width:140mm;">
        Este documento detalla el alcance, proceso y condiciones para la producción
        de tu manual de marca. Sin rodeos.
      </div>
      {data_block([
          ("Fecha", "Abril 2026"),
          ("Alcance", "Profesional"),
          ("Plazo", "4 semanas"),
          ("Revisiones", "2 rondas"),
      ])}
    </div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;gap:8mm;">
    {pull_quote("Cada propuesta sigue esta estructura. Sin slides. Sin filosofía. Solo qué, cómo, cuándo y cuánto", "100%")}
    <div style="background:{ARENA};padding:18px 22px;">
      <div class="eyebrow" style="margin-bottom:4mm;">Estructura fija</div>
      <div class="body-text" style="font-size:11px;">
        Portada → Alcance → Proceso → Timeline → Precio → Condiciones.
        Siempre el mismo orden. Siempre la misma claridad.
      </div>
    </div>
  </div>
</div>"""
    return page_shell(body, 46, section="IX · Aplicaciones", bg=PAPEL)


def p47_web():
    """Web mockup — tramarca.es hero in browser frame."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:flex;flex-direction:column;gap:6mm;">
  {titulo("Web", 38)}
  <!-- Browser mockup -->
  <div style="flex:1;display:flex;flex-direction:column;">
    <!-- Chrome -->
    <div style="height:8mm;background:{ARENA};border:1px solid {CENIZA};
      border-bottom:none;display:flex;align-items:center;padding:0 4mm;gap:2mm;">
      <div style="width:3mm;height:3mm;border-radius:50%;background:{CENIZA};"></div>
      <div style="width:3mm;height:3mm;border-radius:50%;background:{CENIZA};"></div>
      <div style="width:3mm;height:3mm;border-radius:50%;background:{CENIZA};"></div>
      <div style="flex:1;margin-left:4mm;">
        <div style="background:{PAPEL};border:1px solid {CENIZA};border-radius:1mm;
          padding:1mm 3mm;font-family:{MONO};font-size:7px;color:{PIEDRA};width:50mm;">tramarca.es</div>
      </div>
    </div>
    <!-- Dark hero -->
    <div style="flex:2;background:{NEGRO};border:1px solid {CENIZA};border-bottom:none;
      display:flex;flex-direction:column;align-items:center;justify-content:center;">
      <div style="font-family:{FAM};font-size:28px;font-weight:900;color:{PAPEL};margin-bottom:3mm;">
        {BRAND}<span style="color:{LACRE};font-size:34px;">.</span>
      </div>
      <div style="font-family:{FAM};font-size:13px;color:{CENIZA};margin-bottom:6mm;">{DESCRIPTOR}</div>
      <div style="padding:2.5mm 8mm;background:{LACRE};font-family:{FAM};
        font-size:10px;font-weight:700;color:{PAPEL};">Ver servicios</div>
    </div>
    <!-- Light section -->
    <div style="flex:1;background:{PAPEL};border:1px solid {CENIZA};
      display:flex;align-items:center;justify-content:center;">
      <div class="meta">[ Sección servicios — grid de 3 columnas ]</div>
    </div>
  </div>
  <div class="meta">Satoshi para todo. IBM Plex Mono para metadata. Lacre solo en CTA y punto.</div>
</div>"""
    return page_shell(body, 47, section="IX · Aplicaciones", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# 10 PORTFOLIO  (pp. 48-49)
# ══════════════════════════════════════════════════════════════

def p48_portfolio():
    """Section divider — Portfolio."""
    return divider("10", "X", "Portfolio",
                   "Trabajo producido.", pg=48)


def p49_case_anfisbena():
    """Case study — Anfisbena brand manual."""
    body = f"""\
<div style="position:absolute;left:24mm;top:30mm;right:24mm;bottom:20mm;
  display:grid;grid-template-columns:1.4fr 1fr;gap:16mm;align-content:start;">
  <div>
    {titulo("Anfisbena", 42)}
    <!-- Case image -->
    <div class="photo" style="height:90mm;margin-top:4mm;">
      <img src="assets/img-11.jpg" alt="">
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:6mm;">
    <div class="eyebrow">Case study</div>
    {data_block([
        ("Cliente", "Anfisbena"),
        ("Sector", "Knitwear de autor, Toledo"),
        ("Alcance", "43 páginas"),
        ("Entrega", "Identidad + dirección de arte"),
        ("Tipografías", "Gambarino + Switzer"),
        ("Paleta", "7 colores (Noche → Óxido)"),
    ])}
    <div style="background:{ARENA};padding:18px 22px;">
      <div class="body-text" style="font-size:12px;">
        Primer manual producido por Tramarca. Identidad completa para marca de punto
        artesanal con raíces en Toledo. Sistema visual que conecta tradición textil
        con posicionamiento premium contemporáneo.
      </div>
    </div>
    {accent_rule(60, "4mm")}
    <div class="meta">Abril 2026</div>
  </div>
</div>"""
    return page_shell(body, 49, section="X · Portfolio", bg=PAPEL)


# ══════════════════════════════════════════════════════════════
# 11 CIERRE  (pp. 50-51)
# ══════════════════════════════════════════════════════════════

def p50_contact():
    """Contact page — warm close."""
    body = f"""\
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;">
  <div style="text-align:center;">
    <div style="font-family:{FAM};font-size:42px;font-weight:900;
      color:{NEGRO};margin-bottom:10mm;">
      Hablemos de tu marca<span style="color:{LACRE};font-size:50px;">.</span>
    </div>
    <div style="font-family:{MONO};font-size:13px;color:{CARBON};line-height:2.4;">
      tramarca.es<br>
      hola@tramarca.es
    </div>
    {accent_rule(60, "12mm")}
    <div style="font-family:{FAM};font-size:16px;font-weight:500;
      color:{PIEDRA};margin-top:10mm;">
      ¿Tu marca está por escrito?
    </div>
  </div>
</div>"""
    return page_shell(body, 50, section="Cierre", bg=PAPEL)


def p51_back_cover():
    """Back cover — Tm. monogram on Negro."""
    body = f"""\
<div style="position:absolute;left:50%;top:46%;transform:translate(-50%,-50%);text-align:center;">
  <div style="font-family:{FAM};font-size:56px;font-weight:900;color:{PAPEL};">
    Tm<span style="color:{LACRE};font-size:67px;">.</span>
  </div>
</div>
<div style="position:absolute;bottom:14mm;left:50%;transform:translateX(-50%);
  font-family:{MONO};font-size:9px;color:{PIEDRA};">
  tramarca.es
</div>"""
    return page_shell(body, 51, bg=NEGRO, dark=True, no_furniture=True)


# ══════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════

def build():
    pages = [
        p01_cover(),
        p02_colophon(),
        p03_toc(),
        p04_provocacion(),
        p05_the_problem(),
        p06_the_answer(),
        p07_fundamentos(),
        p08_vision_mission(),
        p09_values(),
        p10_positioning(),
        p11_audience(),
        p12_personality(),
        p13_servicio(),
        p14_whats_included(),
        p15_process(),
        p16_scope_tiers(),
        p17_identidad(),
        p18_logo_primary(),
        p19_logo_construction(),
        p20_clearspace(),
        p21_logo_dark(),
        p22_logo_versions(),
        p23_logo_forbidden(),
        p24_logo_context(),
        p25_color(),
        p26_color_system(),
        p27_color_combos(),
        p28_color_donts(),
        p29_tipografia(),
        p30_specimen_satoshi(),
        p31_specimen_plex(),
        p32_type_hierarchy(),
        p33_voz(),
        p34_voice_principles(),
        p35_vocabulary(),
        p36_tone_examples(),
        p37_voice_card(),
        p38_arte(),
        p39_photography(),
        p40_layout_grid(),
        p41_art_proof(),
        p42_aplicaciones(),
        p43_business_card(),
        p44_email_signature(),
        p45_social_media(),
        p46_proposal(),
        p47_web(),
        p48_portfolio(),
        p49_case_anfisbena(),
        p50_contact(),
        p51_back_cover(),
    ]

    DIST.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html_wrap(pages), encoding="utf-8")
    print(f"✓ Built {len(pages)} pages → {OUT}")


if __name__ == "__main__":
    build()
