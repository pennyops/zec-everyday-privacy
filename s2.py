# S2 "Your day, logged": phone center, icons pop around, dotted lines stream to a server
from PIL import Image, ImageDraw, ImageFont
import math, os, sys
W,H,FPS,SEC=1920,1080,30,8
BG=(15,20,25); GOLD=(244,183,40); WHITE=(240,240,240); RED=(230,80,70); GREY=(90,100,110)
F="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
cap=ImageFont.truetype(F,64); lab=ImageFont.truetype(F,30)
os.makedirs("frames_s2",exist_ok=True)
def ease(t): t=min(max(t,0),1); return 1-(1-t)**3
def mix(c,a): return tuple(int(x*a+b*(1-a)) for x,b in zip(c,BG))
PX,PY=760,560; SX,SY=1500,560
icons=[("cart",(-260,-260)),("chat",(260,-260)),("pin",(-260,260)),("card",(260,260))]
def draw_icon(d,kind,x,y,s,col):
    if kind=="cart":
        d.rectangle((x-40*s,y-25*s,x+40*s,y+20*s),outline=col,width=6); d.line((x-60*s,y-40*s,x-40*s,y-25*s),fill=col,width=6)
        for dx in(-25,25): d.ellipse((x+dx*s-9*s,y+30*s-9*s,x+dx*s+9*s,y+30*s+9*s),fill=col)
    elif kind=="chat":
        d.rounded_rectangle((x-50*s,y-35*s,x+50*s,y+25*s),radius=int(15*s)+1,outline=col,width=6); d.polygon([(x-20*s,y+25*s),(x-35*s,y+50*s),(x,y+25*s)],fill=col)
    elif kind=="pin":
        d.ellipse((x-30*s,y-55*s,x+30*s,y+5*s),outline=col,width=6); d.polygon([(x-25*s,y-10*s),(x+25*s,y-10*s),(x,y+45*s)],fill=col)
    elif kind=="card":
        d.rounded_rectangle((x-55*s,y-35*s,x+55*s,y+35*s),radius=int(8*s)+1,outline=col,width=6); d.line((x-55*s,y-12*s,x+55*s,y-12*s),fill=col,width=8)
for i in range(FPS*SEC):
    t=i/FPS; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    a=ease(t/0.6); d.rounded_rectangle((PX-90,PY-170,PX+90,PY+170),radius=28,outline=mix(WHITE,a),width=8)
    d.rounded_rectangle((PX-70,PY-140,PX+70,PY+130),radius=10,fill=mix((40,50,60),a))
    sa=ease((t-2.5)/0.6)
    if sa>0:
        for k in range(3): d.rounded_rectangle((SX-90,SY-160+k*110,SX+90,SY-70+k*110),radius=8,outline=mix(GREY,sa),width=6); d.ellipse((SX+50,SY-125+k*110,SX+66,SY-109+k*110),fill=mix(RED,sa))
        tw=d.textlength("DATA BROKERS",font=lab); d.text((SX-tw/2,SY+200),"DATA BROKERS",font=lab,fill=mix(GREY,sa))
    for n,(kind,(dx,dy)) in enumerate(icons):
        ia=ease((t-0.6-n*0.35)/0.4)
        if ia<=0: continue
        x,y=PX+dx*0.75,PY+dy*0.75; draw_icon(d,kind,x,y,ia,GOLD)
        if t>3.0+n*0.2:
            for j in range(10):
                p=((t-3.0-n*0.2)*0.6+j/10)%1; qx=x+(SX-x)*p; qy=y+(SY-y)*p-math.sin(p*math.pi)*80
                d.ellipse((qx-6,qy-6,qx+6,qy+6),fill=RED)
    ca=ease((t-1.2)/0.6); s="Your day, logged."; w=d.textlength(s,font=cap); d.text(((W-w)/2,90),s,font=cap,fill=mix(WHITE,ca))
    im.save(f"frames_s2/f{i:04d}.png")
