# S3 shopping (mode=shop) / S4 AI (mode=ai): icon -> tags fly to a growing server
from PIL import Image, ImageDraw, ImageFont
import os, sys
mode=sys.argv[1] if len(sys.argv)>1 else "shop"
W,H,FPS,SEC=1920,1080,30,8
BG=(15,20,25); GOLD=(244,183,40); WHITE=(240,240,240); GREY=(120,130,140); RED=(230,80,70)
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FM="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
cap=ImageFont.truetype(FB,64); tagf=ImageFont.truetype(FM,34); lab=ImageFont.truetype(FB,36)
if mode=="shop":
    title="Every purchase..."; tags=["purchase history","home address","habits","card used"]; out="frames_s3"; srv="RETAILER"
else:
    title="Every prompt..."; tags=["prompts stored","used for training","your questions","linked to you"]; out="frames_s4"; srv="AI COMPANY"
os.makedirs(out,exist_ok=True)
def ease(t): t=min(max(t,0),1); return 1-(1-t)**3
def icon(d,cx,cy,a):
    if mode=="shop":
        d.line((cx-120,cy-80,cx-80,cy-80,cx-40,cy+40,cx+100,cy+40,cx+130,cy-50,cx-60,cy-50),fill=GOLD,width=10,joint="curve")
        for x in (cx-20,cx+80): d.ellipse((x-16,cy+60,x+16,cy+92),outline=GOLD,width=8)
    else:
        d.rounded_rectangle((cx-140,cy-90,cx+140,cy+50),radius=30,outline=GOLD,width=10)
        d.polygon([(cx-60,cy+48),(cx-100,cy+110),(cx-10,cy+48)],fill=GOLD)
        for k in range(3): d.ellipse((cx-60+k*50,cy-30,cx-36+k*50,cy-6),fill=GOLD)
for i in range(FPS*SEC):
    t=i/FPS; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    icon(d,420,560,1)
    for x in range(600,1300,40): d.line((x,560,x+20,560),fill=(60,70,80),width=4)
    d.polygon([(1300,545),(1325,560),(1300,575)],fill=(60,70,80))
    n=sum(1 for k in range(len(tags)) if t>1.2+k*1.1+1.4)
    if n: d.text((1500-60,560-260*1.0-60),f"+{n} records",font=tagf,fill=RED)
    g=1+0.25*ease((t-2)/5); sx,sy=1500,560; hw,hh=140*g,180*g
    d.rounded_rectangle((sx-hw,sy-hh,sx+hw,sy+hh),radius=16,outline=GREY,width=8)
    for k in range(4): y=sy-hh+60*g+k*(2*hh-120*g)/3; d.line((sx-hw+40,y,sx+hw-40,y),fill=GREY,width=6)
    w=d.textlength(srv,font=lab); d.text((sx-w/2,sy+hh+20),srv,font=lab,fill=GREY)
    for k,s in enumerate(tags):
        st=1.2+k*1.1; p=ease((t-st)/1.4)
        if t<st: continue
        y0=380+k*120; x=600+(sx-hw-650)*p; y=y0+(sy-y0)*p*p*0.6
        if p<0.98:
            tw=d.textlength(s,font=tagf); d.rounded_rectangle((x-12,y-8,x+tw+12,y+46),radius=10,outline=RED,width=3); d.text((x,y),s,font=tagf,fill=RED)
    w=d.textlength(title,font=cap); d.text(((W-w)/2,120),title,font=cap,fill=WHITE)
    im.save(f"{out}/f{i:04d}.png")
