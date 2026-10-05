from rig import *
from reg import mv
HIPS = RH(3, -6)
KBH = [("kb","handN",270)]
SWB = dict(hip=(92,125), torso=30, head=42, footN=(120,190), footF=(118,190), handN=(104,150), handF=(104,150))
RACK = dict(armN=(285,80), handF=HIPS, gear=[("kb","handN",250)])
STK = lambda **kw: stand(110, **kw)
mv("KB swing", dict(SWB, gear=[("kb","handN",270)]),
   dict(hip=(118,109), torso=92, footN=(120,190), footF=(118,190), handN=(174,64), handF=(174,64), gear=[("kb","handN",0)]))
mv("KB single-arm swing", dict(SWB, handF=R(-26,40), gear=[("kb","handN",270)]),
   dict(hip=(118,109), torso=92, footN=(120,190), footF=(118,190), handN=(174,64), handF=R(-30,30), gear=[("kb","handN",0)]))
mv("KB high pull", dict(SWB, gear=[("kb","handN",270)]),
   STK(handN=R(24,10), handF=R(24,10), eN=1, eF=1, gear=[("kb","handN",270)]))
mv("KB clean", dict(SWB, handF=HIPS, gear=[("kb","handN",270)]), STK(**RACK))
mv("KB snatch", dict(SWB, handF=HIPS, gear=[("kb","handN",270)]),
   STK(armN=(92,88), handF=R(-20,40), gear=[("kb","handN",160)]))
RDLB = dict(hip=(78,120), torso=28, footN=(110,190), footF=(108,190))
mv("KB Romanian deadlift", STK(handN=HANG, handF=HANG, gear=KBH),
   dict(RDLB, handN=R(2,54), handF=R(2,54), gear=KBH))
mv("KB single-leg RDL", stand(110, footN=(112,190), footF=(108,190), handN=HANG, handF=R(-24,40), gear=KBH),
   dict(hip=(106,114), torso=8, footN=(116,190), footF=(30,120), toeF=250, handN=HANG, handF=R(-30,30), gear=KBH))
TA = [("trx",(165,-8),["ankleN","ankleF"])]
mv("TRX hamstring curl",
   dict(hip=(84,152), torso=200, head=190, footN=(160,134), footF=(158,132), toeN=60, toeF=60, handN=R(44,18), handF=R(40,18), gear=TA),
   dict(hip=(84,152), torso=200, head=190, footN=(112,134), footF=(110,132), toeN=60, toeF=60, handN=R(44,18), handF=R(40,18), gear=TA))
ARMS_BACK = R(-46,22)
mv("Squat jump",
   dict(hip=(80,150), torso=55, footN=(114,190), footF=(112,190), handN=R(-46,22), handF=R(-46,22)),
   dict(hip=(112,92), torso=90, footN=(112,172), footF=(108,170), toeN=285, toeF=285, handN=R(10,-48), handF=R(10,-48)))
mv("Split jump",
   dict(hip=(104,130), torso=86, footN=(142,190), footF=(62,176), toeF=262, handN=R(30,-18), handF=R(-30,34)),
   dict(hip=(106,78), torso=90, footN=(146,146), footF=(68,150), toeN=300, toeF=250, handN=R(-30,34), handF=R(30,-18)))
mv("Broad jump, walk back",
   dict(hip=(80,150), torso=50, footN=(114,190), footF=(112,190), handN=R(-46,22), handF=R(-46,22)),
   dict(hip=(108,92), torso=62, footN=(62,150), footF=(58,148), toeN=250, toeF=250, handN=R(50,-18), handF=R(50,-18), gear=[("arrow",(140,176),(206,176))]))
mv("Pogo hop",
   dict(hip=(110,103), torso=90, footN=(114,181), footF=(108,181), toeN=285, toeF=285, handN=HANG, handF=HANG),
   dict(hip=(110,85), torso=90, footN=(114,163), footF=(108,163), toeN=285, toeF=285, handN=HANG, handF=HANG, gear=[("arrow",(160,150),(160,100))]))
SLB = dict(footN=(128,190), toeN=0, footF=(172,134), toeF=50, handN=R(46,6), handF=R(42,6))
mv("Single-leg glute bridge",
   dict(hip=(90,184), torso=190, head=182, **SLB) | dict(footF=(160,150)),
   dict(hip=(100,160), torso=208, head=198, **SLB) | dict(footF=(172,132)))
mv("Nordic curl negative",
   dict(hip=(110,146), torso=90, footN=(66,188), footF=(64,187), toeN=180, toeF=180, handN=R(8,18), handF=R(8,18)),
   dict(hip=(142,158), torso=40, footN=(66,188), footF=(64,187), toeN=180, toeF=180, handN=R(8,18), handF=R(8,18), gear=[("arrow",(206,96),(206,150))]))
mv("Single-leg hinge, arms overhead",
   stand(110, footN=(112,190), footF=(108,190), armN=(90,90), armF=(90,90)),
   dict(hip=(106,114), torso=8, footN=(116,190), footF=(30,120), toeF=250, armN=(10,10), armF=(10,10)))
mv("Tuck jump",
   dict(hip=(82,150), torso=55, footN=(114,190), footF=(112,190), handN=R(-46,22), handF=R(-46,22)),
   dict(hip=(112,84), torso=92, footN=(106,132), footF=(110,134), toeN=290, toeF=290, handN=R(30,26), handF=R(30,26)))
