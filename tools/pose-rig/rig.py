"""NITRO pose rig v2. One skeleton, fixed segment lengths, one stroke system.
Every move = joint targets (IK) or segment angles (FK). Colors are CSS vars so the
figures invert with the app's dark mode and fall back to black/white/grey standalone."""
import math, json, re

TORSO, HEAD_OFF, HEAD_R = 50, 20, 10.5
UA, FA, TH, SN, FT = 29, 27, 42, 40, 14          # upper arm, forearm, thigh, shin, foot
SWD, HWD = 28, 15                                 # front-view shoulder / hip width
W, H, GR = 230, 215, 196                          # pane size, ground line
WARN = []

def pol(p, a, l):
    r = math.radians(a); return (p[0] + l*math.cos(r), p[1] - l*math.sin(r))

def add(a, b): return (a[0]+b[0], a[1]+b[1])

def ik(root, tgt, l1, l2, bend, tag):
    dx, dy = tgt[0]-root[0], tgt[1]-root[1]
    d = max(1e-6, math.hypot(dx, dy))
    if d > l1 + l2 + 1.5: WARN.append(f"{tag}: unreachable by {d-(l1+l2):.1f}px")
    if d > l1 + l2 - 0.01:
        k = (l1 + l2 - 0.01) / d; dx, dy, d = dx*k, dy*k, l1 + l2 - 0.01
    a = (l1*l1 - l2*l2 + d*d) / (2*d); h = math.sqrt(max(0, l1*l1 - a*a))
    mx, my = root[0] + a*dx/d, root[1] + a*dy/d
    px, py = (dy/d, -dx/d) if bend > 0 else (-dy/d, dx/d)
    return (mx + h*px, my + h*py), (root[0]+dx, root[1]+dy)

def fmt(pts): return "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in pts)
def path(pts, cls, w): return f'<path d="{fmt(pts)}" class="{cls}" stroke-width="{w}"/>'

def R(dx, dy):   # target relative to the shoulder
    return lambda sh, hip: (sh[0]+dx, sh[1]+dy)
def RH(dx, dy):  # target relative to the hip
    return lambda sh, hip: (hip[0]+dx, hip[1]+dy)
HANG = R(3, 54)

def figure(p, tag=""):
    view = p.get("view", "side"); hip = p["hip"]; ta = p["torso"]
    sh = pol(hip, ta, TORSO); head = pol(sh, p.get("head", ta), HEAD_OFF)
    pv = pol((0, 0), ta-90, 1)                      # perpendicular, +x when upright
    front = view == "front"
    hipS = {"N": add(hip, (pv[0]*HWD/2, pv[1]*HWD/2)) if front else hip,
            "F": add(hip, (-pv[0]*HWD/2, -pv[1]*HWD/2)) if front else hip}
    shS = {"N": add(sh, (pv[0]*SWD/2, pv[1]*SWD/2)) if front else sh,
           "F": add(sh, (-pv[0]*SWD/2, -pv[1]*SWD/2)) if front else sh}
    J = {"hip": hip, "sh": sh, "head": head}
    limbs = {}
    def res(v): return v(sh, hip) if callable(v) else v
    for s in "NF":
        lb = 1 if (s == "N" or not front) else -1       # leg bend (knee outward in front view)
        ab = (1 if s == "N" else -1) if front else -1   # arm bend
        lb = p.get("k"+s, lb); ab = p.get("e"+s, ab)
        if "leg"+s in p:
            a1, a2 = p["leg"+s]; k = pol(hipS[s], a1, TH); an = pol(k, a2, SN)
        else:
            k, an = ik(hipS[s], res(p["foot"+s]), TH, SN, lb, f"{tag} leg{s}")
        ta_ = p.get("toe"+s, 0 if (s == "N" or not front) else 180)
        toe = pol(an, ta_, FT)
        if "arm"+s in p:
            a1, a2 = p["arm"+s]; e = pol(shS[s], a1, UA); hd = pol(e, a2, FA)
        else:
            e, hd = ik(shS[s], res(p["hand"+s]), UA, FA, ab, f"{tag} arm{s}")
        J.update({"hand"+s: hd, "ankle"+s: an, "knee"+s: k, "elbow"+s: e})
        limbs[s] = ([hipS[s], k, an, toe], [shS[s], e, hd])
    out = []
    back, front_ = [], []
    for g in p.get("gear", []):
        kind = g[0]
        if kind == "box":
            _, x, w, h = g; back.append(f'<rect x="{x}" y="{GR-h}" width="{w}" height="{h}" class="i pf" stroke-width="3"/>')
        elif kind == "table":
            _, x1, x2, h = g
            back += [f'<path d="M{x1},{GR-h} L{x2},{GR-h}" class="i" stroke-width="6"/>',
                     f'<path d="M{x1+34},{GR-h} L{x1+34},{GR} M{x2-6},{GR-h} L{x2-6},{GR}" class="i" stroke-width="4"/>']
        elif kind == "wall":
            _, x, sd = g[:3]
            back.append(f'<path d="M{x},22 L{x},{GR}" class="i" stroke-width="4"/>')
            for y in range(34, GR, 16): back.append(f'<path d="M{x},{y} L{x+sd*9},{y-8}" class="i" stroke-width="2"/>')
            if len(g) > 3:
                back.append(f'<circle cx="{x-sd*7}" cy="{g[3]}" r="5" class="i pf" stroke-width="3"/>')
        elif kind == "trx":
            _, A, joints = g
            back.append(f'<rect x="{A[0]-9}" y="{A[1]-5}" width="18" height="6" class="f"/>')
            for jn in joints:
                j = J[jn] if isinstance(jn, str) else jn
                back.append(f'<path d="M{A[0]},{A[1]} L{j[0]:.0f},{j[1]:.0f}" class="i" stroke-width="2.5" stroke-dasharray="7 3"/>')
        elif kind == "line":
            _, a, b = g
            a = J[a] if isinstance(a, str) else a; b = J[b] if isinstance(b, str) else b
            back.append(f'<path d="M{a[0]:.0f},{a[1]:.0f} L{b[0]:.0f},{b[1]:.0f}" class="i" stroke-width="2.5" stroke-dasharray="7 3"/>')
        elif kind == "kb":
            _, jn, ang = g[:3]; r = g[3] if len(g) > 3 else 10
            j = J[jn] if isinstance(jn, str) else jn; c = pol(j, ang, r+3)
            front_.append(f'<circle cx="{c[0]:.0f}" cy="{c[1]:.0f}" r="{r}" class="f p" stroke-width="2"/>')
            front_.append(f'<circle cx="{j[0]:.0f}" cy="{j[1]:.0f}" r="5" class="pf i" stroke-width="3"/>')
        elif kind == "label":
            _, x, y, t = g
            front_.append(f'<text x="{x}" y="{y}" stroke="none" style="font-size:11px;letter-spacing:.08em">{t}</text>')
        elif kind == "mat":
            _, x1, x2 = g
            back.append(f'<rect x="{x1}" y="6" width="{x2-x1}" height="{GR+8-6}" rx="8" class="i" stroke-width="2" stroke-dasharray="3 5" style="fill:none"/>')
        elif kind == "arc":
            _, c, r, a0, a1 = g
            c = J[c] if isinstance(c, str) else c
            pts = [pol(c, a0 + (a1-a0)*i/12, r) for i in range(13)]
            e = pts[-1]; ang = math.atan2(-(pts[-1][1]-pts[-2][1]), pts[-1][0]-pts[-2][0]); ang = math.degrees(ang)
            h1, h2 = pol(e, ang+150, 8), pol(e, ang-150, 8)
            front_.append(f'<path d="{fmt(pts)} M{h1[0]:.0f},{h1[1]:.0f} L{e[0]:.0f},{e[1]:.0f} L{h2[0]:.0f},{h2[1]:.0f}" class="i" stroke-width="2.5"/>')
        elif kind == "arrow":
            _, a, b = g[:3]
            ang = math.degrees(math.atan2(-(b[1]-a[1]), b[0]-a[0]))
            h1, h2 = pol(b, ang+150, 9), pol(b, ang-150, 9)
            front_.append(f'<path d="M{a[0]:.0f},{a[1]:.0f} L{b[0]:.0f},{b[1]:.0f} M{h1[0]:.0f},{h1[1]:.0f} L{b[0]:.0f},{b[1]:.0f} L{h2[0]:.0f},{h2[1]:.0f}" class="i" stroke-width="3"/>')
    out += back
    def limb(s, cls, halo):
        l, a = limbs[s]; r = []
        if halo: r += [path(l, "p", 13), path(a, "p", 12)]
        r += [path(l, cls, 9), path(a, cls, 8)]
        return r
    if p.get("nolegs"):
        out += [path([shS["F"], shS["N"]], "i", 11), f'<circle cx="{head[0]:.0f}" cy="{head[1]:.0f}" r="{HEAD_R}" class="f"/>']
        out += [path(limbs[s][1], c, 8) for s, c in (("F","g"),("N","i"))]
        return "".join(back + out + front_)
    out += limb("F", "g", False)
    if front:
        out += [path([hipS["F"], hipS["N"]], "i", 8), path([shS["F"], shS["N"]], "i", 9)]
    out += [path([hip, sh], "i", 13), f'<circle cx="{head[0]:.0f}" cy="{head[1]:.0f}" r="{HEAD_R}" class="f"/>']
    out += limb("N", "i", True)
    out += front_
    return "".join(out)

CSS = ("<style>.i{stroke:var(--ink,#000);fill:none}.g{stroke:var(--g,#777);fill:none}.p{stroke:var(--paper,#fff);fill:none}"
       ".f{fill:var(--ink,#000)}.pf{fill:var(--paper,#fff)}.i.pf{fill:var(--paper,#fff)}.f.p{fill:var(--ink,#000);stroke:var(--paper,#fff)}"
       "text{font:700 15px 'IBM Plex Mono',monospace;fill:var(--ink,#000)}g{stroke-linecap:round;stroke-linejoin:round}</style>")

def _miny(svg):
    ys = []
    for d in re.findall(r' d="([^"]+)"', svg):
        ys += [float(y) for _, y in re.findall(r"(-?[\d.]+),(-?[\d.]+)", d)]
    for cy, r in re.findall(r'cy="(-?[\d.]+)" r="([\d.]+)"', svg): ys.append(float(cy) - float(r))
    for y in re.findall(r'<rect x="[^"]*" y="(-?[\d.]+)"', svg): ys.append(float(y))
    return min(ys) if ys else 0

def card(frames, tag="", embed=True):
    n = len(frames); body = []; ymin = 1e9
    for i, p in enumerate(frames):
        fig = figure(p, tag+f"#{i+1}"); ymin = min(ymin, _miny(fig))
        gl = "" if p.get("noground") else f'<path d="M8,{GR} L{W-8},{GR}" class="i" stroke-width="2"/>'
        body.append(f'<g transform="translate({i*W},0)">{gl}{fig}<text x="12" y="{H-6}" stroke="none">{i+1}</text></g>')
        if i: body.append(f'<path d="M{i*W},{{T}} L{i*W},{H-14}" class="i" stroke-width="1" stroke-dasharray="2 4"/>')
    top = int(max(-22, min(ymin - 12, 100)))
    body = "".join(body).replace("{T}", str(top + 8))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {top} {n*W} {H-top}" role="img">{CSS if embed else ""}'
            f'<rect y="{top}" width="{n*W}" height="{H-top}" class="pf" style="fill:var(--paper,#fff)"/>{body}</svg>')

def slug(n): return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")

# ---- stance helpers -------------------------------------------------------
def stand(x=110, **kw):
    d = dict(hip=(x, 109), torso=90, footN=(x+3, 190), footF=(x-3, 190), handN=HANG, handF=HANG)
    d.update(kw); return d

def lean(ax, deg, **kw):
    """Straight body leaning back from ankles at x=ax (head away from the direction faced)."""
    a = 90 + deg; hip = pol((ax, 190), a, 81)
    d = dict(hip=hip, torso=a, footN=(ax, 190), footF=(ax-4, 190)); d.update(kw); return d

def prone(lift=6, headup=14, **kw):
    d = dict(hip=(96,188), torso=lift, head=lift+headup, footN=(17,189), footF=(15,187), toeN=205, toeF=205)
    d.update(kw); return d
