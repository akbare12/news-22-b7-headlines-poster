#!/usr/bin/env python3
"""Draw the news-image-20261122 headline-poster front page.

One day's world news, Sunday 22 November 2026, as a poster front page:
three giant headlines, a big-number strip, a pinned map, and a dense
numbered list of 32 stories. Pure Pillow, no network, deterministic.
"""
import math
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 20, 20)
RED = (178, 24, 24)
NAVY = (16, 34, 66)
GOLD = (184, 134, 11)
GREEN = (34, 120, 60)
BLUE = (30, 90, 160)
GREY = (110, 108, 100)
LIGHT_BLUE = (205, 225, 240)
LAND = (232, 214, 170)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to pixel width, returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def badge(draw, x, y, label, fill):
    f = font(SANS_B, 11)
    w = draw.textlength(label, font=f) + 10
    draw.rounded_rectangle([x, y, x + w, y + 16], radius=3, fill=fill)
    draw.text((x + 5, y + 2), label, font=f, fill=(255, 255, 255))
    return w


def draw_map(draw, x0, y0, x1, y1, pins):
    """Rough world sketch with numbered pins."""
    draw.rectangle([x0, y0, x1, y1], fill=LIGHT_BLUE, outline=INK, width=1)
    for gx in range(x0 + 30, x1, 30):
        draw.line([(gx, y0), (gx, y1)], fill=(255, 255, 255), width=1)
    for gy in range(y0 + 22, y1, 22):
        draw.line([(x0, gy), (x1, gy)], fill=(255, 255, 255), width=1)
    mw, mh = x1 - x0, y1 - y0

    def px(lon, lat):
        return (x0 + (lon + 170) / 360.0 * mw, y0 + (85 - lat) / 170.0 * mh)

    north_america = [(-168, 66), (-140, 70), (-120, 71), (-95, 80), (-75, 72),
                     (-60, 60), (-55, 47), (-70, 42), (-80, 32), (-97, 26),
                     (-105, 20), (-95, 16), (-83, 9), (-105, 15), (-120, 30),
                     (-125, 48), (-150, 60), (-168, 66)]
    south_america = [(-78, 8), (-60, 10), (-50, 0), (-35, -8), (-40, -22),
                     (-48, -28), (-58, -38), (-70, -52), (-73, -35),
                     (-70, -18), (-80, -5), (-78, 8)]
    europe = [(-10, 36), (-9, 43), (0, 46), (-2, 50), (5, 53), (8, 57),
              (12, 55), (18, 56), (21, 59), (28, 71), (40, 68), (32, 60),
              (28, 45), (23, 40), (19, 42), (12, 44), (3, 42), (-10, 36)]
    africa = [(-6, 35), (10, 37), (20, 32), (32, 31), (35, 28), (43, 12),
              (51, 11), (48, -2), (40, -15), (35, -25), (28, -33), (19, -35),
              (15, -27), (12, -17), (9, -1), (-8, 4), (-17, 15), (-15, 27),
              (-6, 35)]
    asia = [(40, 68), (55, 72), (70, 72), (90, 75), (110, 76), (130, 72),
            (160, 66), (178, 65), (162, 60), (158, 52), (142, 50), (140, 40),
            (130, 33), (122, 30), (120, 22), (108, 18), (105, 9), (100, 7),
            (95, 16), (90, 22), (80, 15), (77, 8), (72, 20), (66, 25),
            (58, 25), (52, 27), (48, 30), (44, 29), (40, 36), (36, 36),
            (40, 42), (40, 55), (40, 68)]
    australia = [(114, -22), (122, -14), (132, -12), (142, -11), (146, -19),
                 (153, -27), (150, -37), (140, -38), (132, -32), (124, -33),
                 (115, -35), (114, -22)]
    for poly in (north_america, south_america, europe, africa, asia, australia):
        draw.polygon([px(lo, la) for lo, la in poly], fill=LAND,
                     outline=(150, 130, 90))
    for num, lon, lat, dx, dy in pins:
        cx, cy = px(lon, lat)
        ox, oy = cx + dx, cy + dy
        if dx or dy:
            draw.line([(cx, cy), (ox, oy)], fill=RED, width=1)
            draw.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=RED)
        draw.ellipse([ox - 7, oy - 7, ox + 7, oy + 7], fill=RED,
                     outline=(255, 255, 255), width=2)
        f = font(SANS_B, 9)
        tw = draw.textlength(str(num), font=f)
        draw.text((ox - tw / 2, oy - 6), str(num), font=f, fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- top rule + masthead ----
    d.rectangle([0, 0, W, 7], fill=RED)
    d.text((24, 14), "THE WORLD TODAY", font=font(SERIF, 46), fill=INK)
    d.text((W - 24 - d.textlength("SUNDAY 22 NOVEMBER 2026",
                                  font=font(SANS_B, 20)), 26),
           "SUNDAY 22 NOVEMBER 2026", font=font(SANS_B, 20), fill=RED)
    d.line([(24, 66), (W - 24, 66)], fill=RED, width=2)

    # ---- subline + legend (badges right-aligned, drawn right to left) ----
    d.text((24, 73), "32 STORIES  ·  6 REGIONS  ·  EVERY ITEM FIRST REPORTED 22 NOV",
           font=font(SANS_B, 13), fill=INK)
    lx = W - 24
    for label, fill in (("ONGOING", BLUE), ("CLAIM", GOLD), ("REPORTED", GREEN)):
        f = font(SANS_B, 11)
        w = d.textlength(label, font=f) + 10
        lx -= w
        badge(d, lx, 72, label, fill)
        lx -= 6
    d.text((lx - d.textlength("HOW WE KNOW EACH STORY —", font=font(SANS, 11)) - 6,
            75), "HOW WE KNOW EACH STORY —", font=font(SANS, 11), fill=GREY)

    # ---- big-number strip ----
    d.rectangle([24, 96, W - 24, 124], fill=NAVY)
    nums = [("258", "House seats"), ("2", "tankers hit"), ("194", "COP31 parties"),
            ("330", "vote margin"), ("36", "missing in Banten"),
            ("1,661", "Gaza toll")]
    x = 40
    for val, lab in nums:
        d.text((x, 99), val, font=font(SANS_B, 20), fill=(255, 214, 90))
        x += d.textlength(val, font=font(SANS_B, 20)) + 8
        d.text((x, 104), lab, font=font(SANS, 13), fill=(255, 255, 255))
        x += d.textlength(lab, font=font(SANS, 13)) + 26

    # ---- HERO 1: 2 TANKERS HIT (full width, giant type), 132-302 ----
    y = 132
    d.rectangle([24, y, W - 24, y + 170], fill=(255, 255, 255),
                outline=INK, width=1)
    # small tanker illustration, bottom right corner
    d.rectangle([865, y + 120, 985, y + 148], fill=(210, 90, 20))
    d.rectangle([895, y + 98, 950, y + 120], fill=(230, 230, 230),
                outline=INK, width=1)
    d.rectangle([920, y + 80, 945, y + 98], fill=(230, 230, 230),
                outline=INK, width=1)
    cx, cy = 958, y + 88
    for ang in range(0, 360, 30):
        r1, r2 = 17, 7
        a1 = math.radians(ang)
        a2 = math.radians(ang + 15)
        d.polygon([(cx + r1 * math.cos(a1), cy + r1 * math.sin(a1)),
                   (cx + r2 * math.cos(a2), cy + r2 * math.sin(a2)),
                   (cx + r1 * math.cos(math.radians(ang + 30)),
                    cy + r1 * math.sin(math.radians(ang + 30)))],
                  fill=(255, 200, 0), outline=RED)
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=RED)
    d.rectangle([855, y + 148, 995, y + 164], fill=(40, 110, 180))
    for wx in range(860, 995, 22):
        d.arc([wx, y + 152, wx + 18, y + 164], 180, 360,
              fill=(255, 255, 255), width=2)
    d.ellipse([982 - 7, y + 105, 982 + 7, y + 119], fill=INK)
    d.text((40, y + 8), "CONFLICT  ·  STRAIT OF HORMUZ", font=font(SANS_B, 14),
           fill=RED)
    d.text((W - 24 - d.textlength("17:13 UTC", font=font(SANS_B, 14)), y + 8),
           "17:13 UTC", font=font(SANS_B, 14), fill=GREY)
    d.text((40, y + 28), "2 TANKERS HIT", font=font(SERIF, 64), fill=INK)
    d.text((40, y + 112),
           "Two supertankers hit mines east of the strait, north of Ghanam",
           font=font(SANS, 15), fill=INK)
    d.text((40, y + 130),
           "Island; both on fire. First reported 17:13 UTC.",
           font=font(SANS, 15), fill=INK)
    bw = badge(d, 40, y + 148, "REPORTED", GREEN)
    d.text((40 + bw + 8, y + 150), "Iran navy  ·  AP",
           font=font(SANS, 13), fill=GREY)

    # ---- HERO 2 + HERO 3 side by side, 310-462 ----
    y = 310
    d.rectangle([24, y, 505, y + 152], fill=(255, 255, 255), outline=INK, width=1)
    d.text((40, y + 8), "CLIMATE  ·  ANTALYA", font=font(SANS_B, 14), fill=RED)
    d.text((505 - 16 - d.textlength("EVENING", font=font(SANS_B, 14)), y + 8),
           "EVENING", font=font(SANS_B, 14), fill=GREY)
    d.text((40, y + 26), "NO DEAL", font=font(SERIF, 60), fill=INK)
    for i, line in enumerate(wrap(d, "COP31 collapses with no deal. EU + ~130 "
                                  "parties reject a text with no fossil fuels.",
                                  font(SANS, 13), 445)):
        d.text((40, y + 100 + i * 17), line, font=font(SANS, 13), fill=INK)
    bw = badge(d, 40, y + 134, "REPORTED", GREEN)
    d.text((40 + bw + 8, y + 136), "CNN  ·  Reuters",
           font=font(SANS, 13), fill=GREY)
    # hero 3: 258 (right, navy)
    d.rectangle([519, y, W - 24, y + 152], fill=NAVY, outline=INK, width=1)
    d.text((535, y + 8), "POLITICS  ·  WASHINGTON", font=font(SANS_B, 14),
           fill=(255, 214, 90))
    d.text((W - 24 - 16 - d.textlength("18:00 UTC", font=font(SANS_B, 14)), y + 8),
           "18:00 UTC", font=font(SANS_B, 14), fill=(200, 210, 230))
    d.text((535, y + 14), "258", font=font(SERIF, 74), fill=(255, 255, 255))
    d.text((535, y + 98), "HOUSE SEATS — LARGEST SINCE 1992",
           font=font(SANS_B, 14), fill=(255, 214, 90))
    for i, line in enumerate(wrap(d, "Dems win House; Hubbard beats Foxx by 330 "
                                  "in NC recount. GOP 173, 4 races uncalled.",
                                  font(SANS, 13), 440)):
        d.text((535, y + 118 + i * 17), line, font=font(SANS, 13),
               fill=(255, 255, 255))

    # ---- map band + pin key ----
    y = 470
    d.text((24, y), "WHERE IT HAPPENED — EVERY HERO PINNED",
           font=font(SANS_B, 13), fill=INK)
    d.text((W - 24 - d.textlength("ALL TIMES UTC", font=font(SANS, 11)), y + 2),
           "ALL TIMES UTC", font=font(SANS, 11), fill=GREY)
    my0, my1 = y + 20, y + 130
    pins = [(1, 56, 26, 0, 0), (2, 30, 37, 10, -16), (3, -77, 39, 0, 0),
            (4, 20, 32, -18, 4), (5, 32, 15, 4, 16), (6, 31, 50, -14, -14),
            (7, 106, -6, 0, 0), (8, 34, 31, 18, -4)]
    draw_map(d, 24, my0, 640, my1, pins)
    kx = 656
    d.text((kx, my0), "PIN KEY", font=font(SANS_B, 13), fill=INK)
    key = [("1", "Hormuz — 2 tankers hit mines, 17:13"),
           ("2", "Antalya — COP31 collapses, no deal"),
           ("3", "Washington — Dems reach 258, 18:00"),
           ("4", "Benghazi — Russian ship hit, depot blast"),
           ("5", "Khartoum — drones kill 4, UN hit"),
           ("6", "Kyiv — Dymer drone strike, 11 killed"),
           ("7", "Banten — factory fire, 36 missing"),
           ("8", "Gaza — toll 1,661 since Oct 2025")]
    for i, (n, t) in enumerate(key):
        yy = my0 + 18 + i * 12
        d.ellipse([kx, yy, kx + 11, yy + 11], fill=RED)
        f = font(SANS_B, 9)
        tw = d.textlength(n, font=f)
        d.text((kx + 5 - tw / 2, yy), n, font=f, fill=(255, 255, 255))
        d.text((kx + 16, yy - 1), t, font=font(SANS, 11), fill=INK)

    # ---- story list 04-32, three columns, 2 lines per item ----
    y = 608
    d.text((24, y), "THE DAY IN BRIEF — STORIES 04–32, NUMBERED AS PINNED",
           font=font(SANS_B, 13), fill=INK)
    d.text((W - 24 - d.textlength("ALL TIMES UTC", font=font(SANS, 11)), y + 2),
           "ALL TIMES UTC", font=font(SANS, 11), fill=GREY)
    d.line([(24, y + 18), (W - 24, y + 18)], fill=INK, width=1)

    stories = [
        ("04", "Dymer drone hits flats", "Russian strike kills 11, 14 missing N. of Kyiv. — BBC", "REPORTED"),
        ("05", "Merkury hit at Benghazi", "Ukrainian sea drones sink Russian corvette. — BBC", "CLAIM"),
        ("06", "Khartoum drones kill 4", "Strikes blamed on RSF kill four, damage UN site. — AP", "CLAIM"),
        ("07", "Zelenskyy pleads for Patriots", "Russia fired ~2,700 drones in a week. — Reuters", "REPORTED"),
        ("08", "Iran shows missile city", "Dual-missile launcher shown in underground base. — Al Jazeera", "REPORTED"),
        ("09", "Saudis stop Houthi attack", "Saudis intercept Houthi drone and missile. — Reuters", "CLAIM"),
        ("10", "Bahrain blames Iran", "Industrial site struck, 2 hurt; UAE condemns. — France 24", "REPORTED"),
        ("11", "Europe protests, day 3", "Cost and housing marches; 144 arrested in France. — Le Monde", "REPORTED"),
        ("12", "Settlers burn West Bank cars", "12 vehicles torched near Ramallah villages. — WAFA", "REPORTED"),
        ("13", "Benghazi depot blast", "Explosion hits ammo depot inside naval base. — Local auth.", "REPORTED"),
        ("14", "Unity talks stall", "Eisenkot and Likud meet; wide gap on unity govt. — Al Jazeera", "REPORTED"),
        ("15", "Finland: war spills over", "Drone hits Russian cargo ship in Baltic. — Finnish govt", "REPORTED"),
        ("16", "Gaza aid van strike", "World Central Kitchen: three killed were not its team. — WCK", "REPORTED"),
        ("17", "\u201cIran war was avoidable\u201d", "Ex-UN envoy: the war need not have happened. — MED Dialogues", "REPORTED"),
        ("18", "Banten factory fire", "Candy-plant blaze kills 3; 36 missing in Serang. — BBC", "REPORTED"),
        ("19", "Turkey warns on Syria", "Fidan: Israel may use Druze to provoke Syria op. — Anadolu", "CLAIM"),
        ("20", "Pezeshkian: silent war", "\u201cSilent economic war\u201d; US blockade hits 130 days. — IRNA", "REPORTED"),
        ("21", "War fallout hits markets", "Fidan: war burden threatens global markets. — Anadolu", "REPORTED"),
        ("22", "Aoun: Israel must leave", "Lebanon\u2019s president demands full withdrawal. — Al Jazeera", "REPORTED"),
        ("23", "Gaza: 350,000 homeless", "Displaced protest near Yellow Line amid strikes. — Al Jazeera", "REPORTED"),
        ("24", "Settlers attack homes", "Homes attacked in Hebron, Ramallah; tear gas fired. — WAFA", "REPORTED"),
        ("25", "Gaza homes blocked", "Turkey: Israel blocking container homes. — Anadolu", "CLAIM"),
        ("26", "Germany urged to arrest", "Hind Rajab Foundation files complaint vs soldier. — HRF", "REPORTED"),
        ("27", "Fred Nile dies at 92", "NSW figurehead dies; announced 22 Nov. — Guardian", "REPORTED"),
        ("28", "Gamer rescues girl", "Teen, 16, and his mother help FBI free missing girl. — FBI", "REPORTED"),
        ("29", "Gaza toll 1,661", "Death toll since Oct 2025 reaches 1,661. — Gaza health min.", "REPORTED"),
        ("30", "Trump: strikes if no deal", "Trump may renew Iran strikes in 2027. — Times of Israel", "REPORTED"),
        ("31", "Mongolia snap vote", "Mongolia faces snap presidential vote. — Euronews", "REPORTED"),
        ("32", "Cartel boss captured", "Mexico cartel boss held; 11 killed in the operation. — Al Jazeera", "REPORTED"),
    ]
    col_w = 320
    col_x = [24, 352, 680]
    row_h = 30
    f_head = font(SANS_B, 12)
    f_body = font(SANS, 10)
    for idx, (num, head, body, ver) in enumerate(stories):
        col = idx // 10
        row = idx % 10
        x = col_x[col]
        yy = y + 26 + row * row_h
        d.text((x, yy), num, font=font(SANS_B, 12), fill=RED)
        d.text((x + 24, yy), head, font=f_head, fill=INK)
        if ver == "CLAIM":
            badge(d, x + 24 + d.textlength(head, font=f_head) + 6, yy + 1,
                  "CLAIM", GOLD)
        d.text((x + 24, yy + 14), body, font=f_body, fill=(60, 60, 60))

    # ---- NOT YET strip ----
    y = 944
    d.rectangle([24, y, W - 24, y + 22], fill=(255, 236, 170),
                outline=GOLD, width=1)
    d.text((36, y + 4),
           "NOT YET — DO NOT READ AS DONE:  4 House races uncalled  ·  COP32 venue not set  ·  Gaza ceasefire talks: no deal announced",
           font=font(SANS_B, 11), fill=INK)

    # ---- footer: date check + sources (wrapped to fit) ----
    f_foot = font(SANS, 9)
    y = 972
    lines = wrap(d, "DATE CHECK — Every story above was first reported on 22 Nov, "
                 "unless its kicker says otherwise.  EXCLUDED:  El Chapo Isidro "
                 "captured 20 Nov  ·  BepiColombo Mercury orbit 21 Nov  ·  ICJ "
                 "Myanmar ruling 19 Nov  ·  Wall St rout 20 Nov  ·  FBI NCIC hack "
                 "first reported 21 Nov.", f_foot, W - 48)
    for i, ln in enumerate(lines):
        d.text((24, y + i * 12), ln, font=f_foot, fill=GREY)
    y += len(lines) * 12 + 2
    d.text((24, y), "LEGEND:  REPORTED = confirmed by 2+ sources  ·  CLAIM = one side alleges, unverified  ·  ONGOING = still developing.",
           font=f_foot, fill=GREY)
    y += 12
    d.text((24, y), "SOURCES:  AP  ·  Reuters  ·  BBC  ·  CNN  ·  France 24  ·  Al Jazeera  ·  Guardian  ·  SCMP  ·  IRNA  ·  Anadolu  ·  WAFA  ·  HRF  ·  WCK  ·  FBI  ·  Euronews  ·  dailysummaryof, 22 Nov 2026",
           font=f_foot, fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
