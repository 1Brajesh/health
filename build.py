import json,html,re,datetime
E=html.escape
CSS="""
:root{--bg:#f4f8f5;--card:#fff;--ink:#1f2d27;--muted:#5d6f66;--brand:#2e8b6a;--brand2:#1d6f8f;--accent:#f2a541;--line:#dfe9e3;--chip:#e6f4ee;--shadow:0 2px 10px rgba(30,70,55,.08)}
@media(prefers-color-scheme:dark){:root{--bg:#0f1815;--card:#17241f;--ink:#e8f1ec;--muted:#9bb0a6;--brand:#4cc79a;--brand2:#5bb8dc;--accent:#f5b85c;--line:#27382f;--chip:#1f3a30;--shadow:0 2px 10px rgba(0,0,0,.4)}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--brand2)}
.hero{background:linear-gradient(135deg,var(--brand),var(--brand2));color:#fff;padding:2.2rem 1rem 3.2rem}
.wrap{max-width:1000px;margin:0 auto;padding:0 1rem}
.hero .wrap{padding:0}
.hero h1{margin:.2rem 0;font-size:clamp(1.7rem,4vw,2.4rem);line-height:1.2}
.hero p{margin:.3rem 0 0;opacity:.92;max-width:42rem}
nav{display:flex;gap:.5rem;margin-bottom:1.2rem;flex-wrap:wrap}
nav a{color:#fff;text-decoration:none;padding:.45rem 1rem;border-radius:999px;background:rgba(255,255,255,.16);font-weight:600;font-size:.95rem}
nav a:hover{background:rgba(255,255,255,.28)}nav a.on{background:#fff;color:var(--brand2)}
main{margin-top:-1.8rem;padding-bottom:3rem}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;margin-bottom:1.5rem}
.stat{background:var(--card);border-radius:14px;padding:.9rem 1rem;box-shadow:var(--shadow)}
.stat b{display:block;font-size:1.6rem;color:var(--brand)}.stat span{color:var(--muted);font-size:.9rem}
.note{background:var(--card);border-left:4px solid var(--accent);border-radius:10px;padding:.8rem 1rem;box-shadow:var(--shadow);margin-bottom:1.5rem;color:var(--muted);font-size:.95rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:1rem}
.card{background:var(--card);border-radius:16px;padding:1.1rem 1.2rem;box-shadow:var(--shadow);border-top:4px solid var(--brand)}
.card h3{margin:0 0 .1rem;font-size:1.08rem;line-height:1.3}
.card .brand{color:var(--muted);font-size:.9rem;margin-bottom:.6rem}
.num{display:inline-block;background:var(--brand);color:#fff;border-radius:50%;width:1.7rem;height:1.7rem;line-height:1.7rem;text-align:center;font-size:.85rem;margin-right:.45rem;font-weight:700}
.chip{display:inline-block;background:var(--chip);color:var(--brand);border-radius:999px;padding:.15rem .7rem;font-size:.85rem;font-weight:600;margin:0 .3rem .4rem 0}
.chip.when{background:#fff3df;color:#9a5c00}
@media(prefers-color-scheme:dark){.chip.when{background:#3a2d12;color:var(--accent)}}
.card p{margin:.35rem 0;font-size:.93rem}.card small{color:var(--muted)}
details{margin-top:.4rem}summary{cursor:pointer;color:var(--brand2);font-weight:600;font-size:.9rem}
h2{font-size:1.5rem;margin:2.2rem 0 .8rem;padding-bottom:.3rem;border-bottom:3px solid var(--chip)}
h3{margin:1.4rem 0 .5rem;color:var(--brand)}
.review{background:var(--card);border-radius:16px;padding:1rem 1.4rem 1.4rem;box-shadow:var(--shadow)}
.review h2{margin-top:.8rem}
.tw{overflow-x:auto;margin:.6rem 0;border-radius:10px;border:1px solid var(--line)}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th{background:var(--chip);color:var(--brand);text-align:left;position:sticky;top:0}
td,th{padding:.55rem .7rem;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:0}tbody tr:nth-child(even) td{background:rgba(46,139,106,.04)}
ul{padding-left:1.2rem}li{margin:.3rem 0}
.day{background:var(--card);border-radius:16px;box-shadow:var(--shadow);padding:1rem 1.2rem;margin-bottom:1rem}
.day h2{margin:0 0 .6rem;border:0;font-size:1.2rem;color:var(--brand2)}
.meal{display:flex;gap:.8rem;padding:.55rem 0;border-top:1px solid var(--line)}
.meal:first-of-type{border-top:0}
.ico{font-size:1.4rem;line-height:1.5}.mt{font-weight:700;font-size:.9rem;color:var(--brand)}
.planned{opacity:.75;font-style:italic}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(118px,1fr));gap:.55rem;margin:.2rem 0 .9rem}
.tile{border-radius:12px;padding:.55rem .7rem;background:var(--card);border:1px solid var(--line);border-top:4px solid var(--c)}
.tile .l{font-size:.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;font-weight:700}
.tile .v{font-size:1.25rem;font-weight:800;color:var(--c);line-height:1.25}.tile .v small{font-size:.75rem;font-weight:600;color:var(--muted)}
.tile .r{font-size:.72rem;color:var(--muted);min-height:1.1em}
.bar{height:7px;border-radius:99px;background:var(--line);overflow:hidden;margin:.25rem 0}.bar i{display:block;height:100%;background:var(--c);border-radius:99px}
.tile .t{font-size:.7rem;color:var(--muted)}
.t-cal{--c:#e0762b}.t-pro{--c:#c2493f}.t-fib{--c:#2e8b6a}.t-ca{--c:#5b7fd6}.t-k{--c:#a45bc7}.t-mg{--c:#1d9aa8}.t-na{--c:#b88a1b}
@media(prefers-color-scheme:dark){.t-cal{--c:#f0914f}.t-pro{--c:#ec7a70}.t-fib{--c:#4cc79a}.t-ca{--c:#86a4f0}.t-k{--c:#c98ae6}.t-mg{--c:#4cc9d6}.t-na{--c:#e0b94a}}
.badge{display:inline-block;background:#fff3df;color:#9a5c00;border-radius:999px;padding:.1rem .6rem;font-size:.75rem;font-weight:700;margin-left:.4rem;vertical-align:middle}
@media(prefers-color-scheme:dark){.badge{background:#3a2d12;color:var(--accent)}}
.est{font-size:.85rem;color:var(--muted)}.est td,.est th{padding:.35rem .5rem}
.week td:first-child{white-space:nowrap;font-weight:600}.week td,.week th{text-align:right}.week th:first-child{text-align:left}
.assume{color:var(--accent);font-weight:700}
.wk{margin-bottom:1.2rem}
footer{text-align:center;color:var(--muted);font-size:.85rem;padding:1.5rem 1rem 2.5rem}
"""
def page(title,sub,active,body):
    nav=''.join(f'<a href="{h}"{" class=on" if k==active else ""}>{t}</a>' for k,h,t in [('s','index.html','💊 Supplements'),('f','food.html','🥗 Food Log')])
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Health Tracker</title><meta name="color-scheme" content="light dark"><style>{CSS}</style></head><body><header class="hero"><div class="wrap"><nav>{nav}</nav><h1>{title}</h1><p>{sub}</p></div></header><main class="wrap">{body}</main><footer>Educational information only, not medical advice. Talk to your doctor about changes.</footer></body></html>'
d=json.load(open('supplements.json'))
cards=''
for x in d:
    cards+=f'<article class="card"><h3><span class="num">{x["n"]}</span>{E(x["name"])}</h3><div class="brand">{E(x["brand"])}</div><span class="chip when">🕐 {E(x["schedule"])}</span><span class="chip">{E(x["serving"])}</span><p><b>Key nutrients:</b> {E(x["nutrients"])}</p><details><summary>Other ingredients</summary><p><small>{E(x["other"])}</small></p></details></article>'
rev=open('summary.html-fragment').read()
rev=re.sub(r'(<table.*?</table>)',r'<div class="tw">\1</div>',rev,flags=re.S)
stats=f'<div class="stats"><div class="stat"><b>{len(d)}</b><span>supplements tracked</span></div><div class="stat"><b>#review</b><span><a href="#review">Jump to review &amp; summary</a></span></div></div>'.replace('<b>#review</b>','<b>📋</b>')
body=stats+'<div class="note">Reference list for personal use. Amounts come from product labels and are approximate.</div><div class="grid">'+cards+'</div><section class="review" id="review">'+rev+'</section>'
open('index.html','w').write(page('My Supplements','Everything I take, when I take it, and what to watch for.','s',body))
ICON=[('lunch','🥪'),('dinner','🍽️'),('after','🌙'),('evening','🌙'),('afternoon','☕'),('kefir','🥛'),('snack','🍓'),('11am','🍫'),('bed','🌙')]
def ico(m):
    l=m.lower()
    for k,v in ICON:
        if k in l:return v
    return '🍴'
NUT=[('kcal','Calories','kcal',None,'t-cal'),('protein','Protein','g',56,'t-pro'),('fiber','Fiber','g',30,'t-fib'),('calcium','Calcium (eaten)','mg',1000,'t-ca'),('potassium','Potassium','mg',3400,'t-k'),('magnesium','Magnesium','mg',420,'t-mg'),('sodium','Sodium','mg',2300,'t-na')]
TGT={'protein':'56 g RDA','fiber':'30 g (NAM)','calcium':'1,000 mg RDA','potassium':'3,400 mg AI','magnesium':'420 mg RDA','sodium':'&lt;2,300 mg limit'}
f=json.load(open('foodlog.json'))
nut=json.load(open('nutrition.json'))
foods=nut['foods']
def calc(day):
    tot={k:[0,0,0] for k,*_ in NUT}; missing={k:set() for k,*_ in NUT}
    for en in day['entries']:
        f=foods[en['food']]
        for k,*_ in NUT:
            v=f['per100g'][k]
            if v is None: missing[k].add(f['name']); continue
            x=v*en['grams']/100
            tot[k][0]+=x;tot[k][1]+=x*en['lo'];tot[k][2]+=x*en['hi']
    return tot,missing
def fmt(x):
    return f'{round(x/5)*5:,}' if x>=100 else f'{round(x):,}'
def rng(t): return f'{fmt(t[1])}&ndash;{fmt(t[2])}'
days=sorted(nut['days'],key=lambda x:x['date'],reverse=True)
res={d['date']:calc(d) for d in days}
wk=''
for d in days:
    tot,mi=res[d['date']]
    dt=datetime.date.fromisoformat(d['date']).strftime('%a %b %-d')
    cells=''.join(f'<td>~{fmt(tot[k][0])}{"+" if mi[k] else ""}</td>' for k,*_ in NUT)
    wk+=f'<tr><td>{dt}</td>{cells}</tr>'
weektbl='<section class="day wk"><h2>Week at a glance <span class="badge">logged meals only</span></h2><div class="tw"><table class="week"><tr><th>Day</th>'+''.join(f'<th>{l.replace(" (eaten)","")}<br><small>{u}</small></th>' for k,l,u,*_ in NUT)+f'</tr>{wk}</table></div><p class="est">Targets for a 54-year-old man: protein 56 g, fiber 30 g, calcium 1,000 mg, potassium 3,400 mg, magnesium 420 mg, sodium under 2,300 mg. "+" means some foods had no data for that nutrient, so the true total is higher. Tuna sandwich, curry, and many portions are assumed; see each day.</p></section>'
note='<div class="note"><b>Estimates only.</b> Values come from USDA FoodData Central, scaled to portions you gave or to stated assumptions, and cover only the meals logged (no breakfasts or unlogged snacks). <b>Calcium shown is the amount eaten, not the amount absorbed</b> (for example, spinach calcium is poorly absorbed). Supplements are excluded; they are tracked on the Supplements page. Ranges reflect portion uncertainty.</div>'
b=f'<div class="stats"><div class="stat"><b>{len(f)}</b><span>days logged</span></div><div class="stat"><b>{sum(len(x["meals"]) for x in f)}</b><span>meals and snacks</span></div></div>'+note+weektbl
fm={d['date']:d for d in f}
for day in days:
    raw=fm[day['date']]
    tot,mi=res[day['date']]
    dt=datetime.date.fromisoformat(day['date']).strftime('%A, %B %-d, %Y')
    tiles=''
    for k,l,u,tg,cl in NUT:
        t=tot[k]; plus='+' if mi[k] else ''
        bar=''
        if tg:
            pct=min(100,t[0]/tg*100); bar=f'<div class="bar"><i style="width:{pct:.0f}%"></i></div><div class="t">{t[0]/tg*100:.0f}% of {TGT[k]}</div>'
        else: bar='<div class="t">no target set</div>'
        tiles+=f'<div class="tile {cl}"><div class="l">{l}</div><div class="v">~{fmt(t[0])}{plus} <small>{u}</small></div><div class="r">range {rng(t)}</div>{bar}</div>'
    badge='<span class="badge">partial day: logged meals only</span>' if day['partial'] else ''
    rows=''
    for m in raw['meals']:
        pl=' planned' if 'planned' in m['meal'].lower() else ''
        rows+=f'<div class="meal{pl}"><div class="ico">{ico(m["meal"])}</div><div><div class="mt">{E(m["meal"])}</div>{E(m["items"])}</div></div>'
    er=''
    for en in day['entries']:
        f_=foods[en['food']]
        flag='<span class="assume">assumed</span>' if en['assumed'] else 'given'
        ap=' (approx)' if f_['approx'] else ''
        er+=f'<tr><td>{E(en["meal"])}</td><td>{E(en["label"])}</td><td>{en["grams"]:g} g</td><td>{flag}</td><td><a href="{f_["source"]}">{E(f_["name"])}</a>{ap}</td></tr>'
    used=sorted({e_['food'] for e_ in day['entries']})
    notes=''.join(f'<li><b>{E(foods[u]["name"])}:</b> {E(foods[u]["note"])}</li>' for u in used if foods[u]['note'])
    miss=''.join(f'<li><b>{dict((k,l) for k,l,*_ in NUT)[k]}:</b> no data for {E(", ".join(sorted(v)))}; excluded, not counted as zero.</li>' for k,v in mi.items() if v)
    det=f'<details><summary>How this was estimated</summary><p class="est">{E(day["partial_note"])} Totals are the sum of rows below (USDA per-100 g value x grams). "Assumed" = I chose the portion because it was not logged. Accessed {nut["accessed"]}.</p><div class="tw"><table class="est"><tr><th>Meal</th><th>Item</th><th>Amount</th><th>Portion</th><th>Source</th></tr>{er}</table></div><p class="est"><b>Data gaps:</b></p><ul class="est">{miss}</ul><p class="est"><b>Notes on foods:</b></p><ul class="est">{notes}</ul></details>'
    b+=f'<section class="day"><h2>{dt}{badge}</h2><div class="tiles">{tiles}</div>{rows}{det}</section>'
b+='<p class="est">Reference targets: fiber 30 g (National Academy of Medicine, adult men 51+), calcium 1,000 mg RDA, potassium 3,400 mg AI, magnesium 420 mg RDA, protein 56 g RDA, sodium under 2,300 mg (Dietary Guidelines). Calories have no target here. These are rough estimates, not medical advice.</p>'
open('food.html','w').write(page('Food Log','Daily meals with estimated nutrition, newest first.','f',b))
