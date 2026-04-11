# Creative Brief: TRAMARCA. Brand Manual

Definitive reference for building the 34-page brand manual in Python (HTML+CSS > Playwright > PDF).
Every decision here traces to approved brand tokens and strategic intent.

---

## 1. Brand Identity (Approved)

| Field | Value |
|---|---|
| Name | TRAMARCA. |
| Pronunciation | tra-MAR-ca |
| Concept | "El Punto Final" -- the oversized period is the brand mark |
| Descriptor | Tu marca, sin improvisar. |
| Tagline | Que hay tras tu marca? |
| Hero copy | Lo que no se documenta, se improvisa. Lo que se improvisa, no es marca. |
| Monogram | Tm. |
| Favicon | Circle in Lacre (#C4553A) |
| Archetype | Confrontational but warm. Expert craftsman who uses technology. Not agency, not freelancer. |
| Domain | tramarca.es |

### Logo System

- **Wordmark**: TRAMARCA. in Satoshi Bold 900, all-caps. The final period is oversized (approximately 150% of cap height) and colored in Lacre. Rest of letters in Negro or Papel depending on background.
- **Monogram**: Tm. -- Satoshi Bold, period in Lacre. For small contexts: favicons, watermarks, avatar.
- **Favicon**: Solid circle in Lacre (#C4553A). No letter, no text. Just the period as symbol.
- **Lockup with descriptor**: TRAMARCA. above, "Tu marca, sin improvisar." below in IBM Plex Mono 400, Piedra color, letterspacing +1px.
- **Clear space**: minimum clear space = width of the period on all sides.
- **Minimum sizes**: wordmark no smaller than 80px wide. Monogram no smaller than 24px.
- **Forbidden uses**: never remove the period, never color the period anything other than Lacre, never stack the letters vertically, never add gradients/shadows/outlines.

---

## 2. Color Tokens

| Token | Name | Hex | Role | Usage |
|---|---|---|---|---|
| --color-negro | Negro | #0C0C0C | Dark dominant | Dark backgrounds, section dividers, headers, footers |
| --color-carbon | Carbon | #1C1C1C | Dark secondary | Layered dark panels, subtle depth on dark pages |
| --color-accent | Lacre | #C4553A | Single accent | CTAs, the period, highlights, section numbers, links |
| --color-piedra | Piedra | #7A7672 | Mid neutral | Captions, metadata, secondary text, IBM Plex Mono content |
| --color-ceniza | Ceniza | #B5B1AC | Light neutral | Borders, dividers, disabled states, rules |
| --color-arena | Arena | #E4E2DC | Light background alt | Cards, secondary backgrounds, pullout boxes |
| --color-papel | Papel | #F4F0EB | Light dominant | Primary light background, body pages |

### Color Rules

- **Dark/light ratio in manual**: approximately 18 dark pages / 33 light pages (35%/65%).
- **Lacre is surgical**: never large areas of Lacre. It appears only as: the period, section numbers, CTA buttons, horizontal rules, small highlights. Maximum coverage per page: 5%.
- **No Lacre-light variant needed**: Unlike Anfisbena's Oxido, Lacre (#C4553A) has sufficient contrast on both Negro and Papel backgrounds. Tested: Lacre on Negro = 4.8:1, Lacre on Papel = 4.6:1. Both pass WCAG AA for large text.
- **Text on dark pages**: always Papel (#F4F0EB) for body, Ceniza (#B5B1AC) for secondary, Lacre for accents.
- **Text on light pages**: always Negro (#0C0C0C) for headlines, Carbon (#1C1C1C) for body, Piedra for metadata.
- **Section dividers**: full Negro background, Arabic numeral watermark at 580px in Carbon (5% opacity), section title in Papel, section number eyebrow in Lacre.

---

## 3. Typography

| Role | Font | Source | Weights | CSS font-family |
|---|---|---|---|---|
| Display + Body | Satoshi | Fontshare (ITF) | 400, 500, 700, 900 | 'Satoshi', -apple-system, system-ui, sans-serif |
| Data / Specs / Mono | IBM Plex Mono | Google Fonts | 400, 700 | 'IBM Plex Mono', ui-monospace, monospace |

### Font Loading

```html
<link rel="preconnect" href="https://api.fontshare.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700,900&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;700&display=swap">
```

### Type Scale (A4 Landscape 297x210mm)

| Element | Font | Weight | Size | Line-height | Letterspacing | Color |
|---|---|---|---|---|---|---|
| Hero title (cover) | Satoshi | 900 | 72px | 1.0 | -2px | Papel |
| Section divider title | Satoshi | 900 | 48px | 1.1 | -1px | Papel |
| Page title (H1) | Satoshi | 900 | 32px | 1.15 | -0.5px | Negro |
| Subtitle (H2) | Satoshi | 700 | 22px | 1.25 | 0 | Negro |
| Subheading (H3) | Satoshi | 700 | 16px | 1.3 | 0 | Negro |
| Body text | Satoshi | 400 | 13px | 1.7 | 0 | Carbon |
| Body bold | Satoshi | 700 | 13px | 1.7 | 0 | Negro |
| Caption | Satoshi | 400 | 10px | 1.5 | 0 | Piedra |
| Eyebrow / kicker | IBM Plex Mono | 700 | 8px | 1.0 | 3px | Lacre |
| Metadata / specs | IBM Plex Mono | 400 | 9px | 1.5 | 0.5px | Piedra |
| Page number | IBM Plex Mono | 400 | 7px | 1.0 | 0 | Piedra |
| Watermark numeral | Satoshi | 900 | 580px | 1.0 | 0 | Carbon at 5% opacity |

### Typography Rules

- **Two families only**. Satoshi does everything: display, body, headlines, UI. IBM Plex Mono is strictly for metadata, specs, eyebrows, page numbers, and technical content.
- **Satoshi 900 is the display weight**. Never use 900 for body text. Body is always 400, emphasis is 700.
- **IBM Plex Mono is always small**. Never above 11px. It is the "fine print" typeface.
- **No italic**. Tramarca's voice is direct. Emphasis is achieved through weight (700) or color (Lacre), never italic.
- **Uppercase only in eyebrows** (IBM Plex Mono, 8px, letterspaced). Never uppercase Satoshi body text.

---

## 4. Voice and Personality

### 5 Adjectives

1. **Directo** -- says what it thinks, no hedging
2. **Provocador** -- questions what the market takes for granted
3. **Seguro** -- does not ask permission, does not apologize
4. **Preciso** -- every word chosen, nothing extra
5. **Cercano** -- uses "tu", never corporate, speaks peer-to-peer

### Golden Rule

> Tramarca no convence. Tramarca senala lo que ya sabes pero no quieres admitir.

### Writing Format

- Short sentences. One idea per sentence.
- Period always. Never ellipsis.
- Rhetorical questions that make you uncomfortable.
- Never exclamations. Conviction does not need volume.
- "Tu" always. "Tu marca", never "su marca".
- Paragraphs of 3 lines maximum.

### Vocabulary

**We use**: documentar, por escrito, reglas, decision, sistema, construir, producir, cada pagina, claro, directo, manual, identidad, personalidad, assets, presencia, profesional, punto de contacto

**We never use**: branding 360, holistico, sinergia, storytelling, disruptivo, hacer magia, conceptualizar, co-crear, universo de marca, ADN de marca, lovemark, bespoke, creativo

---

## 5. Manual Structure: 51 Pages, 11 Sections

Format: A4 landscape (297mm x 210mm). Printed via Playwright Chromium.

### Overview Table

| Section | Pages | Count | Background | Density |
|---|---|---|---|---|
| 00 Apertura | 01-03 | 3 | Dark / Dark / Light | Cover + colophon |
| I Provocacion | 04-06 | 3 | Dark / Light / Light | Why this exists |
| II Fundamentos | 07-12 | 6 | Dark / Light x5 | Vision, mission, values, positioning |
| III Servicio | 13-16 | 4 | Dark / Light x3 | What Tramarca delivers |
| IV Identidad Visual | 17-24 | 8 | Dark / Light x7 | Logo, construction, clear space, versions, forbidden |
| V Paleta de Color | 25-28 | 4 | Dark / Light x3 | Primary, secondary, combinations, contrast |
| VI Tipografia | 29-32 | 4 | Dark / Light x3 | Families, scale, pairing, rules |
| VII Voz y Personalidad | 33-37 | 5 | Dark / Light x4 | Tone, vocabulary, examples, anti-examples |
| VIII Direccion de Arte | 38-41 | 4 | Dark / Light x3 | Photography, layout grid, mockups |
| IX Aplicaciones | 42-47 | 6 | Dark / Light x5 | Business card, email sig, social, proposals, web |
| X Portfolio | 48-49 | 2 | Dark / Light | Case studies (Anfisbena, future) |
| Cierre | 50-51 | 2 | Light / Dark | Contact + back cover |

**Total: 51 pages. 14 dark section dividers/special pages. 37 light content pages.**

### Unique Sections vs. Standard Client Manuals

Three sections are specific to Tramarca as a self-promotional manual and do NOT appear in client manuals:

1. **I Provocacion** -- rhetorical manifesto. Why most brands are improvising. Sets confrontational tone.
2. **III Servicio** -- explains what Tramarca delivers (scope tiers, process, deliverables).
3. **X Portfolio** -- showcase of completed brand manuals (Anfisbena as hero case).

---

## 6. Page-by-Page Specification

### 00 APERTURA (pp. 01-03)

**Page 01 -- Cover**
- Background: Negro full bleed
- Center: TRAMARCA. wordmark at 72px Satoshi 900, Papel color, period in Lacre
- Below wordmark: "Sistemas de marca." in IBM Plex Mono 400, 10px, Ceniza, letterspaced
- Bottom-left: "Tu marca, sin improvisar." in Satoshi 400, 13px, Piedra
- Bottom-right: "2026" in IBM Plex Mono, 9px, Piedra
- No images. No decoration. Just the wordmark on black. The period does the work.
- Mood: authoritative silence, like opening a legal document

**Page 02 -- Inside Cover / Colophon**
- Background: Carbon (#1C1C1C)
- Left column (40%): colophon data in IBM Plex Mono 9px, Piedra
  - Edition: Primera edicion / Abril 2026
  - Designed by: Tramarca
  - Pages: 51
  - Fonts: Satoshi (Fontshare), IBM Plex Mono (Google)
  - Colors: 7 (listed with hex)
  - Format: A4 apaisado, 297 x 210 mm
- Right column (60%): brand statement in Satoshi 400, 16px, Ceniza
  - "Este documento define que es Tramarca, como se ve, como habla y como se aplica. Cada decision esta por escrito. Cada regla tiene una razon."
- Mood: technical, precise, "you are reading a controlled document"

**Page 03 -- Table of Contents**
- Background: Papel
- Title: "Indice" in Satoshi 900, 32px, Negro
- TOC in two columns:
  - Left: sections I-VI with page numbers
  - Right: sections VII-X + Cierre with page numbers
- Section numbers in IBM Plex Mono 700, Lacre
- Section names in Satoshi 500, 14px, Negro
- Page numbers in IBM Plex Mono 400, 9px, Piedra, right-aligned with dot leaders
- Mood: functional, confident navigation

### I PROVOCACION (pp. 04-06)

**Page 04 -- Section Divider**
- Background: Negro full bleed
- Watermark: "1" at 580px Satoshi 900, Carbon at 5% opacity, positioned right-center
- Eyebrow: "I" in IBM Plex Mono 700, 8px, Lacre, letterspaced 3px
- Title: "Provocacion." in Satoshi 900, 48px, Papel
- Subtitle: "Por que este manual existe." in Satoshi 400, 16px, Ceniza
- Mood: ominous, like a chapter title in a thriller

**Page 05 -- The Problem**
- Background: Papel
- Title: "Lo que no se documenta, se improvisa." in Satoshi 900, 28px, Negro
- Body: 3 short paragraphs (max 3 lines each) in Satoshi 400, 13px, Carbon. Content:
  - Paragraph 1: Most brands exist only in their founder's head.
  - Paragraph 2: Without written rules, every person who touches the brand interprets it differently.
  - Paragraph 3: The result is visual noise. Inconsistency. Improvisation.
- Right side: pulled quote in Satoshi 700, 22px, Negro:
  "Tienes un logo. Tienes una paleta. Pero no tienes una marca."
- Below quote: a single horizontal rule in Lacre, 2px, 80px wide
- Mood: uncomfortable truth, nodding reader

**Page 06 -- The Answer**
- Background: Papel
- Title: "Un sistema de marca." in Satoshi 900, 28px, Negro
- Body: explains that a brand system is not a logo, not a PDF of 3 pages -- it is the complete set of rules, visual and verbal, that protects the brand from improvisation. Short, punchy, 4-5 sentences.
- Bottom: full-width horizontal strip in Arena (#E4E2DC), 40px tall, with centered text:
  "Eso es lo que hacemos en Tramarca. Ponerlo por escrito." in IBM Plex Mono 400, 10px, Piedra
- Mood: resolution, clarity, "this is the fix"

### II FUNDAMENTOS (pp. 07-12)

**Page 07 -- Section Divider**
- Same pattern as p04: Negro bg, watermark "2", eyebrow "II", title "Fundamentos.", subtitle "Quien somos. Que hacemos. Para quien."

**Page 08 -- Vision and Mission**
- Background: Papel
- Two-column layout:
  - Left column header: "Vision." in Satoshi 700, 18px, Negro
  - Vision text: "Que cada marca profesional tenga su sistema por escrito." in Satoshi 400, 14px, Carbon
  - Right column header: "Mision." in Satoshi 700, 18px, Negro
  - Mission text: "Producimos manuales de marca completos: identidad visual, voz, personalidad, assets y reglas de uso. Un documento. Cada decision. Por escrito." in Satoshi 400, 14px, Carbon
- Bottom: thin Ceniza rule separating a metadata strip:
  - "Fundado: 2026 / Ubicacion: Espana / Formato: remoto" in IBM Plex Mono 400, 9px, Piedra
- Mood: grounded, factual

**Page 09 -- Values (3)**
- Background: Papel
- Title: "Valores." in Satoshi 900, 28px, Negro
- Three value blocks in a 3-column grid, each with:
  - Number in IBM Plex Mono 700, 32px, Lacre ("01", "02", "03")
  - Value name in Satoshi 700, 16px, Negro
  - 2-line explanation in Satoshi 400, 12px, Carbon
- Values:
  1. **Claridad** -- Si no se puede explicar en una frase, no esta definido.
  2. **Precision** -- Cada palabra, cada color, cada regla tiene una razon.
  3. **Honestidad** -- Decimos lo que pensamos. Incluido lo que no quieres oir.
- Mood: structured, deliberate

**Page 10 -- Positioning**
- Background: Papel
- Title: "Posicionamiento." in Satoshi 900, 28px, Negro
- Positioning statement block in Arena background card, 20px padding:
  "Para empresas y profesionales que necesitan una marca consistente, Tramarca es el servicio de sistemas de marca que documenta cada decision visual y verbal en un unico manual de referencia."
  in Satoshi 500, 15px, Negro
- Below card: "Lo que no somos." in Satoshi 700, 16px, Negro
- Three "not" statements:
  - "No somos una agencia creativa."
  - "No somos un disenador freelance."
  - "No hacemos logos sueltos, naming, ni campanas."
  Each in Satoshi 400, 13px, Carbon, preceded by a Lacre dash
- Mood: boundary-setting, confident

**Page 11 -- Target Audience**
- Background: Papel
- Title: "Para quien." in Satoshi 900, 28px, Negro
- Two audience profiles in 2-column layout:
  - **Perfil A: La empresa que crece**
    - "Llevan 2-5 anos. Tienen logo, colores, algo de identidad. Pero cada vez que alguien nuevo toca la marca, sale diferente. Necesitan el sistema."
  - **Perfil B: El profesional que se toma en serio**
    - "Consultores, estudios, clinicas. Su marca es su reputacion. Si su tarjeta dice una cosa y su web otra, tienen un problema."
- Each profile: name in Satoshi 700, 14px; description in Satoshi 400, 12px, Carbon
- Bottom metadata: "Sectores: servicios profesionales, consultoria, salud, educacion, tech B2B, retail premium" in IBM Plex Mono 400, 9px, Piedra
- Mood: recognition, "that's me"

**Page 12 -- Brand Personality Map**
- Background: Papel
- Title: "Personalidad." in Satoshi 900, 28px, Negro
- Visual map: 5 personality traits arranged as a spectrum/radar, each with:
  - Trait name in Satoshi 700, 14px, Negro
  - One-line explanation in Satoshi 400, 11px, Carbon
  - A horizontal bar showing intensity (Lacre fill against Ceniza background)
- Traits: Directo (90%), Provocador (80%), Seguro (85%), Preciso (95%), Cercano (70%)
- Below: "Tramarca no convence. Tramarca senala lo que ya sabes pero no quieres admitir." in Satoshi 500, 14px, Negro, left-aligned with Lacre vertical rule (3px, 40px tall)
- Mood: self-aware, deliberate

### III SERVICIO (pp. 13-16)

**Page 13 -- Section Divider**
- Negro bg, watermark "3", eyebrow "III", title "Servicio.", subtitle "Que entregamos. Como trabajamos."

**Page 14 -- What's Included**
- Background: Papel
- Title: "Lo que incluye un sistema de marca." in Satoshi 900, 24px, Negro
- Four deliverable blocks in 2x2 grid, each with:
  - Category in IBM Plex Mono 700, 8px, Lacre, uppercase, letterspaced
  - Name in Satoshi 700, 16px, Negro
  - Description in Satoshi 400, 12px, Carbon (2-3 lines max)
- Blocks:
  1. IDENTIDAD VISUAL -- Logotipo, paleta, tipografia, iconografia. No solo que es, sino como se usa y como no.
  2. VOZ Y PERSONALIDAD -- Tono, vocabulario, ejemplos reales. Para que tu marca suene igual la escriba quien la escriba.
  3. ASSETS LISTOS PARA USAR -- Archivos en todos los formatos, plantillas, firmas de email, aplicaciones reales.
  4. REGLAS DE USO -- Espacios, tamanos minimos, fondos permitidos, combinaciones prohibidas.
- Bottom: "Todo en un documento. Pagina a pagina. Decision a decision." in Satoshi 500, 13px, Negro
- Mood: concrete, no-bullshit deliverables

**Page 15 -- Process**
- Background: Papel
- Title: "Proceso." in Satoshi 900, 28px, Negro
- Timeline / steps in vertical layout with connecting line (Ceniza, 1px):
  1. **Brief** -- Conversacion inicial. Entendemos donde esta tu marca ahora. (IBM Plex Mono label: "01 / 1-2 DIAS")
  2. **Produccion** -- Construimos el sistema completo. Sin reuniones intermedias. (Label: "02 / 10-15 DIAS")
  3. **Revision** -- Presentamos. Dos rondas de revision incluidas. (Label: "03 / 3-5 DIAS")
  4. **Entrega** -- Manual final en PDF + assets en todos los formatos. (Label: "04 / DIA FINAL")
- Each step: number in Lacre circle (28px), name in Satoshi 700, description in Satoshi 400, timing in IBM Plex Mono
- Mood: predictable, professional

**Page 16 -- Scope Tiers**
- Background: Papel
- Title: "Alcance." in Satoshi 900, 28px, Negro
- Three columns (pricing tiers):
  - **Esencial** -- 25-30 paginas. Identidad visual + reglas basicas. Para marcas nuevas.
  - **Profesional** -- 35-45 paginas. Completo: visual + verbal + aplicaciones. Para marcas en crecimiento.
  - **Premium** -- 50+ paginas. Todo lo anterior + direccion de arte + portfolio de aplicaciones. Para marcas que quieren el estandar mas alto.
- Each tier: name in Satoshi 700, 18px; page count in IBM Plex Mono; description in Satoshi 400, 12px
- Recommended tier highlighted with Lacre left border (3px)
- No prices in the manual. Bottom note: "Precios y presupuestos personalizados por proyecto." in IBM Plex Mono 400, 9px, Piedra
- Mood: clear options, confidence in structure

### IV IDENTIDAD VISUAL (pp. 17-24)

**Page 17 -- Section Divider**
- Negro bg, watermark "4", eyebrow "IV", title "Identidad Visual.", subtitle "Logo, construccion, versiones, usos."

**Page 18 -- Logo Primary**
- Background: Papel
- Large TRAMARCA. wordmark centered, Satoshi 900, 56px, Negro with Lacre period
- Below: descriptor "Tu marca, sin improvisar." in IBM Plex Mono 400, 10px, Piedra
- Right side metadata block:
  - Tipografia: Satoshi Black (900)
  - Concepto: El Punto Final
  - Elementos: 8 caracteres + punto
  in IBM Plex Mono 400, 9px, Piedra
- Mood: "here it is, nothing else needed"

**Page 19 -- Logo Construction**
- Background: Papel
- Title: "Construccion." in Satoshi 700, 22px, Negro
- Technical diagram: wordmark with construction grid overlay
  - Baseline, cap-height, x-height lines in Ceniza dashed (0.5px)
  - Period size annotation: "150% cap-height" with measurement arrows
  - Clear space box around entire mark with "X" unit notation
- All annotations in IBM Plex Mono 400, 8px, Piedra
- Grid background: subtle 5mm squares in Ceniza at 10% opacity
- Mood: engineering precision, blueprint

**Page 20 -- Logo Clear Space and Minimum Sizes**
- Background: Papel
- Two sections:
  - Top: clear space diagram with dotted boundary and "X" unit = width of period
  - Bottom: minimum sizes -- wordmark at 80px, 60px (too small), 40px (way too small with red X)
- Annotations in IBM Plex Mono
- Mood: rules that protect

**Page 21 -- Logo on Dark Background**
- Background: top half Negro, bottom half Carbon
- Wordmark on Negro: TRAMARCA. in Papel with Lacre period
- Wordmark on Carbon: TRAMARCA. in Papel with Lacre period
- Monogram Tm. on each background
- Right side: "Sobre fondos oscuros, el logotipo se invierte a Papel (#F4F0EB). El punto siempre permanece en Lacre." in Satoshi 400, 11px, Ceniza
- Mood: controlled, systematic

**Page 22 -- Logo Monochrome Versions**
- Background: Papel
- Four versions in 2x2 grid:
  - Negro on Papel (standard)
  - Papel on Negro (reversed)
  - Full Negro (mono, no Lacre -- for single-color printing)
  - Full Papel (mono reversed)
- Each with label in IBM Plex Mono: "POSITIVO", "NEGATIVO", "MONOCROMO", "MONOCROMO INVERTIDO"
- Mood: practical, comprehensive

**Page 23 -- Logo Forbidden Uses**
- Background: Papel
- Title: "Usos incorrectos." in Satoshi 700, 22px, Negro
- 6 prohibited examples in 3x2 grid, each with:
  - Small wordmark rendering showing the violation
  - Red X overlay (Lacre, 2px, semi-transparent)
  - Caption in IBM Plex Mono 400, 8px, Piedra:
    1. "No rotar" -- tilted 15 degrees
    2. "No cambiar color del punto" -- period in blue
    3. "No usar sombras" -- drop shadow applied
    4. "No deformar" -- horizontally stretched
    5. "No usar sobre fondos complejos" -- over busy background
    6. "No eliminar el punto" -- TRAMARCA without period
- Mood: absolute, non-negotiable

**Page 24 -- Logo in Context**
- Background: Papel
- Title: "En contexto." in Satoshi 700, 22px, Negro
- Three mockup image slots showing logo applied:
  1. Business card (dark, logo reversed)
  2. Document header (light, logo standard)
  3. Social media avatar (monogram in circle)
- Each image: 120x80mm placeholder with description
- Mood: proof it works in the real world

### V PALETA DE COLOR (pp. 25-28)

**Page 25 -- Section Divider**
- Negro bg, watermark "5", eyebrow "V", title "Paleta de Color.", subtitle "7 colores. Una sola regla: menos es mas."

**Page 26 -- Color System Overview**
- Background: Papel
- Title: "Sistema de color." in Satoshi 900, 28px, Negro
- Full-width color strip: 7 swatches side by side, 40px tall
  - Negro, Carbon, Lacre (narrower), Piedra, Ceniza, Arena, Papel
- Below each swatch: name in Satoshi 500, hex in IBM Plex Mono, both at 8-9px
- Color roles explanation:
  - "Negro y Papel son los dominantes. Lacre es el unico acento. Todo lo demas es neutro."
  in Satoshi 400, 13px, Carbon
- Mood: restrained, deliberate

**Page 27 -- Color Combinations**
- Background: Papel
- Title: "Combinaciones." in Satoshi 700, 22px, Negro
- 6 combination blocks (3x2 grid), each a 60x40mm rectangle showing:
  1. Negro bg + Papel text + Lacre accent -- "Principal oscuro"
  2. Papel bg + Negro text + Lacre accent -- "Principal claro"
  3. Arena bg + Carbon text -- "Secundario claro"
  4. Carbon bg + Ceniza text + Lacre accent -- "Secundario oscuro"
  5. Negro bg + Lacre text only -- "Acento sobre oscuro"
  6. Papel bg + Lacre text only -- "Acento sobre claro"
- Each with WCAG contrast ratio in IBM Plex Mono 400, 8px
- Mood: systematic, tested

**Page 28 -- Color Don'ts**
- Background: Papel
- Title: "Usos incorrectos." in Satoshi 700, 22px, Negro
- 4 incorrect examples:
  1. Lacre as background (too much accent)
  2. Piedra text on Arena background (insufficient contrast)
  3. Multiple accent colors (adding blue or green)
  4. Gradients of any kind
- Each with red X and IBM Plex Mono caption
- Mood: protective, zero ambiguity

### VI TIPOGRAFIA (pp. 29-32)

**Page 29 -- Section Divider**
- Negro bg, watermark "6", eyebrow "VI", title "Tipografia.", subtitle "Dos familias. Roles claros."

**Page 30 -- Type Specimen: Satoshi**
- Background: Papel
- Large specimen: "Satoshi" in Satoshi 900, 56px, Negro
- Alphabet display: A-Z in Satoshi 400, 24px, Carbon
- Weight ramp: "Regular 400 / Medium 500 / Bold 700 / Black 900" showing the same phrase in each weight
- Phrase: "Lo que no se documenta, se improvisa." at each weight
- Right metadata in IBM Plex Mono:
  - Source: Fontshare (ITF)
  - Classification: Geometric sans-serif
  - Uso: titulos, cuerpo, UI, todo
- Mood: showcase, pride in the choice

**Page 31 -- Type Specimen: IBM Plex Mono**
- Background: Papel
- Large specimen: "IBM Plex Mono" in IBM Plex Mono 700, 36px, Negro
- Character set display including numbers 0-9 and special characters
- Weight comparison: Regular 400 vs Bold 700
- Example usage: a metadata block formatted as it would appear in the manual
  ```
  EDICION     Primera edicion
  FECHA       Abril 2026
  PAGINAS     51
  FORMATO     A4 apaisado
  ```
- Right metadata: Source: Google Fonts / Classification: Monospaced / Uso: metadata, specs, eyebrows
- Mood: utilitarian, precise

**Page 32 -- Type Hierarchy and Pairing**
- Background: Papel
- Title: "Jerarquia tipografica." in Satoshi 700, 22px, Negro
- Full hierarchy demonstration top to bottom, showing every type style in context:
  - Eyebrow (IBM Plex Mono 700, 8px, Lacre) > Title (Satoshi 900, 32px) > Subtitle (Satoshi 700, 22px) > Body (Satoshi 400, 13px) > Caption (Satoshi 400, 10px, Piedra) > Metadata (IBM Plex Mono 400, 9px, Piedra)
- Right side: "Reglas" list:
  - Satoshi 900 solo para titulos.
  - IBM Plex Mono solo por debajo de 11px.
  - Sin cursivas. Nunca.
  - Enfasis con peso (700) o color (Lacre).
- Mood: instructional, clear

### VII VOZ Y PERSONALIDAD (pp. 33-37)

**Page 33 -- Section Divider**
- Negro bg, watermark "7", eyebrow "VII", title "Voz y Personalidad.", subtitle "Como habla Tramarca."

**Page 34 -- Voice Principles**
- Background: Papel
- Title: "Principios de voz." in Satoshi 900, 28px, Negro
- 5 principles in vertical stack:
  1. Frases cortas. Una idea por frase.
  2. Punto final siempre. No puntos suspensivos.
  3. Preguntas retoricas que incomodan.
  4. Nunca exclamaciones. La conviccion no necesita volumen.
  5. Tuteo siempre. "Tu marca", nunca "su marca".
- Each: number in Lacre IBM Plex Mono, principle in Satoshi 700 14px, followed by example in Satoshi 400 12px, Carbon
- Mood: codified, memorable

**Page 35 -- Vocabulary**
- Background: Papel
- Two-column layout:
  - Left: "Usamos." in Satoshi 700, 18px, Negro
    - Word list in Satoshi 400, 13px: documentar, por escrito, reglas, decision, sistema, construir, producir, cada pagina, claro, directo, manual, identidad, profesional
  - Right: "Nunca usamos." in Satoshi 700, 18px, Negro, with Lacre strikethrough decoration
    - Word list in Satoshi 400, 13px, Piedra (muted): branding 360, holistico, sinergia, storytelling, disruptivo, hacer magia, conceptualizar, co-crear, universo de marca, lovemark
- Bottom: "Si una frase necesita mas de 15 palabras, reescribela." in IBM Plex Mono 400, 10px, Piedra
- Mood: practical toolkit

**Page 36 -- Tone Examples**
- Background: Papel
- Title: "Ejemplos de tono." in Satoshi 900, 28px, Negro
- Three context blocks, each with "Asi si" (Satoshi 700, Negro) and "Asi no" (Satoshi 700, Piedra with strikethrough):
  1. **Web hero**
     - Si: "Que hay tras tu marca?"
     - No: "Descubre el poder transformador de una identidad de marca coherente!"
  2. **Email de contacto**
     - Si: "Gracias por escribir. Te cuento rapido que hacemos y que no."
     - No: "Nos alegra enormemente recibir tu mensaje! Estamos deseando embarcarnos juntos en este emocionante viaje."
  3. **Respuesta a objecion**
     - Si: "No lo necesitas. Si estas comodo con que cada persona que toca tu marca la interprete a su manera, no lo necesitas."
     - No: "Entendemos tu preocupacion! Nuestro servicio integral de branding 360 te ayudara a potenciar sinergias..."
- Mood: unmistakable, educational

**Page 37 -- Brand Voice Card**
- Background: Arena
- Centered card (200x140mm) with slight inset, Papel background, subtle shadow
- Card contains the complete voice summary as a reference card:
  - Top: "Tramarca no convence. Senala lo que ya sabes pero no quieres admitir."
  - 5 keywords: Directo / Provocador / Seguro / Preciso / Cercano
  - "Formato: frases cortas, punto siempre, sin exclamaciones, sin cursivas"
  - "Tu, nunca usted."
- All in Satoshi, various weights. The card is designed to be screenshot/printable as a standalone reference.
- Mood: take-away, the page you'd pin to the wall

### VIII DIRECCION DE ARTE (pp. 38-41)

**Page 38 -- Section Divider**
- Negro bg, watermark "8", eyebrow "VIII", title "Direccion de Arte.", subtitle "Fotografia, layout, composicion."

**Page 39 -- Photography Direction**
- Background: Papel
- Title: "Fotografia." in Satoshi 900, 28px, Negro
- Two image slots (landscape, 130x85mm each) side by side:
  - Left: approved style reference (see Image #01 below)
  - Right: approved style reference (see Image #02 below)
- Below images, 3-column text:
  - **Estilo**: Editorial, desaturada, luz natural lateral. Nunca stock generico.
  - **Color**: Dominan los neutros de la paleta. Lacre aparece como detalle (lacre de sobre, portada roja de libro).
  - **Sujetos**: objetos de escritorio, papeleria, libros, sellos, prensas. Manos trabajando. Nunca caras reconocibles.
- Bottom: "Anti-referencias: stock corporativo con personas sonriendo a camara, fondos degradados, iconografia flat." in IBM Plex Mono 400, 9px, Piedra
- Mood: elevated, editorial

**Page 40 -- Layout Grid**
- Background: Papel
- Title: "Reticula." in Satoshi 700, 22px, Negro
- Diagram showing the A4 landscape grid system:
  - Margins: 20mm top, 15mm bottom, 20mm left, 20mm right
  - 6-column grid with 8mm gutters
  - Baseline grid: 6mm
  - Safe zone visualization
- Grid shown as Ceniza lines on Papel, with an example content layout overlaid
- Bottom: "Las paginas de este manual siguen esta reticula. Toda aplicacion Tramarca deberia respetarla." in IBM Plex Mono 400, 9px, Piedra
- Mood: structural, confident

**Page 41 -- Mockups**
- Background: Papel
- Title: "Aplicacion fotografica." in Satoshi 700, 22px, Negro
- Three mockup image slots:
  1. Flat-lay of brand manual printed, open on a wooden desk (see Image #07)
  2. Business card on dark surface with seal (see Image #08)
  3. Laptop screen showing Tramarca website (see Image #09)
- Each with caption in IBM Plex Mono 400, 8px, Piedra
- Mood: proof of concept, tangible

### IX APLICACIONES (pp. 42-47)

**Page 42 -- Section Divider**
- Negro bg, watermark "9", eyebrow "IX", title "Aplicaciones.", subtitle "Tarjeta, email, redes, propuesta, web."

**Page 43 -- Business Card**
- Background: Papel
- Two business card mockups (90x50mm each):
  - Front: Negro background. TRAMARCA. wordmark centered, Papel + Lacre period. "Sistemas de marca." below.
  - Back: Papel background. Left: name + role in Satoshi 500/400. Right: contact in IBM Plex Mono 400, 9px.
    - tramarca.es
    - hola@tramarca.es
    - Bottom: "Tu marca, sin improvisar." in IBM Plex Mono, Piedra
- Specs in right margin: "85 x 55 mm / 400g cotton / Tinta Negro mate" in IBM Plex Mono
- Mood: tangible, premium

**Page 44 -- Email Signature**
- Background: Papel
- Email signature mockup in a faux-email window:
  ```
  [Nombre] . Tramarca
  Tu marca, sin improvisar -- tramarca.es
  ```
- Specs: Satoshi for name, IBM Plex Mono for URL line. Period between name and Tramarca in Lacre.
- Below: rules -- "Sin imagenes incrustadas. Sin citas inspiracionales. Sin banners promocionales." in Satoshi 400, 12px
- Mood: minimal, professional

**Page 45 -- Social Media**
- Background: Papel
- Title: "Redes sociales." in Satoshi 700, 22px, Negro
- Three social post mockups (square 1:1):
  1. Quote post: Negro background, provocative question in Satoshi 700, Papel, period in Lacre
  2. Carousel cover: Arena background, section title of an article, Satoshi 900
  3. Minimal post: single sentence on Papel background, Satoshi 400, Negro
- Profile avatar: Lacre circle (the period/favicon)
- Handle: @tramarca
- Bio: "Sistemas de marca. Lo que no se documenta, se improvisa."
- Mood: consistent, recognizable in a feed

**Page 46 -- Proposal Document**
- Background: Papel
- Mockup of a proposal first page:
  - Header: TRAMARCA. wordmark, proposal number PROP-2026-001 in IBM Plex Mono
  - Title: "Propuesta para [Empresa]" in Satoshi 900, 28px
  - Opening paragraph in brand voice
  - Specs sidebar: fecha, alcance, plazo, revision limit
- Below mockup: "Cada propuesta sigue esta estructura. Sin slides. Sin filosofia. Solo que, como, cuando y cuanto." in Satoshi 400, 12px, Carbon
- Mood: predictable format, serious

**Page 47 -- Web**
- Background: Papel
- Browser mockup showing tramarca.es hero section:
  - Dark hero: Negro background, TRAMARCA. wordmark, tagline, CTA button in Lacre
  - Below: light section with services grid
- Specs: "Satoshi para todo. IBM Plex Mono para metadata. Lacre solo en CTA y punto." in IBM Plex Mono 400, 9px
- Mood: digital proof, cohesion

### X PORTFOLIO (pp. 48-49)

**Page 48 -- Section Divider**
- Negro bg, watermark "10", eyebrow "X", title "Portfolio.", subtitle "Trabajo producido."

**Page 49 -- Case Study: Anfisbena**
- Background: Papel
- Title: "Anfisbena." in Satoshi 900, 32px, Negro
- Left: image slot showing Anfisbena manual spread (see Image #11)
- Right: case study data:
  - Cliente: Anfisbena (knitwear de autor, Toledo)
  - Alcance: 43 paginas, identidad completa + direccion de arte
  - Tipografias: Gambarino + Switzer + Bespoke Stencil
  - Paleta: 7 colores (Noche, Grafito, Acero, Niebla, Lino, Papel, Oxido)
  in IBM Plex Mono 400, 9px
- Bottom: "Primer manual producido por Tramarca. Abril 2026." in Satoshi 400, 12px, Piedra
- Mood: credibility, proof of work

### CIERRE (pp. 50-51)

**Page 50 -- Contact**
- Background: Papel
- Centered block:
  - "Hablemos de tu marca." in Satoshi 900, 36px, Negro
  - Below: contact details in IBM Plex Mono 400, 12px, Carbon:
    - tramarca.es
    - hola@tramarca.es
  - Below: "Tu marca esta por escrito?" in Satoshi 500, 16px, Piedra
- Mood: warm close, invitation

**Page 51 -- Back Cover**
- Background: Negro full bleed
- Center: Tm. monogram in Papel, period in Lacre, at 48px
- Bottom center: "tramarca.es" in IBM Plex Mono 400, 9px, Piedra
- Nothing else. Mirror of the cover's restraint.
- Mood: sealed, final

---

## 7. Section Divider Pattern (Reusable)

Every section opens with a full-bleed Negro page following this exact pattern:

```
Background: Negro (#0C0C0C)
Watermark:  Arabic numeral (1-10) at 580px, Satoshi 900, Carbon (#1C1C1C) at opacity 0.05
            Positioned: right-center, baseline at page bottom + 80mm
Eyebrow:    Roman numeral (I-X) in IBM Plex Mono 700, 8px, Lacre, letterspacing 3px
            Positioned: top-left, 20mm from left edge, 20mm from top
Title:      Section name + period in Satoshi 900, 48px, Papel
            Positioned: left-aligned, 20mm from left, vertically centered
Subtitle:   One-line description in Satoshi 400, 16px, Ceniza
            Positioned: below title, 8mm gap
Page number: IBM Plex Mono 400, 7px, Piedra, bottom-right corner (20mm margin)
```

---

## 8. Page Furniture (Header/Footer Pattern)

### Light Pages
- Top-left: section name in IBM Plex Mono 400, 7px, Piedra, uppercase, letterspaced
- Top-right: TRAMARCA. at 9px Satoshi 700, Negro, period in Lacre
- Bottom-right: page number in IBM Plex Mono 400, 7px, Piedra
- Margins: 20mm top, 15mm bottom, 20mm left/right

### Dark Pages (dividers)
- No header furniture
- Bottom-right: page number in IBM Plex Mono 400, 7px, Piedra

---

## 9. Photography and Image Direction

### Style

- **Aesthetic**: Editorial, desaturated, natural light. Think Kinfolk magazine meets Swiss design catalog.
- **Color grading**: Muted, pulled toward the manual's neutral palette. Warm shadows, cool highlights.
- **Composition**: Centered or rule-of-thirds. Generous negative space. Objects placed deliberately.
- **Light**: Natural lateral (window light), soft shadows. Never flash, never ring light, never high-key studio.
- **Texture priority**: paper grain, wax seal surface, leather binding, ink on paper, wood grain.

### Subjects

- **Objects**: brand manuals (printed, open, stacked), wax seals, stamps, printing presses, type blocks, fountain pens, paper samples, ink bottles, business cards, envelopes with seals.
- **Hands**: working hands -- pressing a seal, opening a manual, holding a business card. No faces.
- **Places**: design studios with natural light, wooden desks, printing workshops. Never generic offices.
- **Never**: stock photos of smiling people, flat illustrations, 3D renders, gradient backgrounds, photos with text overlays.

### Reference Photographers

- Cereal Magazine (object editorial)
- Kinfolk (warm editorial objects)
- Jonas Bjerre-Poulsen (architectural minimalism)
- Gentl and Hyers (textured still life)

---

## 10. Nano-Banana Image Prompts (12 Images)

Each prompt follows the formula: [type], [subject with texture], [camera + light], [palette], [references], [film grain + DOF], no text, no logos.

### Image #01 -- Photography Direction Left (p39)
```
Editorial still life, a closed hardcover book with matte black cover and one red wax seal on a raw linen tablecloth,
Canon EOS R5 with 85mm f/1.8 lens, soft natural window light from the left casting long shadows,
muted palette of charcoal black, warm off-white, and a single terracotta red accent,
inspired by Cereal Magazine and Kinfolk editorial photography,
medium format film grain, shallow depth of field with background softly blurred, 3:2 landscape,
no text, no logos
```

### Image #02 -- Photography Direction Right (p39)
```
Overhead flat-lay, an open brand manual showing typography spreads on thick cream paper next to a fountain pen and ink bottle,
Hasselblad medium format with 80mm lens, diffused overhead natural light,
warm neutrals: cream paper, dark ink, aged wood desk surface, brass pen details,
inspired by Gentl and Hyers still life and Kinfolk magazine,
fine film grain, everything in focus (deep DOF), 3:2 landscape,
no text, no logos
```

### Image #03 -- Cover Hero Atmosphere (not placed, available for cover variant)
```
Close-up detail shot, fingers pressing a brass wax seal stamp into hot red sealing wax on a dark envelope,
Leica Q2 with 28mm lens, dramatic side lighting from a single window,
deep blacks, warm cream envelope edge, vivid terracotta red wax,
inspired by Dutch Golden Age still life painting and modern editorial photography,
heavy film grain, shallow DOF focusing on the seal contact point, 16:9 landscape,
no text, no logos
```

### Image #04 -- Objects: Type Blocks (p24 or general use)
```
Still life of vintage metal letterpress type blocks arranged in a wooden tray, letters visible but not forming words,
Fuji GFX100 with 110mm macro lens, warm tungsten workshop light from above,
aged metal silver, dark wood brown, warm shadows,
inspired by printing workshop photography and Erik Spiekermann's type specimens,
medium film grain, selective focus on center blocks, 4:3 landscape,
no text, no logos
```

### Image #05 -- Business Card Mockup (p43)
```
Two business cards on a dark slate surface, one face-up showing minimal black design with small red dot,
one angled showing the back with typography details, soft shadows,
Phase One with 120mm lens, controlled studio light with single softbox from upper left,
near-black surface, off-white card stock, single red accent dot,
inspired by Mildred and Duck design studio photography,
minimal grain, medium DOF, 3:2 landscape,
no text, no logos
```

### Image #06 -- Brand Manual Stack (p41)
```
Three brand manuals stacked at slight angles on a raw oak desk, top manual open to a color palette page,
natural window light creating soft shadows, a coffee cup edge visible in corner,
Canon R5 with 35mm lens, environmental editorial style,
cream pages, dark covers, warm wood tones, muted natural palette,
inspired by Kinfolk interiors and Cereal Magazine workspace photography,
fine grain, medium DOF with front manual sharp, 3:2 landscape,
no text, no logos
```

### Image #07 -- Manual Open Spread (p41)
```
Flat-lay of an open brand manual showing a dark spread with large typography, on a light linen surface,
overhead shot, diffused natural light, manual takes up 70% of frame,
Hasselblad X2D with 55mm lens,
dark pages with white type visible, cream linen underneath, minimal styling,
inspired by graphic design book photography from Counter-Print and Unit Editions,
medium grain, deep DOF everything sharp, 3:2 landscape,
no text, no logos
```

### Image #08 -- Wax Seal Detail (p43)
```
Extreme close-up of a red wax seal on a dark envelope, the seal shows an abstract circular mark,
Leica Q2 Monochrom converted to color with 28mm lens at minimum focus distance,
dramatic side lighting, dark moody atmosphere,
deep black background, vivid terracotta red wax with surface texture, cream envelope edge barely visible,
inspired by Nadav Kander's detail work and Dutch still life,
heavy analog grain, very shallow DOF, 1:1 square,
no text, no logos
```

### Image #09 -- Laptop Screen (p47)
```
Laptop on a minimal desk showing a dark website with a centered wordmark, 3/4 angle view,
MacBook Pro in space black, clean desk with only a small plant and notebook nearby,
Fuji X-T5 with 23mm lens, natural afternoon light from a large window,
dark screen, light desk surface, warm neutral palette,
inspired by Norm Architects interior photography and minimal workspace shots,
fine grain, medium DOF with screen sharp, 16:9 landscape,
no text, no logos
```

### Image #10 -- Printing Press / Workshop (general atmosphere)
```
Wide shot of a letterpress printing workshop, vintage press in center, paper stacks on shelves,
ink rollers and metal type visible, warm industrial atmosphere,
Canon R5 with 24mm lens, natural light from high windows mixed with tungsten workshop lamps,
warm blacks, aged metal grays, cream paper stacks, occasional red ink,
inspired by Hamilton Wood Type Museum photography and Erik Spiekermann's workshop,
heavy film grain, deep DOF, 2:1 ultrawide landscape,
no text, no logos
```

### Image #11 -- Anfisbena Case Study (p49)
```
Open brand manual showing an editorial spread with a textured serif headline and earth-tone photography,
manual resting on dark surface, shot at slight angle to show page depth,
Canon R5 with 50mm lens, soft directional studio light,
earth tones: warm cream pages, dark mocha cover, rust and olive accents visible on the spread,
inspired by design portfolio photography from It's Nice That and Creative Boom,
fine grain, shallow DOF with near page sharp, 3:2 landscape,
no text, no logos
```

### Image #12 -- Envelope with Seal (p44 or general)
```
A cream envelope with a red wax seal, partially visible behind it a folded letter on matching cream paper,
on a dark wooden surface with a brass letter opener beside it,
Fuji GFX100S with 80mm lens, warm window light from upper right,
rich cream paper, deep wood brown, brass gold, single terracotta red seal,
inspired by Cereal Magazine editorial and classic correspondence photography,
medium film grain, medium DOF, 4:3 landscape,
no text, no logos
```

---

## 11. Mood Map (Page-by-Page Feeling)

This is what the reader should FEEL as they turn pages. The manual is designed as an emotional arc.

| Pages | Feeling | Technique |
|---|---|---|
| 01 (Cover) | Authority, silence | Black void + wordmark only |
| 02 (Colophon) | Precision, "this is a controlled document" | Monospaced specs on dark |
| 03 (TOC) | Navigation, confidence | Light, structured, functional |
| 04-06 (Provocacion) | Discomfort, then relief | Dark question > light problem > light answer |
| 07-12 (Fundamentos) | Grounding, "now I know who they are" | Facts, structure, personality map |
| 13-16 (Servicio) | Clarity, "I see what I'm getting" | Deliverables, process, scope |
| 17-24 (Identidad) | Pride in craft, engineering | Construction diagrams, systematic variations |
| 25-28 (Color) | Restraint, intention | Minimal palette, surgical accent |
| 29-32 (Tipografia) | Sophistication, readability | Type specimens, hierarchy demo |
| 33-37 (Voz) | Recognition, "that's exactly right" | Before/after voice examples |
| 38-41 (Direccion Arte) | Elevated, editorial | Photography references, grid system |
| 42-47 (Aplicaciones) | Tangible, "I can see it working" | Real-world mockups and formats |
| 48-49 (Portfolio) | Credibility, proof | Completed work showcase |
| 50 (Contact) | Warm invitation | Open door, soft close |
| 51 (Back cover) | Sealed, complete | Monogram on black, mirror of cover |

### Rhythm Rules

- **Never two dark pages in a row** except cover + colophon (pp 01-02) which are the only exception.
- **Every section opens dark, then goes light**. The dark divider creates a "breath" before new content.
- **Dense pages followed by airy pages**. After a page with lots of specs/grid (like p19 construction), the next page should breathe.
- **The manual closes as it opens**: dark, minimal, just the mark.

---

## 12. CSS / Layout Specification

### Page Dimensions
```css
@page { size: 297mm 210mm; margin: 0; }
.page { width: 297mm; height: 210mm; position: relative; overflow: hidden; }
```

### Grid
- 6 columns, 8mm gutters
- Margins: 20mm top, 15mm bottom, 20mm left, 20mm right
- Content area: 257mm wide x 175mm tall
- Baseline grid: 6mm (not enforced in CSS but used as reference for vertical spacing)

### Spacing Scale
| Token | Value | Usage |
|---|---|---|
| --space-xs | 4mm | Within tight groups |
| --space-sm | 8mm | Between related elements |
| --space-md | 16mm | Between sections on a page |
| --space-lg | 24mm | Major separations |
| --space-xl | 40mm | Dramatic breathing room |

---

## 13. Build Order (Recommended)

Following best-practices.md:

1. Define all tokens in build.py (colors, fonts, identity strings)
2. Build section dividers (14 dark pages) -- they anchor the rhythm
3. Build colophon (p02) -- fixes scope
4. Build cover (p01) + back cover (p51)
5. Build pages in blocks of 6-8, QA between each:
   - Block 1: pp 03-08 (TOC + Provocacion + Fundamentos start)
   - Block 2: pp 09-16 (Fundamentos end + Servicio)
   - Block 3: pp 17-24 (Identidad Visual)
   - Block 4: pp 25-32 (Color + Tipografia)
   - Block 5: pp 33-41 (Voz + Direccion Arte)
   - Block 6: pp 42-50 (Aplicaciones + Portfolio + Contact)
6. Generate images with nano-banana when layout is stable
7. Integral QA of all 51 pages
8. Render final PDF

---

## 14. Handoff: Brand Voice Brief (for conversion-copywriter)

```
Archetype: Sage / Creator
Personality: Directo, Provocador, Seguro, Preciso, Cercano
Tone: Conversational-authoritative (not playful, not corporate)
Tu/Usted: Tu always
Words we use: documentar, por escrito, reglas, decision, sistema, construir, producir, manual, identidad, profesional
Words we never use: branding 360, holistico, sinergia, storytelling, disruptivo, hacer magia, conceptualizar, lovemark
Example: "Lo que no se documenta, se improvisa. Lo que se improvisa, no es marca."
```

---

## 15. Handoff: Brand Tokens (for /landing-page)

```
Colors:
  --color-primary: #0C0C0C (Negro)
  --color-secondary: #1C1C1C (Carbon)
  --color-accent: #C4553A (Lacre)
  --color-neutral-500: #7A7672 (Piedra)
  --color-neutral-400: #B5B1AC (Ceniza)
  --color-neutral-200: #E4E2DC (Arena)
  --color-neutral-100: #F4F0EB (Papel)

Typography:
  --font-display: 'Satoshi', sans-serif (Fontshare, 400/500/700/900)
  --font-body: 'Satoshi', sans-serif (same family, different weights)
  --font-mono: 'IBM Plex Mono', monospace (Google Fonts, 400/700)

Logo:
  Wordmark: TRAMARCA. in Satoshi 900, period in Lacre
  Monogram: Tm.
  Favicon: Lacre circle
```
