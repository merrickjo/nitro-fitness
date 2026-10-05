from rig import *
from reg import mv
HIPS = RH(3, -6)
FH = dict(view="front")
CLASP = dict(handN=R(6,14), handF=R(-6,14))
GOBF = dict(handN=R(2,14), handF=R(-2,14), gear=[("kb","handN",270)])
def stF(x=110, **kw): return dict(FH, hip=(x,109), torso=90, footN=(x+14,190), footF=(x-14,190), **kw)
LL = dict(FH, hip=(130,134), torso=90, footN=(170,190), footF=(62,190), toeF=180)
def cossack(side, **kw):
    if side == "R": return dict(FH, hip=(128,148), torso=90, footN=(150,190), footF=(50,190), toeN=0, toeF=135, **kw)
    return dict(FH, hip=(92,148), torso=90, footN=(168,190), footF=(60,190), toeN=45, toeF=180, **kw)
# --- KB ---
mv("KB lateral lunge", stF(110, **GOBF), dict(LL, **GOBF))
mv("KB goblet Cossack squat", cossack("R", **GOBF), cossack("L", **GOBF))
BXF = [("box",118,50,40)]
mv("KB lateral step-up",
   dict(FH, hip=(120,128), torso=90, footN=(143,152), footF=(96,190), **GOBF, ) | dict(gear=BXF+[("kb","handN",270)]),
   dict(FH, hip=(143,72), torso=90, footN=(143,152), footF=(120,126), toeF=180, **GOBF) | dict(gear=BXF+[("kb","handN",270)]))
SUITF = dict(handN=R(24,52), handF=RH(-18,-4), gear=[("kb","handN",270)])
mv("KB suitcase lateral march",
   dict(FH, hip=(110,109), torso=90, footN=(150,190), footF=(70,190), **SUITF),
   dict(FH, hip=(110,109), torso=90, footN=(150,190), footF=(112,190), **SUITF) | dict(gear=[("kb","handN",270),("arrow",(150,40),(200,40))]))
# skater / bound (shared with BW + warm-up)
SK1 = dict(FH, hip=(118,128), torso=96, footN=(126,190), footF=(152,180), toeF=270)
SK2 = dict(FH, hip=(102,128), torso=84, footN=(68,180), footF=(94,190), toeN=270)
mv("KB skater step, no jump", dict(SK1, **GOBF), dict(SK2, **GOBF))
mv("Skater step, no jump", dict(SK1, **CLASP), dict(SK2, **CLASP))
mv("Skater bound",
   dict(SK1, handN=R(-30,24), handF=R(30,-10)),
   dict(FH, hip=(150,100), torso=84, footN=(160,150), footF=(112,160), toeN=300, toeF=300, handN=R(30,-10), handF=R(-30,24), gear=[("arrow",(76,40),(130,40))]))
TF = [("trx",(110,-16),["handN","handF"])]
TFH = dict(handN=R(26,18), handF=R(-26,18), gear=TF)
mv("TRX lateral lunge", stF(110, **TFH), dict(LL, **TFH))
mv("TRX crossing balance lunge", stF(110, **TFH),
   dict(FH, hip=(112,142), torso=90, footN=(124,190), footF=(150,178), toeF=270, **TFH))
# --- BW ---
mv("Lateral lunge", stF(110, **CLASP), dict(LL, **CLASP))
mv("Cossack squat", cossack("R", **CLASP), cossack("L", **CLASP))
mv("Lateral bound to stick",
   dict(FH, hip=(92,138), torso=90, footF=(90,190), footN=(150,158), toeN=300, **CLASP),
   dict(FH, hip=(150,138), torso=90, footN=(152,190), footF=(112,170), toeF=270, **CLASP, ) | dict(gear=[("arrow",(80,60),(140,60))]))
mv("Lateral shuffle, three steps to stop",
   dict(FH, hip=(100,128), torso=90, footN=(140,190), footF=(60,190), handN=R(30,28), handF=R(-30,28), gear=[("arrow",(130,50),(190,50))]),
   dict(FH, hip=(140,132), torso=90, footN=(190,190), footF=(96,190), handN=R(34,22), handF=R(-34,22)))
SB = [("box",92,30,24)]
mv("Lateral step-over",
   dict(FH, hip=(100,112), torso=90, footN=(112,164), footF=(84,190), toeN=0, **CLASP, gear=SB),
   dict(FH, hip=(142,112), torso=90, footN=(150,190), footF=(124,164), toeF=180, **CLASP, gear=SB))
BC = dict(hip=(96,134), torso=0, head=12, footN=(60,186), footF=(58,185), toeN=270, toeF=270)
mv("Lateral crawl",
   dict(BC, handN=(148,189), handF=(144,189)),
   dict(BC, handN=(148,160), handF=(144,189), footN=(60,186), footF=(70,160), gear=[]))
