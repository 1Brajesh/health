import json,html
CSS="body{font-family:system-ui,sans-serif;margin:2rem;color:#222}table{border-collapse:collapse;width:100%}td,th{border:1px solid #ccc;padding:8px;vertical-align:top;text-align:left}th{background:#eef6ee}nav a{margin-right:1rem;font-weight:600}"
NAV='<nav><a href="index.html">Supplements</a><a href="food.html">Food Log</a></nav>'
def page(title,body):
    return f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head><body>{NAV}{body}</body></html>'
d=json.load(open('supplements.json'))
r=''.join(f"<tr><td>{x['n']}</td><td><b>{html.escape(x['name'])}</b><br><small>{html.escape(x['brand'])}</small></td><td>{html.escape(x['schedule'])}</td><td>{html.escape(x['serving'])}</td><td>{html.escape(x['nutrients'])}</td><td><small>{html.escape(x['other'])}</small></td></tr>" for x in d)
open('index.html','w').write(page('Supplements',f'<h1>My Supplements</h1><p>Reference list. Amounts are approximate; consult a doctor for personal advice.</p><table><tr><th>#</th><th>Supplement</th><th>When</th><th>Serving</th><th>Key nutrients</th><th>Other ingredients</th></tr>{r}</table>'))
f=json.load(open('foodlog.json'))
b=''
for day in sorted(f,key=lambda x:x['date'],reverse=True):
    rows=''.join(f"<tr><td>{html.escape(m['meal'])}</td><td>{html.escape(m['items'])}</td></tr>" for m in day['meals'])
    b+=f"<h2>{day['date']}</h2><table><tr><th>Meal</th><th>What I ate</th></tr>{rows}</table>"
open('food.html','w').write(page('Food Log','<h1>Food Log</h1>'+b))
