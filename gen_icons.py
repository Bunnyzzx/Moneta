"""Gera os icones PWA do Moneta a partir do tema do app."""
import os
from PIL import Image, ImageDraw, ImageFont


def lerp(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def make_icon(size, path, maskable=False):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # fundo com gradiente diagonal roxo -> verde (cores do app)
    roxo = (124, 92, 255)
    verde = (0, 212, 166)
    for y in range(size):
        for x in range(0, size, 1):
            pass  # placeholder; gradiente feito por linhas abaixo
    # gradiente por linhas diagonais (rapido o suficiente)
    grad = Image.new("RGB", (size, size))
    gd = grad.load()
    for y in range(size):
        for x in range(size):
            t = (x + y) / (2 * size)
            gd[x, y] = lerp(roxo, verde, t)

    # canto arredondado (icone normal) ou quadrado cheio (maskable)
    mask = Image.new("L", (size, size), 0)
    md = ImageDraw.Draw(mask)
    if maskable:
        md.rectangle([0, 0, size, size], fill=255)
    else:
        radius = int(size * 0.22)
        md.rounded_rectangle([0, 0, size, size], radius=radius, fill=255)

    img.paste(grad, (0, 0), mask)

    # letra "M" central
    draw = ImageDraw.Draw(img)
    # area segura menor no maskable (icone pode ser cortado em circulo)
    fsize = int(size * 0.5) if maskable else int(size * 0.62)
    font = None
    for fname in ("segoeuib.ttf", "arialbd.ttf", "arial.ttf"):
        try:
            font = ImageFont.truetype(fname, fsize)
            break
        except OSError:
            continue
    if font is None:
        font = ImageFont.load_default()

    text = "M"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pos = ((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1])
    # leve sombra
    draw.text((pos[0] + size * 0.01, pos[1] + size * 0.01), text,
              font=font, fill=(0, 0, 0, 90))
    draw.text(pos, text, font=font, fill=(255, 255, 255, 255))

    img.save(path)
    print("gerado:", path)


os.makedirs("icons", exist_ok=True)
make_icon(192, "icons/icon-192.png")
make_icon(512, "icons/icon-512.png")
make_icon(512, "icons/icon-maskable-512.png", maskable=True)
make_icon(180, "icons/apple-touch-icon.png")
make_icon(32, "icons/favicon-32.png")
