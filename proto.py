# Prototype: render an animated title card to frames, then ffmpeg -> mp4
from PIL import Image, ImageDraw, ImageFont
import math, os
W,H,FPS,SEC=1920,1080,30,4
BG=(15,20,25); GOLD=(244,183,40); WHITE=(240,240,240)
F="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
big=ImageFont.truetype(F,120); small=ImageFont.truetype(F,48)
def ease(t): return 1-(1-min(max(t,0),1))**3
for i in range(FPS*SEC):
    t=i/FPS; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    r=int(200*ease(t/1.0)); d.ellipse((W/2-r,H/2-260-r/2,W/2+r,H/2-260+r/2+r/2),outline=GOLD,width=8) if r>0 else None
    a=ease((t-0.6)/0.8); y=int(H/2+40*(1-a))
    txt="Everyday Privacy"; w=d.textlength(txt,font=big)
    d.text(((W-w)/2,y),txt,font=big,fill=tuple(int(c*a+b*(1-a)) for c,b in zip(WHITE,BG)))
    a2=ease((t-1.6)/0.8); s="Your data is being collected. Zcash keeps it yours."; w2=d.textlength(s,font=small)
    d.text(((W-w2)/2,H/2+190),s,font=small,fill=tuple(int(c*a2+b*(1-a2)) for c,b in zip(GOLD,BG)))
    im.save(f"frames/f{i:04d}.png")
