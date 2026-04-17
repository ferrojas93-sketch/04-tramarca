"""
Generate brand manual imagery via Gemini 2.5 Flash Image (nano-banana, FREE).
Outputs to dist/assets/generated/*.png
"""
from __future__ import annotations
import base64, json, os, sys, time
from pathlib import Path
import urllib.request
from PIL import Image

# Claude multi-image reads reject >2000px. All generated images downscaled to 1800px.
MAX_EDGE = 1800

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "assets" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

ENV = Path.home() / ".nano-banana" / ".env"
API_KEY = next(
    line.split("=", 1)[1].strip()
    for line in ENV.read_text().splitlines()
    if line.startswith("GEMINI_API_KEY=")
)

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent"


def gen(prompt: str, outfile: str) -> None:
    target = OUT / outfile
    if target.exists() and target.stat().st_size > 50_000:
        print(f"  SKIP {outfile} (exists)")
        return
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }).encode("utf-8")
    req = urllib.request.Request(
        URL,
        data=payload,
        headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  FAIL {outfile}: {e}")
        return
    cands = data.get("candidates", [])
    if not cands:
        print(f"  FAIL {outfile}: no candidates — {json.dumps(data)[:200]}")
        return
    for part in cands[0].get("content", {}).get("parts", []):
        if "inlineData" in part:
            target.write_bytes(base64.b64decode(part["inlineData"]["data"]))
            # Downscale to stay under Claude's 2000px limit on multi-image reads.
            try:
                im = Image.open(target)
                if max(im.size) > MAX_EDGE:
                    im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
                    im.save(target, optimize=True)
            except Exception as e:
                print(f"  WARN {outfile}: resize failed: {e}")
            print(f"  OK   {outfile}: {target.stat().st_size // 1024} KB · {im.size}")
            return
    print(f"  FAIL {outfile}: no inline image")


# ── Prompts ──
JOBS = [
    ("cover-dark.png",
     "Extreme macro photograph of matte black uncoated cardstock paper 300gsm "
     "filling the frame. Subtle fiber texture visible only in raking light from "
     "the left. Deep rich black, no reflections, no text, no objects. Editorial "
     "still-life, cold flat daylight, contemporary minimal, studio photography. "
     "3:2 landscape aspect ratio."),

    ("divider-concrete.png",
     "Close-up architectural photograph of raw polished concrete wall, cold "
     "grey, subtle stains and aggregate detail, no cracks, no text, no objects. "
     "Flat north-light diffused daylight. Contemporary minimal, Herzog & de "
     "Meuron aesthetic. Muted cool neutrals. Pure wall filling frame. 3:2 landscape."),

    ("divider-steel.png",
     "Close-up of brushed stainless steel surface filling the frame. Visible "
     "fine brushed grain texture, cold flat daylight producing muted "
     "non-specular reflection, no hotspots, no fingerprints, no text, no "
     "objects. Industrial minimal, Swiss design aesthetic, contemporary "
     "editorial. 3:2 landscape."),

    ("divider-paper-dark.png",
     "Macro photograph of matte black textured paper with a single clean "
     "horizontal fold running across the middle. Flat diffused cold daylight, "
     "subtle fiber texture, no text, no objects. Editorial minimal, "
     "contemplative, contemporary, Pentagram aesthetic. 3:2 landscape."),

    ("persona-a-saas.png",
     "Editorial portrait photograph of a woman in her early thirties, Spanish, "
     "short dark hair, wearing a plain charcoal grey knit sweater, sitting at a "
     "minimal desk with one laptop, natural daylight from the left, shallow "
     "depth of field. Cold neutral tones, desaturated. Shot waist-up, slight "
     "three-quarter angle. Contemporary editorial photography, Monocle magazine "
     "aesthetic. Thoughtful expression, not smiling. Blurred warm-neutral office "
     "background. 3:2 landscape."),

    ("persona-b-freelance.png",
     "Editorial portrait photograph of a woman in her mid thirties, Spanish, "
     "longer brown hair tied back, wearing a beige blazer over a simple "
     "off-white shirt, standing in a minimal studio with a warm off-white wall "
     "behind her. Soft natural daylight, no hotspots. Shot waist-up, "
     "three-quarter angle. Contemporary editorial photography, Monocle magazine "
     "aesthetic. Confident expression, not smiling. Desaturated warm neutrals. "
     "3:2 landscape."),

    ("persona-c-partner.png",
     "Editorial portrait photograph of a man in his late thirties, Spanish, "
     "short dark hair with some grey, minimal beard, wearing a plain black "
     "crew-neck sweater, standing against a pale concrete wall. Cold flat "
     "daylight, desaturated. Shot chest-up, direct angle. Contemporary editorial "
     "photography, Monocle magazine aesthetic. Steady neutral expression, not "
     "smiling. 3:2 landscape."),

    # ── Chapter dividers — themed imagery v2 (no repeats) ──

    ("div-provocacion.png",
     "Extreme macro photograph of a single clean, deep circular deboss mark pressed "
     "into matte warm off-white uncoated cardstock 300gsm. The deboss is precise, "
     "casting a crisp circular shadow. Raking cold daylight from 15 degrees left "
     "reveals the depth of the impression. Subtle paper fiber texture visible. No "
     "text, no ink, no other marks. Editorial still-life, contemporary minimal, "
     "Stripe Press monograph aesthetic. 3:2 landscape, centered composition with "
     "negative space."),

    ("div-fundamentos.png",
     "Overhead flat-lay on cold grey polished concrete surface: three precision "
     "tools arranged loosely — a brushed stainless steel caliper (partially open, "
     "showing 20mm), a small metal drafting compass, a black triangular set-square. "
     "Tools slightly overlap. Flat cold north-light daylight, desaturated, "
     "contemporary editorial photography. No hands, no labels, no text. "
     "Industrial-minimal, reductive. 3:2 landscape."),

    ("div-logo.png",
     "Technical blueprint photograph: a sheet of warm off-white paper lying flat, "
     "showing a precise grid of thin pale pencil construction lines drawn freehand "
     "with a ruler. Overlaid on the grid: a single small matte-black rectangular "
     "logo placeholder with one tiny terracotta red dot aligned to the baseline. "
     "Flat cold diffused daylight, close-up, editorial still-life, contemporary "
     "minimal, Pentagram aesthetic. No words, no numbers. 3:2 landscape."),

    ("div-tipografia.png",
     "Extreme macro photograph of a printed type specimen sheet: massive lowercase "
     "letter 'a' in sharp black Satoshi-style sans-serif, filling most of the frame. "
     "Matte warm off-white uncoated paper background with subtle fiber texture. "
     "Flat cold daylight. Single letter occupies 70% of the composition. No other "
     "text. Editorial, contemporary, Stripe Press / Pentagram specimen aesthetic. "
     "3:2 landscape."),

    ("div-iconografia.png",
     "Close-up photograph of a brushed stainless-steel plate, 20x15cm, lying flat. "
     "Eight simple abstract line-art marks etched into its surface in a precise 4x2 "
     "grid: a horizontal line, a vertical line, a small circle, a small square, a "
     "plus sign, a triangle outline, an X mark, and a dot. Etchings are shallow, "
     "shadowed, monochrome. Flat cold overhead daylight producing muted reflection. "
     "No hotspots, no fingerprints, no text. Industrial Swiss-modern. 3:2 landscape."),

    ("div-fotografia.png",
     "Close-up editorial photograph of a matte-black vintage film camera lens "
     "lying on its side on a cold grey polished concrete surface. Focus on the "
     "lens front element and numeric scale rings. Cold flat diffused daylight, "
     "desaturated, no specular highlights. Single object centered, generous "
     "negative space. Contemporary editorial, reductive, Monocle aesthetic. "
     "No text readable, no branding. 3:2 landscape."),

    ("div-voz.png",
     "Macro photograph of vintage typewriter keys, extreme close-up of three or "
     "four black round key caps. Cold flat overhead daylight. Matte finish, fine "
     "dust showing age, but clean. Desaturated cool tones, no warm nostalgia, no "
     "sepia. Contemporary editorial still-life, Pentagram aesthetic. Letters on "
     "keys blurred or abstract so NO specific word is readable. 3:2 landscape."),

    ("div-arquitectura.png",
     "Architectural photograph of a modular wood-and-steel shelving unit against "
     "a pale warm off-white wall. Clean regular 4x3 open grid of empty compartments. "
     "Flat cold north-light diffused daylight, soft shadows. No objects on shelves, "
     "no text, no clutter. Contemporary minimal, Herzog & de Meuron / Pentagram "
     "aesthetic. Desaturated warm neutrals. 3:2 landscape."),

    ("div-governance.png",
     "Overhead flat-lay on warm off-white paper surface: a small neat stack of "
     "three or four manila archival folders with slightly offset edges, each "
     "bearing a single thin horizontal terracotta red label stripe (no text). "
     "Flat cold daylight, desaturated warm neutrals, contemporary editorial "
     "still-life. No hands, no labels readable, no clutter. Pentagram aesthetic. "
     "3:2 landscape."),

    ("div-motion.png",
     "Long-exposure photograph of a single thin terracotta red horizontal line "
     "streaking across a matte black background, slight motion blur on both ends, "
     "bright sharp in the middle. Extreme minimal, abstract, cinematic still. "
     "Editorial contemporary, Stripe Press aesthetic. No text, no objects. "
     "3:2 landscape."),

    ("div-servicio.png",
     "Overhead flat-lay on warm off-white paper: a neat small stack of four "
     "matte-black uncoated business cards, slightly fanned, top card showing a "
     "single tiny centered terracotta red dot (no text). Flat cold diffused "
     "daylight, subtle shadows. Contemporary editorial still-life, desaturated. "
     "No other objects, no hands. 3:2 landscape."),

    ("hero-logos-chaos.png",
     "Overhead flat-lay on cold grey concrete surface: a messy scattered spread "
     "of eight different loose printed logo mockups on various small white paper "
     "cards, overlapping randomly, none aligned. Each card shows a different "
     "abstract geometric brand mark (circles, squares, lines, dots — no letters, "
     "no words). Flat cold daylight, desaturated, editorial still-life. Implies "
     "brand inconsistency / fragmentation. Pentagram aesthetic. 3:2 landscape."),

    # ── Replacement round (session 2026-04-17 second review) ──

    ("cover-hero.png",
     "Editorial photograph of a matte black hardcover book lying closed on "
     "warm off-white uncoated paper surface, shot three-quarter angle from "
     "above. Clean book spine visible, no text, no branding, no marks. Single "
     "tiny terracotta red dot (8mm diameter, flat ink) positioned on the cover "
     "dead center. Flat cold diffused north-light daylight, desaturated, zero "
     "warm tones. Reductive minimal, Pentagram aesthetic. Contemporary editorial "
     "still-life. 3:2 landscape portrait-ratio crop, empty space around the "
     "book (~40 percent negative space)."),

    ("div-logo-v2.png",
     "Close-up editorial photograph of a typographic construction sketch on a "
     "matte warm off-white paper: hand-drawn pencil grid lines with a single "
     "bold sans-serif letterform being constructed with ruler and compass marks, "
     "pencil shavings scattered minimally. Cold flat daylight, desaturated, "
     "reductive. Suggests the craft of logo construction. Contemporary editorial, "
     "Pentagram aesthetic. Very close-up macro, shallow depth of field. "
     "3:2 landscape. No readable text, no complete letterforms."),

    ("div-personas.png",
     "Editorial photograph of three empty minimalist wooden chairs arranged "
     "facing slightly inward on a cold grey polished concrete floor, against "
     "a pale warm off-white wall. Clean contemporary Scandinavian aesthetic. "
     "Flat cold north-light diffused daylight, desaturated. No people, no "
     "objects on chairs, no clutter. Suggests audience / archetypes without "
     "literal figures. Monocle magazine still-life. 3:2 landscape."),

    ("div-fotografia-v2.png",
     "Overhead flat-lay on warm off-white paper: a classic photographic contact "
     "sheet of black-and-white 35mm negatives, 6 rows of 6 small frames visible, "
     "some frames faintly showing abstract architectural shadows and patterns (no "
     "recognizable faces, no objects, no text readable). Next to the contact "
     "sheet, a matte-black loupe magnifier and a thin terracotta red grease "
     "pencil. Flat cold diffused daylight, editorial still-life, contemporary "
     "minimal. 3:2 landscape."),

    ("div-aplicaciones.png",
     "Overhead flat-lay on warm off-white paper surface: a clean editorial "
     "composition of printed brand collateral — a folded letter on white paper, "
     "a matte-black business card with a tiny red dot, a kraft paper envelope, "
     "and a folded cotton label. Items overlap loosely at right angles. Flat "
     "cold diffused daylight, desaturated warm neutrals. No text readable on "
     "any item, no branding marks. Contemporary editorial still-life, "
     "Pentagram aesthetic. 3:2 landscape."),

    ("div-motion-v2.png",
     "Chronophotography editorial still: a single matte-black sphere captured "
     "in 5 sequential positions across a cold grey concrete surface, left to "
     "right, each position slightly blurred suggesting motion. Single thin "
     "terracotta red horizontal line traces the path between all positions. "
     "Flat cold daylight, desaturated, cinematic minimal. Abstract still "
     "from a brand motion reel. No text, no objects. 3:2 landscape."),

    ("div-servicio-v2.png",
     "Overhead editorial still-life on a cold grey concrete desk surface: a "
     "neatly wrapped kraft paper package tied with twine, sealed with a single "
     "matte terracotta red wax seal (clean circular, no insignia visible). "
     "Next to it, a folded card and a black fountain pen lying at a right "
     "angle. Flat cold diffused daylight, desaturated warm neutrals, contemporary "
     "editorial, Pentagram aesthetic. Zero warm nostalgia, no sepia. 3:2 "
     "landscape."),

    # ── Round 3 replacements (session 2026-04-18) ──

    ("div-color-v2.png",
     "Editorial macro photograph of a painter's mixing palette (matte white "
     "ceramic rectangle, 20x14cm) seen overhead on a cold grey concrete "
     "surface. On the palette: seven distinct small pools of matte flat "
     "gouache paint — one deep matte black, one charcoal, one terracotta red, "
     "one warm stone grey, one cool ceniza grey, one warm sand, one warm "
     "off-white. No brushes, no text. Clean, ordered, not messy. Flat cold "
     "diffused daylight, desaturated. Contemporary editorial still-life, "
     "Pentagram / Wim Crouwel aesthetic. 3:2 landscape."),

    ("div-fotografia-v3.png",
     "Editorial black-and-white photograph of a photographer's darkroom "
     "workspace overhead: a light table (milky acrylic glowing from below), "
     "a strip of 35mm black-and-white negatives laid across it, a matte-black "
     "loupe magnifier, and a red grease pencil. Abstract architectural "
     "shadows barely visible in the negatives — no recognizable faces or "
     "text. Cold cinematic lighting, strong silver-grey palette. Contemporary "
     "editorial, Stripe Press aesthetic. 3:2 landscape."),

    ("div-voz-v2.png",
     "Macro editorial photograph of a matte off-white paper sheet lying flat, "
     "with a single horizontal line of handwritten ink annotations in matte "
     "black fountain pen — elegant cursive strokes forming abstract marks "
     "and editorial proofreading symbols (tildes, crossings, carets) but NO "
     "readable words or letters. Subtle terracotta red underline beneath one "
     "mark. Flat cold diffused daylight, desaturated, paper fiber texture "
     "visible. Contemporary editorial still-life, literary minimal. 3:2 "
     "landscape."),

    # ── Round 4 replacements (session 2026-04-18) ──

    ("div-fotografia-v4.png",
     "Abstract editorial photograph: a grid of sixteen small square black-and-"
     "white photographic prints (4x4 arrangement) pinned to a cold grey "
     "concrete wall. Each print shows a different abstract minimalist "
     "composition — a shadow, a line, a corner, a diagonal, a texture, a "
     "fragment of architecture. Zero recognizable people, no text, no objects "
     "with brand marks. Soft cold daylight. Pentagram / Wolfgang Tillmans "
     "grid aesthetic. Cinematic, reductive. 3:2 landscape."),

    ("div-voz-v3.png",
     "Editorial still-life macro: an open matte off-white paper notebook "
     "page showing a single bold handwritten horizontal quotation mark in "
     "black ink (simple geometric dash with slight ink bleed), next to it a "
     "thin terracotta red editorial mark (a caret or tilde). Paper fiber "
     "texture visible, no readable words. Composition centered with generous "
     "negative space. Flat cold diffused daylight, desaturated, contemporary "
     "editorial, literary minimal, Pentagram aesthetic. 3:2 landscape."),
]


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    for outfile, prompt in JOBS:
        if arg and arg not in outfile:
            continue
        print(f"→ {outfile}")
        gen(prompt, outfile)
        time.sleep(2)
    print("DONE")
