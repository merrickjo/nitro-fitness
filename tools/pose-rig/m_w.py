from rig import *
from reg import MOVES, mv
import m_c1, m_a1
HIPS = RH(3, -6)
# aliases that share a figure with an existing move
MOVES["Bodyweight reverse lunge"] = MOVES["Reverse lunge"]
MOVES["Bodyweight lateral lunge"] = MOVES["Lateral lunge"]
MOVES["Cossack rock"] = MOVES["Cossack squat"]
PR = dict(handN=R(16,14), handF=R(16,14))
mv("Deep squat ankle rock",
   dict(hip=(80,162), torso=72, footN=(114,190), footF=(112,190), **PR),
   dict(hip=(90,164), torso=66, footN=(114,190), footF=(112,190), **PR, gear=[("arrow",(150,150),(176,150))]))
S90 = dict(hip=(100,186), torso=90)
mv("90/90 hip switch",
   dict(S90, legN=(10,190), legF=(172,350), handN=R(24,26), handF=R(24,26)),
   dict(S90, legN=(172,350), legF=(10,190), handN=R(24,26), handF=R(24,26)))
LG = dict(hip=(96,160), footN=(146,190), footF=(44,182), toeF=262)
mv("World's greatest stretch",
   dict(LG, torso=25, handN=(142,186), handF=(138,186)),
   dict(LG, torso=40, armN=(90,90), handF=(140,184)))
SLH = dict(hip=(106,114), torso=8, footN=(116,190), footF=(30,120), toeF=250)
mv("Hip airplane", dict(SLH, handN=R(2,54), handF=R(2,54)), dict(SLH, armN=(90,90), armF=(270,270)))
mv("Knee circles + ankle CARs",
   stand(110, footN=(112,190), footF=(104,134), toeF=270, handN=HIPS, handF=HIPS, gear=[("arc","kneeF",18,40,330)]),
   stand(110, footN=(112,190), footF=(104,134), toeF=270, handN=HIPS, handF=HIPS, gear=[("arc","ankleF",18,40,330)]))
mv("Split-stance ankle bounce",
   dict(hip=(110,114), torso=90, footN=(136,190), footF=(84,190), handN=R(20,32), handF=R(-10,30)),
   dict(hip=(110,106), torso=90, footN=(136,180), footF=(84,180), toeN=285, toeF=285, handN=R(20,32), handF=R(-10,30)))
mv("Walking knee hug into lunge",
   stand(110, footN=(112,190), footF=(104,134), toeF=270, handN=R(34,40), handF=R(34,40)),
   dict(hip=(106,130), torso=86, footN=(148,190), footF=(66,176), toeF=262, handN=HIPS, handF=HIPS))
mv("A-march into split step",
   stand(110, footN=(112,190), footF=(150,124), toeF=0, handN=R(24,24), handF=R(-24,30)),
   dict(hip=(110,118), torso=84, footN=(138,190), footF=(86,190), handN=R(26,26), handF=R(-10,28)))
MOVES["Kettlebell halo"] = MOVES.pop("KB halo")
MOVES["Kettlebell around-the-world"] = MOVES.pop("KB around-the-world")
