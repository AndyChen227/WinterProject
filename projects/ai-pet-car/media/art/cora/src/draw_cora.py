#!/usr/bin/env python3
"""小橙 Cora 立绘生成脚本：输出 cora.svg（600x600 矢量图）。

运行：python3 draw_cora.py
"""
import os

def mx(d):
    """Mirror an SVG path's x coordinates around x=300 (only absolute M/L/C/Q/Z with numbers)."""
    out, toks = [], d.replace(",", " , ").split()
    expect_x = True
    for t in toks:
        try:
            v = float(t)
        except ValueError:
            out.append(t)
            if t != ",":
                expect_x = True
            continue
        if expect_x:
            out.append(f"{600 - v:g}")
        else:
            out.append(f"{v:g}")
        expect_x = not expect_x
    return " ".join(out).replace(" , ", ", ")


LINE = "#6E3624"
HAIR_D = "#D2683C"
SKIN = "#FFEBDF"
SKIN_D = "#F7CDBA"
CORAL = "#EE7A55"
CREAM = "#FFFBF4"
SLATE = "#3E4466"
GOLD = "#F4B544"


def P(d, fill, sw=2.6, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{LINE}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'


def star(x, y, r, fill=GOLD, sw=2):
    k = r * 0.22
    d = (f"M {x} {y-r} Q {x+k} {y-k} {x+r} {y} Q {x+k} {y+k} {x} {y+r} "
         f"Q {x-k} {y+k} {x-r} {y} Q {x-k} {y-k} {x} {y-r} Z")
    return P(d, fill, sw)


def both(d, fill, sw=2.6, extra=""):
    return P(d, fill, sw, extra) + P(mx(d), fill, sw, extra)


def line(d, color, w, op=1.0):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" opacity="{op}"/>'


DEFS = """
<defs>
  <linearGradient id="hairG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#F0814E"/><stop offset="0.6" stop-color="#F89A66"/><stop offset="1" stop-color="#FFC3A0"/>
  </linearGradient>
  <linearGradient id="backG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#DA6E40"/><stop offset="1" stop-color="#F6A57A"/>
  </linearGradient>
  <linearGradient id="irisG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#6A260C"/><stop offset="0.45" stop-color="#D0641F"/><stop offset="1" stop-color="#FFC765"/>
  </linearGradient>
  <radialGradient id="blushG">
    <stop offset="0" stop-color="#FF9C9C" stop-opacity="0.75"/><stop offset="1" stop-color="#FF9C9C" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="bgG" cx="0.5" cy="0.4" r="0.75">
    <stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#FFE7D6"/>
  </radialGradient>
  <linearGradient id="deskG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFF6EC"/><stop offset="1" stop-color="#F6DCC6"/>
  </linearGradient>
  <filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>
  <clipPath id="faceClip"><path d="M 140 250 C 136 372, 210 436, 300 436 C 390 436, 464 372, 460 250 Z"/></clipPath>
</defs>"""

FACE = "M 140 250 C 136 372, 210 436, 300 436 C 390 436, 464 372, 460 250 Z"


def back_hair():
    d = ("M 300 96 C 150 96, 92 190, 100 310 C 106 400, 80 460, 92 530 C 98 566, 120 580, 140 572 "
         "L 460 572 C 480 580, 502 566, 508 530 C 520 460, 494 400, 500 310 C 508 190, 450 96, 300 96 Z")
    s = P(d, "url(#backG)", 2.8)
    return s


def body():
    s = ""
    # neck (very short)
    s += P("M 284 424 L 284 448 L 316 448 L 316 424 Z", SKIN, 2.2)
    # torso: small rounded
    s += P("M 210 560 C 210 500, 236 452, 300 448 C 364 452, 390 500, 390 560 Z", CREAM, 2.6)
    # slate pinafore
    s += P("M 238 560 C 240 520, 252 494, 262 486 L 338 486 C 348 494, 360 520, 362 560 Z", SLATE, 2.4)
    s += line("M 300 492 L 300 556", "#2C3150", 2)
    for y in (508, 528):
        s += f'<circle cx="300" cy="{y}" r="4" fill="#F4B544" stroke="{LINE}" stroke-width="1.4"/>'
    # round collar
    s += both("M 300 448 C 280 448, 254 452, 248 466 C 244 482, 270 494, 290 484 C 298 478, 300 468, 300 456 Z", "#FFFFFF", 2.4)
    s += line("M 254 470 C 262 482, 280 484, 292 474", CORAL, 2.2, 0.85)
    s += line(mx("M 254 470 C 262 482, 280 484, 292 474"), CORAL, 2.2, 0.85)
    # bow
    s += P("M 300 470 C 284 450, 256 452, 260 472 C 262 490, 288 486, 300 470 Z", CORAL)
    s += P(mx("M 300 470 C 284 450, 256 452, 260 472 C 262 490, 288 486, 300 470 Z"), CORAL)
    s += f'<rect x="292" y="462" width="16" height="16" rx="6" fill="#D9603E" stroke="{LINE}" stroke-width="2.2"/>'
    s += star(300, 470, 5, "#F4B544", 1)
    return s


def arms_and_desk():
    s = ""
    # puffy sleeves reaching down to hands
    sl = "M 232 470 C 196 478, 188 520, 200 552 L 262 552 C 262 520, 256 488, 232 470 Z"
    s += both(sl, CREAM, 2.6)
    s += line("M 214 500 Q 222 522 236 536", "#EADBCF", 3)
    s += line(mx("M 214 500 Q 222 522 236 536"), "#EADBCF", 3)
    # desk / screen bezel the girl peeks over
    s += P("M 30 556 Q 30 540 46 540 L 554 540 Q 570 540 570 556 L 570 600 L 30 600 Z", "url(#deskG)", 2.8)
    s += line("M 46 560 L 554 560", CORAL, 3, 0.7)
    for x in (90, 510):
        s += star(x, 576, 7, "#F4B544", 1.2)
    # cuffs (frills) on the desk edge
    for cx in (232, 368):
        fr = f"M {cx-34} 548 "
        for i in range(6):
            x0 = cx - 34 + i * 11.3
            fr += f"Q {x0 + 5.6:.1f} 538 {x0 + 11.3:.1f} 548 "
        fr += f"L {cx+30} 556 L {cx-30} 556 Z"
        s += P(f"M {cx-32} 552 C {cx-32} 530, {cx+32} 530, {cx+32} 552 Z", "#FFFFFF", 2.2)
        # little round fists resting on the edge
        s += P(f"M {cx-22} 552 C {cx-24} 530, {cx+24} 530, {cx+22} 552 C {cx+20} 566, {cx-20} 566, {cx-22} 552 Z", SKIN, 2.4)
        s += line(f"M {cx-8} 556 Q {cx-6} 562 {cx-2} 562", SKIN_D, 2.2)
        s += line(f"M {cx+4} 556 Q {cx+6} 562 {cx+10} 562", SKIN_D, 2.2)
    return s


SCLERA = "M -31 -4 C -30 -32, 30 -32, 31 -4 C 33 20, 18 37, 0 37 C -18 37, -33 20, -31 -4 Z"
LASH = "M -34 -2 C -30 -38, 30 -38, 35 -6 L 41 -8 L 34 4 C 28 -27, -26 -27, -30 2 Z"


def eye(cx, cy, flip, uid):
    s = -1 if flip else 1
    g = [f"<g transform=\"translate({cx} {cy}) scale(1.14)\">"]
    g.append(f'<clipPath id="c{uid}"><path d="{SCLERA}"/></clipPath>')
    g.append(f'<path d="{SCLERA}" fill="#FFFFFF" stroke="#E6CFC6" stroke-width="1"/>')
    g.append(f'<g clip-path="url(#c{uid})">')
    g.append('<ellipse cx="0" cy="4" rx="26" ry="31" fill="url(#irisG)" stroke="#7A2E10" stroke-width="1.6"/>')
    g.append('<ellipse cx="0" cy="2" rx="11" ry="13.5" fill="#43160A"/>')
    g.append('<path d="M -18 18 Q 0 34 18 18 Q 0 27 -18 18 Z" fill="#FFEDB0" opacity="0.85"/>')
    g.append('<path d="M -40 -40 L 40 -40 L 40 -10 Q 0 -22 -40 -10 Z" fill="#B57B70" opacity="0.35"/>')
    g.append('<circle cx="-10" cy="-8" r="8.5" fill="#FFFFFF"/>')
    g.append('<circle cx="11" cy="14" r="4" fill="#FFFFFF"/>')
    g.append('</g>')
    g.append(f'<path d="{LASH}" fill="#3D1A10" transform="scale({s} 1)"/>')
    g.append('</g>')
    return "".join(g)


def face():
    s = P(FACE, SKIN, 2.8)
    s += ('<path d="M 130 240 L 470 240 L 470 300 Q 440 280 420 300 Q 390 280 362 296 Q 330 290 316 316 '
          'Q 300 290 280 300 Q 250 282 226 300 Q 196 282 176 300 Q 150 282 130 304 Z" '
          f'fill="{SKIN_D}" clip-path="url(#faceClip)" opacity="0.8" filter="url(#soft)"/>')
    s += '<ellipse cx="196" cy="384" rx="44" ry="24" fill="url(#blushG)"/><ellipse cx="404" cy="384" rx="44" ry="24" fill="url(#blushG)"/>'
    s += eye(222, 336, True, "L") + eye(378, 336, False, "R")
    # tiny open mouth
    s += P("M 292 396 C 292 386, 308 386, 308 396 C 308 406, 292 406, 292 396 Z", "#B8403A", 2.2)
    s += '<ellipse cx="300" cy="401" rx="4.5" ry="2.6" fill="#FF9090"/>'
    return s


def rounded_fringe(edge, top):
    d = top
    for (x0, y0), (x1, y1) in zip(edge, edge[1:]):
        if y1 > y0:  # down to a rounded tip
            d += f"C {x0 - 2} {y0 + (y1 - y0) * 0.6:.0f}, {x1 + 9} {y1}, {x1} {y1} "
        else:        # rounded tip back up to the notch
            d += f"C {x0 - 9} {y0}, {x1 + 2} {y1 + (y0 - y1) * 0.6:.0f}, {x1} {y1} "
    return d + "Z"


EDGE = [(474, 336), (456, 246), (434, 300), (410, 236), (388, 292), (364, 224),
        (326, 314), (314, 236), (288, 298), (262, 230), (238, 292), (212, 240),
        (184, 300), (156, 252), (126, 336)]


def front_hair():
    s = ""
    # side locks: chunky, wavy, in front of shoulders
    lock = ("M 150 260 C 112 330, 112 400, 128 450 C 140 488, 112 518, 124 560 C 130 582, 156 590, 170 572 "
            "C 158 556, 160 534, 172 516 C 190 486, 180 448, 176 410 C 172 360, 178 310, 196 270 Z")
    s += both(lock, "url(#hairG)", 2.6)
    s += line("M 146 330 C 136 380, 140 420, 152 458 C 160 486, 142 516, 144 548", HAIR_D, 2.6, 0.7)
    s += line(mx("M 146 330 C 136 380, 140 420, 152 458 C 160 486, 142 516, 144 548"), HAIR_D, 2.6, 0.7)
    s += line("M 136 470 C 130 494, 128 516, 134 536", "#FFE0C8", 4, 0.9)
    s += line(mx("M 136 470 C 130 494, 128 516, 134 536"), "#FFE0C8", 4, 0.9)
    # fringe
    top = "M 126 336 C 104 170, 200 108, 300 108 C 400 108, 496 170, 474 336 "
    s += P(rounded_fringe(EDGE, top), "url(#hairG)", 2.8)
    # clump separation lines (soft)
    for (x, y) in EDGE[1:-1:2]:
        s += line(f"M {x} {y + 4} Q {x + (300 - x) * 0.05:.0f} {y - 34} {x + (300 - x) * 0.16:.0f} {y - 70}", HAIR_D, 2.6, 0.65)
    # glossy ring: soft rounded highlights
    for d in ["M 176 200 Q 196 176 226 164", "M 250 152 Q 276 146 300 146", "M 322 147 Q 350 150 374 162", "M 396 176 Q 414 190 424 206"]:
        s += line(d, "#FFE2CB", 9, 0.9)
    # ahoge (soft curl)
    s += P("M 294 110 C 284 68, 314 44, 344 54 C 364 62, 360 90, 340 90 C 326 90, 322 76, 332 70 "
           "C 314 70, 304 88, 308 110 Z", "#F2874F", 2.4)
    # star clip & ribbon
    s += star(184, 226, 17, "#F4B544", 2.2) + star(210, 206, 8, "#FFE08A", 1.6)
    s += P("M 432 196 C 452 162, 500 160, 498 190 C 496 212, 460 212, 432 196 Z", CORAL)
    s += P("M 432 196 C 412 166, 370 168, 372 194 C 374 216, 410 214, 432 196 Z", CORAL)
    s += P("M 438 204 C 452 226, 458 248, 454 270 L 442 258 L 432 274 C 436 250, 432 228, 426 210 Z", "#DD6340", 2.2)
    s += line("M 440 188 C 458 178, 478 178, 488 184", "#C24E30", 2)
    s += line("M 424 188 C 406 178, 388 178, 380 186", "#C24E30", 2)
    s += f'<ellipse cx="432" cy="196" rx="12" ry="13" fill="#DD6340" stroke="{LINE}" stroke-width="2.4"/>'
    return s


def bg():
    s = '<rect width="600" height="600" fill="url(#bgG)"/>'
    for (x, y, r, o) in [(70, 120, 14, 0.8), (540, 110, 10, 0.7), (60, 330, 8, 0.6), (548, 320, 12, 0.7), (520, 470, 7, 0.6), (80, 470, 9, 0.6)]:
        k = r * 0.22
        s += (f'<path d="M {x} {y-r} Q {x+k} {y-k} {x+r} {y} Q {x+k} {y+k} {x} {y+r} Q {x-k} {y+k} {x-r} {y} Q {x-k} {y-k} {x} {y-r} Z" '
              f'fill="#FFC88A" opacity="{o}"/>')
    return s


def build():
    return "\n".join(['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">', DEFS,
                      bg(), back_hair(), body(), face(), front_hair(), arms_and_desk(), "</svg>"])


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "..", "cora.svg"), "w").write(build())
    print("ok")
