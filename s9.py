# S9: CTA
from PIL import Image, ImageDraw, ImageFont
import os
W,H,FPS,SEC=1920,1080,30,5
BG=(15,20,25); GOLD=(244,183,40); WHITE=(240,240,240); BLUE=(25,132,199)
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
big=ImageFont.truetype(FB,96); mid=ImageFont.truetype(FB,56)
os.makedirs("frames_s9",exist_ok=True)
def ease(t): t=min(max(t,0),1); return 1-(1-t)**3
def mix(c,a): return tuple(int(x*a+b*(1-a)) for x,b in zip(c,BG))
for i in range(FPS*SEC):
    t=i/FPS; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    a=ease(t/0.8); s="Take your privacy back."; w=d.textlength(s,font=big); d.text(((W-w)/2,400-int(30*(1-a))),s,font=big,fill=mix(WHITE,a))
    b=ease((t-1.0)/0.8); s2="zechub.wiki/wallets"; w=d.textlength(s2,font=mid); d.text(((W-w)/2,580),s2,font=mid,fill=mix(GOLD,b))
    c=ease((t-1.5)/0.8); d.line((W/2-int(400*c),680,W/2+int(400*c),680),fill=BLUE,width=6)
    im.save(f"frames_s9/f{i:04d}.png")
