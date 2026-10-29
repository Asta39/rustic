import os, glob, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

R = '/home/user/rustic/stripped-golf'
S = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(S, 'frames'); os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1920
AUDIO = '/root/.claude/uploads/43eb2aa6-3670-55e7-96e3-c2a66ade3a8f/fad20066-Video_by_wrnsweats_1920p1793271963343_SealX.m4a'

BLACK, CHAR, DEEP, LIGHT = (17,17,17), (26,26,26), (74,74,74), (245,243,240)

def cover(im, cx=0.5, cy=0.5):
    im = im.convert('RGB'); s = max(W/im.width, H/im.height)
    im = im.resize((round(im.width*s), round(im.height*s)), Image.LANCZOS)
    x = int((im.width-W)*cx); y = int((im.height-H)*cy)
    return im.crop((x, y, x+W, y+H))

def flat(c): return Image.new('RGB', (W, H), c)

def gradient(top, bottom, mid=0.35):
    t = np.clip((np.linspace(0, 1, H)-mid)/0.35, 0, 1)[:, None, None]
    a = np.array(top)*(1-t)+np.array(bottom)*t
    return Image.fromarray(np.broadcast_to(a, (H, W, 3)).astype('uint8'))

def model(path, bg=(214,214,212)):
    fig = Image.open(path).convert('RGBA'); fig = fig.crop(fig.getbbox())
    s = H*0.62/fig.height; fig = fig.resize((int(fig.width*s), int(fig.height*s)), Image.LANCZOS)
    c = Image.new('RGB', (W, H), bg)
    # chest of figure sits under the centre mark
    c.paste(fig, ((W-fig.width)//2, int(H*0.5-fig.height*0.28)), fig)
    return c

def mark(color):
    im = Image.open(f'{R}/logo-system/stripped-logomark-{color}.png').convert('RGBA')
    im = im.crop(im.getbbox()); s = 64/im.width
    return im.resize((64, int(im.height*s)), Image.LANCZOS)
MW, MB = mark('white'), mark('black')

def with_mark(im):
    if getattr(im, 'nomark', False): return im
    c = np.array(im.convert('L'))[H//2-60:H//2+60, W//2-60:W//2+60].mean()
    m = MB if c > 140 else MW
    im = im.copy(); im.paste(m, ((W-m.width)//2, (H-m.height)//2), m); return im

# ---- tag with the logo printed on it
tag = cover(Image.open(f'{S}/src/tag1.png'))
lg = Image.open(f'{R}/logo-system/stripped-logomark-black.png').convert('RGBA'); lg = lg.crop(lg.getbbox())

# ---- image pool (flicker order alternates dark / light / texture / model)
F = lambda p, **k: cover(Image.open(p), **k)
ind = f'{R}/pgm-shoot/club-set/individual'
hero = f'{R}/pgm-shoot/homepage-hero'
def fit(p, bg=(244,244,244)):
    im = Image.open(p).convert('RGB'); s = W*0.92/im.width
    im = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
    c = Image.new('RGB', (W, H), bg); c.paste(im, ((W-im.width)//2, (H-im.height)//2)); return c
def nm(im): im.nomark = True; return im
pool = [
    nm(F(f'{S}/src/emb1.png')), F(f'{S}/src/fold3.png'), model(f'{hero}/stripped-hero-pose1-back.png'),
    tag, gradient(BLACK, (200,200,200)), flat(BLACK), flat(LIGHT), flat(DEEP),
    model(f'{hero}/stripped-hero-pose6-black-polo.png'), F(f'{S}/src/knit1.png'),
    model(f'{hero}/stripped-hero-pose2-front.png'), F('/tmp/claude-0/-home-user-rustic/43eb2aa6-3670-55e7-96e3-c2a66ade3a8f/images/36.webp'),
    F(f'{S}/src/fold1.png'), F('/tmp/claude-0/-home-user-rustic/43eb2aa6-3670-55e7-96e3-c2a66ade3a8f/images/34.jpg', cy=0.45), flat(CHAR),
    nm(F(f'{S}/src/emb2.png')), model(f'{hero}/stripped-hero-pose3-anorak.png'), F(f'{S}/src/fold2.png'),
    F('/tmp/claude-0/-home-user-rustic/43eb2aa6-3670-55e7-96e3-c2a66ade3a8f/images/37.webp'), F(f'{S}/src/knit2.png'),
    model(f'{hero}/stripped-hero-pose4-polo-sweater.png'), F(f'{R}/pgm-shoot/club-set/01-pgm-stand-bag.jpg', cy=0.55),
    F('/tmp/claude-0/-home-user-rustic/43eb2aa6-3670-55e7-96e3-c2a66ade3a8f/images/34.jpg', cx=0.3, cy=0.6), model(f'{hero}/stripped-hero-pose5-anorak-glove-cap.png'),
    F(f'{R}/pgm-shoot/club-set/02-clubs-in-bag.jpg'), fit('/tmp/claude-0/-home-user-rustic/43eb2aa6-3670-55e7-96e3-c2a66ade3a8f/images/35.jpg', (255,255,255)),
]
# put the logo on the tag (centred, so the overlay mark lands on it)

# ---- end cards
def font(name, size): return ImageFont.truetype(name, size)
SERIF = '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'
BLK = '/usr/share/fonts/opentype/inter/Inter-Black.otf'
MED = '/usr/share/fonts/opentype/inter/Inter-Medium.otf'

def spaced(d, cy, text, f, fill, track=14):
    ws = [d.textlength(ch, font=f) for ch in text]; tw = sum(ws)+track*(len(text)-1)
    x = (W-tw)/2
    for ch, w in zip(text, ws): d.text((x, cy), ch, font=f, fill=fill, anchor='lm'); x += w+track

tagline = F(f'{S}/src/fold3.png'); d = ImageDraw.Draw(tagline); f = font(SERIF, 46)
spaced(d, H*0.40, 'PLAY IT', f, (235,235,235)); spaced(d, H*0.40+70, 'STRIPPED BACK', f, (235,235,235))

def wordmark_card(t, light):
    bg = gradient((200,200,200), (226,226,224), 0.1) if light else gradient((150,150,150), BLACK, 0.05)
    d = ImageDraw.Draw(bg); f = font(BLK, 96)
    x0 = W//2+60 + int((1-t)*W*0.6)
    d.text((x0, H//2), 'STRIPPED', font=f, fill=(15,15,15) if light else (240,240,240), anchor='lm')
    return bg

def palette(dark):
    fl, fs = font(MED, 26), font(MED, 17)
    W2, P = W//2, int(H*0.6); H4 = (H-P)//2
    first = (CHAR, 'PRIMARY', '#1A1A1A', '26, 26, 26', '0, 0, 0, 90') if dark else ((220,220,220), 'PRIMARY', '#DCDCDC', '220, 220, 220', '0, 0, 0, 14')
    cells = [((0, 0, W, P),) + first,
             ((0, P, W2, H4), LIGHT if dark else BLACK, 'LIGHT', '#F5F3F0', '245, 243, 240', '0, 1, 2, 4'),
             ((W2, P, W2, H4), DEEP, 'DEEP', '#4A4A4A', '74, 74, 74', '0, 0, 0, 71'),
             ((0, P+H4, W2, H-P-H4), BLACK if dark else LIGHT, 'DARK', '#111111', '17, 17, 17', '0, 0, 0, 93'),
             ((W2, P+H4, W2, H-P-H4), (150,150,150), 'GREY', '#969696', '150, 150, 150', '0, 0, 0, 41')]
    im = flat(BLACK); d = ImageDraw.Draw(im)
    for n, ((x, y, w, h), c, name, hx, rgb, cm) in enumerate(cells, 1):
        d.rectangle((x, y, x+w, y+h), fill=c)
        ink = (20,20,20) if sum(c) > 380 else (232,232,232)
        d.text((x+24, y+22), name, font=fl, fill=ink)
        d.ellipse((x+w-56, y+22, x+w-28, y+50), outline=ink, width=2)
        d.text((x+w-42, y+36), str(n), font=fs, fill=ink, anchor='mm')
        for i, (k, v) in enumerate([('HEX', hx), ('RGB', rgb), ('CMYK', cm)]):
            d.text((x+24, y+h-100+i*26), k, font=fs, fill=ink); d.text((x+100, y+h-100+i*26), v, font=fs, fill=ink)
    return im

# ---- timeline: cut frames copied from the reference reel (30 fps, 241 frames)
cuts = list(range(0, 51, 2)) + [53, 56, 59, 62, 65, 68, 71, 74, 77, 81, 85, 89, 93, 97, 102, 107, 113, 119, 126, 133, 141, 150]
frames = []
for i, start in enumerate(cuts):
    end = cuts[i+1] if i+1 < len(cuts) else 150
    frames += [with_mark(pool[i % len(pool)])]*(end-start)
frames += [with_mark(tagline)]*(172-150)
for k in range(172, 186): frames.append(with_mark(wordmark_card(min(1, (k-172)/9)**0.5, False)))
for k in range(186, 203): frames.append(with_mark(wordmark_card(1, True)))
pd, pl = with_mark(palette(True)), with_mark(palette(False))
frames += [pd]*(223-203) + [pl]*(241-223)

for i, fr in enumerate(frames): fr.save(f'{OUT}/{i:04d}.png')
print(len(frames), 'frames')
dst = f'{R}/showreel/stripped-showreel.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '30', '-i', f'{OUT}/%04d.png', '-i', AUDIO,
                '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '17', '-c:a', 'aac', '-b:a', '192k',
                '-shortest', '-movflags', '+faststart', dst], check=True)
print(dst)
