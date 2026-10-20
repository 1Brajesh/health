import json,html,re,datetime,math
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
.nt{margin:.2rem 0 .9rem}.nhead,.nr{display:grid;grid-template-columns:1.1fr 1fr 1fr 1.2fr;gap:.4rem;align-items:start}
.nhead{font-size:.72rem;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);font-weight:700;padding:0 .3rem}
.nr{padding:.45rem .5rem;margin:.3rem 0;border:1px solid var(--line);border-left:5px solid var(--c);border-radius:10px}
.nr .l{font-weight:700;font-size:.85rem;color:var(--c)}.nr .l small,.nr .h{color:var(--muted);font-weight:600}
.nr .h{display:none;font-size:.65rem;text-transform:uppercase;letter-spacing:.04em}
.nr .c b{display:block;font-size:1.05rem}.nr .c.o b{color:var(--c)}.nr .c.s b{color:var(--brand2)}
.nr .t{font-size:.7rem;color:var(--muted);display:block}
.sx{font-size:.85rem;margin-top:.7rem;color:var(--muted)}
.gap{border-left:5px solid var(--accent)}.gap.ok{border-left-color:var(--brand)}.gap.un{border-left-color:var(--muted)}
.bd{margin:-.2rem 0 .5rem;border:1px solid var(--line);border-left:5px solid var(--c);border-top:0;border-radius:0 0 10px 10px;padding:0 .6rem;background:var(--card)}
.bd>summary{display:block;padding:.65rem .1rem;min-height:44px;box-sizing:border-box;font-size:.85rem;list-style:none}
.bd>summary::-webkit-details-marker{display:none}
.bd>summary::before{content:"▸";display:inline-block;width:1.1em;transition:transform .15s}
.bd[open]>summary::before{transform:rotate(90deg)}
.bd[open]{padding-bottom:.5rem}
.bd table{font-size:.8rem}.bd td,.bd th{padding:.35rem .45rem}.bd td.n,.bd th.n{text-align:right;white-space:nowrap}
.bd tr.sup td{background:rgba(91,184,220,.10)}.bd tr.nd td{color:var(--muted);font-style:italic}
.bd .tag{display:inline-block;background:var(--chip);color:var(--brand2);border-radius:999px;padding:0 .5rem;font-size:.7rem;font-weight:700;margin-left:.3rem;font-style:normal}
.bd .est{margin:.4rem 0}
@media(max-width:560px){.nhead{display:none}.nr{grid-template-columns:1fr 1fr 1fr}.nr .l{grid-column:1/-1}.nr .h{display:block}}
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
def fm0(x):
    # ONE whole-number formatter used by day cards, possible-gaps and the overlay chart (round half up)
    return f'{math.floor(x+0.5):,}'
fmt=fm0
def rng(t): return f'{fmt(t[1])}&ndash;{fmt(t[2])}'
days=sorted(nut['days'],key=lambda x:x['date'],reverse=True)
res={d['date']:calc(d) for d in days}

# ---- supplement contributions (label values x schedule) ----
SUPK=['kcal','protein','fiber','calcium','potassium','magnesium','sodium']
def supp_day(date):
    wd=datetime.date.fromisoformat(date).weekday()  # Mon=0
    mwf=wd in (0,2,4); wkd=wd<5
    z=lambda:{k:0.0 for k in SUPK+['vitd','k2','zinc','iodine','b12','vita','vitc','iron','omega3']}
    t=z()
    t['magnesium']+=200;t['kcal']+=10;t['protein']+=2                     # #4 Nature Made, 2 caps nightly
    t['zinc']+=10;t['vitc']+=30                                           # #3 two tablets/day x (5 mg Zn, 15 mg C)
    t['omega3']+=640                                                      # #5 1 softgel = half of 1,280 mg/2 softgels
    t['vitc']+=250                                                        # #10 1 capsule = half of 500 mg/2 caps
    if wkd: t['vitd']+=125;t['k2']+=100                                   # #2
    if mwf: t['iodine']+=225;t['b12']+=1000                               # #11, #1
    h=0.5                                                                 # every-other-day items, averaged (start day not logged)
    t['vita']+=1391*h;t['b12']+=13.6*h;t['iron']+=2*h                     # #6 liver label values
    t['vitc']+=60*h;t['potassium']+=260*h;t['sodium']+=120*h              # #7 glucosamine
    t['protein']+=11*h                                                    # #8 collagen
    return t

def supp_items(date):
    wd=datetime.date.fromisoformat(date).weekday();mwf=wd in (0,2,4);wkd=wd<5;h=0.5
    L=[('Magnesium bisglycinate (Nature Made, 2 caps)',{'magnesium':200,'kcal':10,'protein':2}),
       ('Collagen (every other day, averaged at half a dose)',{'protein':11*h}),
       ('Glucosamine (every other day, averaged at half a dose)',{'potassium':260*h,'sodium':120*h})]
    return L
SUPX=[('vitd','Vitamin D','mcg'),('k2','Vitamin K2','mcg'),('zinc','Zinc','mg'),('iodine','Iodine','mcg'),('b12','Vitamin B12','mcg'),('vita','Vitamin A','mcg RAE'),('vitc','Vitamin C','mg'),('iron','Iron','mg'),('omega3','Omega-3 (total)','mg')]
sup={d['date']:supp_day(d['date']) for d in days}
def avg(k,which):
    v=[(res[d['date']][0][k][0] if which!='s' else 0)+(sup[d['date']].get(k,0) if which!='f' else 0) for d in days if not d.get('in_progress')]
    return sum(v)/len(v)
def numset(date,k):
    # single source of display numbers for day cards AND the overlay chart
    fv=res[date][0][k][0]; sv=sup[date].get(k,0)
    return dict(f=fm0(fv),s=fm0(sv) if sv else '0',c=fm0(fv+sv),p='+' if res[date][1][k] else '')
wk=''
for d in days:
    tot,mi=res[d['date']]
    dt=datetime.date.fromisoformat(d['date']).strftime('%a %b %-d')
    cells=''.join(f'<td>~{fmt(tot[k][0])}{"+" if mi[k] else ""}</td>' for k,*_ in NUT)
    wk+=f'<tr><td>{dt}</td>{cells}</tr>'
weektbl='@@CHART@@'
note='<div class="note"><b>Estimates only.</b> Values come from USDA FoodData Central, scaled to portions you gave or to stated assumptions, and cover only the meals logged (breakfast is not normally eaten, so none is expected; unlogged snacks are not counted). <b>Calcium shown is the amount eaten, not the amount absorbed</b> (for example, spinach calcium is poorly absorbed). Each day shows food, supplements and combined separately. Supplement amounts are label values times the schedule on the Supplements page. Every-other-day items (liver, glucosamine, collagen) are averaged at half a dose per day because their start day is not logged; iodine and B12 count only Mon/Wed/Fri, vitamin D3+K2 only Mon-Fri. Collagen calories are not on the label, so they are excluded. Supplement magnesium upper limit of 350 mg/day (NIH ODS) applies to supplement magnesium only, not food. Ranges reflect portion uncertainty.</div>'
b0=f'<div class="stats"><div class="stat"><b>{len(f)}</b><span>days logged</span></div><div class="stat"><b>{sum(len(x["meals"]) for x in f)}</b><span>meals and snacks</span></div></div>'+note+weektbl


def salt_mg(date,mode=None):
    dd=next(x for x in nut['days'] if x['date']==date)
    return sum(foods[e['food']]['per100g']['sodium']*e['grams']/100 for e in dd['entries'] if e['food']=='salt_table')
SALT_NOTE='Includes assumed table salt (salt to taste, amount unknown; default ~1/4 tsp, about 575 mg sodium, per home-cooked dish, range half to double). Not measured; packaged and restaurant food is not given extra salt.'
def contrib(day,k,sp):
    items=[];nd=[]
    for en in day['entries']:
        fd=foods[en['food']];v=fd['per100g'][k]
        if v is None: nd.append(en);continue
        items.append((v*en['grams']/100,en,fd))
    sup_=[(it[1][k],it[0]) for it in supp_items(day['date']) if it[1].get(k)]
    fsum=sum(i[0] for i in items);ssum=sum(x[0] for x in sup_);ctot=fsum+ssum
    assert abs(ssum-sp[k])<1e-6,(k,ssum,sp[k])
    rows=[(a,'f',en,fd) for a,en,fd in items]+[(a,'s',n_,None) for a,n_ in sup_]
    rows.sort(key=lambda r:-r[0])
    return rows,nd,fsum,ssum,ctot
def d1(x): return f'{x:,.1f}' if x<10 else f'{x:,.0f}'
def breakdown(day,k,l,u,sp,cl_):
    rows,nd,fsum,ssum,ctot=contrib(day,k,sp)
    h=''
    for a,t,en,fd in rows:
        pc=a/ctot*100 if ctot else 0
        if t=='f': h+=f'<tr{" class=\"salt\"" if en["food"]=="salt_table" else ""}><td>{E(en["label"])}{"<span class=\"tag\">assumed salt</span>" if en["food"]=="salt_table" else ""} <small>({E(en["meal"])})</small></td><td class="n">{en["grams"]:g} g</td><td class="n">{d1(a)}</td><td class="n">{pc:.0f}%</td></tr>'
        else: h+=f'<tr class="sup"><td>{E(en)}<span class="tag">supplement</span></td><td class="n">label dose</td><td class="n">{d1(a)}</td><td class="n">{pc:.0f}%</td></tr>'
    for en in nd:
        h+=f'<tr class="nd"><td>{E(en["label"])} <small>({E(en["meal"])})</small></td><td class="n">{en["grams"]:g} g</td><td class="n" colspan="2">no data</td></tr>'
    plus=' (food excludes no-data items, so true total is higher)' if nd else ''
    if k=='sodium' and salt_mg(day['date'])>0: plus+=f' {SALT_NOTE} Assumed salt this day: ~{salt_mg(day["date"]):,.0f} mg of the food total.'
    return (f'<details class="bd {cl_}"><summary>See what contributed to {l.lower().replace(" (eaten)","")} ({len(rows)} sources{", "+str(len(nd))+" no data" if nd else ""})</summary>'
     f'<div class="tw"><table class="est"><tr><th>Source</th><th class="n">Portion</th><th class="n">{u}</th><th class="n">% of day</th></tr>{h}</table></div>'
     f'<p class="est">Food {d1(fsum)} + supplements {d1(ssum)} = combined {d1(ctot)} {u}{plus}. Percentages are of the combined day total. Uses the same midpoint estimates as the tiles; each line is rounded, so lines may differ from the tile total by a rounding step. Sorted highest to lowest; "no data" foods are unknown, not zero.</p></details>')

gdays=[d for d in days if not d.get('in_progress')]
n=len(gdays)
def row(label,k,tg,u,src,extra=''):
    f_=avg(k,'f');c=avg(k,'c');sv=c-f_
    st='Possible gap' if c<0.85*tg else 'Looks adequate'
    cls='gap' if c<0.85*tg else 'gap ok'
    return f'<tr><td>{label}</td><td>{fmt(f_)}</td><td>{fmt(sv) if sv else "0"}</td><td><b>{fmt(c)}</b> {u}</td><td>{tg:,} {u}</td><td>{st}{extra}</td><td>{src}</td></tr>'
ODS='https://ods.od.nih.gov/factsheets/'
gp=''
gp+=row('Fiber','fiber',30,'g','<a href="https://nap.nationalacademies.org/catalog/10490">NAM DRI 2005</a>')
gp+=row('Calcium (eaten)','calcium',1000,'mg',f'<a href="{ODS}Calcium-HealthProfessional/">NIH ODS Calcium</a>',' (no listed supplement has calcium)')
gp+=row('Potassium','potassium',3400,'mg','<a href="https://nap.nationalacademies.org/catalog/25353">NASEM 2019</a>',' (AI)')
gp+=row('Magnesium','magnesium',420,'mg',f'<a href="{ODS}Magnesium-HealthProfessional/">NIH ODS Magnesium</a>')
gp+=row('Protein','protein',56,'g','<a href="https://www.ncbi.nlm.nih.gov/books/NBK56068/">NAM DRI</a>')
unk='<tr><td>Vitamin D</td><td colspan=5>Supplement D3 125 mcg on Mon-Fri (about 75 mcg/day averaged) is far above the 15 mcg RDA, so no gap from supplements. Food vitamin D was not computed. Note: 125 mcg is above the 100 mcg/day tolerable upper limit (NIH ODS), so worth raising with your doctor and asking about a vitamin D blood test.</td><td><a href="'+ODS+'VitaminD-HealthProfessional/">NIH ODS Vitamin D</a></td></tr>'
unk+='<tr><td>Vitamin K, vitamin E, choline, omega-3 from food, folate, B vitamins, selenium</td><td colspan=5><b>Unknown.</b> Food values for these are not in the data yet, so no gap can be claimed. Supplements give K2 100 mcg (Mon-Fri), omega-3 640 mcg EPA+DHA... see below, and choline only as an unquantified trace from liver.</td><td><a href="'+ODS+'">NIH ODS fact sheets</a></td></tr>'
unk=unk.replace('640 mcg EPA+DHA... see below','about 640 mg EPA+DHA a day (label 1,280 mg per 2 softgels, 1 taken)')
gapsec=f'<section class="day"><h2>Possible gaps <span class="badge">estimates</span></h2><p class="est">Average per day over {n} logged days ({gdays[-1]["date"]} to {gdays[0]["date"]}; Oct 17 included now that dinner is logged. Breakfast is not normally eaten, so it is not counted as a gap), food plus supplements, against adult male 51+ reference intakes. Logged meals only (lunch and dinner are the usual pattern), many portions assumed, so real intake is likely higher than shown. Estimates, not medical advice. Sources accessed 2026-10-15.</p><div class="tw"><table class="est"><tr><th>Nutrient</th><th>Food avg</th><th>Supp avg</th><th>Combined avg</th><th>Reference</th><th>Verdict</th><th>Source</th></tr>{gp}{unk}</table></div><p class="est">Reading: only rows marked "Possible gap" are supported by the data, and even those may reflect unlogged meals. Sodium and the 350 mg supplement-magnesium limit (NIH ODS) are not gaps; the limit applies to supplement magnesium only.</p></section>'
fm={d['date']:d for d in f}
b=b0+gapsec
for day in days:
    raw=fm[day['date']]
    tot,mi=res[day['date']]
    dt=datetime.date.fromisoformat(day['date']).strftime('%A, %B %-d, %Y')
    sp=sup[day['date']]
    rowsn=''
    for k,l,u,tg,cl in NUT:
        t=tot[k]; NSD=numset(day['date'],k); plus=NSD['p']
        fv=t[0]; sv=sp[k]; cv=fv+sv
        cu=' <small>'+'unknown (excluded)'+'</small>' if False else ''
        bar=''
        if tg: bar=f'<div class="bar"><i style="width:{min(100,cv/tg*100):.0f}%"></i></div><div class="t">{cv/tg*100:.0f}% of {TGT[k]}</div>'
        extra=' <span class="t">(+collagen kcal unknown)</span>' if k=='kcal' else ''
        sdisp=NSD['s']
        rowsn+=f'<div class="nr {cl}"><div class="l">{l} <small>{u}</small></div><div class="c f"><span class="h">Food</span><b>~{NSD['f']}{plus}</b><span class="t">{rng(t)}</span></div><div class="c s"><span class="h">Supplements</span><b>{sdisp}</b>{extra if sv or k=="kcal" else ""}</div><div class="c o"><span class="h">Combined</span><b>~{NSD['c']}{plus}</b>{bar}</div></div>'
        if k!='kcal': rowsn+=breakdown(day,k,l,u,sp,cl)
    sx=''.join(f'<span class="chip">{l}: <b>{sp[k]:,.0f}</b> {u}</span>' if sp[k]>=10 or sp[k]==0 else f'<span class="chip">{l}: <b>{sp[k]:,.1f}</b> {u}</span>' for k,l,u in SUPX)
    tiles=f'<div class="nhead"><span></span><span>Food</span><span>Supplements</span><span>Combined</span></div>{rowsn}<div class="sx"><b>Supplement-only nutrients today (not tracked in food data):</b><br>{sx}</div>'
    badge='<span class="badge">estimates: logged meals only</span>' if day['partial'] else ''
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
    b+=f'<section class="day"><h2>{dt}{badge}</h2><div class="nt">{tiles}</div>{rows}{det}</section>'
b+='<p class="est">Reference targets: fiber 30 g (National Academy of Medicine, adult men 51+), calcium 1,000 mg RDA, potassium 3,400 mg AI, magnesium 420 mg RDA, protein 56 g RDA, sodium under 2,300 mg (Dietary Guidelines). Calories have no target here. These are rough estimates, not medical advice.</p>'
FOOD_BODY=b

# ================= mock.html : week-at-a-glance chart variations =================
import math
MK=[('protein','Protein','g',56,'t-pro'),('fiber','Fiber','g',30,'t-fib'),('calcium','Calcium','mg',1000,'t-ca'),('potassium','Potassium','mg',3400,'t-k'),('magnesium','Magnesium','mg',420,'t-mg'),('sodium','Sodium*','mg',2300,'t-na')]
MD=sorted(days,key=lambda x:x['date'])
MDATES=[d['date'] for d in MD]
MIP=[bool(d.get('in_progress')) for d in MD]
MDL=[datetime.date.fromisoformat(x).strftime('%b %-d') for x in MDATES]
WDL=[datetime.date.fromisoformat(x).strftime('%a %-d') for x in MDATES]
NC=[i for i,v in enumerate(MIP) if not v]          # complete-day indexes
LAST=NC[-1]
def raw(i,k,mode):
    fv=res[MDATES[i]][0][k][0]; sv=sup[MDATES[i]].get(k,0)
    return fv if mode=='f' else fv+sv
def P(i,k,mode):
    tg=[m[3] for m in MK if m[0]==k][0]; return raw(i,k,mode)/tg*100
def AVG(k,mode): return sum(P(i,k,mode) for i in NC)/len(NC)
MODELAB={'f':'food only','c':'food + supplements'}
def smax(mode,extra=0):
    m=max([P(i,m_[0],mode) for i in range(len(MD)) for m_ in MK]+[extra,100])
    return max(150,math.ceil((m+5)/50)*50)
def toggled(fn):
    return f'<div class="m-f">{fn("f")}</div><div class="m-c">{fn("c")}</div>'
def alt(mode,extra=''):
    parts=[f'{l.rstrip("*")}: '+', '.join(f'{MDL[i]} {P(i,k,mode):.0f}%' for i in range(len(MD))) for k,l,u,t,c in MK]
    return f'Percent of daily target, {MODELAB[mode]}{extra}. '+'; '.join(parts)+'.'
SVGN=[0]
def svg(w,h,label,inner,mode=None):
    SVGN[0]+=1; inner=inner.replace('id="hz"',f'id="hz{SVGN[0]}"').replace('url(#hz)',f'url(#hz{SVGN[0]})')
    return f'<div class="sc"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{E(label)}" class="mk"><title>{E(label[:90])}</title><desc>{E(label)}</desc>{inner}</svg></div>'
def legend():
    return '<div class="lg">'+''.join(f'<span class="{c}"><i></i>{l}</span>' for k,l,u,t,c in MK)+'</div>'
HATCH='<defs><pattern id="hz" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="var(--card)"/><rect width="3" height="6" fill="currentColor" opacity=".55"/></pattern></defs>'
def axisY(x0,x1,y0,y1,mx,step=50,fmtf=lambda v:f'{v}%'):
    s=''
    for v in range(0,int(mx)+1,step):
        y=y1-(y1-y0)*v/mx
        s+=f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" class="gl"/><text x="{x0-6}" y="{y+4:.1f}" class="tx" text-anchor="end">{fmtf(v)}</text>'
    return s
def tline(x0,x1,y0,y1,mx,lab='100% target'):
    y=y1-(y1-y0)*100/mx
    return f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" class="tl"/><text x="{x1}" y="{y-5:.1f}" class="tx tg" text-anchor="end">{lab}</text>'
def xlabels(xs,y):
    return ''.join(f'<text x="{x:.1f}" y="{y}" class="tx{" ip" if MIP[i] else ""}" text-anchor="middle">{MDL[i]}{"*" if MIP[i] else ""}</text>' for i,x in enumerate(xs))
n_=len(MD)

# 1 multi-line
def c1(mode):
    W,H,L,R,T,B=560,300,44,28,14,34; mx=smax(mode)
    xs=[L+(W-L-R)*i/(n_-1) for i in range(n_)]
    yy=lambda p:H-B-(H-B-T)*p/mx
    s=axisY(L,W-R,T,H-B,mx)+tline(L,W-R,T,H-B,mx)+xlabels(xs,H-12)
    for k,l,u,t,c in MK:
        pts=[(xs[i],yy(P(i,k,mode))) for i in range(n_)]
        solid=' '.join(f'{x:.1f},{y:.1f}' for x,y in pts[:LAST+1])
        s+=f'<g class="{c}"><polyline points="{solid}" class="ln{" lo" if k=="sodium" else ""}"/>'
        if LAST<n_-1: s+=f'<polyline points="{pts[LAST][0]:.1f},{pts[LAST][1]:.1f} {pts[-1][0]:.1f},{pts[-1][1]:.1f}" class="ln da"/>'
        for i,(x,y) in enumerate(pts):
            s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" class="{"dot hol" if MIP[i] else "dot"}"><title>{l.rstrip("*")} {MDL[i]}: {P(i,k,mode):.0f}%</title></circle>'
        s+='</g>'
    return legend()+svg(W,H,'Multi-line chart. '+alt(mode,'; last day dashed because in progress'),s)

# 2 heatmap (HTML table)
def hcol(p,k):
    if k=='sodium':
        return f'rgba(214,78,66,{min(.75,max(0,(p-70)/90)):.2f})' if p>70 else f'rgba(76,199,154,{.15+.25*(1-p/70):.2f})'
    if p>=100: return f'rgba(76,199,154,{min(.7,.35+(p-100)/150):.2f})'
    return f'rgba(242,165,65,{.12+.6*(1-p/100):.2f})'
def c2(mode):
    h='<div class="tw"><table class="hm"><caption class="sr">Percent of daily target by nutrient and day, '+MODELAB[mode]+'</caption><thead><tr><th scope="col">Nutrient</th>'
    h+=''.join(f'<th scope="col"{" class=ipc" if MIP[i] else ""}>{MDL[i]}{"<br><small>in progress</small>" if MIP[i] else ""}</th>' for i in range(n_))+f'<th scope="col">{len(NC)}-day avg</th></tr></thead><tbody>'
    for k,l,u,t,c in MK:
        h+=f'<tr class="{c}"><th scope="row">{l}</th>'
        for i in range(n_):
            p=P(i,k,mode); h+=f'<td class="{"ipc" if MIP[i] else ""}" style="background-color:{hcol(p,k)}">{p:.0f}%</td>'
        a=AVG(k,mode); h+=f'<td class="av" style="background-color:{hcol(a,k)}">{a:.0f}%</td></tr>'
    return h+'</tbody></table></div><p class="est">Green = at/above target (for sodium: well under the limit), amber = below target, red = near/over the sodium limit. Hatched column = in-progress day.</p>'

# 3 grouped bars
def c3(mode):
    W,H,L,R,T,B=560,300,44,10,14,34; mx=smax(mode)
    gw=(W-L-R)/len(MK); bw=(gw-12)/n_
    s=HATCH+axisY(L,W-R,T,H-B,mx)+tline(L,W-R,T,H-B,mx)
    for gi,(k,l,u,t,c) in enumerate(MK):
        s+=f'<g class="{c}">'
        for i in range(n_):
            p=min(P(i,k,mode),mx); h_=(H-B-T)*p/mx; x=L+gi*gw+6+i*bw
            fill='url(#hz)' if MIP[i] else 'var(--c)'
            op='' if MIP[i] else f' opacity="{.45+.55*i/(n_-1):.2f}"'
            s+=f'<rect x="{x:.1f}" y="{H-B-h_:.1f}" width="{bw-1:.1f}" height="{h_:.1f}" fill="{fill}"{op} class="br"><title>{l.rstrip("*")} {MDL[i]}: {P(i,k,mode):.0f}%</title></rect>'
        s+=f'<text x="{L+gi*gw+gw/2:.1f}" y="{H-14}" class="tx" text-anchor="middle">{l}</text></g>'
    return svg(W,H,'Grouped bars, each nutrient has one bar per day (oldest left, shading darkens toward newer; hatched = in progress). '+alt(mode),s)+f'<p class="est">Within each group: {MDL[0]} (lightest) to {MDL[-1]} (hatched, in progress).</p>'

# 4 small multiples
def c4(mode):
    out='<div class="sm">'
    for k,l,u,t,c in MK:
        W,H,L,R,T,B=220,130,32,8,10,22; mx=max(150,math.ceil((max(P(i,k,mode) for i in range(n_))+5)/50)*50)
        xs=[L+(W-L-R)*i/(n_-1) for i in range(n_)]; yy=lambda p:H-B-(H-B-T)*p/mx
        s=axisY(L,W-R,T,H-B,mx,50 if mx<=200 else 100)+tline(L,W-R,T,H-B,mx,'100%')
        pts=[(xs[i],yy(P(i,k,mode))) for i in range(n_)]
        s+=f'<g class="{c}"><polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts[:LAST+1])+'" class="ln"/>'
        if LAST<n_-1: s+=f'<polyline points="{pts[LAST][0]:.1f},{pts[LAST][1]:.1f} {pts[-1][0]:.1f},{pts[-1][1]:.1f}" class="ln da"/>'
        for i,(x,y) in enumerate(pts): s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.8" class="{"dot hol" if MIP[i] else "dot"}"><title>{MDL[i]}: {P(i,k,mode):.0f}%</title></circle>'
        s+='</g>'+''.join(f'<text x="{xs[i]:.1f}" y="{H-6}" class="tx s" text-anchor="middle">{MDL[i].split()[1]}</text>' for i in (0,3,n_-1))
        lab=f'{l.rstrip("*")}: '+', '.join(f'{MDL[i]} {P(i,k,mode):.0f}%' for i in range(n_))+f' (target {t:,} {u}'+(', upper limit, lower is better' if k=='sodium' else '')+')'
        out+=f'<figure class="{c}"><figcaption><b>{l}</b> <small>avg {AVG(k,mode):.0f}% of {t:,} {u}</small></figcaption>'+svg(W,H,lab,s)+'</figure>'
    return out+'</div>'

# 5 radar
def c5(mode):
    W,H=420,340; cx,cy,R_=210,172,112; mx=max(150,math.ceil((max(max(P(LAST,k,mode),AVG(k,mode)) for k,*_ in MK)+5)/50)*50)
    ang=lambda j:-math.pi/2+2*math.pi*j/len(MK)
    pt=lambda j,p:(cx+R_*p/mx*math.cos(ang(j)),cy+R_*p/mx*math.sin(ang(j)))
    s=''
    for v in range(50,int(mx)+1,50):
        poly=' '.join('%.1f,%.1f'%pt(j,v) for j in range(len(MK)))
        s+=f'<polygon points="{poly}" class="{"ring100" if v==100 else "ring"}"/>'
    s+=f'<text x="{cx+4}" y="{cy-R_*100/mx-3:.1f}" class="tx tg">100%</text>'
    for j,(k,l,u,t,c) in enumerate(MK):
        x,y=pt(j,mx); s+=f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" class="gl"/>'
        lx,ly=cx+(R_+22)*math.cos(ang(j)),cy+(R_+16)*math.sin(ang(j))
        s+=f'<text x="{lx:.1f}" y="{ly+4:.1f}" class="tx" text-anchor="middle">{l}</text>'
    pa=' '.join('%.1f,%.1f'%pt(j,AVG(k,mode)) for j,(k,*_) in enumerate(MK))
    pl=' '.join('%.1f,%.1f'%pt(j,P(LAST,k,mode)) for j,(k,*_) in enumerate(MK))
    s+=f'<polygon points="{pa}" class="ra"/><polygon points="{pl}" class="rl"/>'
    lab=f'Radar chart, % of target, {MODELAB[mode]}. {MDL[LAST]} (latest complete day): '+', '.join(f'{l.rstrip("*")} {P(LAST,k,mode):.0f}%' for k,l,*_ in MK)+f'. {len(NC)}-day average: '+', '.join(f'{l.rstrip("*")} {AVG(k,mode):.0f}%' for k,l,*_ in MK)+'.'
    return f'<div class="lg"><span class="k1"><i></i>{MDL[LAST]} (latest complete day)</span><span class="k2"><i></i>{len(NC)}-day average</span></div>'+svg(W,H,lab,s)

# 6 bullet bars
def c6(mode):
    h='<div class="bl">'
    for k,l,u,t,c in MK:
        a=AVG(k,mode); lo=min(P(i,k,mode) for i in NC); hi=max(P(i,k,mode) for i in NC); mx=smax(mode)
        w=lambda p:min(100,p/mx*100)
        good=(a<=100) if k=='sodium' else (a>=100)
        h+=(f'<div class="bi {c}" role="img" aria-label="{l.rstrip("*")}: {len(NC)}-day average {a:.0f}% of target, range {lo:.0f} to {hi:.0f}%"><div class="bn"><b>{l}</b><span>{a:.0f}% <small>({lo:.0f}–{hi:.0f}%)</small></span></div>'
            f'<div class="trk"><i class="fl" style="width:{w(a):.1f}%"></i><i class="rg" style="left:{w(lo):.1f}%;width:{max(.8,w(hi)-w(lo)):.1f}%"></i><i class="tm" style="left:{w(100):.1f}%"></i></div></div>')
    return h+f'</div><p class="est">Bar = {len(NC)}-day average, thin band = lowest to highest day, vertical tick = 100% target. Scale 0–{smax(mode)}%.</p>'

# 7 stacked food vs supplement (average)
def c7(_):
    W,H,L,R=560,40*len(MK)+46,92,64; mx=smax('c')
    xx=lambda p:L+(W-L-R)*min(p,mx)/mx
    s=HATCH
    for v in range(0,mx+1,50): s+=f'<line x1="{xx(v):.1f}" x2="{xx(v):.1f}" y1="8" y2="{H-30}" class="gl"/><text x="{xx(v):.1f}" y="{H-14}" class="tx" text-anchor="middle">{v}%</text>'
    for r,(k,l,u,t,c) in enumerate(MK):
        fa=AVG(k,'f'); ca=AVG(k,'c'); y=14+r*40
        s+=f'<g class="{c}"><text x="{L-8}" y="{y+17}" class="tx" text-anchor="end">{l}</text><rect x="{L}" y="{y}" width="{xx(fa)-L:.1f}" height="24" fill="var(--c)" class="br"><title>{l.rstrip("*")} food: {fa:.0f}%</title></rect>'
        if ca-fa>0.05: s+=f'<rect x="{xx(fa):.1f}" y="{y}" width="{xx(ca)-xx(fa):.1f}" height="24" fill="url(#hz)" stroke="var(--c)" class="br"><title>{l.rstrip("*")} supplements: {ca-fa:.0f}%</title></rect>'
        s+=f'<text x="{xx(ca)+5:.1f}" y="{y+17}" class="tx v">{fa:.0f}%'+(f' + {ca-fa:.0f}%' if ca-fa>=.5 else '')+'</text></g>'
    s+=f'<line x1="{xx(100):.1f}" x2="{xx(100):.1f}" y1="6" y2="{H-30}" class="tl"/>'
    lab=f'Stacked horizontal bars, {len(NC)}-day average % of target, food then supplement share. '+'; '.join(f'{l.rstrip("*")}: food {AVG(k,"f"):.0f}%, supplements {AVG(k,"c")-AVG(k,"f"):.0f}%' for k,l,*_ in MK)+'.'
    return '<div class="lg"><span class="solid"><i></i>Food (solid)</span><span class="hat"><i></i>Supplements (hatched)</span></div>'+svg(W,H,lab,s)

# 8 dot plot
def c8(mode):
    W,H,L,R=560,46*len(MK)+40,88,30; mx=smax(mode)
    xx=lambda p:L+(W-L-R)*min(p,mx)/mx
    s=''
    for v in range(0,mx+1,50): s+=f'<line x1="{xx(v):.1f}" x2="{xx(v):.1f}" y1="6" y2="{H-30}" class="gl"/><text x="{xx(v):.1f}" y="{H-12}" class="tx" text-anchor="middle">{v}%</text>'
    s+=f'<line x1="{xx(100):.1f}" x2="{xx(100):.1f}" y1="6" y2="{H-30}" class="tl"/>'
    for r,(k,l,u,t,c) in enumerate(MK):
        y=26+r*46; vals=[P(i,k,mode) for i in range(n_)]
        s+=f'<g class="{c}"><text x="{L-8}" y="{y+4}" class="tx" text-anchor="end">{l}</text><line x1="{L}" x2="{xx(max(vals)):.1f}" y1="{y}" y2="{y}" class="stem"/>'
        for i,p in enumerate(vals): s+=f'<circle cx="{xx(p):.1f}" cy="{y}" r="5.5" class="{"dot hol" if MIP[i] else "dot"}" opacity=".85"><title>{l.rstrip("*")} {MDL[i]}: {p:.0f}%</title></circle>'
        s+=f'<path d="M{xx(AVG(k,mode)):.1f},{y-12} l-4,-6 h8 z" class="av"><title>{len(NC)}-day avg {AVG(k,mode):.0f}%</title></path></g>'
    return svg(W,H,'Dot plot, one dot per day per nutrient (hollow = in progress, triangle = average). '+alt(mode),s)+'<p class="est">Filled dot = complete day, hollow = in progress, triangle = 7-day average.</p>'

# 9 diverging
def c9(mode):
    W,H,L,R,T,B=560,300,44,10,14,34
    ext=max(abs(P(i,k,mode)-100) for i in range(n_) for k,*_ in MK); mx=max(50,math.ceil((ext+5)/25)*25)
    mid=(T+H-B)/2; sc=(H-B-T)/2/mx
    gw=(W-L-R)/len(MK); bw=(gw-12)/n_
    s=HATCH
    for v in range(-mx,mx+1,25 if mx<=100 else 50):
        y=mid-v*sc; s+=f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" class="{"tl" if v==0 else "gl"}"/><text x="{L-6}" y="{y+4:.1f}" class="tx" text-anchor="end">{"+" if v>0 else ""}{v}%</text>'
    s+=f'<text x="{W-R}" y="{mid-5:.1f}" class="tx tg" text-anchor="end">0 = on target</text>'
    for gi,(k,l,u,t,c) in enumerate(MK):
        s+=f'<g class="{c}">'
        for i in range(n_):
            d_=P(i,k,mode)-100; h_=abs(d_)*sc; x=L+gi*gw+6+i*bw
            bad=(d_>0) if k=='sodium' else (d_<0)
            cl='bad' if bad else 'good'
            fill='url(#hz)' if MIP[i] else 'currentColor'
            y=mid-h_ if d_>=0 else mid
            s+=f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw-1:.1f}" height="{max(h_,.5):.1f}" fill="{fill}" class="dv {cl}"><title>{l.rstrip("*")} {MDL[i]}: {"+" if d_>=0 else ""}{d_:.0f}% vs target</title></rect>'
        s+=f'<text x="{L+gi*gw+gw/2:.1f}" y="{H-14}" class="tx" text-anchor="middle">{l}</text></g>'
    lab='Diverging bars, distance from 100% of target, one bar per day (oldest left). '+'; '.join(f'{l.rstrip("*")}: '+', '.join(f'{MDL[i]} {P(i,k,mode)-100:+.0f}%' for i in range(n_)) for k,l,*_ in MK)+'.'
    return '<div class="lg"><span class="gd"><i></i>On/better than target</span><span class="bd2"><i></i>Short of target (sodium: over limit)</span></div>'+svg(W,H,lab,s)

# 10 log-scale raw
def c10(mode):
    W,H,L,R,T,B=560,300,52,28,14,34; lo,hi=1,4
    xs=[L+(W-L-R)*i/(n_-1) for i in range(n_)]
    yy=lambda v:H-B-(H-B-T)*(math.log10(max(v,1))-lo)/(hi-lo)
    s=''
    for e in range(lo,hi+1):
        for m in ([1] if e==hi else [1,2,5]):
            v=m*10**e; y=yy(v); s+=f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" class="gl{" ms" if m==1 else " mn"}"/>'+(f'<text x="{L-6}" y="{y+4:.1f}" class="tx" text-anchor="end">{v:,}</text>' if m==1 else '')
    s+=xlabels(xs,H-12)
    for k,l,u,t,c in MK+[('kcal','Calories','kcal',0,'t-cal')]:
        pts=[(xs[i],yy(raw(i,k,mode))) for i in range(n_)]
        s+=f'<g class="{c}"><polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts[:LAST+1])+'" class="ln"/>'
        if LAST<n_-1: s+=f'<polyline points="{pts[LAST][0]:.1f},{pts[LAST][1]:.1f} {pts[-1][0]:.1f},{pts[-1][1]:.1f}" class="ln da"/>'
        for i,(x,y) in enumerate(pts): s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" class="{"dot hol" if MIP[i] else "dot"}"><title>{l.rstrip("*")} {MDL[i]}: {raw(i,k,mode):,.0f} {u}</title></circle>'
        s+='</g>'
    lab=f'Log-scale line chart of raw amounts, {MODELAB[mode]} (g, mg or kcal, units differ). '+'; '.join(f'{l.rstrip("*")}: '+', '.join(f'{MDL[i]} {raw(i,k,mode):,.0f}' for i in range(n_)) for k,l,*_ in MK+[('kcal','Calories','',0,'')])+'.'
    return legend().replace('</div>','<span class="t-cal"><i></i>Calories</span></div>')+svg(W,H,lab,s)+'<p class="est">Log axis: each gridline step is a multiple of 10 (10, 100, 1,000, 10,000). Mixed units (g, mg, kcal).</p>'


# ===== calcium eaten vs absorbed mockups =====
NIHCA='https://ods.od.nih.gov/factsheets/Calcium-HealthProfessional/'
NAS='https://www.nationalacademies.org/read/13050/chapter/4'
ABS_DEF=25
ABSR={'milk_2':(27,'NIH ODS: ~27% from milk'),'hot_cocoa':(27,'assumed: milk-based, NIH milk figure'),
 'spinach':(5,'NIH ODS: ~5% from spinach (high oxalate)'),
 'cabbage':(27,'NIH ODS: low-oxalate greens (broccoli, kale, cabbage) similar to milk'),
 'broccoli':(27,'NIH ODS: low-oxalate greens (broccoli, kale, cabbage) similar to milk'),
 'kale_raw':(49,'Weaver, Proulx & Heaney 1999: ~49% from kale')}
def absr(fk):
    if fk in ABSR:
        p,s=ABSR[fk]; return p,s,('assumed' if s.startswith('assumed') else 'sourced')
    return ABS_DEF,f'assumed default ~{ABS_DEF}% (adult average, National Academies 2011)','assumed'
AD=[]
for i,dd in enumerate(MD):
    agg={}; nd=[]
    for en in dd['entries']:
        fd=foods[en['food']]; v=fd['per100g']['calcium']
        if v is None: nd.append(en['label']); continue
        a=agg.setdefault(en['food'],{'name':fd['name'].replace(', raw','').replace(', cooked',''),'g':0,'mg':0.0})
        a['g']+=en['grams']; a['mg']+=v*en['grams']/100
    items=[]
    for fk,a in agg.items():
        p,s,t=absr(fk); items.append(dict(a,key=fk,pct=p,src=s,typ=t,ab=a['mg']*p/100))
    items.sort(key=lambda x:-x['mg'])
    e=sum(x['mg'] for x in items); ab=sum(x['ab'] for x in items)
    AD.append(dict(i=i,e=e,a=ab,items=items,nd=nd,ip=MIP[i],l=MDL[i]))

# ===== absorption config for overlay split (typical adult; estimates). Percentages live here, not in JS =====
SPLIT={
 'potassium':dict(mid=87.5,lo=85,hi=90,src='NIH ODS Potassium fact sheet, updated June 2, 2022',note='Absorbed is not the same as retained; healthy kidneys excrete the excess.'),
 'magnesium':dict(mid=35,lo=30,hi=40,src='NIH ODS Magnesium fact sheet, updated Jan 6, 2026',note='Absorption is lower at higher per-meal doses (Fine 1991), so a smaller evening dose likely absorbs a larger share, but no sourced number exists for your dose. Your supplement (Nature Made bisglycinate) uses the same 30-40%: <b>assumed, form-specific data lacking</b>.'),
}
PRO_DEF=90   # assumed default protein digestibility for foods without data
PRO_SRC='FAO 2013 (Food and Nutrition Paper 92) and Nutrients 2019;11(8):1825'
PRO_DIG={ # food key: (percent, sourced?)
 'milk_2':(96,True),'egg_fried':(98,True),'cod':(90,True),'tuna':(90,True),'lentils':(84,True),'bread':(91,True),'tortilla':(91,True),
 'kefir':(96,False),'kefir_maplehill':(96,False),'skyr':(96,False),'siggis':(96,False),'hot_cocoa':(96,False),
 'wf_lentil_soup':(84,False),'croissant':(91,False)}
NOSPLIT={'sodium':'~98% absorbed (NASEM 2005, EFSA 2019)','fiber':'not absorbed by definition; partly fermented in colon (FAO/WHO 1998)'}
def split_info(i,k,mode):
    fv=raw(i,k,'f'); tot=raw(i,k,mode); sv=tot-fv
    if k in SPLIT:
        c=SPLIT[k]; return dict(e=tot,a=tot*c['mid']/100,lo=tot*c['lo']/100,hi=tot*c['hi']/100,sh=None)
    # protein: per-food digestibility, weighted by food protein from log entries
    num=den=srcd=0.0
    for en in MD[i]['entries']:
        fd=foods[en['food']]; v=fd['per100g']['protein']
        if v is None: continue
        g=v*en['grams']/100; p,so=PRO_DIG.get(en['food'],(PRO_DEF,False))
        num+=g*p; den+=g; srcd+=g if so else 0
    fr=(num/den/100) if den>0 else PRO_DEF/100
    a=fv*fr; sh=(srcd/den*100) if den>0 else 0
    if sv>0: a+=sv*PRO_DEF/100; sh=sh*fv/tot
    return dict(e=tot,a=a,lo=None,hi=None,sh=sh)
# ===== 0 overlay bar =====
OVC={'protein':'#5a2d0c','fiber':'#00a650','calcium':'#ffffff','potassium':'#e00000','magnesium':'#ff8a00','sodium':'#ffe600'}
OVO={'protein':'#ffffff','fiber':'#ffffff','calcium':'#cdbfa8','potassium':'#ffffff','magnesium':'#ffffff','sodium':'#ffffff'}
def sw(k): return f'<i class="sw" style="--oc:{OVC[k]};--ol:{OVO[k]}"></i>'
def ov_scale(mode,pct):
    if pct: return smax(mode)
    m=max(raw(i,k,mode) for i in range(n_) for k,*_ in MK)
    return max(1000,math.ceil((m+50)/500)*500)
def cabs(i,mode):
    x=AD[i]; r=raw(i,'calcium',mode)
    return (r*x['a']/x['e'] if x['e']>0 else r), x['e'], (x['a']/x['e']*100 if x['e']>0 else 100)

KMAX=2500
def PL(i,k): return '+' if res[MDATES[i]][1][k] else ''     # '+' = some foods lack data, true amount higher
def NS(i,k): return numset(MDATES[i],k)
def kcal_info(i,mode):
    d=MD[i]; fk=res[d['date']][0]['kcal'][0]; sk=sup[d['date']].get('kcal',0)
    grp={}
    for en in d['entries']:
        v=foods[en['food']]['per100g']['kcal']
        if v is None: continue
        m=en['meal'].lower()
        g='Lunch' if m.startswith('lunch') else 'Dinner' if m.startswith('dinner') else 'Snacks &amp; other'
        grp[g]=grp.get(g,0)+v*en['grams']/100
    return dict(f=fk,s=sk,tot=fk+sk,shown=(fk if mode=='f' else fk+sk),grp=grp)
TOPN=6
def tipbd(i,k,mode,u):
    """ranked contributors for the tooltip; same contrib() rows as the day-card breakdown"""
    day=MD[i]; rows,nd,fsum,ssum,ctot=contrib(day,k,sup[day['date']])
    assert abs(fsum-res[day['date']][0][k][0])<1e-6 and abs(ctot-res[day['date']][0][k][0]-sup[day['date']][k])<1e-6,(i,k)
    fr=[r for r in rows if r[1]=='f']; sr=[r for r in rows if r[1]=='s'] if mode=='c' else []
    den=ctot if mode=='c' else fsum
    top=fr[:TOPN]; rest=fr[TOPN:]
    def rw(a,name,tag='',cls=''):
        pc=a/den*100 if den else 0
        return f'<span class="br{cls}"><span class="bn"><span class="nm">{name}</span>{tag}</span><b>{d1(a)}</b><em>{pc:.0f}%</em></span>'
    h=''
    for a,t,en,fd in top:
        salt=en['food']=='salt_table'
        h+=rw(a,E(en['label']),'<span class="tg">assumed</span>' if salt else '',' salt' if salt else '')
    if rest: h+=rw(sum(r[0] for r in rest),f'other ({len(rest)} more)','','  oth')
    for a,t,n_,_ in sr: h+=rw(a,E(n_),'<span class="tg">supplement</span>',' sup')
    if nd: h+=f'<span class="bnd">{len(nd)} food{"s" if len(nd)>1 else ""} with no data (not counted)</span>'
    ttl=f'{"Food" if mode=="f" else "Food + supplements"} {d1(den)} {u}'
    return f'<span class="bh">Top sources · % of {ttl}</span>'+h
def kmark(i,mode):
    ki=kcal_info(i,mode); ip=MIP[i]; x=min(ki['shown'],KMAX)/KMAX*100
    meal=''.join(f'{g}: {fm0(ki["grp"][g])} kcal<br>' for g in ('Lunch','Dinner','Snacks &amp; other') if g in ki['grp'])
    meal+=f'Supplements: {fm0(ki["s"])} kcal<br>'
    body=f'<b>Calories</b> · {MDL[i]}{" (in progress)" if ip else ""}<br>{"Eaten (food only): " if mode=="f" else "Eaten (food + supplements): "}<b>~{fm0(ki["shown"])}{PL(i,"kcal")} kcal</b>'
    if mode=='f': body+=f' (food + supplements ~{fm0(ki["tot"])}{PL(i,"kcal")})'
    body+=f'<br>food ~{fm0(ki["f"])}{PL(i,"kcal")} + supplements {fm0(ki["s"])} kcal<br>{meal}<i>estimate</i>; logged meals only{"; day in progress, so the total is partial" if ip else ""}. No calorie target is used.'
    if ki['shown']>KMAX: body+=' Marker clipped at the 2,500 kcal edge.'
    aria=f'Calories, {MDL[i]}{" in progress" if ip else ""}: about {fm0(ki["shown"])}{PL(i,"kcal")} kcal, estimate; food {fm0(ki["f"])}, supplements {fm0(ki["s"])}'
    kr=' kr' if x>50 else ''
    head=f'<b>Calories</b> · {MDL[i]}{" (in progress)" if ip else ""}<br>{"Eaten (food only): " if mode=="f" else "Eaten (food + supplements): "}<b>~{fm0(ki["shown"])}{PL(i,"kcal")} kcal</b>'
    return (f'<div class="kc{" kh" if ip else ""}{kr}" data-x="{x:.2f}" tabindex="0" role="img" aria-label="{E(aria)}" style="left:{x:.2f}%">'
            f'<span class="tp kt tb" aria-hidden="true">{head}{tipbd(i,"kcal",mode,"kcal")}<small class="hint">Meal split and notes in the panel below the chart.</small></span><span class="dt" aria-hidden="true">{body}</span></div>')
def kaxis():
    return ('<div class="ovb"><span class="ovd kl axt"><i class="sw ksw"></i>kcal</span><div class="ovt kt2">'
      +''.join(f'<span style="left:{v/KMAX*100:.2f}%">{v:,}</span>' for v in range(0,KMAX+1,500))+'</div></div>')
def ov(mode,pct,ab=False):
    mx=ov_scale(mode,pct); cl='s-p' if pct else 's-r'
    ticks=range(0,mx+1,50 if pct else 500)
    if pct and mx>300: ticks=range(0,mx+1,100)
    h=f'<div class="{cl}"><div class="ovl">'
    h+='<div class="ova"><span class="ovd axt">'+('% of daily target' if pct else 'raw amount')+'</span><div class="ovt">'+''.join(f'<span style="left:{v/mx*100:.2f}%">{v}{"%" if pct else ""}</span>' for v in ticks)+'</div></div>'
    for i in range(n_):
        items=[]
        for k,l,u,t,c in MK:
            v=raw(i,k,mode); fv=raw(i,k,'f'); sv=raw(i,k,'c')-fv
            if ab and k=='calcium': v=cabs(i,mode)[0]
            val=v/t*100 if pct else v
            items.append((val,k,l,u,t,v,fv,sv))
        items.sort(key=lambda x:-x[0])
        ip=MIP[i]
        allrows={it[1]:f'<span class="ar" data-n="{it[1]}">{sw(it[1])}{it[2].rstrip("*")}: ~{fm0(it[5])}{PL(i,it[1])} {it[3]} · {it[5]/it[4]*100:.0f}%</span>' for it in items}
        h+=f'<div class="ovr{" ip" if ip else ""}"><div class="ovd" title="{MDL[i]}"><span class="wd">{WDL[i]}</span>{"<small>in progress</small>" if ip else ""}</div><div class="ovk">'
        for z,(val,k,l,u,t,v,fv,sv) in enumerate(items):
            w=max(min(val,mx)/mx*100,.7)
            ln=l.rstrip('*')
            lab='food only' if mode=='f' else 'food + supplements'
            plk=PL(i,k); nsx=NS(i,k)
            if mode=='f': sp=f'food ~{nsx["f"]}{plk} {u} + supplements {nsx["s"]} {u} (supplements not counted in this view)'
            else: sp=f'food ~{nsx["f"]}{plk} {u} + supplements {nsx["s"]} {u}'
            pnote=f'<br><small>&ldquo;+&rdquo; = some foods have no data for {l.rstrip("*").lower()}, so the true amount is higher.</small>' if plk else ''
            if k=='sodium' and salt_mg(MDATES[i])>0: pnote+=f'<br><small>{SALT_NOTE} Assumed salt: ~{fm0(salt_mg(MDATES[i]))} mg of the food figure.</small>'
            pc=v/t*100
            pcs=f'{pc:.0f}% of '+(f'{t:,} {u} limit' if k=='sodium' else f'{t:,} {u} target')
            aria=f'{ln}, {MDL[i]}{" in progress" if ip else ""}: eaten ({lab}) {fm0(v)}{plk} {u}, {pcs}; {sp}'
            zi=z+1
            if ab:
                zi=2*z+2
                if k=='calcium':
                    _,ce,cp=cabs(i,mode)
                    ex=f'eaten {fm0(ce)} mg · absorbed {fm0(v)} mg · {cp:.0f}% absorbed (estimate)'
                    aria=f'{ln}, {MDL[i]}{" in progress" if ip else ""}: estimated absorbed {fm0(v)} mg, {pcs}; {ex}. Estimate for a typical adult.'
                    sp2=ex+'<br><i>estimate</i>, typical adult'
                    gw=max(min((ce/t*100) if pct else ce,mx)/mx*100,.7)
                    h+=f'<div class="gh" aria-hidden="true" style="width:{gw:.2f}%;z-index:{zi-1}"></div>'
                else:
                    aria+='; absorption not adjusted'
                    sp2=sp+'<br>absorption not adjusted'
            else: sp2=''
            seg=''
            if k=='calcium':
                _,ce,cp=cabs(i,mode); ca=ce*cp/100
                srcd=sum(it['mg'] for it in AD[i]['items'] if it['typ']=='sourced'); tot=sum(it['mg'] for it in AD[i]['items'])
                ss=(srcd/tot*100 if tot>0 else 0)
                seg=f'<span class="sn" aria-hidden="true" style="left:{cp:.2f}%"></span>'
                sp2=(f'<b>Calcium split (estimate)</b><br>Absorbed ~{fm0(ca)}{plk} mg ({cp:.0f}%) <span class="kd">solid</span><br>Not absorbed ~{fm0(ce-ca)}{plk} mg <span class="kd h">hatched</span><br>{ss:.0f}% of eaten calcium uses sourced percentages (milk 27%, spinach 5%, cabbage/broccoli 27%, kale 49%); the rest uses an assumed default of {ABS_DEF}%.<br><small>Source: NIH ODS calcium fact sheet, updated June 22, 2026. Typical adult, not a personal value.</small>')
                aria+=f'; estimated absorbed about {fm0(ca)}{plk} mg of {fm0(ce)}{plk} mg eaten ({cp:.0f}%), not absorbed about {fm0(ce-ca)} mg. Estimate, typical adult.'
            if k in SPLIT or k=='protein':
                si=split_info(i,k,mode); sa=si['a']; spc=sa/si['e']*100 if si['e']>0 else 0
                seg=f'<span class="sn" aria-hidden="true" style="left:{spc:.2f}%"></span>'
                if k=='protein':
                    rng=''; srcl=f'{si["sh"]:.0f}% of the protein eaten uses sourced digestibility (milk 96%, egg 98%, fish ~90%, lentils 84%, wheat ~91%); the rest is <b>assumed</b> at a default {PRO_DEF}% (chicken, duck, nuts, seeds, vegetables, most dairy products have no usable data).'
                    srcc=f'Source: {PRO_SRC}. Digestibility, not amino-acid quality.'
                else:
                    c=SPLIT[k]; rng=f' (range {fm0(si["lo"])}-{fm0(si["hi"])} {u}, {c["lo"]}-{c["hi"]}%)'
                    srcl=c['note']; srcc='Source: '+c['src']+'.'
                sp2=(f'<b>{ln} split (estimate)</b><br>Absorbed ~{fm0(sa)}{plk} {u}{rng} · {spc:.0f}% <span class="kd">solid</span><br>Not absorbed ~{fm0(si["e"]-sa)}{plk} {u} <span class="kd h">hatched</span><br>{srcl}<br><small>{srcc} Typical adult, estimate, not a personal value.</small>')
                aria+=f'; estimated absorbed about {fm0(sa)}{plk} {u} of {fm0(si["e"])}{plk} {u} eaten ({spc:.0f}%){rng}. Estimate, typical adult.'
            elif k in NOSPLIT:
                sp2=f'<small>{ln}: {NOSPLIT[k]}. No split shown.</small>'
                aria+=f'; {NOSPLIT[k]}'
            allr='<span class="al"><b>All nutrients, '+MDL[i]+'</b>'+''.join(r.replace('class="ar"','class="ar me"') if kk==k else r for kk,r in allrows.items())+'</span>'
            near=any((abs(val-o[0])<1.5 if pct else abs(w-max(min(o[0],mx)/mx*100,.7))<1.5) for o in items if o[1]!=k and o[0]<=val)
            edge='<span class="ed" aria-hidden="true"></span>' if near else ''
            h+=(f'<div class="ly{" cs" if (k=="calcium" or k in SPLIT or k=="protein") else ""}{" nr" if near else ""}" data-k="{k}" data-d="{MDATES[i]}" data-f="{nsx['f']}" data-s="{nsx['s']}" data-c="{nsx['c']}" data-p="{plk}" tabindex="0" role="img" aria-label="{E(aria+"; all nutrients: "+"; ".join(f"{o[2].rstrip(chr(42))} {fm0(o[5])} {o[3]}" for o in items))}" style="width:{w:.2f}%;--oc:{OVC[k]};--ol:{OVO[k]};z-index:{zi}"><span class="tp tb" aria-hidden="true">{sw(k)}<b>{ln}</b> · {MDL[i]}{" (in progress)" if ip else ""}<br>Eaten ({lab}): <b class="tv">~{fm0(v)}{plk} {u}</b> · {pcs}{tipbd(i,k,mode,u)}<small class="hint">Absorption, sources and all nutrients in the panel below the chart.</small></span><span class="dt" aria-hidden="true">{sw(k)}<b>{ln}</b> · {MDL[i]}{" (in progress)" if ip else ""}<br>Eaten ({lab}): <b class="tv">~{fm0(v)}{plk} {u}</b> · {pcs}<br>{sp}{pnote}{("<br>"+sp2) if sp2 else ""}{allr}</span>{seg}{edge}</div>')
        h+=kmark(i,mode)
        if pct:
            h+=f'<i class="m100" style="left:{100/mx*100:.2f}%"></i>'
            for gv in (50,150):
                if gv<mx: h+=f'<i class="gl5" style="left:{gv/mx*100:.2f}%"></i>'
        h+='</div></div>'
    h+=kaxis()+'<svg class="kln" aria-hidden="true"></svg>'
    h+='</div></div>'
    return h
def ovleg():
    return '<div class="lg ovg">'+''.join(f'<span class="lc" tabindex="0" role="button" aria-pressed="false" data-k="{k}" title="Hover, tap or focus to bring {l.rstrip("*")} to the front">{sw(k)}{l}</span>' for k,l,u,t,c in MK)+'<span class="lk on" tabindex="0" role="button" aria-pressed="true" title="Show or hide the calorie line (bottom axis, kcal)"><i class="sw ksw"></i>Calories</span></div>'
def ov_all(mode): return ovleg()+ov(mode,True)+ov(mode,False)
OVCSS="""
.tp.tb{max-width:min(300px,calc(100vw - 5.5rem));width:max-content;min-width:12rem}
.tb .bh{display:block;margin-top:.4rem;padding-top:.3rem;border-top:1px solid var(--muted);font-size:.7rem;opacity:.85}
.tb .br{display:grid;grid-template-columns:minmax(0,1fr) auto 2.6rem;gap:.4rem;align-items:baseline;font-size:.76rem;line-height:1.35}
.tb .br .bn{display:flex;align-items:baseline;min-width:0}.tb .br .nm{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}.tb .br .tg{flex:none}.tb .br b{text-align:right;font-weight:700}.tb .br em{text-align:right;font-style:normal;opacity:.8}
.tb .br .tg{margin-left:.3rem;font-size:.62rem;border:1px solid currentColor;border-radius:999px;padding:0 .3rem;opacity:.9}
.tb .br.oth{opacity:.8;font-style:italic}.tb .bnd{display:block;font-size:.68rem;opacity:.8;margin-top:.15rem}
.tb .hint{display:block;margin-top:.35rem;opacity:.7;font-size:.66rem}
.dt{display:none}
.kc.kr .tp{left:auto;right:-4px;transform:none}
.dpn{margin:.6rem 0 1rem;padding:.7rem .9rem;border:1px solid var(--line);border-radius:12px;background:var(--card);color:var(--ink);font-size:.82rem;line-height:1.45;min-height:5.5rem}
.dpn.empty{color:var(--muted)}.dpn .al{border-top:1px solid var(--line)}.dpn small{opacity:.85}.dpn .ar{display:block;opacity:.85}.dpn .ar.me{opacity:1;font-weight:700}.dpn .al b{display:block}
.dpn .pin{display:block;margin-top:.5rem;font-size:.7rem;color:var(--muted)}
.ovl{margin:.4rem 0 1.2rem}
.ovr,.ova{display:grid;grid-template-columns:4.6rem 1fr;gap:.5rem;align-items:center;margin:.3rem 0;position:relative}
.ovr:hover,.ovr:focus-within{z-index:60}.ovl{position:relative}
.ovd{font-size:.85rem;color:var(--muted);line-height:1.1}.ovd small{display:block;font-size:.65rem;font-style:italic}
.ovk{position:relative;height:30px;border-radius:7px;background:var(--line);margin-right:.4rem}
.ovr.ip .ovk{background:repeating-linear-gradient(45deg,var(--line) 0 4px,transparent 4px 9px),var(--card);outline:1px dashed var(--muted)}

.ly{position:absolute;left:0;top:0;bottom:0;background:var(--oc);border-radius:7px;opacity:1;border:2px solid var(--ol);box-sizing:border-box;min-width:4px;cursor:pointer}
.ly:hover,.ly:focus{outline:3px solid #ff00d4;outline-offset:1px;z-index:50!important}
.ly:hover .tp,.ly:focus .tp{display:block}
.tp{display:none;position:absolute;left:0;top:calc(100% + 6px);width:max-content;max-width:min(260px,80vw);background:var(--ink);color:var(--card);padding:.45rem .6rem;border-radius:8px;font-size:.78rem;line-height:1.35;box-shadow:0 3px 14px rgba(0,0,0,.35);pointer-events:none;z-index:99;font-weight:400}
.m100{position:absolute;top:-4px;bottom:-4px;width:4px;margin-left:-2px;background:repeating-linear-gradient(to bottom,#ff00d4 0 5px,#fff 5px 8px);outline:1px solid #111;z-index:30;pointer-events:none}
.ovt{position:relative;height:1.1rem;margin-right:.4rem}.ovt span{position:absolute;transform:translateX(-50%);font-size:.7rem;color:var(--muted)}.ovt span:first-child{transform:none}
.ova .ovd{visibility:hidden}
.sw{display:inline-block;vertical-align:middle;height:12px;width:16px;border-radius:3px;background:var(--oc);border:2px solid var(--ol);box-sizing:border-box;margin-right:.3rem}.tp .sw{border-color:var(--ol)}
.lg .sw{width:16px;height:12px;border-radius:3px;background:var(--oc);border:2px solid var(--ol)}.lg.ovg{color:var(--ink)}
.ovt span,.ovd{color:var(--ink)}
.tp{border:1px solid var(--muted)}
.tg3{margin-top:.2rem}
.cs .sn{position:absolute;top:0;bottom:0;right:0;border-radius:0 5px 5px 0;border-left:2px solid #111;background:repeating-linear-gradient(135deg,#bdbdbd 0 3px,#fff 3px 7px);opacity:0;transform:scaleX(0);transform-origin:left;transition:transform .4s ease,opacity .3s ease;pointer-events:none}
.cs:hover .sn,.cs:focus .sn{opacity:1;transform:scaleX(1)}
.kd{display:inline-block;width:.8em;height:.8em;background:#fff;border:1px solid #111;vertical-align:baseline;margin-left:.2rem}.kd.h{background:repeating-linear-gradient(135deg,#bdbdbd 0 2px,#fff 2px 4px)}
.tp small{opacity:.85}
.al{display:block;margin-top:.4rem;padding-top:.3rem;border-top:1px solid var(--muted)}.al b{display:block}
.ar{display:block;opacity:.8}.ar.me{opacity:1;font-weight:700}
.ed{position:absolute;right:-7px;bottom:-8px;width:14px;height:8px;background:var(--oc);border:2px solid var(--ol);border-top:0;border-radius:0 0 4px 4px;box-sizing:border-box;box-shadow:0 0 0 1px #111}
.ly.nr{border-right-width:3px}
.lc{cursor:pointer;padding:.15rem .4rem;border-radius:999px;border:2px solid transparent;user-select:none;-webkit-tap-highlight-color:transparent}
.lc:hover,.lc:focus,.lc.on{border-color:#ff00d4;outline:none}
#v0[data-hl] .ly[data-k]{opacity:.45}
#v0[data-hl=protein] .ly[data-k=protein],#v0[data-hl=fiber] .ly[data-k=fiber],#v0[data-hl=calcium] .ly[data-k=calcium],#v0[data-hl=potassium] .ly[data-k=potassium],#v0[data-hl=magnesium] .ly[data-k=magnesium],#v0[data-hl=sodium] .ly[data-k=sodium]{opacity:1;z-index:45!important;outline:3px solid #ff00d4;outline-offset:1px}
#v0[data-hl=calcium] .cs[data-k=calcium] .sn,#v0[data-hl=potassium] .cs[data-k=potassium] .sn,#v0[data-hl=magnesium] .cs[data-k=magnesium] .sn,#v0[data-hl=protein] .cs[data-k=protein] .sn{opacity:1;transform:scaleX(1)}

.ovb{display:grid;grid-template-columns:4.6rem 1fr;gap:.5rem;align-items:center;margin:.3rem 0}
.ovb .ovt{border-top:2px solid #111}.kt2 span{font-weight:700;color:#111}.kt2 span:last-child{transform:translateX(-100%)}
.ovb .kl{font-weight:700;color:#111;display:flex;align-items:center}
.ksw{background:#111!important;border:2px solid #fff!important;box-shadow:0 0 0 1px #111;width:8px!important;height:14px!important;border-radius:2px!important}
.kc{position:absolute;top:-5px;bottom:-5px;width:10px;margin-left:-5px;border-radius:3px;box-sizing:border-box;z-index:70;cursor:pointer}
.kc:hover,.kc:focus{outline:3px solid #ff00d4;outline-offset:2px}
.kc:hover .tp,.kc:focus .tp{display:block}
.kc .tp{left:50%;transform:translateX(-30%);text-align:left}
.kln{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;z-index:55;overflow:visible}
.kln polyline{fill:none;stroke-linejoin:round;stroke-linecap:round}
.lk{cursor:pointer;padding:.15rem .4rem;border-radius:999px;border:2px solid transparent;user-select:none;display:inline-flex;align-items:center;opacity:.55}
.lk.on{opacity:1;border-color:#111}.lk:hover,.lk:focus{outline:none;border-color:#ff00d4}
#v0.nok .kc,#v0.nok .kln,#v0.nok .ovb{display:none}
@media(max-width:560px){.ovb{grid-template-columns:3.6rem 1fr}.kt2 span{font-size:.62rem}}
@media(prefers-reduced-motion:reduce){.cs .sn{transition:none}}
#sp:checked ~ .charts label[for=sp],#sr:checked ~ .charts label[for=sr]{background:var(--brand);color:#fff}
#sr:checked ~ .charts .s-p,#sp:checked ~ .charts .s-r{display:none}
#sp:focus-visible ~ .charts label[for=sp],#sr:focus-visible ~ .charts label[for=sr]{outline:3px solid var(--accent);outline-offset:2px}
.ovs{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;margin:.3rem 0}
.ovs label{cursor:pointer;padding:.35rem .9rem;border-radius:999px;border:2px solid var(--brand);color:var(--brand);font-weight:700;font-size:.85rem}
@media(max-width:560px){.ovr,.ova{grid-template-columns:3.6rem 1fr}.ovk{height:26px}}
/* ===== calmer restyle of #v0 overlay chart ===== */
#v0{--pin:#6d5bd0;--trk:#f3eee4;--grd:#e2d9c8;--ax:#9a9285;box-shadow:0 1px 2px rgba(60,40,10,.06),0 10px 28px rgba(60,40,10,.09);border-radius:16px}
@media(prefers-color-scheme:dark){#v0{--pin:#a99cff;--trk:#2b2a27;--grd:#3d3b36;--ax:#8d887d;box-shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px rgba(0,0,0,.35)}}
#v0 .ovr,#v0 .ova{margin:.55rem 0}#v0 .ova{margin-bottom:.1rem}
#v0 .ovk{height:20px;border-radius:7px;background:var(--trk)}
#v0 .ovr.ip .ovk{background:repeating-linear-gradient(45deg,var(--trk) 0 4px,transparent 4px 9px),var(--card);outline:1px dashed var(--grd)}
#v0 .ovd{color:var(--ink);font-size:.8rem}#v0 .ovd .wd{font-weight:600}
#v0 .ovd.axt{font-size:.6rem;color:var(--ax);line-height:1.15;font-weight:400;letter-spacing:.01em}
#v0 .ovt span{font-size:.62rem;color:var(--ax)}
#v0 .ly{border:1.5px solid var(--ol);border-radius:7px 3px 3px 7px;min-width:5px}
#v0 .ovk>.ly:first-child{border-radius:7px 7px 7px 7px}
#v0 .ly[data-k=calcium]{box-shadow:inset 0 0 0 .5px rgba(120,100,70,.25)}
#v0 .ly:hover,#v0 .ly:focus{outline:2px solid var(--pin);outline-offset:1px}
#v0 .ly:focus:not(:focus-visible):not(:hover){outline:none}
#v0[data-hl=protein] .ly[data-k=protein],#v0[data-hl=fiber] .ly[data-k=fiber],#v0[data-hl=calcium] .ly[data-k=calcium],#v0[data-hl=potassium] .ly[data-k=potassium],#v0[data-hl=magnesium] .ly[data-k=magnesium],#v0[data-hl=sodium] .ly[data-k=sodium]{outline:2px solid var(--pin);outline-offset:1px}
#v0[data-hl] .ly[data-k]{opacity:1;background:color-mix(in srgb,var(--oc) 38%,var(--trk));border-color:color-mix(in srgb,var(--ol) 38%,var(--trk));outline:none}
#v0[data-hl=protein] .ly[data-k=protein],#v0[data-hl=fiber] .ly[data-k=fiber],#v0[data-hl=calcium] .ly[data-k=calcium],#v0[data-hl=potassium] .ly[data-k=potassium],#v0[data-hl=magnesium] .ly[data-k=magnesium],#v0[data-hl=sodium] .ly[data-k=sodium]{opacity:1;background:var(--oc);border:2px solid var(--pin);outline:none;z-index:45!important}
#v0 .m100{width:4px;margin-left:-2px;top:-4px;bottom:-4px;background:repeating-linear-gradient(to bottom,#ff00d4 0 5px,#fff 5px 8px);outline:1px solid #111;border:0;z-index:30}
#v0 .gl5{position:absolute;top:0;bottom:0;width:0;border-left:1px solid var(--grd);opacity:.8;z-index:0;pointer-events:none}
#v0 .ovb .ovt{border-top:1px solid var(--grd)}#v0 .kt2 span{font-weight:500;color:#5b5446;font-size:.62rem}
#v0 .ovb .kl{font-weight:400;color:var(--ax)}
#v0 .sw,#v0 .lg .sw{width:10px;height:10px;border-radius:50%;border:1px solid rgba(60,40,10,.28);background:var(--oc);margin-right:.35rem}
#v0 .ksw{width:4px!important;height:12px!important;border:1px solid #fff!important;box-shadow:0 0 0 .5px #111;border-radius:2px!important;margin-right:.4rem}
#v0 .kc{top:-3px;bottom:-3px;width:8px;margin-left:-4px;border-radius:2px}
#v0 .kc:hover,#v0 .kc:focus{outline:2px solid var(--pin);outline-offset:2px}
#v0 .lg.ovg{gap:.2rem .35rem;justify-content:flex-start;font-size:.8rem;margin:.4rem 0 .8rem}
#v0 .lc,#v0 .lk{display:inline-flex;align-items:center;padding:.2rem .65rem;border:1px solid transparent;border-radius:999px;color:var(--ink)}
#v0 .lc:hover,#v0 .lc:focus,#v0 .lk:hover,#v0 .lk:focus{border-color:transparent;outline:none}
#v0 .lc:focus-visible,#v0 .lk:focus-visible{outline:2px solid var(--pin);outline-offset:1px}
#v0 .lc.on{border-color:var(--pin);background:color-mix(in srgb,var(--pin) 12%,transparent)}
#v0 .lk{opacity:.45;text-decoration:line-through}#v0 .lk.on{opacity:1;text-decoration:none}
#v0 .ova .ovd.axt{visibility:visible}
#v0 .cs .sn{border-left:1px solid rgba(60,40,10,.5)}
@keyframes ovgrow{from{width:0}}
@keyframes ovfade{from{opacity:0}}
#v0 .ly{animation:ovgrow .8s cubic-bezier(.2,.7,.2,1) both}
#v0 .kc{animation:ovfade .6s ease .6s both}
#v0 .ovr:nth-of-type(2) .ly{animation-delay:.04s}#v0 .ovr:nth-of-type(3) .ly{animation-delay:.08s}#v0 .ovr:nth-of-type(4) .ly{animation-delay:.12s}#v0 .ovr:nth-of-type(5) .ly{animation-delay:.16s}#v0 .ovr:nth-of-type(6) .ly{animation-delay:.2s}#v0 .ovr:nth-of-type(7) .ly{animation-delay:.24s}#v0 .ovr:nth-of-type(8) .ly{animation-delay:.28s}
@media(prefers-reduced-motion:reduce){#v0 .ly,#v0 .kc{animation:none}}
@media(max-width:560px){#v0 .ovr,#v0 .ova{grid-template-columns:3.6rem 1fr}#v0 .ovk{height:18px}#v0 .lc,#v0 .lk{padding:.2rem .5rem}}

"""
PANEL='<div class="dpn empty" id="dpn" aria-live="polite">Hover, tap or Tab onto a bar layer or a calorie tick: the tooltip lists the top sources for that day, and the full detail (eaten vs absorbed, sources, all nutrients, meal split) appears here. Tapping pins the last selection.</div>'
PANEL_JS='''<script>(function(){var s=document.getElementById("v0"),p=document.getElementById("dpn"),pin=null,D=p.innerHTML;function show(h,pn){p.classList.remove("empty");p.innerHTML=h+(pn?'<span class="pin">Pinned. Tap another layer to change, or the same one to clear.</span>':"")}function reset(){if(pin){show(pin.querySelector(".dt").innerHTML,true)}else{p.classList.add("empty");p.innerHTML=D}}function dt(e){return e.querySelector(".dt").innerHTML}function cl(e){var t=e.querySelector(".tp");if(!t)return;requestAnimationFrame(function(){t.style.translate="0px";var r=t.getBoundingClientRect(),w=document.documentElement.clientWidth,m=0;if(r.width&&r.left<6)m=6-r.left;else if(r.right>w-6)m=w-6-r.right;t.style.translate=m+"px"})}s.querySelectorAll(".ly,.kc").forEach(function(e){e.addEventListener("mouseenter",function(){show(dt(e));cl(e)});e.addEventListener("mouseleave",reset);e.addEventListener("focus",function(){show(dt(e));cl(e)});e.addEventListener("blur",reset);e.addEventListener("click",function(){cl(e);pin=(pin===e)?null:e;if(pin)show(dt(e),true);else show(dt(e))})});s.querySelectorAll(".rd").forEach(function(r){r.addEventListener("change",function(){pin=null;reset()})})})()</script>'''
ov_sec=('<section class="day var" id="v0"><h2>New) Overlay bar <span class="mockbadge">new</span></h2>'
 '<p class="pc">One bar per day; every nutrient is its own colored layer starting at the left, longest at the back so none is hidden. Hover, tap or Tab onto a layer for the numbers. Hover or tap the <b>calcium, potassium, magnesium or protein</b> layer (or its legend name) to see it split into estimated absorbed (solid) and not absorbed (hatched). Sodium and fiber show a one-line note instead of a split.</p>'
 '<p class="est"><b>Calories:</b> the black tick on each bar shows each day’s estimated calories on the <b>bottom kcal axis</b> (0 to 2,500). The top axis is still % of target. There is no calorie target; the line only shows the amount. A hollow marker means the day is in progress. Use the “Calories” chip in the legend to hide it.</p>'
 '<div class="ovs" role="group" aria-label="Scale"><b>Scale:</b><label for="sp">% of target (default)</label><label for="sr">Raw amount (mg-equivalent, small nutrients tiny)</label></div>'
 '<p class="est s-p">Scale: % of each nutrient’s daily target (protein 56 g, fiber 30 g, calcium 1,000 mg, potassium 3,400 mg, magnesium 420 mg). Sodium* is against its 2,300 mg limit, so shorter is better. Dashed magenta line = 100%; faint lines = 50% and 150%. Bars past the right edge are clipped.</p>'
 '<p class="est s-r">Scale: raw numbers on one shared axis, as logged (mg for calcium, potassium, magnesium and sodium; g for protein and fiber). Fiber and protein, in grams, look tiny next to potassium in mg, which is why % mode is the default. Tiny layers are given a minimum width so they stay visible.</p>'
 '<p class="est">Can’t see a layer? Hover, tap or Tab onto its name in the legend to bring it to the front and highlight it. When two layers end within about 1.5% of each other, the hidden one gets a small tab under the end of its bar that you can also hover or tap.</p>'
 +toggled(ov_all)+PANEL+
 '<script>(function(){var s=document.getElementById("v0");function draw(l){var svg=l.querySelector(".kln");if(!svg)return;var lr=l.getBoundingClientRect();if(!lr.width){return}svg.setAttribute("viewBox","0 0 "+lr.width+" "+lr.height);var p=[];l.querySelectorAll(".kc").forEach(function(m){var r=m.getBoundingClientRect();p.push((r.left+r.width/2-lr.left).toFixed(1)+","+(r.top+r.height/2-lr.top).toFixed(1))});var q=p.join(" ");var mk="";l.querySelectorAll(".kc").forEach(function(m){var r=m.getBoundingClientRect(),h=m.classList.contains("kh");mk+=\'<rect x="\'+(r.left+1.5-lr.left).toFixed(1)+\'" y="\'+(r.top-lr.top).toFixed(1)+\'" width="\'+(r.width-3)+\'" height="\'+r.height+\'" rx="2" fill="\'+(h?"#fff":"#111")+\'" stroke="\'+(h?"#111":"#fff")+\'" stroke-width="1.5"/>\'});svg.innerHTML=mk}var ls=s.querySelectorAll(".ovl");function all(){ls.forEach(draw)}if(window.ResizeObserver){var ro=new ResizeObserver(all);ls.forEach(function(l){ro.observe(l)})}window.addEventListener("resize",all);window.addEventListener("load",all);all();s.querySelectorAll(".lk").forEach(function(e){function t(){var off=s.classList.toggle("nok");s.querySelectorAll(".lk").forEach(function(x){x.classList.toggle("on",!off);x.setAttribute("aria-pressed",!off)})}e.addEventListener("click",t);e.addEventListener("keydown",function(ev){if(ev.key==="Enter"||ev.key===" "){ev.preventDefault();t()}})})})()</script><script>(function(){var s=document.getElementById("v0"),c=null;function set(k){if(k)s.setAttribute("data-hl",k);else s.removeAttribute("data-hl");s.querySelectorAll(".lc").forEach(function(e){var on=e.dataset.k===k;e.classList.toggle("on",on);e.setAttribute("aria-pressed",on)})}s.querySelectorAll(".lc").forEach(function(e){var k=e.dataset.k;e.addEventListener("mouseenter",function(){if(!c)set(k)});e.addEventListener("mouseleave",function(){if(!c)set(null)});e.addEventListener("focus",function(){if(!c)set(k)});e.addEventListener("blur",function(){if(!c)set(null)});e.addEventListener("click",function(){c=(c===k)?null:k;set(c)});e.addEventListener("keydown",function(ev){if(ev.key==="Enter"||ev.key===" "){ev.preventDefault();e.click()}})})})()</script>'+
 PANEL_JS+
 '<p class="est">Hatched row = in progress. Layers are solid with a thin outline (white or dark) so each stays visible; where one is hidden behind another, hover its visible part or use Tab. Food + supplements view includes supplements; food only excludes them.</p>'
 '<details><summary>Data table (amounts and % of target, food + supplements)</summary><div class="tw"><table class="est"><tr><th>Day</th>'+''.join(f'<th>{sw(k)}{l}</th>' for k,l,u,t,c in MK)+'<th>Calcium absorbed, estimate</th></tr>'
 +''.join(f'<tr><td>{MDL[i]}{" (in progress)" if MIP[i] else ""}</td>'+''.join(f'<td>~{NS(i,k)["c"]}{NS(i,k)["p"]} {u} ({P(i,k,"c"):.0f}%)</td>' for k,l,u,t,c in MK)+f'<td>{fm0(cabs(i,"c")[0])}{NS(i,"calcium")["p"]} mg ({cabs(i,"c")[0]/10:.0f}% of target; {cabs(i,"c")[2]:.0f}% of eaten)</td></tr>' for i in range(n_))
 +'</table></div></details></section>')

ABMAX=max(1100,math.ceil((max(x['e'] for x in AD)+40)/100)*100)
ILL=ABS_DEF*10   # 25% x 1,000 mg = 250 mg
CRM='#fff4d0';GRN='#00c040'
def dl(x): return f'{x["l"]}{" (in progress)" if x["ip"] else ""}'
def asw(kind): return f'<i class="asw {kind}"></i>'
ALEG=('<div class="lg alg"><span>'+asw('e')+'Calcium eaten (food only)</span><span>'+asw('a')+'Estimated absorbed (typical adult)</span>'
 '<span><i class="tgl"></i>1,000 mg RDA target</span><span><i class="ill"></i>~250 mg illustrative arithmetic (25% × 1,000), not an official figure</span><span>* = day in progress, dashed</span></div>')
def aalt(): return 'Calcium eaten vs estimated absorbed, food only: '+'; '.join(f'{dl(x)} eaten {x["e"]:,.0f} mg, absorbed about {x["a"]:,.0f} mg ({x["a"]/x["e"]*100:.0f}%)' for x in AD)+'.'
# (1) paired bars
def a1():
    W,H,L,R,T,B=560,310,46,16,18,36; mx=ABMAX
    yy=lambda v:H-B-(H-B-T)*v/mx
    s=''
    for v in range(0,mx+1,200 if mx<=1400 else 500):
        s+=f'<line x1="{L}" x2="{W-R}" y1="{yy(v):.1f}" y2="{yy(v):.1f}" class="gl"/><text x="{L-6}" y="{yy(v)+4:.1f}" class="tx" text-anchor="end">{v:,}</text>'
    n=len(AD); sl=(W-L-R)/n; bw=sl*.34
    for j,x in enumerate(AD):
        cx=L+sl*(j+.5); da=' stroke-dasharray="4 3"' if x['ip'] else ''
        for o,(val,fill,nm) in enumerate([(x['e'],CRM,'eaten'),(x['a'],GRN,'absorbed (est.)')]):
            bx=cx-bw-1 if o==0 else cx+1; y=yy(val)
            s+=f'<rect x="{bx:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{H-B-y:.1f}" fill="{fill}" stroke="#111" stroke-width="1.5"{da}><title>{dl(x)}: {nm} {val:,.0f} mg</title></rect>'
            s+=f'<text x="{bx+bw/2:.1f}" y="{y-4:.1f}" class="tx s v" text-anchor="middle">{val:,.0f}</text>'
        s+=f'<text x="{cx:.1f}" y="{H-18}" class="tx{" ip" if x["ip"] else ""}" text-anchor="middle">{x["l"]}{"*" if x["ip"] else ""}</text>'
    s+=f'<line x1="{L}" x2="{W-R}" y1="{yy(1000):.1f}" y2="{yy(1000):.1f}" class="tl"/><text x="{W-R}" y="{yy(1000)-5:.1f}" class="tx tg" text-anchor="end">1,000 mg target</text>'
    s+=f'<line x1="{L}" x2="{W-R}" y1="{yy(ILL):.1f}" y2="{yy(ILL):.1f}" class="il"/>'
    return ALEG+svg(W,H,aalt(),s)
# (2) overlay style
def a2():
    mx=ABMAX; ticks=range(0,mx+1,200 if mx<=1400 else 500)
    h='<div class="ovl"><div class="ova"><span class="ovd"></span><div class="ovt">'+''.join(f'<span style="left:{v/mx*100:.2f}%">{v:,}</span>' for v in ticks)+'</div></div>'
    for x in AD:
        h+=f'<div class="ovr{" ip" if x["ip"] else ""}"><div class="ovd">{x["l"]}{"<small>in progress</small>" if x["ip"] else ""}</div><div class="ovk">'
        pc=x['a']/x['e']*100
        tipe=f'Eaten {x["e"]:,.0f} mg · absorbed (est.) {x["a"]:,.0f} mg · {pc:.0f}% absorbed<br>ESTIMATE, typical adult; assumed defaults used for most foods'
        for z,(val,nm,oc,ol) in enumerate([(x['e'],'Calcium eaten',CRM,'#111'),(x['a'],'Absorbed (estimate)',GRN,'#111')]):
            ar=f'{nm}, {dl(x)}: {val:,.0f} mg. Eaten {x["e"]:,.0f} mg, estimated absorbed {x["a"]:,.0f} mg, {pc:.0f}% absorbed. Estimate for a typical adult.'
            h+=f'<div class="ly" tabindex="0" role="img" aria-label="{E(ar)}" style="width:{max(val/mx*100,.7):.2f}%;--oc:{oc};--ol:{ol};z-index:{z+1}"><span class="tp" aria-hidden="true"><b>{nm}</b> · {dl(x)}<br>{tipe}</span></div>'
        h+=f'<i class="m100" style="left:{1000/mx*100:.2f}%"></i><i class="m250" style="left:{ILL/mx*100:.2f}%"></i></div></div>'
    h+='</div>'
    return ALEG+h+'<p class="est">Solid green layer sits inside the cream eaten layer. Dashed magenta = 1,000 mg target; thin dark dashed = illustrative ~250 mg. Hover, tap or Tab onto a layer for numbers.</p>'
# (3) food breakdown
def a3day(x):
    if not x['items']: return '<p class="est">No calcium data.</p>'
    m=max(i['mg'] for i in x['items']); h='<div class="fb">'
    for it in x['items']:
        tag=f'<span class="tag2 {it["typ"]}">{"sourced" if it["typ"]=="sourced" else "assumed default"}</span>'
        h+=(f'<div class="fr" role="group" aria-label="{E(it["name"])}: eaten {it["mg"]:,.0f} mg, estimated absorbed {it["ab"]:,.1f} mg at {it["pct"]}%"><div class="fn"><b>{E(it["name"])}</b> <small>{it["g"]:g} g · {it["pct"]}%</small> {tag}</div>'
         f'<div class="fbars"><div class="mb"><i class="e" style="width:{max(it["mg"]/m*100,1):.1f}%"></i></div><div class="mb"><i class="a" style="width:{max(it["ab"]/m*100,.8):.1f}%"></i></div></div>'
         f'<div class="fv"><span>{it["mg"]:,.0f} <small>eaten</small></span><span class="g">{it["ab"]:,.1f} <small>absorbed</small></span></div></div>')
    h+='</div>'
    if x['nd']: h+='<p class="est">No calcium data (excluded, not zero): '+E('; '.join(x['nd']))+'</p>'
    return h+f'<p class="est"><b>Total:</b> {x["e"]:,.0f} mg eaten, about {x["a"]:,.0f} mg absorbed ({x["a"]/x["e"]*100:.0f}%). Sorted by calcium eaten, highest first.</p>'
def a3():
    h='<div class="lg"><span>'+asw('e')+'Eaten (top bar)</span><span>'+asw('a')+'Absorbed, est. (bottom bar)</span></div>'
    for x in sorted(AD,key=lambda z:(z['ip'],-z['i'])):
        op=' open' if x['i'] in (LAST,0) else ''
        lab=('latest complete day' if x['i']==LAST else 'in progress' if x['ip'] else '')
        h+=f'<details class="bd3"{op}><summary>{x["l"]} · {x["e"]:,.0f} mg eaten, ~{x["a"]:,.0f} mg absorbed{" · "+lab if lab else ""}</summary>{a3day(x)}</details>'
    return h
# (4) stacked
def a4():
    W,H,L,R,T,B=560,320,46,16,18,36; mx=ABMAX
    yy=lambda v:H-B-(H-B-T)*v/mx
    s=''
    for v in range(0,mx+1,200 if mx<=1400 else 500):
        s+=f'<line x1="{L}" x2="{W-R}" y1="{yy(v):.1f}" y2="{yy(v):.1f}" class="gl"/><text x="{L-6}" y="{yy(v)+4:.1f}" class="tx" text-anchor="end">{v:,}</text>'
    n=len(AD); sl=(W-L-R)/n; bw=sl*.56
    for j,x in enumerate(AD):
        cx=L+sl*(j+.5); da=' stroke-dasharray="4 3"' if x['ip'] else ''; bx=cx-bw/2
        na=x['e']-x['a']
        s+=f'<rect x="{bx:.1f}" y="{yy(x["a"]):.1f}" width="{bw:.1f}" height="{H-B-yy(x["a"]):.1f}" fill="{GRN}" stroke="#111" stroke-width="1.5"{da}><title>{dl(x)}: absorbed (est.) {x["a"]:,.0f} mg</title></rect>'
        s+=f'<rect x="{bx:.1f}" y="{yy(x["e"]):.1f}" width="{bw:.1f}" height="{yy(x["a"])-yy(x["e"]):.1f}" fill="{CRM}" stroke="#111" stroke-width="1.5"{da}><title>{dl(x)}: not absorbed (est.) {na:,.0f} mg</title></rect>'
        if H-B-yy(x['a'])>16: s+=f'<text x="{cx:.1f}" y="{(yy(x["a"])+H-B)/2+4:.1f}" class="tx s v" text-anchor="middle" style="fill:#111">{x["a"]:,.0f}</text>'
        s+=f'<text x="{cx:.1f}" y="{(yy(x["e"])+yy(x["a"]))/2+4:.1f}" class="tx s v" text-anchor="middle" style="fill:#111">{na:,.0f}</text>'
        s+=f'<text x="{cx:.1f}" y="{yy(x["e"])-5:.1f}" class="tx s v" text-anchor="middle">{x["e"]:,.0f}</text>'
        s+=f'<text x="{cx:.1f}" y="{H-18}" class="tx{" ip" if x["ip"] else ""}" text-anchor="middle">{x["l"]}{"*" if x["ip"] else ""}</text>'
    s+=f'<line x1="{L}" x2="{W-R}" y1="{yy(1000):.1f}" y2="{yy(1000):.1f}" class="tl"/><text x="{W-R}" y="{yy(1000)-5:.1f}" class="tx tg" text-anchor="end">1,000 mg target</text>'
    return '<div class="lg alg"><span>'+asw('a')+'Absorbed (est.)</span><span>'+asw('e')+'Not absorbed (est.), top of bar = calcium eaten</span><span><i class="tgl"></i>1,000 mg target</span></div>'+svg(W,H,aalt(),s)
ACSS="""
.lg .asw,.asw{display:inline-block;width:16px;height:12px;border-radius:3px;border:2px solid #111;box-sizing:border-box}.lg .asw.e,.asw.e{background:#fff4d0}.lg .asw.a,.asw.a{background:#00c040}
.lg .tgl{height:4px;width:18px;background:repeating-linear-gradient(to right,#ff00d4 0 5px,transparent 5px 8px)}.lg .ill{height:0;width:18px;border-top:2px dashed var(--ink);background:none;border-radius:0}
.mk .il{stroke:var(--ink);stroke-width:1.3;stroke-dasharray:2 3}
.m250{position:absolute;top:-2px;bottom:-2px;width:0;border-left:2px dashed var(--ink);z-index:29;pointer-events:none}
.bd3{margin:.4rem 0;border:1px solid var(--line);border-radius:10px;padding:0 .7rem}.bd3>summary{padding:.6rem 0;min-height:44px;font-size:.9rem}.bd3[open]{padding-bottom:.4rem}
.fr{display:grid;grid-template-columns:minmax(8rem,1.2fr) 2fr minmax(7rem,.8fr);gap:.5rem;align-items:center;padding:.35rem 0;border-top:1px solid var(--line)}
.fn small{color:var(--muted)}.tag2{display:inline-block;border-radius:999px;padding:0 .45rem;font-size:.65rem;font-weight:700;background:var(--chip);color:var(--brand)}.tag2.assumed{background:#fff3df;color:#9a5c00}
@media(prefers-color-scheme:dark){.tag2.assumed{background:#3a2d12;color:var(--accent)}}
.mb{height:11px;margin:2px 0;background:var(--line);border-radius:3px;overflow:hidden}.mb i{display:block;height:100%;border:1.5px solid #111;box-sizing:border-box;border-radius:3px}.mb i.e{background:#fff4d0}.mb i.a{background:#00c040}
.fv{display:flex;flex-direction:column;font-size:.82rem;text-align:right;line-height:1.3}.fv small{color:var(--muted);font-size:.7rem}.fv .g{color:#0a8a33;font-weight:700}
@media(prefers-color-scheme:dark){.fv .g{color:#4de07a}}
@media(max-width:560px){.fr{grid-template-columns:1fr 6.2rem}.fn{grid-column:1/-1}}
"""
abs_sec=('<section class="day var" id="va"><h2>Eaten vs absorbed (calcium mockups) <span class="mockbadge">new</span></h2>'
 '<p class="pc">Four ways to show calcium eaten next to calcium absorbed, using the real logged data, food only (supplements have no calcium). All absorbed numbers are <b>ESTIMATES</b> for a typical adult, not personal values; these mockups ignore the food/supplement toggle.</p>'
 f'<div class="note"><b>Assumptions (estimates):</b> absorbed = eaten × an assumed percentage per food. <b>Sourced</b> ({"NIH ODS calcium fact sheet"}, <a href="{NIHCA}">link</a>, accessed 2026-10-17): milk ~27%, spinach ~5%, and low-oxalate greens such as broccoli, kale and cabbage described as similar to milk (27% used). <b>Assumed default</b> ~{ABS_DEF}% (adult average per <a href="{NAS}">National Academies 2011 report</a>) for everything else: pumpkin seeds, lentils, walnuts, fish, eggs, bread, yogurt, kefir, skyr and so on (NIH gives ~30% for dairy and fortified foods, but I kept the default as marked). Hot chocolate is treated as milk (27%, assumed). Real absorption varies with dose, age and the rest of the meal. There is <b>no official “absorbed requirement”</b>; the dashed ~250 mg line (25% × 1,000 mg) is <b>illustrative arithmetic, not an official figure</b>.</div>'
 '<h3>A) Paired bars per day</h3><p class="pc">Cream = eaten, green in front = estimated absorbed.</p>'+a1()+
 '<h3>B) Overlay bar style</h3><p class="pc">Same look as the Overlay bar: cream layer = eaten, solid green layer inside = absorbed.</p>'+a2()+
 '<h3>C) Food breakdown per day</h3><p class="pc">Each food’s eaten and estimated absorbed calcium, highest first. Latest complete day (and Oct 10, which has a big spinach portion) are open; tap another day to expand.</p>'+a3()+
 '<h3>D) Stacked bar: absorbed vs not absorbed</h3><p class="pc">Total height = calcium eaten; green part = estimated absorbed.</p>'+a4()+
 '<details><summary>Data table (calcium eaten and estimated absorbed per day)</summary><div class="tw"><table class="est"><tr><th>Day</th><th>Eaten (mg)</th><th>Absorbed, est. (mg)</th><th>% absorbed</th><th>% of 1,000 mg eaten</th></tr>'
 +''.join(f'<tr><td>{dl(x)}</td><td>{x["e"]:,.0f}</td><td>{x["a"]:,.0f}</td><td>{x["a"]/x["e"]*100:.0f}%</td><td>{x["e"]/10:.0f}%</td></tr>' for x in AD)
 +'</table></div></details></section>')
VAR=[
 (1,'Multi-line with 100% target line','Pro: shows trends and all nutrients together. Con: lines tangle when values are close.',c1,True),
 (2,'Heatmap grid (nutrients × days)','Pro: exact numbers plus color, easiest to spot gaps. Con: no trend shape, only color and digits.',c2,True),
 (3,'Grouped bars per nutrient','Pro: compare days within a nutrient at a glance. Con: 48 thin bars is busy on a phone.',c3,True),
 (4,'Small multiples (one chart per nutrient)','Pro: clearest per-nutrient trend, no overlap. Con: takes the most space, harder to compare across nutrients.',c4,True),
 (5,'Radar chart: latest complete day vs average','Pro: one-glance shape of the balance. Con: only two snapshots, area is easy to misread.',c5,True),
 (6,'Bullet bars: 7-day average vs target','Pro: simplest answer to "am I meeting targets". Con: hides day-to-day swings except the thin range band.',c6,True),
 (7,'Stacked bars: food vs supplement share','Pro: shows how much of each target comes from supplements. Con: averages only (always food vs supplement, no toggle).',c7,False),
 (8,'Dot plot (lollipop) of daily %','Pro: every day visible on one shared axis per nutrient, low clutter. Con: no ordering by day unless you hover or count dots.',c8,True),
 (9,'Diverging bars: over/under target','Pro: gaps and surpluses pop out around a single center line. Con: loses absolute level, and good/bad flips for sodium.',c9,True),
 (10,'Log-scale raw values (contrast)','Pro: real units on one axis. Con: log scale hides size differences and can’t show target attainment, so it’s a poor fit.',c10,True),
]
MCSS=OVCSS+ACSS+"""
.mk{width:100%;height:auto;display:block;max-width:760px;margin:0 auto}
.sc{overflow-x:auto}
.mk .tx{fill:var(--muted);font-size:12px;font-family:inherit}.mk .tx.s{font-size:11px}.mk .tx.ip{font-style:italic}.mk .tx.tg{fill:var(--brand2);font-weight:700}.mk .tx.v{font-weight:700;fill:var(--ink)}
.mk .gl{stroke:var(--line);stroke-width:1}.mk .gl.mn{stroke-dasharray:2 4;opacity:.7}.mk .tl{stroke:var(--brand2);stroke-width:1.6;stroke-dasharray:5 4}
.mk .ln{fill:none;stroke:var(--c);stroke-width:2.4;stroke-linejoin:round}.mk .ln.da{stroke-dasharray:5 5;opacity:.8}.mk .ln.lo{stroke-width:2.4;opacity:.95}
.mk .dot{fill:var(--c);stroke:var(--card);stroke-width:1}.mk .dot.hol{fill:var(--card);stroke:var(--c);stroke-width:2}
.mk .stem{stroke:var(--c);stroke-width:2;opacity:.35}.mk .av{fill:var(--ink)}
.mk g{color:var(--c)}.mk .br{stroke-width:1.2}
.mk .dv.good{color:#2e8b6a}.mk .dv.bad{color:#d98a1e}.mk .dv.good{fill:#2e8b6a}.mk .dv.bad{fill:#e0a23a}
@media(prefers-color-scheme:dark){.mk .dv.good{color:#4cc79a;fill:#4cc79a}.mk .dv.bad{color:#f5b85c;fill:#f5b85c}}
.mk .ring{fill:none;stroke:var(--line)}.mk .ring100{fill:none;stroke:var(--brand2);stroke-width:1.6;stroke-dasharray:5 4}
.mk .ra{fill:rgba(245,184,92,.28);stroke:var(--accent);stroke-width:2;stroke-dasharray:5 3}.mk .rl{fill:rgba(76,199,154,.30);stroke:var(--brand);stroke-width:2.4}
.lg{display:flex;flex-wrap:wrap;gap:.3rem .9rem;margin:.2rem 0 .5rem;font-size:.82rem;color:var(--muted)}
.lg span{display:inline-flex;align-items:center;gap:.35rem}.lg i{display:inline-block;width:14px;height:4px;border-radius:2px;background:var(--c,var(--brand))}
.lg .k1 i{background:var(--brand)}.lg .k2 i{background:var(--accent)}.lg .solid i{height:12px;background:var(--brand2)}.lg .hat i{height:12px;border:1.5px solid var(--brand2);background:repeating-linear-gradient(45deg,var(--brand2) 0 2px,transparent 2px 5px)}
.lg .gd i{height:12px;background:#2e8b6a}.lg .bd2 i{height:12px;background:#e0a23a}
.sr{position:absolute;left:-9999px}
.hm{font-size:.85rem}.hm th,.hm td{text-align:center;padding:.45rem .35rem;white-space:nowrap}.hm tbody th{text-align:left;color:var(--c);position:static}.hm thead th{position:static}
.hm td.av{font-weight:800;border-left:2px solid var(--line)}
.hm .ipc{background-image:repeating-linear-gradient(45deg,rgba(128,128,128,.28) 0 3px,transparent 3px 8px);font-style:italic}
.hm small{font-weight:400;color:var(--muted);font-size:.65rem}
.sm{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:.7rem}
.sm figure{margin:0;border:1px solid var(--line);border-radius:12px;padding:.4rem .5rem;border-top:4px solid var(--c)}
.sm figcaption{font-size:.85rem;color:var(--c)}.sm figcaption small{color:var(--muted)}
.sm .sc{overflow:visible}.sm .mk{max-width:none}
.bl{display:grid;gap:.7rem}.bn{display:flex;justify-content:space-between;font-size:.88rem;color:var(--c)}.bn small{color:var(--muted)}
.trk{position:relative;height:18px;border-radius:9px;background:var(--line);overflow:hidden}
.trk i{position:absolute;top:0;bottom:0}.trk .fl{left:0;background:var(--c);opacity:.85}.trk .rg{top:7px;bottom:7px;background:var(--ink);opacity:.7;border-radius:2px}.trk .tm{width:3px;margin-left:-1px;background:var(--brand2);box-shadow:0 0 0 1px var(--card)}
.tg2{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;margin:.4rem 0 1rem}
.tg2 label{cursor:pointer;padding:.45rem 1rem;border-radius:999px;border:2px solid var(--brand);color:var(--brand);font-weight:700;font-size:.9rem}
.rd{position:absolute;opacity:0;pointer-events:none}
#mc:checked ~ .tg2 label[for=mc],#mf:checked ~ .tg2 label[for=mf]{background:var(--brand);color:#fff}
#mf:checked ~ .charts .m-c,#mc:checked ~ .charts .m-f{display:none}
#mf:focus-visible ~ .tg2 label[for=mf],#mc:focus-visible ~ .tg2 label[for=mc]{outline:3px solid var(--accent);outline-offset:2px}
.var h2{font-size:1.15rem;margin:.1rem 0 .1rem;border:0;color:var(--brand2)}.var .pc{color:var(--muted);font-size:.9rem;margin:0 0 .6rem}
.mockbadge{display:inline-block;background:#fff3df;color:#9a5c00;border-radius:999px;padding:.1rem .7rem;font-size:.75rem;font-weight:700}
@media(prefers-color-scheme:dark){.mockbadge{background:#3a2d12;color:var(--accent)}}
@media(min-width:561px){.swipe{display:none}}
@media(max-width:560px){.mk{min-width:430px}.sm .mk{min-width:0}.var{padding:.9rem .8rem}}
"""
# ================= mock.html : food nutrition explorer (USDA data from foods_full.json) =================
XCSS="""
.mockbadge{display:inline-block;background:#fff3df;color:#9a5c00;border-radius:999px;padding:.1rem .7rem;font-size:.75rem;font-weight:700}
@media(prefers-color-scheme:dark){.mockbadge{background:#3a2d12;color:var(--accent)}}
.xn{position:sticky;top:0;z-index:5;background:var(--bg);padding:.5rem 0;margin:0 0 1rem;border-bottom:1px solid var(--line)}
.xn a{background:var(--chip);color:var(--brand);font-size:.85rem;padding:.4rem .8rem}.xn a:hover,.xn a:focus-visible{background:var(--brand);color:#fff}
.xs{scroll-margin-top:4rem}.xs h2{font-size:1.25rem}.xs .pc{color:var(--muted);font-size:.92rem;margin:0 0 .7rem}
.px{background:#fff3df;color:#9a5c00;border-radius:999px;padding:0 .5rem;font-size:.8rem;font-weight:700}
@media(prefers-color-scheme:dark){.px{background:#3a2d12;color:var(--accent)}}
.ctl{display:flex;flex-wrap:wrap;gap:.6rem .9rem;align-items:flex-end;margin:.3rem 0 .8rem}
.ctl label{display:flex;flex-direction:column;font-size:.8rem;font-weight:700;color:var(--muted);gap:.15rem}
.ctl input,.ctl select,.ctl button{font:inherit;font-size:.95rem;padding:.45rem .6rem;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--ink);min-height:44px;max-width:100%}
.ctl input[type=number]{width:7rem}.ctl select{min-width:12rem}
.ctl label.ck{flex-direction:row;align-items:center;gap:.4rem;min-height:44px}.ctl label.ck input{min-height:0;width:1.1rem;height:1.1rem}
.ctl button{cursor:pointer;font-weight:600;color:var(--brand2)}.ctl button.go{background:var(--brand);color:#fff;border-color:var(--brand)}
.qb{display:flex;gap:.3rem;flex-wrap:wrap}
.ctl :focus-visible,.hm button:focus-visible,.fr button:focus-visible,.xn a:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.pf h3{margin:.2rem 0}.px2{background:#fff8ea;border-left:4px solid var(--accent);padding:.5rem .8rem;border-radius:8px;font-size:.9rem;margin:.4rem 0}
@media(prefers-color-scheme:dark){.px2{background:#2e2614}}
.pg{display:grid;grid-template-columns:repeat(auto-fit,minmax(285px,1fr));gap:1rem}
.pgc h4{margin:.2rem 0 .3rem;color:var(--brand);font-size:.95rem;border-bottom:2px solid var(--chip)}
.nrw{display:grid;grid-template-columns:1fr auto;gap:0 .6rem;padding:.25rem 0;font-size:.88rem;border-bottom:1px solid var(--line)}
.nrw .nl{font-weight:600}.nrw .nv{text-align:right;white-space:nowrap}.nrw .nv em{font-style:normal;font-weight:800;color:var(--brand);margin-left:.3rem}
.nrw.lim .nv em{color:#9a5c00}.nrw.nd .nv,.nrw.nd .nl{color:var(--muted);font-style:italic;font-weight:400}
.bt{grid-column:1/-1;height:7px;border-radius:99px;background:var(--line);overflow:hidden;display:block}.bt i{display:block;height:100%;background:var(--brand);border-radius:99px}
.lim .bt i{background:var(--accent)}.nd .bt{background:repeating-linear-gradient(90deg,var(--line) 0 4px,transparent 4px 8px)}
.lb{list-style:none;margin:0;padding:0}.lb li{display:grid;grid-template-columns:2rem minmax(0,1.3fr) minmax(60px,1fr) auto;gap:.5rem;align-items:center;padding:.3rem 0;border-bottom:1px solid var(--line);font-size:.88rem}
.lb .rk{color:var(--muted);text-align:right;font-weight:700}.lb .fv{text-align:right;white-space:nowrap}.lb .fv em,.tc .fv em,#e-t em{font-style:normal;font-weight:800;color:var(--brand);margin-left:.25rem}
.lb .bt{grid-column:auto}.lb .nd{color:var(--muted);font-style:italic}.lb .sep{display:block;font-weight:700;color:var(--muted);padding:.8rem 0 .2rem;border-bottom:2px solid var(--line)}
.lb .fn{overflow-wrap:anywhere}
.hm{max-height:70vh;overflow:auto}.hm table{font-size:.8rem;min-width:900px}.hm th,.hm td{padding:.3rem .45rem;white-space:nowrap}.hm td{text-align:right;font-variant-numeric:tabular-nums}
.hm thead th{top:0;z-index:2;text-align:center}.hm th.sc{white-space:normal;min-width:8.5rem;max-width:11rem;position:sticky;left:0;z-index:1;background:var(--card);text-align:left}.hm thead th.sc{z-index:3;background:var(--chip)}
.hm th button{all:unset;cursor:pointer;color:inherit;font-weight:700;display:block;padding:.2rem;text-align:center}.hm th.sc button{text-align:left}.hm th button small{display:block;font-weight:400;color:var(--muted)}
.hm th[aria-sort=ascending] button::after{content:" ▲"}.hm th[aria-sort=descending] button::after{content:" ▼"}
.hm td.nd{color:var(--muted);font-style:italic;font-size:.7rem;background:repeating-linear-gradient(45deg,transparent 0 4px,rgba(128,128,128,.12) 4px 8px)}
.hm tbody tr:nth-child(even) td{background-color:transparent}
.tops{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:.8rem}
.tc{border:1px solid var(--line);border-top:4px solid var(--brand);border-radius:12px;padding:.4rem .8rem .6rem}.tc h3{margin:.3rem 0;font-size:1rem}
.tc ol{list-style:none;margin:0;padding:0}.tc li{display:grid;grid-template-columns:1fr auto;gap:0 .5rem;font-size:.85rem;padding:.2rem 0}.tc .bt{grid-column:1/-1}.tc .fv{text-align:right;white-space:nowrap}
.rw{display:grid;grid-template-columns:minmax(0,380px) 1fr;gap:1rem;align-items:start}@media(max-width:700px){.rw{grid-template-columns:1fr}}
#e-svg svg{width:100%;height:auto;max-width:380px;display:block;margin:0 auto}
.rg{fill:none;stroke:var(--line);stroke-width:1}.rl{font-size:12px;fill:var(--ink)}
.r1{fill:rgba(46,139,106,.28);stroke:#2e8b6a;stroke-width:2}.r2{fill:rgba(224,118,43,.25);stroke:#e0762b;stroke-width:2}
.r1d{fill:#2e8b6a}.r2d{fill:#e0762b}.hol{fill:var(--card)!important;stroke:var(--muted);stroke-width:1.5}
.lg2{text-align:center;font-size:.85rem}.k1,.k2{display:inline-block;width:.8rem;height:.8rem;border-radius:3px;vertical-align:middle;margin-right:.2rem}.k1{background:#2e8b6a}.k2{background:#e0762b;margin-left:.8rem}
#e-t td.nd{color:var(--muted);font-style:italic}
.fr{list-style:none;padding:0;margin:.3rem 0;display:flex;flex-wrap:wrap;gap:.4rem}.fr button{font:inherit;font-size:.88rem;cursor:pointer;border:1px solid var(--line);background:var(--chip);color:var(--ink);border-radius:10px;padding:.4rem .7rem;min-height:44px;text-align:left}.fr button:hover{border-color:var(--brand)}.fr small{color:var(--muted)}
@media(max-width:560px){.lb li{grid-template-columns:1.4rem minmax(0,1fr) auto}.lb .bt{display:none}.xn a{padding:.4rem .6rem}.ctl select{min-width:0;width:100%}.ctl label{flex:1 1 40%}}
"""
_ff=json.load(open('foods_full.json'))
_nf=nut['foods']
# public page data only: USDA values, stand-in flags and generic public notes (no personal logs or quantities)
_pub={'accessed':_ff['accessed'],'nutrients':_ff['nutrients'],'foods':[{k:f[k] for k in ('key','fdc_id','name','usda_description','data_type','source','accessed','proxy','note','extra','per100g')} for f in _ff['foods']]}
assert len(_pub['foods'])==len([k for k,v in _nf.items() if v.get('fdc_id')])+8
assert all(f['key'] in _nf for f in _pub['foods'] if not f['extra'])
assert all(v in (None,) or isinstance(v,(int,float)) for f in _pub['foods'] for v in f['per100g'].values()), 'bad nutrient value'
assert not any(isinstance(v,(int,float)) and v<0 for f in _pub['foods'] for v in f['per100g'].values())
_tpl=open('explorer_tpl.html').read().replace('@@ACC@@',_ff['accessed']).replace('@@DATA@@',json.dumps(_pub,separators=(',',':'),ensure_ascii=False).replace('</','<\\/'))
mp=page('Food Nutrition Explorer','Look up what is in a food, or rank every food by a nutrient. Public USDA FoodData Central data.','',_tpl)
mp=mp.replace('</style>',XCSS+'</style>',1).replace('<nav><a href="index.html">💊 Supplements</a><a href="food.html">🥗 Food Log</a></nav>','<nav><a href="food.html">&larr; Food Log</a></nav>')
open('mock.html','w').write(mp)
print('mock.html explorer:',len(_pub['foods']),'foods,',len(_pub['nutrients']),'nutrients')


# ================= food.html : final assembly with the overlay chart replacing "Week at a glance" =================
def scope_css(css,pre='#v0'):
    css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
    out=[];i=0
    def block(i):
        # returns (text, next index) for one rule or at-rule starting at i
        j=css.index('{',i); head=css[i:j].strip()
        if head.startswith('@keyframes'):
            d=1;k=j+1
            while d:
                d+= (css[k]=='{')-(css[k]=='}'); k+=1
            return css[i:k],k
        if head.startswith('@media'):
            inner=[];k=j+1
            while css[k:].lstrip()[:1]!='}':
                k=len(css)-len(css[k:].lstrip())
                t,k=block(k); inner.append(t)
            k=css.index('}',k)+1
            return head+'{'+''.join(inner)+'}',k
        e=css.index('}',j)
        sels=[x.strip() for x in head.split(',')]
        sels=[x if x.startswith(pre) else pre+' '+x for x in sels]
        return ','.join(sels)+css[j:e+1],e+1
    while css[i:].strip():
        i=len(css)-len(css[i:].lstrip())
        t,i=block(i); out.append(t)
    return ''.join(out)
FCSS_EXTRA="""
.rd{position:absolute;opacity:0;pointer-events:none}
.tg2{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;margin:.4rem 0 1rem}
.tg2 label{cursor:pointer;padding:.45rem 1rem;border-radius:999px;border:2px solid var(--brand);color:var(--brand);font-weight:700;font-size:.9rem}
#mc:checked ~ .tg2 label[for=mc],#mf:checked ~ .tg2 label[for=mf]{background:var(--brand);color:#fff}
#mf:checked ~ .charts .m-c,#mc:checked ~ .charts .m-f{display:none}
#mf:focus-visible ~ .tg2 label[for=mf],#mc:focus-visible ~ .tg2 label[for=mc]{outline:3px solid var(--accent);outline-offset:2px}
.lg{display:flex;flex-wrap:wrap;gap:.3rem .9rem;margin:.2rem 0 .5rem;font-size:.82rem;color:var(--muted)}
"""
# drop the first (mock-only) #v0 block of OVCSS that is already #v0-prefixed: harmless; scope everything else
FOODCSS=scope_css(OVCSS+FCSS_EXTRA)
chart_html=(
 '<section class="day wk" id="v0"><h2>Week at a glance <span class="badge">estimates, logged meals only</span></h2>'
 '<p class="est">One bar per day; every nutrient is its own colored layer, longest at the back. Hover, tap or Tab onto a layer to see eaten amounts, % of target, and (for calcium, potassium, magnesium and protein) an estimated absorbed vs not-absorbed split. The black tick is calories on the bottom kcal axis.</p>'
 '<input class="rd" type="radio" name="s" id="sp" checked aria-label="Percent of target scale"><input class="rd" type="radio" name="s" id="sr" aria-label="Raw amount scale"><input class="rd" type="radio" name="m" id="mf" aria-label="Food only"><input class="rd" type="radio" name="m" id="mc" checked aria-label="Food plus supplements"><div class="tg2" role="group" aria-label="Data shown"><b>Show:</b><label for="mf">Food only</label><label for="mc">Food + supplements</label></div>'
 '<div class="charts">'
 '<div class="ovs" role="group" aria-label="Scale"><b>Scale:</b><label for="sp">% of target (default)</label><label for="sr">Raw amount</label></div>'
 '<p class="est s-p">% of each nutrient&rsquo;s daily target (protein 56 g, fiber 30 g, calcium 1,000 mg, potassium 3,400 mg, magnesium 420 mg). Sodium* is against its 2,300 mg limit, so shorter is better. Dashed magenta line = 100%. Bars past the right edge are clipped.</p>'
 '<p class="est s-r">Raw numbers on one shared axis (mg or g as logged). Small nutrients in grams look tiny, which is why % mode is the default.</p>'
 '<p class="est">Can&rsquo;t see a layer? Hover, tap or Tab onto its name in the legend to bring it to the front. A small tab under a bar&rsquo;s end marks a layer hidden behind another. &ldquo;+&rdquo; after a number means some foods had no data, so the true amount is higher. Hollow marker or hatched row = day in progress. Calories have no target; tap &ldquo;Calories&rdquo; in the legend to hide the tick. Estimates for a typical adult; targets are for a 54-year-old man. Tuna sandwich, curry and many portions are assumed; see each day.</p>'
 +toggled(ov_all)+'</div>'+PANEL
 +ov_sec[ov_sec.index('<script>'):ov_sec.index('<p class="est">Hatched row')]
 +ov_sec[ov_sec.index('<details><summary>Data table'):]
)
FOOD_BODY=FOOD_BODY.replace('@@CHART@@',chart_html)
fp=page('Food Log','Daily meals with estimated nutrition, newest first.','f',FOOD_BODY).replace('</style>',FOODCSS+'</style>',1)
open('food.html','w').write(fp)

# ---- check: chart numbers == day-card numbers for every day/nutrient ----
cards_={}
for sec in fp.split('<section class="day"><h2>')[1:]:
    m=re.match(r'([A-Z][a-z]+day, [A-Z][a-z]+ \d+, \d{4})',sec)
    if not m: continue
    dd=datetime.datetime.strptime(m.group(1),'%A, %B %d, %Y').date().isoformat()
    for cl,fv_,sv_,cv_ in re.findall(r'<div class="nr (t-\w+)">.*?<span class="h">Food</span><b>~([^<]+)</b>.*?<span class="h">Supplements</span><b>([^<]+)</b>.*?<span class="h">Combined</span><b>~([^<]+)</b>',sec,flags=re.S):
        cards_[(dd,cl)]=(fv_,sv_,cv_)
cmap={c:k for k,l,u,t,c in NUT}
chart_={}
for m in re.finditer(r'<div class="ly[^"]*" data-k="(\w+)" data-d="([\d-]+)" data-f="([^"]*)" data-s="([^"]*)" data-c="([^"]*)" data-p="([^"]*)"',chart_html):
    chart_[(m.group(2),m.group(1))]=(m.group(3),m.group(4),m.group(5),m.group(6))
cnt=0
for d_ in days:
    for k,l,u,t,c in MK:
        cf,cs,cc,cp=chart_[(d_['date'],k)]
        df,ds,dc=cards_[(d_['date'],c)]
        assert (cf+cp,cs,cc+cp)==(df,ds,dc),(d_['date'],k,(cf+cp,cs,cc+cp),(df,ds,dc))
        cnt+=1
assert cnt==len(days)*len(MK)
print('chart/day-card numbers match for',cnt,'day-nutrient pairs')

# ---- check: tooltip contributor rows == day-card breakdown rows (names, amounts, and % in combined view) ----
import html as _h
cardrows={}
for sec in fp.split('<section class="day"><h2>')[1:]:
    m=re.match(r'([A-Z][a-z]+day, [A-Z][a-z]+ \d+, \d{4})',sec)
    if not m: continue
    dd=datetime.datetime.strptime(m.group(1),'%A, %B %d, %Y').date().isoformat()
    for cl,body in re.findall(r'<details class="bd (t-\w+)">(.*?)</details>',sec,flags=re.S):
        rl=[]
        for lab,amt,pc in re.findall(r'<tr[^>]*><td>(.*?)</td><td class="n">[^<]*</td><td class="n">([^<]*)</td><td class="n">(\d+)%</td></tr>',body):
            lab=re.split(r'<span class="tag">| <small>',lab)[0]
            rl.append((_h.unescape(lab),amt,pc))
        cardrows[(dd,cmap[cl])]=rl
tcount=0
for mode,seg in (('f',chart_html.split('<div class="m-c">')[0]),('c',chart_html.split('<div class="m-c">')[1])):
    for m in re.finditer(r'<div class="ly[^"]*" data-k="(\w+)" data-d="([\d-]+)".*?<span class="tp tb"(.*?)</span><span class="dt"',seg,flags=re.S):
        k,dd,tp=m.groups()
        trs=re.findall(r'<span class="br([^"]*)"><span class="bn"><span class="nm">(.*?)</span>(?:<span class="tg">[^<]*</span>)?</span><b>([^<]*)</b><em>(\d+)%</em></span>',tp)
        cr=cardrows[(dd,k)]; used=0; last=1e18
        for cls,lab,amt,pc in trs:
            if 'oth' in cls: continue
            lab=_h.unescape(lab); hit=[r for r in cr if r[0]==lab and r[1]==amt and (mode=='f' or r[2]==pc)]
            assert hit,(mode,dd,k,lab,amt,pc)
            v=float(amt.replace(',',''))
            if 'sup' not in cls: assert v<=last+1e-9,(dd,k,'not ranked'); last=v
            used+=1
        assert 0<used<=TOPN+3,(dd,k,used)
        tcount+=1
assert tcount>=2*len(days)*len(MK)
print('tooltip breakdown rows match day-card breakdowns for',tcount,'layer tooltips')
