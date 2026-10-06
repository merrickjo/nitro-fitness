"""Gym kit: pin-loaded machines, the cable station, dumbbells and benches.
Machines are drawn as a few thin rods and thick pads so the body position stays the subject."""
from rig import *
from reg import mv
HIPS = RH(3, -6)
DBV = [("db", "handN", 90)]                       # one dumbbell held upright at the chest
DB2 = [("db", "handN", 0), ("db", "handF", 0)]    # one in each hand
DB1 = [("db", "handN", 0)]
def gob(d):
    d = dict(d); d.update(handN=R(17,14), handF=R(17,14), gear=d.get("gear", []) + DBV); return d
def sides(d, extra=()):
    d = dict(d); d.update(handN=R(3,54), handF=R(1,54), gear=list(extra) + DB2); return d

# ── A1 knee-dominant ────────────────────────────────────────────
def rl_bottom(**kw): return dict(hip=(104,130), torso=86, footN=(142,190), footF=(62,176), toeF=262, **kw)
def split(top=True, **kw):
    return dict(hip=(106,116 if top else 154), torso=88, footN=(142 if top else 140,190), footF=(74,180), toeF=262, **kw)
mv("DB goblet reverse lunge", gob(stand(110)), gob(rl_bottom()))
mv("DB split squat", sides(split(True)), sides(split(False)))
BB = [("bench",14,62,46)]
mv("DB Bulgarian split squat, rear foot on bench",
   sides(dict(hip=(108,118), torso=88, footN=(146,190), footF=(58,144), toeF=180), BB),
   sides(dict(hip=(106,156), torso=84, footN=(146,190), footF=(58,144), toeF=180), BB))
mv("DB goblet squat, 3-second lower",
   gob(stand(110, gear=[("arrow",(176,60),(176,112))])),
   gob(dict(hip=(86,158), torso=66, footN=(114,190), footF=(112,190))))
SB = [("bench",118,190,44)]
mv("DB step-up onto bench",
   sides(dict(hip=(110,118), torso=80, footN=(142,150), footF=(98,190)), SB),
   sides(dict(hip=(140,70), torso=90, footN=(142,150), footF=(158,116), toeF=0), SB))
mv("DB walking lunge",
   sides(rl_bottom() | dict(footN=(148,190), footF=(66,176))),
   sides(dict(hip=(112,112), torso=88, footN=(112,190), footF=(140,148), toeF=0)))

# ── A2 pull ─────────────────────────────────────────────────────
def seated(x=92, **kw):
    d = dict(hip=(x,146), torso=90, footN=(x+46,190), footF=(x+44,190)); d.update(kw); return d
def rowm(**kw):   # seated row machine: seat, chest pad, foot plates, swinging lever
    d = seated(84, footN=(138,176), footF=(136,176), toeN=55, toeF=55)
    d["gear"] = [("pad",(66,158),(104,158)), ("rod",(84,160),(84,196)),
                 ("pad",(110,84),(110,128)), ("rod",(110,128),(126,196)),
                 ("rod","handN",(176,194)), ("rod",(140,196),(200,196))]
    d.update(kw); return d
mv("Seated row machine", rowm(handN=R(54,6), handF=R(54,6)), rowm(armN=(215,8), armF=(215,8)))
mv("Seated row machine, single arm", rowm(handN=R(54,6), handF=RH(26,-6)), rowm(armN=(215,8), handF=RH(26,-6)))
def post(x, py):  return [("rod",(x,-8),(x,196)), ("pulley",(x,py))]
CS = dict(hip=(98,114), torso=84, footN=(120,190), footF=(84,190))
mv("Standing cable row",
   dict(CS, handN=R(52,10), handF=R(52,10), gear=post(214,74)+[("line",(214,74),"handN")]),
   dict(CS, armN=(215,5), armF=(215,5), gear=post(214,74)+[("line",(214,74),"handN")]))
TK = dict(hip=(110,146), torso=90, footN=(66,188), footF=(64,187), toeN=180, toeF=180)
LP = [("pulley",(124,-12)), ("line",(124,-12),"handN"), ("pulley","handN",1)]
mv("Cable lat pulldown, kneeling",
   dict(TK, handN=R(12,-54), handF=R(12,-54), gear=LP),
   dict(TK, torso=94, handN=R(16,-4), handF=R(16,-4), eN=-1, eF=-1, gear=LP))
OB = [("bench",120,206,44)]
ROW = dict(hip=(88,118), torso=22, footN=(108,190), footF=(84,190), handF=(140,150))
mv("DB one-arm row, hand on bench",
   dict(ROW, handN=R(-2,54), gear=OB+DB1),
   dict(ROW, armN=(184,266), gear=OB+DB1))
# prone on an incline bench (chest supported), facing up the pad
def incl(**kw):
    d = dict(hip=(90,146), torso=45, head=38, footN=(46,190), footF=(40,190), toeN=180, toeF=180,
             gear=[("pad",(86,164),(142,108)), ("rod",(114,138),(114,196)), ("rod",(92,196),(140,196))])
    g = kw.pop("gear", []); d.update(kw); d["gear"] = d["gear"] + g; return d
mv("Chest-supported DB row, incline bench",
   incl(handN=R(2,54), handF=R(0,54), gear=DB2), incl(armN=(203,268), armF=(203,268), gear=DB2))

# ── B1 hinge ────────────────────────────────────────────────────
def chest(sh, hip): return (sh[0] + (hip[0]-sh[0])*.42 + 4, sh[1] + (hip[1]-sh[1])*.42 + 4)
BE = [("pad",(84,154),(104,134)), ("rod",(94,146),(94,196)), ("rod",(28,196),(128,196)),
      ("rod",(28,196),(46,184)), ("pulley",(31,172))]
def bext(torso, **kw):
    d = dict(hip=(98,124), torso=torso, footN=(40,182), footF=(38,181), toeN=320, toeF=320, handN=chest, handF=chest, gear=BE)
    d.update(kw); return d
mv("45° back extension", bext(-52, head=-40), bext(45))
mv("45° back extension, single leg",
   bext(-52, head=-40, footF=(36,140), toeF=250), bext(45, footF=(30,150), toeF=250))
STK = lambda **kw: stand(110, **kw)
RDLB = dict(hip=(78,120), torso=28, footN=(110,190), footF=(108,190))
mv("DB Romanian deadlift", STK(handN=R(3,54), handF=R(1,54), gear=DB2),
   dict(RDLB, handN=R(2,54), handF=R(0,54), gear=DB2))
mv("DB single-leg RDL", stand(110, footN=(112,190), footF=(108,190), handN=HANG, handF=R(-24,40), gear=DB1),
   dict(hip=(106,114), torso=8, footN=(116,190), footF=(30,120), toeF=250, handN=HANG, handF=R(-30,30), gear=DB1))
PT = post(12,176)
mv("Cable pull-through",
   dict(hip=(84,122), torso=30, head=40, footN=(120,190), footF=(112,190), handN=(100,146), handF=(100,146), gear=PT+[("line",(12,176),"handN")]),
   dict(hip=(118,109), torso=92, footN=(120,190), footF=(112,190), handN=RH(4,0), handF=RH(4,0), gear=PT+[("line",(12,176),"handN")]))
mv("DB squat jump",
   dict(hip=(80,150), torso=55, footN=(114,190), footF=(112,190), handN=R(8,50), handF=R(6,50), gear=DB2),
   dict(hip=(112,92), torso=90, footN=(112,172), footF=(108,170), toeN=285, toeF=285, handN=R(3,54), handF=R(1,54), gear=DB2))

# ── B2 scapula + cuff ───────────────────────────────────────────
def topv(**kw):   # seen from above: shoulders, head, arms
    d = dict(view="front", nolegs=True, noground=True, hip=(110,180), torso=90, head=270,
             footN=(118,192), footF=(102,192)); g = kw.pop("gear", []); d.update(kw)
    ly = kw.pop("ly", 84)   # the zero-width rod only reserves headroom so the label is inside the card
    d["gear"] = g + [("label",70,ly,"TOP VIEW"), ("rod",(70,ly-14),(70,ly-14),0)]; return d
RD = [("pad",(94,116),(126,116))]
def rdf(**kw): return topv(gear=RD, ly=62, **kw)
mv("Rear delt fly machine", rdf(handN=R(15,-54), handF=R(-15,-54)), rdf(armN=(-10,-14), armF=(190,194)))
FP = post(214,34)
FS = dict(hip=(100,112), torso=94, footN=(124,190), footF=(84,190))
mv("Cable face pull",
   dict(FS, handN=R(52,-12), handF=R(52,-12), gear=FP+[("line",(214,34),"handN")]),
   dict(FS, handN=R(14,-8), handF=R(14,-8), eN=1, eF=1, gear=FP+[("line",(214,34),"handN")]))
SL = dict(hip=(140,140), torso=180, head=172, footN=(206,142), footF=(204,140), toeN=60, toeF=60, handF=R(42,6))
SLB = [("bench",52,222,46)]
mv("Side-lying DB external rotation, on bench",
   dict(SL, armN=(20,320), gear=SLB+[("db","handN",50)]), dict(SL, armN=(20,90), gear=SLB+[("db","handN",0)]))
def spm(**kw):    # shoulder press machine: reclined back pad, seat, lever from a rear pivot
    d = seated(96, torso=102)
    d["gear"] = [("pad",(76,160),(116,160)), ("rod",(96,162),(96,196)), ("pad",(82,150),(70,92)),
                 ("rod",(40,36),(40,196)), ("pulley",(40,36)), ("rod",(40,36),"handN")]
    d.update(kw); return d
mv("Shoulder press machine", spm(armN=(282,84), armF=(282,84)), spm(armN=(98,94), armF=(98,94)))
HK = dict(hip=(92,148), torso=90, footN=(132,190), footF=(48,188), toeF=180)
mv("Half-kneeling DB overhead press",
   dict(HK, armN=(285,80), handF=HIPS, gear=DB1), dict(HK, armN=(92,88), handF=HIPS, gear=DB1))
mv("Prone DB Y-raise, incline bench",
   incl(handN=R(2,54), handF=R(0,54), gear=DB2), incl(armN=(40,42), armF=(44,46), gear=DB2))

# ── C1 lateral (front view) ─────────────────────────────────────
FH = dict(view="front")
GOBF = dict(handN=R(2,14), handF=R(-2,14), gear=DBV)
def stF(x=110, **kw): return dict(FH, hip=(x,109), torso=90, footN=(x+14,190), footF=(x-14,190), **kw)
LL = dict(FH, hip=(130,134), torso=90, footN=(170,190), footF=(62,190), toeF=180)
def cossack(side, **kw):
    if side == "R": return dict(FH, hip=(128,148), torso=90, footN=(150,190), footF=(50,190), toeN=0, toeF=135, **kw)
    return dict(FH, hip=(92,148), torso=90, footN=(168,190), footF=(60,190), toeN=45, toeF=180, **kw)
mv("DB lateral lunge", stF(110, **GOBF), dict(LL, **GOBF))
mv("DB goblet Cossack squat", cossack("R", **GOBF), cossack("L", **GOBF))
BXF = [("box",118,50,40)]
mv("DB lateral step-up onto bench",
   dict(FH, hip=(120,128), torso=90, footN=(143,152), footF=(96,190), **GOBF) | dict(gear=BXF+DBV),
   dict(FH, hip=(143,72), torso=90, footN=(143,152), footF=(120,126), toeF=180, **GOBF) | dict(gear=BXF+DBV))
SUITF = dict(handN=R(24,52), handF=RH(-18,-4), gear=[("db","handN",90)])
mv("DB suitcase lateral march",
   dict(FH, hip=(110,109), torso=90, footN=(150,190), footF=(70,190), **SUITF),
   dict(FH, hip=(110,109), torso=90, footN=(150,190), footF=(112,190), **SUITF) | dict(gear=[("db","handN",90),("arrow",(150,40),(200,40))]))
SK1 = dict(FH, hip=(118,128), torso=96, footN=(126,190), footF=(152,180), toeF=270)
SK2 = dict(FH, hip=(102,128), torso=84, footN=(68,180), footF=(94,190), toeN=270)
mv("DB skater step, no jump", dict(SK1, **GOBF), dict(SK2, **GOBF))

# ── C2 rotation ─────────────────────────────────────────────────
def rot(dx, arc):   # rotary torso machine, front view: hands fixed on the handles, seat and knees swing
    return dict(FH, hip=(110,138), torso=90, handN=(150,44), handF=(70,44),
                footN=(110+dx+12,188), footF=(110+dx-12,188), toeN=270, toeF=270, kN=1 if dx > 0 else -1, kF=1 if dx > 0 else -1,
                gear=[("pad",(92,150),(128,150)), ("rod",(110,152),(110,196)), ("rod",(70,44),(86,14),3), ("rod",(150,44),(134,14),3),
                      ("rod",(86,14),(134,14),3), ("arc",(110,150),50,*arc)])
mv("Rotary torso machine", rot(-30, (250,300)), rot(30, (290,240)))
def chopf(hand, py): 
    return dict(FH, hip=(110,109), torso=90, footN=(134,190), footF=(86,190), handN=hand, handF=hand,
                gear=post(16,py)+[("line",(16,py),"handN")])
mv("Cable woodchop, high to low", chopf((84,34),8), chopf((128,104),8))
mv("Cable reverse chop, low to high", chopf((92,104),176), chopf((136,34),176))
def pal(hy): return topv(hip=(110,200), ly=70, handN=R(5,hy), handF=R(-1,hy), gear=[("pulley",(8,100)),("line",(8,100),"handN")])
mv("Cable Pallof press", pal(-24), pal(-54))
SUIT = dict(handN=HANG, handF=HIPS, gear=DB1)
mv("DB suitcase carry", stand(110, footN=(128,190), footF=(92,190), **SUIT),
   stand(110, footN=(112,190), footF=(136,150), toeF=0, **SUIT))
