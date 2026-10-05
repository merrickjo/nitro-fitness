from rig import *
from reg import mv
HIPS = RH(3, -6)
# --- TRX shoulder work (front view, leaning back into the straps) ---
def ftx(hands, **kw):
    d = dict(view="front", hip=(110,114), torso=90, footN=(122,190), footF=(98,190),
             gear=[("trx",(110,-16),["handN","handF"])]); d.update(hands); d.update(kw); return d
Y = dict(armN=(52,52), armF=(128,128)); T = dict(armN=(2,2), armF=(178,178))
Wp = dict(armN=(-35,55), armF=(215,125)); I = dict(armN=(88,88), armF=(92,92))
FWD = dict(handN=R(10,26), handF=R(-10,26))
mv("TRX Y-fly", ftx(FWD), ftx(Y))
mv("TRX T-fly", ftx(FWD), ftx(T))
mv("TRX I-Y-T complex", ftx(I), ftx(Y), ftx(T))
mv("TRX Y-T-W pull", ftx(Y), ftx(T), ftx(Wp))
# face pull: side view, leaning back, hands pull to face with elbows high
FPA = [("trx",(212,-6),["handN","handF"])]
mv("TRX face pull",
   dict(lean(150,18), handN=(162,46), handF=(162,46), gear=FPA),
   dict(lean(150,18), handN=R(14,-6), handF=R(14,-6), eN=1, eF=1, gear=FPA))
# --- prone, seen from above ---
def top(**kw):
    d = dict(view="front", noground=True, hip=(110,112), torso=90, footN=(118,192), footF=(102,192), toeN=270, toeF=270,
             gear=[("mat",52,178),("label",72,14,"TOP VIEW")]); d.update(kw); return d
mv("Prone Y-T-W", top(**Y), top(**T), top(**Wp))
mv("Prone external rotation, elbows at 90", top(armN=(0,270), armF=(180,270)), top(armN=(0,90), armF=(180,90)))
# --- kneeling presses ---
HK = dict(hip=(92,148), torso=90, footN=(132,190), footF=(48,188), toeF=180)
mv("KB bottoms-up press, half kneeling",
   dict(HK, armN=(285,80), handF=HIPS, gear=[("kb","handN",100)]),
   dict(HK, armN=(92,88), handF=HIPS, gear=[("kb","handN",92)]))
mv("KB half-kneeling overhead press",
   dict(HK, armN=(285,80), handF=HIPS, gear=[("kb","handN",250)]),
   dict(HK, armN=(92,88), handF=HIPS, gear=[("kb","handN",160)]))
# --- armbar (lying, bell up) ---
AB = dict(hip=(140,186), torso=180, head=172, footN=(172,190), footF=(214,188), toeN=60, toeF=70, handF=R(46,8))
mv("KB armbar", dict(AB, armN=(90,90), gear=[("kb","handN",120)]),
   dict(AB, torso=192, head=186, armN=(90,90), gear=[("kb","handN",120),("arrow",(150,140),(150,160))]))
mv("KB waiter carry",
   dict(hip=(108,113), torso=90, footN=(128,190), footF=(88,190), armN=(92,88), handF=R(-26,40), gear=[("kb","handN",120)]),
   dict(hip=(110,113), torso=90, footN=(112,190), footF=(138,148), toeF=0, armN=(92,88), handF=R(-26,40), gear=[("kb","handN",120)]))
# --- wall work (side view, back to the wall) ---
WL = [("wall",74,-1)]
BK = dict(hip=(94,109), torso=90, footN=(100,190), footF=(98,190))
mv("Wall slide", dict(BK, armN=(180,90), armF=(180,90), gear=WL), dict(BK, armN=(92,92), armF=(94,94), gear=WL))
mv("Wall slide with lift-off", dict(BK, armN=(92,92), armF=(94,94), gear=WL), dict(BK, armN=(62,62), armF=(64,64), gear=WL))
# --- plank-based ---
def plank(shy, ax=32, **kw):
    sx = 150; dx = sx-ax; dy = math.sqrt(max(0, 131**2 - dx**2)); sy = 188-dy+ (shy)
    th = math.degrees(math.atan2(188-sy, dx)); hip = (sx-50*math.cos(math.radians(th)), sy+50*math.sin(math.radians(th)))
    d = dict(hip=hip, torso=th, head=th-6, footN=(ax,188), footF=(ax-3,188), toeN=300, toeF=300,
             handN=(sx,189), handF=(sx-4,189)); d.update(kw); return d
mv("Scapular push-up", plank(4, gear=[("arrow",(104,110),(104,128))]), plank(-4, ax=36, gear=[("arrow",(104,128),(104,110))]))
def pike(hip, torso, **kw):
    d = dict(hip=hip, torso=torso, head=torso+20, footN=(150,190), footF=(147,190), toeN=0, toeF=0, handN=(66,190), handF=(70,190)); d.update(kw); return d
mv("Pike push-up", pike((116,116), 205), pike((112,120), 235))
# --- side-lying external rotation ---
SL = dict(hip=(150,184), torso=180, head=172, footN=(214,186), footF=(212,184), toeN=60, toeF=60, handF=R(42,6))
mv("Side-lying external rotation", dict(SL, armN=(20,320)), dict(SL, armN=(20,90)))
# --- standing shoulder drills ---
mv("KB halo",
   stand(110, handN=R(18,-6), handF=R(18,-6), gear=[("kb","handN",270)]),
   stand(110, handN=R(-14,-14), handF=R(-14,-14), gear=[("kb","handN",270)]))
mv("KB around-the-world",
   stand(110, handN=RH(18,2), handF=RH(18,2), gear=[("kb","handN",270)]),
   stand(110, handN=RH(-16,0), handF=RH(-16,0), gear=[("kb","handN",270)]))
mv("Shoulder CARs",
   stand(110, armN=(60,70), handF=HANG, gear=[("arc","sh",34,110,330)]),
   stand(110, armN=(235,250), handF=HANG, gear=[("arc","sh",34,330,110+360)]))
