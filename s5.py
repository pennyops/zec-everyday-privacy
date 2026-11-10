# S5: breach: server box cracks, records spill out
from PIL import Image, ImageDraw, ImageFont
import os, random
W,H,FPS,SEC=1920,1080,30,7
BG=(15,20,25); RED=(230,80,70); WHITE=(240,240,240); GREY=(120,130,140)
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FM="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
cap=ImageFont.truetype(FB,64); mono=ImageFont.truetype(FM,28)
os.makedirs("frames_s5",exist_ok=True); random.seed(7)
labels=["name: ****","email: ****","card: ****","address: ****","prompts: ****"]
recs=[((-1 if k%2 else 1)*(0.45+0.5*(k//2)/4),0.25+0.18*(k%5),labels[k%5]) for k in range(10)]
def ease(t): t=min(max(t,0),1); return 1-(1-t)**3
for i in range(FPS*SEC):
    t=i/FPS; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im); cx,cy=960,560
    d.rounded_rectangle((cx-160,cy-200,cx+160,cy+200),radius=16,outline=GREY,width=8)
    for k in range(4): d.line((cx-120,cy-140+k*90,cx+120,cy-140+k*90),fill=GREY,width=6)
    if t>2.0:
        c=ease((t-2.0)/0.4); pts=[(cx-10,cy-200),(cx+20,cy-100),(cx-15,cy),(cx+25,cy+100),(cx,cy+200)]
        d.line(pts[:1+int(c*4)],fill=RED,width=8)
        for vx,vy,s in recs:
            p=ease((t-2.4)/2.5); x=cx+vx*700*p; y=cy-vy*300*p+300*p*p
            if p>0: d.text((x-(d.textlength(s,font=mono) if vx<0 else 0),y),s,font=mono,fill=RED)
    s="Then it leaks." if t>2.0 else "Stored somewhere..."; w=d.textlength(s,font=cap); d.text(((W-w)/2,120),s,font=cap,fill=WHITE)
    im.save(f"frames_s5/f{i:04d}.png")
