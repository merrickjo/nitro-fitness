from rig import *
from reg import mv
HIPS = RH(3, -6)
A1 = (212, 6)
TA = [("trx", A1, ["handN", "handF"])]
# --- TRX ---
mv("TRX row",
   dict(hip=(92,132), torso=135, footN=(150,190), footF=(148,190), toeN=55, toeF=55, handN=(106,69), handF=(106,69), gear=TA),
   dict(hip=(122,113), torso=110, footN=(150,190), footF=(148,190), toeN=55, toeF=55, handN=(107,71), handF=(107,71), gear=TA))
mv("TRX wide row",
   dict(hip=(92,132), torso=135, footN=(150,190), footF=(148,190), toeN=55, toeF=55, handN=(106,69), handF=(106,69), gear=TA),
   dict(hip=(122,113), torso=110, footN=(150,190), footF=(148,190), toeN=55, toeF=55, armN=(188,12), armF=(188,12), gear=TA))
TS = [("trx", A1, ["handN"])]
mv("TRX single-arm row",
   dict(hip=(92,132), torso=135, footN=(150,190), footF=(148,190), toeN=55, toeF=55, handN=(106,69), handF=RH(-6,-18), gear=TS),
   dict(hip=(122,113), torso=110, footN=(150,190), footF=(148,190), toeN=55, toeF=55, handN=(107,71), handF=RH(-6,-18), gear=TS))
FB = [("box",150,60,40), ("trx",(48,-14),["handN","handF"])]
mv("TRX row, feet elevated",
   dict(hip=(98,146), torso=173, head=185, footN=(176,151), footF=(172,151), toeN=70, toeF=70, handN=R(2,-56), handF=R(2,-56), gear=FB),
   dict(hip=(100,140), torso=158, head=170, footN=(176,151), footF=(172,151), toeN=70, toeF=70, handN=R(8,-18), handF=R(8,-18), gear=FB))
# --- KB ---
HING = dict(hip=(90,120), torso=40, footN=(112,190), footF=(110,190))
KBH = [("kb","handN",270)]
mv("KB bent-over row",
   dict(HING, handN=R(2,54), handF=(118,138), gear=KBH),
   dict(HING, armN=(203,265), handF=(118,138), gear=KBH))
GOR = dict(hip=(84,128), torso=20, footN=(110,190), footF=(108,190))
KB2 = [("kb","handN",270), ("kb","handF",270)]
mv("KB gorilla row",
   dict(GOR, handN=(134,166), handF=(130,166), gear=KB2),
   dict(GOR, armN=(203,265), handF=(130,166), gear=KB2))
mv("KB high-elbow row",
   dict(HING, handN=R(2,54), handF=(118,138), gear=KBH),
   dict(HING, armN=(172,255), handF=(118,138), gear=KBH))
# --- BW ---
TB = [("table",156,230,76)]
mv("Inverted row under a table",
   dict(hip=(94,178), torso=3, footN=(16,190), footF=(14,190), toeN=70, toeF=70, handN=(156,122), handF=(156,122), gear=TB),
   dict(hip=(94,166), torso=27, footN=(16,190), footF=(14,190), toeN=70, toeF=70, handN=(156,122), handF=(156,122), gear=TB))
DOOR = [("wall",150,1,90)]
mv("Towel row on a door handle",
   dict(lean(138,20), handN=(143,90), handF=(143,90), toeN=0, gear=DOOR+[("line",(143,90),"handN")]),
   dict(lean(138,8), handN=(143,90), handF=(143,90), toeN=0, gear=DOOR+[("line",(143,90),"handN")]))
mv("Reverse snow angel",
   prone(10, handN=R(-50,-8), handF=R(-50,-8)),
   prone(10, handN=R(52,-12), handF=R(52,-12)))
mv("Prone swimmer pull",
   prone(8, handN=R(52,-12), handF=R(52,-12)),
   prone(8, handN=R(-26,-14), handF=R(-26,-14)))
mv("Prone W hold-and-pull",
   prone(8, handN=R(52,-12), handF=R(52,-12)),
   prone(8, armN=(205,95), armF=(205,95)))
