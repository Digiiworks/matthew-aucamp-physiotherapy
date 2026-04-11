"""Generate a single OG social card for Matthew Aucamp Physiotherapy.

Produces site/assets/images/og-image.jpg (1200x630) used as the shared
OG/Twitter image across all pages.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
OUT = ASSETS / "images" / "og-image.jpg"

W, H = 1200, 630
PRIMARY = (11, 79, 138)
PRIMARY_DARK = (8, 57, 102)
ACCENT = (46, 173, 108)
WHITE = (255, 255, 255)
MUTED = (203, 219, 236)

FONT_TITLE = ASSETS / "fonts" / "montserrat-800-latin.woff2"
FONT_SUB = ASSETS / "fonts" / "montserrat-600-latin.woff2"
FONT_SMALL = ASSETS / "fonts" / "inter-500-latin.woff2"


def load_font(path: Path, size: int):
    """Pillow can't read woff2 directly — fall back to a TTF system font."""
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        for candidate in [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/Library/Fonts/Arial.ttf",
        ]:
            if Path(candidate).exists():
                return ImageFont.truetype(candidate, size)
        return ImageFont.load_default()


def make_gradient(w: int, h: int, top, bottom):
    base = Image.new("RGB", (1, h), PRIMARY)
    px = base.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        px[0, y] = (
            int(top[0] + (bottom[0] - top[0]) * t),
            int(top[1] + (bottom[1] - top[1]) * t),
            int(top[2] + (bottom[2] - top[2]) * t),
        )
    return base.resize((w, h))


def circular_photo(path: Path, size: int) -> Image.Image:
    img = Image.open(path).convert("RGB")
    s = min(img.size)
    left = (img.width - s) // 2
    top = (img.height - s) // 2
    img = img.crop((left, top, left + s, top + s)).resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def main() -> None:
    canvas = make_gradient(W, H, PRIMARY, PRIMARY_DARK).convert("RGBA")
    draw = ImageDraw.Draw(canvas)

    # Soft radial highlight top-left
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-200, -300, 700, 500), fill=(26, 115, 197, 90))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    canvas = Image.alpha_composite(canvas, glow)
    draw = ImageDraw.Draw(canvas)

    # Left accent bar
    draw.rectangle((0, 0, 10, H), fill=ACCENT)

    # Photo on the right
    photo_size = 380
    photo_path = ASSETS / "images" / "matthew.jpg"
    if photo_path.exists():
        photo = circular_photo(photo_path, photo_size)
        ring = Image.new("RGBA", (photo_size + 24, photo_size + 24), (0, 0, 0, 0))
        ImageDraw.Draw(ring).ellipse(
            (0, 0, photo_size + 24, photo_size + 24), outline=ACCENT, width=6
        )
        px, py = W - photo_size - 90, (H - photo_size) // 2
        canvas.paste(ring, (px - 12, py - 12), ring)
        canvas.paste(photo, (px, py), photo)
        draw = ImageDraw.Draw(canvas)

    # Text block (left column)
    x = 80
    y = 150

    # Small eyebrow label
    eyebrow_font = load_font(FONT_SMALL, 24)
    draw.text((x, y), "PHYSIOTHERAPY · GQEBERHA", font=eyebrow_font, fill=ACCENT)
    y += 48

    # Title
    title_font = load_font(FONT_TITLE, 66)
    draw.text((x, y), "Matthew Aucamp", font=title_font, fill=WHITE)
    y += 78
    draw.text((x, y), "Physiotherapy", font=title_font, fill=WHITE)
    y += 104

    # Accent underline
    draw.rectangle((x, y, x + 120, y + 5), fill=ACCENT)
    y += 30

    # Subtitle
    sub_font = load_font(FONT_SUB, 28)
    draw.text(
        (x, y),
        "DBC Certified Back & Neck Expert",
        font=sub_font,
        fill=MUTED,
    )

    # Footer URL
    url_font = load_font(FONT_SMALL, 22)
    draw.text(
        (x, H - 70),
        "matthewaucampphysio.co.za",
        font=url_font,
        fill=WHITE,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
