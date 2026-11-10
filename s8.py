# S8: use cases (pay, donate, save, tip)
from PIL import Image, ImageDraw, ImageFont
import os
W,H,FPS,SEC=1920,1080,30,6
BG=(15,20,25); GOLD=(244,183,40); WHITE=(240,240,240)
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
cap=ImageFont.truetype(FB,64); lab=ImageFont.truetype(FB,52)
os.makedirs("frames_s8",exist_ok=True)
def ease(t): t=min(max(t,0),1); return 1-(1-t)**3
def mix(c,a): return tuple(int(x*a+b*(1-a)) for x,b in zip(c,BG))
items=["Pay","Donate","Save","Tip"]
for i in range(FPS*SEC):
    t=i/FPS; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    s="Privately, every day"; w=d.textlength(s,font=cap); d.text(((W-w)/2,160),s,font=cap,fill=mix(WHITE,ease(t/0.6)))
    for k,n in enumerate(items):
        a=ease((t-0.6-k*0.4)/0.5); cx=360+k*400; r=int(120*a)
        if r>0: d.ellipse((cx-r,540-r,cx+r,540+r),outline=GOLD,width=8)
        w=d.textlength(n,font=lab); d.text((cx-w/2,512),n,font=lab,fill=mix(WHITE,a))
    im.save(f"frames_s8/f{i:04d}.png")
