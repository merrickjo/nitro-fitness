from rig import *
from reg import mv
HIPS = RH(3, -6)
GOB = dict(handN=R(0,14), handF=R(0,14), gear=[("kb","handN",270)])
def gob(d, front=False):
    d = dict(d); d.update(handN=R(17,14), handF=R(17,14), gear=[("kb","handN",270)]); return d
def squat_bottom(**kw): return dict(hip=(86,158), torso=66, footN=(114,190), footF=(112,190), **kw)
def rl_bottom(**kw): return dict(hip=(104,130), torso=86, footN=(142,190), footF=(62,176), toeF=262, **kw)
def split(top=True, **kw):
    return dict(hip=(106,116 if top else 154), torso=88, footN=(142 if top else 140,190), footF=(74,180), toeF=262, **kw)
ARM_FWD = R(52,4)

# --- KB ---
mv("KB goblet reverse lunge", gob(stand(110)), gob(rl_bottom()))
mv("KB goblet split squat", gob(split(True)), gob(split(False)))
RACK = dict(armN=(285,80), handF=HIPS, gear=[("kb","handN",250)])
mv("KB front-rack step-back lunge", stand(110, **RACK), rl_bottom(**RACK))
mv("KB goblet squat, 3-second lower",
   dict(gob(stand(110)), gear=[("kb","handN",270),("arrow",(176,60),(176,112))]),
   gob(squat_bottom()))
# curtsy (front view): bell at chest
CH = dict(view="front", handN=R(0,14), handF=R(0,14), gear=[("kb","handN",270)])
mv("KB goblet curtsy lunge",
   dict(hip=(110,109), torso=90, footN=(125,190), footF=(95,190), **CH),
   dict(hip=(112,142), torso=90, footN=(124,190), footF=(150,178), toeF=270, **CH))
TP = [("trx",(205,4),["handN","handF"])]
mv("TRX-assisted pistol squat",
   dict(hip=(110,109), torso=90, footN=(112,190), footF=(150,158), toeF=60, handN=R(34,-8), handF=R(34,-8), gear=TP),
   dict(hip=(78,152), torso=62, footN=(112,190), footF=(158,150), toeF=70, handN=R(34,-8), handF=R(34,-8), gear=TP))
RF = [("trx",(46,4),["ankleF"])]
mv("TRX lunge, rear foot in strap",
   dict(hip=(118,114), torso=84, footN=(140,190), footF=(55,150), toeF=250, handN=R(28,22), handF=R(28,22), gear=RF),
   dict(hip=(100,150), torso=78, footN=(140,190), footF=(55,150), toeF=250, handN=R(28,22), handF=R(28,22), gear=RF))
SUIT = dict(handN=HANG, handF=HIPS, gear=[("kb","handN",270)])
mv("KB suitcase reverse lunge", stand(110, **SUIT), rl_bottom(**SUIT))

# --- BW ---
mv("Reverse lunge", stand(110, handN=HIPS, handF=HIPS), rl_bottom(handN=HIPS, handF=HIPS))
mv("Split squat, 2-second pause", split(True, handN=HIPS, handF=HIPS), split(False, handN=HIPS, handF=HIPS))
BOX = [("box",18,44,42)]
mv("Bulgarian split squat",
   dict(hip=(108,118), torso=88, footN=(146,190), footF=(60,148), toeF=180, handN=HIPS, handF=HIPS, gear=BOX),
   dict(hip=(106,156), torso=84, footN=(146,190), footF=(60,148), toeF=180, handN=HIPS, handF=HIPS, gear=BOX))
mv("Tempo squat, 3-second lower",
   stand(110, handN=ARM_FWD, handF=ARM_FWD, gear=[("arrow",(176,60),(176,112))]),
   squat_bottom(handN=ARM_FWD, handF=ARM_FWD))
CB = [("box",118,48,40)]
mv("Step-up onto a chair",
   dict(hip=(110,118), torso=80, footN=(142,152), footF=(98,190), handN=HIPS, handF=HIPS, gear=CB),
   dict(hip=(140,72), torso=90, footN=(142,152), footF=(158,118), toeF=0, handN=HIPS, handF=HIPS, gear=CB))
CH2 = dict(view="front", handN=RH(18,-4), handF=RH(-18,-4))
mv("Curtsy lunge",
   dict(hip=(110,109), torso=90, footN=(125,190), footF=(95,190), view="front", handN=RH(18,-4), handF=RH(-18,-4)),
   dict(hip=(112,142), torso=90, footN=(124,190), footF=(150,178), toeF=270, **CH2))
BX = [("box",18,44,36)]
mv("Assisted pistol squat",
   dict(hip=(110,109), torso=90, footN=(112,190), footF=(150,158), toeF=60, handN=ARM_FWD, handF=ARM_FWD, gear=BX),
   dict(hip=(76,152), torso=62, footN=(112,190), footF=(156,150), toeF=70, handN=ARM_FWD, handF=ARM_FWD, gear=BX))
mv("Walking lunge",
   rl_bottom(handN=HIPS, handF=HIPS) | dict(footN=(148,190), footF=(66,176)),
   dict(hip=(112,112), torso=88, footN=(112,190), footF=(140,148), toeF=0, handN=HIPS, handF=HIPS))
