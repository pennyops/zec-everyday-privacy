# S6: transparent ledger rows visible, then a gold shield sweep turns them into redacted (shielded) rows
from PIL import Image, ImageDraw, ImageFont
import os
W,H,FPS,SEC=1920,1080,30,8
BG=(15,20,25); GOLD=(244,183,40); WHITE=(240,240,240); GREY=(120,130,140)
F="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"; FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
mono=ImageFont.truetype(F,40); cap=ImageFont.truetype(FB,64)
os.makedirs("frames_s6",exist_ok=True)
rows=[("t1Rk...9xQa","2.50 ZEC","t1Mz...4kPw"),("t1Mz...4kPw","0.80 ZEC","t1Ab...7cNe"),("t1Ab...7cNe","12.00 ZEC","t1Qp...2wLs"),("t1Qp...2wLs","0.05 ZEC","t1Rk...9xQa")]
def ease(t): t=min(max(t,0),1); return 1-(1-t)**3
def mix(c,a): return tuple(int(x*a+b*(1-a)) for x,b in zip(c,BG))
for i in range(FPS*SEC):
    t=i/FPS; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    sweep=ease((t-3.5)/1.5)*(W+400)-200
    for n,(a,amt,b) in enumerate(rows):
        ra=ease((t-0.3-n*0.25)/0.4); y=330+n*130
        if ra<=0: continue
        d.rounded_rectangle((260,y-20,1660,y+80),radius=12,outline=mix(GREY,ra),width=3)
        cols=[(300,a),(840,amt),(1240,b)]
        for x,s in cols:
            if x+300<sweep: d.rectangle((x,y+5,x+d.textlength(s,font=mono),y+55),fill=mix(GOLD,ra))
            else: d.text((x,y+5),s,font=mono,fill=mix(WHITE,ra))
        d.text((740,y+5),"→",font=mono,fill=mix(GREY,ra)); d.text((1170,y+5),"→",font=mono,fill=mix(GREY,ra))
    if 3.5<t<5.2: d.rectangle((sweep-12,280,sweep+12,860),fill=GOLD)
    title="Transparent: everyone sees everything." if t<4.6 else "Shielded ZEC: only you know."
    ca=ease((t-0.2)/0.5) if t<4.6 else ease((t-4.6)/0.5)
    w=d.textlength(title,font=cap); d.text(((W-w)/2,120),title,font=cap,fill=mix(WHITE if t<4.6 else GOLD,ca))
    im.save(f"frames_s6/f{i:04d}.png")
