import sys, json, importlib, os, subprocess
import rig
from reg import MOVES, mv
def load(mods):
    for m in mods:
        importlib.import_module(m)
def sheet(names, out, cols=2):
    cells = "".join(f'<figure><figcaption>{n}</figcaption>{rig.card(MOVES[n], n)}</figure>' for n in names)
    open(out+'.html','w').write(f'<!doctype html><meta charset=utf-8><style>body{{margin:14px;font:600 14px system-ui;background:#fff;display:grid;grid-template-columns:repeat({cols},1fr);gap:12px;width:{cols*500}px}}figure{{margin:0;border:2px solid #000}}figcaption{{padding:5px 10px;border-bottom:2px solid #000}}svg{{display:block;width:100%}}</style>{cells}')
    open('shot.js','w').write(f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium'}});const p=await b.newPage({{viewport:{{width:{cols*500+40},height:600}}}});await p.goto('file://'+process.cwd()+'/{out}.html');await p.screenshot({{path:'{out}.png',fullPage:true}});await b.close()}})()")
    subprocess.run(['node','shot.js'],cwd=os.getcwd())
