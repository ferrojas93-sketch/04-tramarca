# TRAMARCA. Manual de marca — Proceso

## Cronologia

### Sesion 1 — v2 rechazada
- 51 paginas, tecnicamente correctas pero visualmente planas
- "Soso de cojones, sin personalidad, sin wow factor"
- Copy y tono buenos — el problema era 100% visual

### Sesion 2 — Proof v3 aprobado
- Toolkit v3: CSS brutal (clip-path, gradients, noise SVG, diagonal cuts)
- Proof 7 paginas — "joder esto si!"
- Estructura condensada: 51 → 34 paginas
- Skill /visual-qa creada

### Sesion 3 — Build v3 + cinematic upgrade
- 34 paginas construidas con nivel v3
- 6 imagenes branded generadas (escenas con la marca viviendo en contexto)
- 12 screenshots reales de portfolio (Anfisbena, Claramel, Matraz Innova)
- Cinematic spreads: full-bleed fotos + gradient overlay + CSS mockups

#### Upgrade aplicaciones (p27-p32)
| Pagina | Cambio clave |
|---|---|
| p27 | Divider con stationery flatlay de fondo |
| p28 | Tarjeta anverso (Papel, contraste) + reverso (logo, Lacre, personalidad) |
| p29 | Email recto con browser chrome sobre laptop background |
| p30 | Factura recta sobre letterhead background |
| p31 | Social (phone Instagram) + Propuesta en split |
| p32 | Portfolio en filas horizontales con screenshots reales |

#### Skill /visual-qa actualizada — 6 reglas nuevas
1. Min 9px en print (antes 7px)
2. Mockups de marca SIEMPRE rectos (rotate = BLOCKER)
3. Verificar contraste dentro del mockup, no de la pagina
4. Rotacion + tamano grande = clipeo por bordes
5. Portfolio: min 40mm por imagen, sin solapar contenido
6. Mockups con min 2 elementos identitarios (logo, acento, separador)

---

## Errores y aprendizajes

| Error | Severidad | Aprendizaje |
|---|---|---|
| Texto superpuesto sobre swatches | BLOCKER | Nunca position:absolute sobre contenido variable |
| Claim tarjeta a 6.5px sobre Negro | BLOCKER | Min 9px, contraste dentro del mockup |
| Email/factura rotados | BLOCKER | Ejemplos oficiales siempre rectos |
| Portfolio imagenes 56mm solapadas | MAJOR | Min 40mm, sin ocultar contenido |
| Reverso tarjeta plano | MAJOR | Min 2 elementos identitarios por mockup |
| QA mecanico (v2) | CRITICAL | Auditar VISUALMENTE con screenshots |
| Specs foto a 10px | MAJOR | Min 12px para specs en print |

---

## Stack

- **Pipeline**: Python → HTML → Playwright → PDF
- **Formato**: A4 landscape (297x210mm)
- **Imagenes**: nano-banana (Gemini 2.5 Flash, gratis)
- **Portfolio**: Screenshots reales via Playwright
- **QA**: /visual-qa skill

## Archivos

| Archivo | Rol |
|---|---|
| `src/build_v3.py` | Build actual — 34 paginas |
| `src/toolkit.py` | Design system v3 |
| `dist/tramarca-v3.pdf` | PDF final 29MB, 34pp |
| `dist/assets/branded/` | 6 imagenes de escena |
| `dist/assets/portfolio/` | 12 screenshots reales |
