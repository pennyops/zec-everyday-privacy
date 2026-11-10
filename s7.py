# S7: wallet tour, cards slide in 3 at a time with tags (names from zechub.wiki/wallets; YWallet deprecated -> excluded)
from PIL import Image, ImageDraw, ImageFont
import os
W,H,FPS=1920,1080,30
BG=(15,20,25); GOLD=(244,183,40); WHITE=(240,240,240); CARD=(30,38,46); GREY=(150,160,170)
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FR="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
LOGO={n:Image.open(f"assets/wallets/{f}.webp").convert("RGBA").resize((300,172)) for n,f in [("ZODL","zodl"),("Zingo!","zingo"),("Edge","edge"),("Unstoppable","unstoppable"),("Cake","cake"),("Zkool","zkool"),("Keystone","keystone"),("Ledger","ledger"),("Trezor","trezor")]}
nm=ImageFont.truetype(FB,56); tg=ImageFont.truetype(FR,32); cap=ImageFont.truetype(FB,64)
groups=[[("ZODL","Mobile · Shielded"),("Zingo!","Mobile/Desktop · Shielded"),("Edge","Mobile · Multi-coin")],
        [("Unstoppable","Mobile · Multi-coin"),("Cake","Mobile · Multi-coin"),("Zkool","Desktop/Mobile · Shielded")],
        [("Keystone","Hardware"),("Ledger","Hardware"),("Trezor","Hardware")]]
SEG=6; SEC=SEG*len(groups)
os.makedirs("frames_s7",exist_ok=True)
def ease(t): t=min(max(t,0),1); return 1-(1-t)**3
def mix(c,a): return tuple(int(x*a+b*(1-a)) for x,b in zip(c,BG))
for i in range(FPS*SEC):
    t=i/FPS; g=int(t//SEG); lt=t-g*SEG; im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    s="Pick a Zcash wallet"; w=d.textlength(s,font=cap); d.text(((W-w)/2,110),s,font=cap,fill=WHITE)
    out=ease((lt-(SEG-0.6))/0.6)
    for k,(name,tag) in enumerate(groups[g]):
        a=ease((lt-k*0.3)/0.6); x0=160+k*560+int((1-a)*300)-int(out*400); y0=380
        al=a*(1-out)
        if al<=0: continue
        d.rounded_rectangle((x0,y0,x0+480,y0+360),radius=24,fill=mix(CARD,al),outline=mix(GOLD,al),width=4)
        d.rounded_rectangle((x0+80,y0+14,x0+400,y0+186),radius=16,fill=mix((228,232,236),al))
        lg=LOGO[name].copy(); lg.putalpha(lg.getchannel("A").point(lambda v:int(v*al))); im.paste(lg,(x0+90,y0+14),lg)
        w=d.textlength(name,font=nm); d.text((x0+240-w/2,y0+192),name,font=nm,fill=mix(WHITE,al))
        w=d.textlength(tag,font=tg); d.text((x0+240-w/2,y0+275),tag,font=tg,fill=mix(GREY,al))
    f="More at zechub.wiki/wallets"; w=d.textlength(f,font=tg); d.text(((W-w)/2,900),f,font=tg,fill=GOLD)
    im.save(f"frames_s7/f{i:04d}.png")
