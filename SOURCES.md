# Tramarca Manual v4 — SOURCES.md

Document fidelity reference. Every claim in the manual maps here.

## Legend

- **FIEL** — Extracted verbatim from tramarca.es (the public brand) or from real project artefacts
- **PROPUESTA** — Studio recommendation not yet published but consistent with the system
- **INVENTADO** — Placeholder needing Fernando's sign-off before going public

Any line the manual ships must be tagged; audit rejects untagged claims.

---

## 1 · IDENTITY (FIEL)

| Token | Value | Source |
|---|---|---|
| Brand name | TRAMARCA | tramarca.es masthead |
| Masthead | Tramarca. · Manuales de marca · Por escrito · Desde 2026 · Madrid · Edición 1 | home masthead |
| Descriptor | Tu marca, por escrito. | /home H1 |
| Mantra | Un estudio que solo hace manuales. | /sobre H1 |
| Secondary claim | Lo que no se documenta, se improvisa. | /home hero description |
| Positioning line | Estudio editorial, no agencia creativa. | /sobre paragraph |
| Contact | hola@tramarca.es | /contacto |
| Location | Madrid · España | footer |
| Edition | Primera edición · 2026 | masthead |

## 2 · PALETTE (FIEL — post audit 360 update)

Updated 2026-04-16 after WCAG audit — PIEDRA darkened for AA compliance.

| Token | HEX | Role | Notes |
|---|---|---|---|
| NEGRO | `#0C0C0C` | ink primary | text, wordmark |
| CARBON | `#1C1C1C` | ink secondary | dark surfaces |
| LACRE | `#C4553A` | accent, signature | the period, never a background |
| PIEDRA | `#5E5A57` | muted text AA | was #7A7672 (ratio 3.6:1 fail) |
| PIEDRA_LIGHT | `#7A7672` | decorative only | non-text use |
| CENIZA | `#B5B1AC` | rules, borders | light greys |
| ARENA | `#E4E2DC` | panels | warm neutral |
| PAPEL | `#F4F0EB` | page background | warm paper |

## 3 · TYPOGRAPHY (FIEL)

| Role | Family | Weights | Source |
|---|---|---|---|
| Display + body | Satoshi | 400 · 500 · 700 · 900 | tramarca.es (self-hosted next/font/local) |
| Mono, metadata | IBM Plex Mono | 400 · 700 | tramarca.es |

Load strategy: self-hosted .woff2 with preload (not @import). Fallback adjustFontFallback Arial.

## 4 · TIER PRICING (FIEL — /precios)

| Tier | Price | Pages | Timeline | Key deliverable |
|---|---|---|---|---|
| Esencial | 490€ IVA incl. | 20–25 pp | 5 días laborables | logo + paleta + tipo base + 3 apps |
| Profesional | 990€ IVA incl. | 30–40 pp | 7 días laborables | voz documentada + Figma templates |
| Premium | 1.990€ IVA incl. | 40–50 pp | 10 días laborables | estrategia + libro físico encuadernado |

Guarantee (FIEL): si tras la primera entrega el manual no resuelve lo firmado en brief, devolución 50% del kickoff en 14 días.

Revisions (FIEL): 2 rondas acotadas incluidas.

## 5 · ANATOMY — 12 chapters / 48 components (FIEL /anatomia)

1. **Fundamentos** — Propósito · Visión · Valores · Personalidad
2. **Sistema de logo** — Marca principal · Variantes · Zona de exclusión · Usos incorrectos
3. **Tipografía** — Familia display · Familia texto · Jerarquía · Sistema de escalas
4. **Color** — Primarios · Secundarios + acento · Usos por jerarquía · Valores técnicos
5. **Iconografía** — Sistema de trazo · Tamaños · Colección base · Do & Don'ts
6. **Fotografía** — Dirección visual · Tratamiento · Composición · Moodboard
7. **Voz y tono** — Principios de voz · Registro por canal · Glosario aprobado · Frases prohibidas
8. **Aplicaciones** — Papelería · Digital · Merch · Señalética
9. **Arquitectura de marca** — Marca ↔ producto · Co-branding · Submarcas · Endorsement
10. **Governance** — Checklist de uso · Aprobación · Versionado · Formación del equipo
11. **Marca en movimiento** — Motion del logo · Microinteracciones · Video y reel · Identidad sonora
12. **Extensiones** — Accesibilidad · Sistema digital · Territorial · Legal y marca registrada

## 6 · PROCESS (FIEL /contacto)

01 · Rellena formulario — cliente envía brief
02 · Respuesta 24h — propuesta + link Stripe
03 · Kickoff 48h — firma brief + arranca contador del tier

Timelines FIEL: 5 / 7 / 10 días laborables por tier.
Revisiones FIEL: 2 rondas incluidas.
Refund FIEL: 50% kickoff / 14 días si la primera entrega no resuelve el brief.

## 7 · "QUÉ ENTREGAMOS" (FIEL /home)

- PDF A4 landscape editable
- Biblioteca Figma con variables
- SVG + PNG @1x/2x/3x
- Tokens CSS + tipografía documentada

## 8 · PORTFOLIO — 5 manuales (FIEL /manuales)

| Cliente | Tier | Páginas | Sector |
|---|---|---|---|
| Anfisbena | Profesional | 43pp | Cultural institutional |
| Claramel | Esencial | 29pp | Artisanal product |
| Matraz Innova | Profesional | 33pp | Deeptech B2B |
| Shamusic | Premium | 46pp | Music-tech platform |
| Tramarca | Proprietary | 34pp → v4 this document | Meta — studio's own |

## 9 · PERSONAS (PROPUESTA — requires Fernando sign-off)

3 archetypes extracted from /sobre + audit sessions. Not published on web — studio internal.

### A · Fundadora SaaS solo
- Perfil: solo-founder bootstrapping una app B2B, 1-5 empleados
- JTBD: "Necesito que mi marca parezca profesional cuando pitcho inversión o firmo con el primer cliente enterprise"
- Stat tensionales (PROPUESTA):
  - 68% improvisa assets cada sprint
  - 3+ fuentes distintas en la misma landing
  - 0 sistema documentado
- Trigger: deck de inversores; onboarding enterprise; primer rebrand post-PMF
- Canal: Twitter/X + referido via community Slack
- Tier: Esencial o Profesional

### B · Consultora freelance
- Perfil: freelance 3+ años de trayectoria lanzando producto propio o subiendo rates
- JTBD: "Voy a cobrar 3x, necesito que la marca esté a la altura del precio"
- Stat tensionales (PROPUESTA):
  - 80% de freelances operan sin manual
  - +40% conversión esperada al nivelar precio/marca
  - 7 días hasta kickoff
- Trigger: cambio de posicionamiento; primer contrato retainer; lanzamiento nuevo producto
- Canal: LinkedIn + referidos clientes
- Tier: Profesional

### C · Estudio partner (sector: agencia pequeña, estudio de diseño, dev shop)
- Perfil: fundador de agencia/estudio 5-15 empleados que externaliza branding porque no es su core
- JTBD: "Necesito un partner que produzca manuales para mis clientes; yo aporto la relación, ellos el rigor editorial"
- Stat tensionales (PROPUESTA):
  - 12-18k€ coste oculto de producir in-house
  - 2-3 manuales/año de volumen recurrente
  - 0% conflicto de canal (Tramarca no compite por servicios)
- Trigger: cliente pide rebrand que el estudio no quiere hacer solo; white-label; margen sobre 1990€
- Canal: referido por agencia o Awwwards/Brandemia
- Tier: Premium (repetido)

## 10 · OBSERVATIONS / RULES ENCODED

- Cover v9 discipline (Shamusic v6): NO mantra on cover, NO chrome (metastrip/vertical), NO roman numerals on cover. Cover = typographic logo + hairline + italic subtitle + 2026.
- Every page ships a fidelity badge if making a claim (FIEL / PROPUESTA).
- Spread 00 "Estado del sistema" at p02-03: what's FIEL vs PROPUESTA vs INVENTADO in this very document.
- TL;DR V9 on last content page (before back cover): 10 rules max.
- Metastrip always `position:absolute !important; z-index:99;` to survive `.grain > *` override bug from toolkit.
- Logo is typographic (Satoshi Black + Lacre period). No PNG — rendered via CSS always.

---

**Last updated**: 2026-04-17
