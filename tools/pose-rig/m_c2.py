from rig import *
from reg import mv
HIPS = RH(3, -6)
HK = dict(hip=(92,148), torso=90, footN=(132,190), footF=(48,188), toeF=180)
# --- KB chops: half kneeling, bell travels diagonally ---
HI = dict(handN=R(26,-34), handF=R(24,-30), gear=[("kb","handN",250)])
LO = dict(handN=R(-6,56), handF=R(-8,54), gear=[("kb","handN",270)])
mv("KB half-kneeling woodchop", dict(HK, **HI), dict(HK, **LO))
mv("KB half-kneeling reverse chop", dict(HK, **LO), dict(HK, **HI))
# windmill (front view): bell overhead, hinge toward the free hand
WM = dict(view="front", footN=(160,190), footF=(78,190), toeN=0, toeF=180)
mv("KB windmill",
   dict(WM, hip=(119,112), torso=90, armN=(90,90), handF=RH(-24,-4), gear=[("kb","handN",90)]),
   dict(WM, hip=(140,126), torso=140, footN=(168,190), footF=(82,190), armN=(90,90), handF=(88,160), gear=[("kb","handN",90)]))
SUIT = dict(handN=HANG, handF=HIPS, gear=[("kb","handN",270)])
mv("KB suitcase carry", stand(110, footN=(128,190), footF=(92,190), **SUIT),
   stand(110, footN=(112,190), footF=(136,150), toeF=0, **SUIT))
# Russian twist: seated V, bell passes side to side
RT = dict(hip=(96,186), torso=124, head=130, footN=(172,160), footF=(170,158), toeN=60, toeF=60)
mv("KB Russian twist", dict(RT, handN=R(34,30), handF=R(34,30), gear=[("kb","handN",300)]),
   dict(RT, handN=R(-8,52), handF=R(-8,52), gear=[("kb","handN",270)]))
# TRX anti-rotation / trunk work
mv("TRX body saw",
   dict(hip=(98,150), torso=0, head=8, footN=(18,150), footF=(16,149), toeN=270, toeF=270, armN=(270,0), armF=(270,0), gear=[("trx",(18,-14),["ankleN","ankleF"])]),
   dict(hip=(128,150), torso=0, head=8, footN=(48,150), footF=(46,149), toeN=270, toeF=270, armN=(270,0), armF=(270,0), gear=[("trx",(18,-14),["ankleN","ankleF"]),("arrow",(70,100),(130,100))]))
FA = [("trx",(206,-12),["handN","handF"])]
mv("TRX fallout",
   dict(lean(100,-14), handN=R(6,40), handF=R(6,40), gear=FA),
   dict(lean(86,-34), armN=(40,40), armF=(42,42), gear=FA))
# Pallof (seen from above: shoulders, head, arms; strap from the anchor at the side)
def pal(hy, **kw):
    d = dict(view="front", nolegs=True, noground=True, hip=(110,200), torso=90, head=270, footN=(118,192), footF=(102,192),
             handN=R(5,hy), handF=R(-1,hy), gear=[("line",(8,100),"handN"),("label",70,22,"TOP VIEW")]); d.update(kw); return d
mv("TRX Pallof press", pal(-24), pal(-54))
# --- BW ---
mv("Half-kneeling anti-rotation reach",
   dict(HK, handN=R(10,-10), handF=R(12,-6)),
   dict(HK, armN=(14,14), armF=(190,190)))
DB = dict(hip=(110,186), torso=180, head=172, handN=None)
def db(legN, legF, armN, armF):
    return dict(hip=(110,186), torso=180, head=172, legN=legN, legF=legF, armN=armN, armF=armF, toeN=60, toeF=60)
mv("Dead bug", db((90,0),(90,0),(90,90),(90,90)), db((90,0),(8,8),(172,172),(90,90)))
SPN = lambda **kw: dict(lean(190,66), handN=(70,189), handF=RH(0,0), **kw)
sp1 = lean(190,66); sp1.update(handN=(70,189), handF=RH(2,-6), toeN=0)
mv("Side plank with top-leg lift", dict(sp1), dict(sp1, footF=(196,150)))
mv("Side plank thread the needle", dict(sp1, armF=(90,90)), dict(sp1, armF=(235,200)))
mv("Hollow body rock",
   dict(hip=(110,184), torso=162, head=150, armN=(166,166), armF=(168,168), footN=(186,158), footF=(184,156), toeN=70, toeF=70, gear=[]),
   dict(hip=(110,184), torso=172, head=164, armN=(176,176), armF=(178,178), footN=(190,168), footF=(188,166), toeN=70, toeF=70))
QD = dict(hip=(96,134), torso=0, head=12, footN=(58,186), footF=(56,185), toeN=270, toeF=270)
mv("Bird dog with a 2-second hold",
   dict(QD, handN=(148,189), handF=(144,189)),
   dict(QD, armN=(2,2), handF=(144,189), footN=(18,134), toeN=260))
PK = lambda **kw: dict(lean(36,-0), **kw)
def plk(ax=32, sy=0, **kw):
    sx = 150; dx = sx-ax; dy = math.sqrt(max(0, 131**2 - dx**2)); sy_ = 188-dy+sy
    th = math.degrees(math.atan2(188-sy_, dx)); hip = (sx-50*math.cos(math.radians(th)), sy_+50*math.sin(math.radians(th)))
    d = dict(hip=hip, torso=th, head=th-6, footN=(ax,188), footF=(ax-3,188), toeN=300, toeF=300, handN=(sx,189), handF=(sx-4,189)); d.update(kw); return d
mv("Plank shoulder tap", plk(), plk(handN=R(14,6)))
BC = dict(hip=(112,186), torso=168, head=160)
mv("Slow bicycle crunch",
   dict(BC, footN=(142,150), footF=(192,168), handN=R(-6,-20), handF=R(-6,-20), eN=1, eF=1, toeN=60, toeF=70),
   dict(BC, footN=(192,168), footF=(142,150), handN=R(-6,-20), handF=R(-6,-20), eN=1, eF=1, toeN=70, toeF=60))
