#!/usr/bin/env python3
"""首页横幅生成脚本：输出 banner-repo.svg（1200x340 矢量图）。

横幅右边的角色是《某科学的超电磁炮》的御坂美琴，Q 版同人绘制，
全部用代码画出来，没有使用任何官方图片。角色版权归原作者和版权方所有。

运行：python3 draw_banner_repo.py
"""
import os

LINE = "#4E2B1E"
SKIN = "#FFEDE2"
SKIN_D = "#F6CDB8"
HAIR_D = "#A9683A"
VEST = "#EAD2A4"
VEST_D = "#CFAE78"
WHITE = "#FFFFFF"

def mx(d, cx=300):
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
        out.append(f"{2*cx - v:g}" if expect_x else f"{v:g}")
        expect_x = not expect_x
    return " ".join(out).replace(" , ", ", ")

def P(d, fill, sw=2.8, extra="", stroke=LINE):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'

def both(d, fill, sw=2.8, extra=""):
    return P(d, fill, sw, extra) + P(mx(d), fill, sw, extra)

def line(d, color, w, op=1.0, extra=""):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" opacity="{op}" {extra}/>'

CHAR_DEFS = """
  <linearGradient id="hairG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#C98448"/><stop offset="0.6" stop-color="#D99A5E"/><stop offset="1" stop-color="#EBB983"/>
  </linearGradient>
  <linearGradient id="backG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#B8743E"/><stop offset="0.7" stop-color="#B06C38"/><stop offset="1" stop-color="#9A5A2C"/>
  </linearGradient>
  <linearGradient id="irisG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#4A2110"/><stop offset="0.5" stop-color="#A9592A"/><stop offset="1" stop-color="#F0B06A"/>
  </linearGradient>
  <radialGradient id="blushG">
    <stop offset="0" stop-color="#FF9C9C" stop-opacity="0.7"/><stop offset="1" stop-color="#FF9C9C" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="coinG" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#FFF3B0"/><stop offset="0.5" stop-color="#FFD24A"/><stop offset="1" stop-color="#E89B1C"/>
  </linearGradient>
  <filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>
  <filter id="glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="6"/></filter>
  <filter id="glowS" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="3"/></filter>
"""

FACE = ("M 142 250 C 136 336, 176 396, 232 424 C 262 438, 284 444, 300 444 "
        "C 316 444, 338 438, 368 424 C 424 396, 464 336, 458 250 Z")

def back_hair():
    d = ("M 300 88 C 160 88, 96 186, 102 306 C 106 372, 104 410, 94 438 C 88 452, 78 462, 64 468 "
         "C 90 482, 120 478, 138 460 C 142 476, 152 488, 166 494 C 168 482, 174 472, 184 464 "
         "Q 300 452 416 464 C 426 472, 432 482, 434 494 C 448 488, 458 476, 462 460 "
         "C 480 478, 510 482, 536 468 C 522 462, 512 452, 506 438 C 496 410, 494 372, 498 306 "
         "C 504 186, 440 88, 300 88 Z")
    s = P(d, "url(#backG)", 3)
    # darker underside behind the neck
    return s

def body():
    s = ""
    # neck
    s += P("M 280 426 L 280 462 L 320 462 L 320 426 Z", SKIN, 2.4)
    s += f'<path d="M 281 440 Q 300 452 319 440 L 319 430 L 281 430 Z" fill="{SKIN_D}" opacity="0.8"/>'
    # her left arm (viewer's right), hanging down: sleeve + skin
    s += P("M 392 520 C 400 546, 404 574, 402 604 L 436 604 C 438 570, 432 540, 420 514 Z", SKIN, 2.6)
    s += P("M 372 476 C 408 478, 432 502, 438 540 L 388 552 C 388 524, 382 498, 372 476 Z", WHITE, 2.8)
    s += line("M 392 546 L 436 535", "#D9DCE8", 3, 0.9)
    # torso: vest
    s += P("M 206 604 C 204 540, 222 478, 262 464 L 338 464 C 378 478, 396 540, 394 604 Z", VEST, 2.8)
    # shirt in the V
    s += P("M 262 464 L 300 536 L 338 464 Z", WHITE, 2.4)
    # vest V ribbing
    s += line("M 255 470 L 300 548 L 345 470", VEST_D, 7, 1)
    s += P("M 248 468 L 300 558 L 352 468 L 340 464 L 300 536 L 260 464 Z", VEST_D, 2.4)
    # collar wings
    wing = "M 300 498 C 288 486, 272 470, 262 458 C 250 462, 240 474, 240 488 C 256 498, 276 506, 292 510 Z"
    s += both(wing, WHITE, 2.6)
    # emblem on her left chest (viewer's right)
    s += P("M 345 546 L 371 546 L 371 562 C 371 572, 363 579, 358 582 C 353 579, 345 572, 345 562 Z", "#7B2D3B", 2)
    s += line("M 351 555 L 358 562 L 365 555", "#F3D58A", 2.4)
    s += '<circle cx="358" cy="570" r="2" fill="#F3D58A"/>'
    # hem shading
    s += line("M 226 560 C 232 580, 234 592, 234 604", VEST_D, 3, 0.8)
    s += line("M 372 580 C 370 590, 370 598, 370 604", VEST_D, 3, 0.8)
    return s

SCLERA = "M -31 -4 C -30 -30, 28 -34, 32 -8 C 34 18, 18 36, 0 36 C -18 36, -33 20, -31 -4 Z"
# upper lash with a sharp upward flick at the outer corner (x>0 = outer for the right eye)
LASH = ("M -35 0 C -32 -34, 22 -42, 36 -14 L 47 -24 L 42 -4 L 36 2 "
        "C 28 -26, -22 -28, -29 4 Z")

def eye(cx, cy, flip, uid):
    sgn = -1 if flip else 1
    g = [f'<g transform="translate({cx} {cy}) scale({1.12*sgn} 1.12)">']
    g.append(f'<clipPath id="c{uid}"><path d="{SCLERA}"/></clipPath>')
    g.append(f'<path d="{SCLERA}" fill="#FFFFFF" stroke="#E6CFC6" stroke-width="1"/>')
    g.append(f'<g clip-path="url(#c{uid})">')
    g.append('<ellipse cx="1" cy="3" rx="25" ry="31" fill="url(#irisG)" stroke="#5C2A12" stroke-width="1.6"/>')
    g.append('<ellipse cx="1" cy="2" rx="10.5" ry="13.5" fill="#34130A"/>')
    g.append('<path d="M -17 18 Q 1 34 19 18 Q 1 27 -17 18 Z" fill="#FFE2B0" opacity="0.9"/>')
    g.append('<path d="M -40 -44 L 44 -44 L 44 -12 Q 0 -22 -40 -8 Z" fill="#7A4A3A" opacity="0.38"/>')
    g.append('</g>')
    g.append(f'<path d="{LASH}" fill="#3A1A10"/>')
    g.append('<path d="M -30 8 C -31 16, -29 22, -25 27" fill="none" stroke="#3A1A10" stroke-width="2.2" stroke-linecap="round" opacity="0.55"/>')
    g.append('</g>')
    # highlights are NOT mirrored: both on the upper-left of each iris
    g.append(f'<circle cx="{cx-10}" cy="{cy-9}" r="9" fill="#FFFFFF"/>')
    g.append(f'<circle cx="{cx+13}" cy="{cy+17}" r="4.2" fill="#FFFFFF"/>')
    return "".join(g)

def face():
    s = P(FACE, SKIN, 3)
    s += f'<clipPath id="faceClip"><path d="{FACE}"/></clipPath>'
    # hair shadow on forehead
    s += ('<path d="M 130 236 L 470 236 L 470 300 Q 440 282 420 302 Q 390 282 362 298 Q 330 292 316 318 '
          'Q 300 292 280 302 Q 250 284 226 302 Q 196 284 176 302 Q 150 284 130 306 Z" '
          f'fill="{SKIN_D}" clip-path="url(#faceClip)" opacity="0.75" filter="url(#soft)"/>')
    s += '<ellipse cx="192" cy="386" rx="42" ry="22" fill="url(#blushG)"/><ellipse cx="408" cy="386" rx="42" ry="22" fill="url(#blushG)"/>'
    s += eye(222, 340, True, "L") + eye(378, 340, False, "R")
    # confident brows (inner end lower)
    # mouth: confident open grin, slightly lopsided
    s += P("M 278 398 Q 300 404 326 394 Q 322 420 300 420 Q 284 418 278 398 Z", "#B8403A", 2.4)
    s += '<path d="M 290 412 Q 302 406 314 412 Q 308 419 300 419 Q 294 419 290 412 Z" fill="#FF9A94"/>'
    s += '<path d="M 282 400 Q 300 405 322 397 L 320 402 Q 300 409 284 404 Z" fill="#FFFFFF"/>'
    # tiny nose
    s += line("M 298 378 Q 301 381 304 378", "#D99A86", 2, 0.9)
    return s

def tips(edge, top):
    """Pointed fringe: alternating notch(up)/tip(down) points, right to left."""
    d = top
    for (x0, y0), (x1, y1) in zip(edge, edge[1:]):
        if y1 > y0:   # going down to a pointed tip: bulge outward (to the right), arrive sharp
            d += f"C {x0 + 6} {y0 + (y1 - y0) * 0.55:.0f}, {x1 + 16} {y1 - 18}, {x1} {y1} "
        else:         # from the tip back up to the notch: slightly concave
            d += f"C {x0 - 2} {y0 - 26}, {x1 + 4} {y1 + 22}, {x1} {y1} "
    return d + "Z"

EDGE = [(476, 330), (458, 252), (440, 322), (418, 244), (394, 304), (372, 232),
        (328, 326), (312, 240), (280, 306), (258, 232), (224, 300), (204, 242),
        (174, 310), (156, 254), (124, 330)]

def flower(cx, cy, r, rot=0):
    s = f'<g transform="translate({cx} {cy}) rotate({rot})">'
    for i in range(5):
        a = i * 72
        s += (f'<ellipse cx="0" cy="{-r*0.62:.1f}" rx="{r*0.42:.1f}" ry="{r*0.6:.1f}" fill="#FFFFFF" stroke="{LINE}" '
              f'stroke-width="2.2" transform="rotate({a})"/>')
    for i in range(5):
        a = i * 72
        s += (f'<ellipse cx="0" cy="{-r*0.55:.1f}" rx="{r*0.3:.1f}" ry="{r*0.46:.1f}" fill="#FFFFFF" transform="rotate({a})"/>')
    s += f'<circle cx="0" cy="0" r="{r*0.3:.1f}" fill="#FFD76A" stroke="{LINE}" stroke-width="1.8"/></g>'
    return s

def front_hair():
    s = ""
    # side locks: short, to the jaw, flicking outward
    lock = ("M 134 286 C 108 340, 106 396, 118 432 C 112 446, 102 456, 88 460 C 114 472, 142 464, 156 442 "
            "C 168 412, 162 356, 176 296 Z")
    s += both(lock, "url(#hairG)", 2.8)
    s += line("M 138 330 C 128 372, 128 408, 136 438", HAIR_D, 2.6, 0.7)
    s += line(mx("M 138 330 C 128 372, 128 408, 136 438"), HAIR_D, 2.6, 0.7)
    # fringe
    top = "M 124 330 C 100 168, 198 102, 300 102 C 402 102, 500 168, 476 330 "
    s += P(tips(EDGE, top), "url(#hairG)", 3)
    # strand lines
    for (x, y) in EDGE[1:-1:2]:
        s += line(f"M {x} {y + 4} Q {x + (300 - x) * 0.05:.0f} {y - 34} {x + (300 - x) * 0.18:.0f} {y - 74}", HAIR_D, 2.6, 0.6)
    # glossy highlights
    for d in ["M 172 204 Q 192 178 224 164", "M 248 152 Q 274 145 300 145", "M 324 146 Q 352 150 376 162"]:
        s += line(d, "#FFE3C4", 9, 0.85)
    # confident brows, drawn over the fringe like in anime
    s += line("M 188 279 Q 222 274 254 290", "#6B3D22", 4, 0.8)
    s += line("M 412 279 Q 378 274 346 290", "#6B3D22", 4, 0.8)
    # flower hairpin on her left (viewer's right)
    s += flower(432, 214, 25, -12)
    return s

def coin_arm():
    s = ""
    # her right arm (viewer's left) raised: sleeve, forearm, fist, thumb, coin
    s += P("M 166 536 C 138 512, 110 484, 92 458 L 128 434 C 146 458, 172 486, 200 508 Z", SKIN, 2.8)
    s += P("M 244 470 C 206 468, 172 488, 152 520 L 190 560 C 206 540, 232 526, 254 520 Z", WHITE, 2.8)
    s += line("M 160 512 L 198 550", "#D9DCE8", 3, 0.9)
    # fist
    s += P("M 78 448 C 68 426, 84 404, 108 404 C 132 404, 146 424, 138 446 C 132 464, 88 468, 78 448 Z", SKIN, 2.8)
    s += line("M 96 452 Q 100 442 98 432 M 114 454 Q 118 444 116 432", SKIN_D, 2.4)
    # thumb flicking up
    s += P("M 92 414 C 86 398, 92 380, 104 380 C 116 380, 120 396, 116 414 Z", SKIN, 2.6)
    return s

def coin(cx, cy):
    s = ""
    s += f'<ellipse cx="{cx}" cy="{cy}" rx="34" ry="34" fill="#FFE27A" opacity="0.55" filter="url(#glow)"/>'
    s += f'<g transform="translate({cx} {cy}) rotate(-18)">'
    s += f'<ellipse cx="0" cy="3" rx="20" ry="13" fill="#B8770F" stroke="{LINE}" stroke-width="2.4"/>'
    s += f'<ellipse cx="0" cy="0" rx="20" ry="13" fill="url(#coinG)" stroke="{LINE}" stroke-width="2.4"/>'
    s += '<ellipse cx="0" cy="0" rx="13" ry="8" fill="none" stroke="#C98A1A" stroke-width="2"/>'
    s += '<path d="M -12 -5 Q -4 -10 6 -9" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round" opacity="0.9"/>'
    s += '</g>'
    return s

def bolt(pts, w=4, op=1.0, col="#8FE6FF"):
    d = "M " + " L ".join(f"{x} {y}" for x, y in pts)
    return (line(d, col, w * 2.6, op * 0.55, 'filter="url(#glowS)"') +
            line(d, "#DFF8FF", w, op) + line(d, "#FFFFFF", max(1.2, w * 0.4), op))

def character():
    s = back_hair() + body() + face() + front_hair() + coin_arm()
    return s

def character_fx():
    s = ""
    # motion arc from thumb to coin
    s += line("M 100 370 Q 78 330 70 286", "#FFE9A8", 3, 0.85, 'stroke-dasharray="2 9"')
    s += coin(64, 248)
    # sparks around the coin, hair and shoulder
    s += bolt([(6, 286), (26, 304), (14, 316), (38, 336)], 3.2)
    s += bolt([(92, 196), (108, 174), (98, 166), (120, 144)], 3)
    s += bolt([(486, 126), (506, 110), (498, 98), (524, 76)], 3.4)
    s += bolt([(540, 300), (558, 322), (546, 334), (572, 360)], 3.2)
    s += bolt([(60, 540), (40, 520), (52, 508), (28, 486)], 3)
    return s

def star(x, y, r, fill, op=1.0):
    k = r * 0.2
    d = (f"M {x} {y-r} Q {x+k} {y-k} {x+r} {y} Q {x+k} {y+k} {x} {y+r} "
         f"Q {x-k} {y+k} {x-r} {y} Q {x-k} {y-k} {x} {y-r} Z")
    return f'<path d="{d}" fill="{fill}" opacity="{op}"/>'

FONT = "'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Noto Sans CJK SC','Noto Sans SC',sans-serif"

def chip(x, y, w, label, color):
    return (f'<g transform="translate({x} {y})">'
            f'<rect width="{w}" height="62" rx="18" fill="#FFFFFF" fill-opacity="0.07" stroke="{color}" stroke-opacity="0.9" stroke-width="2.5"/>'
            f'<text x="{w/2}" y="41" text-anchor="middle" font-size="27" fill="{color}">{label}</text></g>')

def arrow(x, y):
    return (f'<path d="M {x} {y} h 26" stroke="#9FB4F5" stroke-width="3.5" stroke-linecap="round" opacity="0.9"/>'
            f'<path d="M {x+22} {y-9} l 10 9 l -10 9" fill="none" stroke="#9FB4F5" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.9"/>')

def traces():
    """Faint PCB traces in the background."""
    s = '<g fill="none" stroke="#6FD6FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity="0.16">'
    paths = [
        "M 0 44 H 180 l 22 -22 H 420",
        "M 0 300 H 120 l 18 -18 H 300 l 16 16 H 520",
        "M 520 24 H 700 l 20 20 H 860",
        "M 600 316 H 780 l 22 -22 H 900",
        "M 1200 60 H 1120 l -20 20",
        "M 1200 300 H 1150",
    ]
    for p in paths:
        s += f'<path d="{p}"/>'
    s += '</g><g fill="#6FD6FF" opacity="0.22">'
    for (x, y) in [(420, 22), (520, 298), (860, 44), (900, 294), (1100, 80), (520, 24), (600, 316)]:
        s += f'<circle cx="{x}" cy="{y}" r="4.5"/>'
    s += '</g>'
    return s

def banner():
    W, H = 1200, 340
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="从零学 C 到 AI 宠物小车">',
         '<!-- 由 src/draw_banner_repo.py 生成。角色：御坂美琴（《某科学的超电磁炮》），Q 版同人绘制，角色版权归原作者和版权方所有。 -->']
    o.append('<defs>')
    o.append("""
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0D1230"/><stop offset="0.55" stop-color="#1A1F55"/><stop offset="1" stop-color="#2B2170"/>
  </linearGradient>
  <radialGradient id="aura" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#8FE6FF" stop-opacity="0.55"/><stop offset="0.55" stop-color="#5B8CFF" stop-opacity="0.22"/><stop offset="1" stop-color="#5B8CFF" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="beam" gradientUnits="userSpaceOnUse" x1="70" y1="0" x2="700" y2="0">
    <stop offset="0" stop-color="#FFB347" stop-opacity="0"/><stop offset="0.25" stop-color="#FFB347" stop-opacity="0.9"/>
    <stop offset="0.8" stop-color="#FFF1C4"/><stop offset="1" stop-color="#FFFFFF"/>
  </linearGradient>
  <linearGradient id="titleG" gradientUnits="userSpaceOnUse" x1="70" y1="60" x2="70" y2="116">
    <stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#CFE4FF"/>
  </linearGradient>
  <linearGradient id="accentG" gradientUnits="userSpaceOnUse" x1="380" y1="0" x2="720" y2="0">
    <stop offset="0" stop-color="#7FE3FF"/><stop offset="1" stop-color="#FFD27A"/>
  </linearGradient>
  <clipPath id="card"><rect width="1200" height="340" rx="28"/></clipPath>""")
    o.append(CHAR_DEFS)
    o.append('</defs>')
    o.append('<g clip-path="url(#card)">')
    o.append('<!-- 背景：夜空渐变 + 电路板走线 -->')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    o.append(traces())
    o.append('<!-- 角色身后的电光 -->')
    o.append('<ellipse cx="1024" cy="190" rx="330" ry="250" fill="url(#aura)"/>')
    # distant lightning toward the title
    o.append(bolt([(894, 120), (854, 96), (866, 84), (814, 58), (826, 48), (784, 30)], 2.4, 0.5))
    o.append(bolt([(1140, 250), (1168, 262), (1158, 276), (1192, 296)], 2.4, 0.5))
    for (x, y, r, c, op) in [(742, 96, 9, "#FFD27A", 0.9), (812, 176, 6, "#8FE6FF", 0.9), (1168, 40, 10, "#FFD27A", 0.9),
                             (1126, 96, 5, "#FFFFFF", 0.8), (486, 28, 5, "#8FE6FF", 0.7), (36, 180, 6, "#FFD27A", 0.6),
                             (840, 300, 5, "#FF9EBB", 0.8)]:
        o.append(star(x, y, r, c, op))
    o.append('<!-- 标题、副标题、学习路线 -->')
    o.append(f'<g font-family="{FONT}" font-weight="800">')
    o.append(f'<text x="70" y="108" font-size="56"><tspan fill="url(#titleG)">从零学 C 到 </tspan><tspan fill="url(#accentG)">AI 宠物小车</tspan></text>')
    o.append('</g>')
    # railgun streak under the title
    o.append('<rect x="70" y="126" width="630" height="5" rx="2.5" fill="url(#beam)"/>')
    o.append('<circle cx="700" cy="128.5" r="9" fill="#FFE9A8" opacity="0.9" filter="url(#glowS)"/><circle cx="700" cy="128.5" r="4" fill="#FFFFFF"/>')
    o.append(f'<text x="72" y="170" font-size="25" fill="#B4C2F0" font-family="{FONT}">嵌入式学习日记 · 课程笔记 · 刷题 · 项目</text>')
    # chips
    o.append(f'<g font-family="{FONT}" font-weight="800">')
    x = 70; y = 212
    for i, (label, w, col) in enumerate([("C 语言", 136, "#7DB8FF"), ("ESP32", 136, "#6BE3A6"), ("FreeRTOS", 160, "#FFCB5C"), ("AI 小车", 136, "#FF9EBB")]):
        o.append(chip(x, y, w, label, col))
        x += w
        if i < 3:
            o.append(arrow(x + 12, y + 31))
            x += 56
    o.append('</g>')
    o.append('<!-- 角色：御坂美琴（Q 版同人绘制） -->')
    o.append('<g transform="translate(820 -34) scale(0.63)">')
    o.append(character())
    o.append(character_fx())
    o.append('</g>')
    o.append('</g></svg>')
    return "\n".join(o)

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "..", "banner-repo.svg"), "w", encoding="utf-8").write(banner() + "\n")
    print("ok")
