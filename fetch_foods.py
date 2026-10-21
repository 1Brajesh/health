"""Builds foods_full.json: full USDA FoodData Central nutrient profiles (per 100 g) for every food in nutrition.json
that has an fdc_id, plus a few extra reference foods. SR Legacy entries come from the public FDC bulk CSV download
(identical to the API's SR Legacy data); Branded entries come from the public FDC API (DEMO_KEY).
Missing nutrients are simply absent (= 'no data'); nothing is invented or defaulted to 0."""
import csv,json,os,sys,datetime,zipfile,urllib.request
ACC='2026-10-18'
D='/workspace/fdc/FoodData_Central_sr_legacy_food_csv_2018-04'
NUTS=[ # key,label,unit,group,fdc nutrient id
('kcal','Energy','kcal','macro',1008),('protein','Protein','g','macro',1003),('fat','Total fat','g','macro',1004),
('sat','Saturated fat','g','macro',1258),('mono','Monounsaturated fat','g','macro',1292),('poly','Polyunsaturated fat','g','macro',1293),('trans','Trans fat','g','macro',1257),
('carbs','Carbohydrate','g','macro',1005),('sugars','Total sugars','g','macro',2000),('addsug','Added sugars','g','macro',1235),('fiber','Fiber','g','macro',1079),
('chol','Cholesterol','mg','macro',1253),('water','Water','g','macro',1051),('caffeine','Caffeine','mg','macro',1057),('alcohol','Alcohol','g','macro',1018),
('calcium','Calcium','mg','mineral',1087),('iron','Iron','mg','mineral',1089),('magnesium','Magnesium','mg','mineral',1090),('phosphorus','Phosphorus','mg','mineral',1091),
('potassium','Potassium','mg','mineral',1092),('sodium','Sodium','mg','mineral',1093),('zinc','Zinc','mg','mineral',1095),('copper','Copper','mg','mineral',1098),
('manganese','Manganese','mg','mineral',1101),('selenium','Selenium','µg','mineral',1103),
('vita','Vitamin A (RAE)','µg','vitamin',1106),('vitc','Vitamin C','mg','vitamin',1162),('vitd','Vitamin D','µg','vitamin',1114),('vite','Vitamin E','mg','vitamin',1109),
('vitk','Vitamin K','µg','vitamin',1185),('b1','Thiamin (B1)','mg','vitamin',1165),('b2','Riboflavin (B2)','mg','vitamin',1166),('b3','Niacin (B3)','mg','vitamin',1167),
('b5','Pantothenic acid (B5)','mg','vitamin',1170),('b6','Vitamin B6','mg','vitamin',1175),('folate','Folate (DFE)','µg','vitamin',1190),('b12','Vitamin B12','µg','vitamin',1178),
('choline','Choline','mg','vitamin',1180)]
EXTRA=[('sweet_potato_raw',168482),('sweet_potato_baked',168483),('kale_boiled',169238),('bok_choy_raw',170390),('bok_choy_boiled',170391),
('collards_raw',170406),('collards_boiled',170407),('broccoli_raw',170379)]
PUB={ # public, generic notes for stand-in entries (no personal details)
'polish_sausage':'Generic pork Polish sausage; brand not specified.','milk_2':'2% reduced-fat milk entry used for milk in general.',
'croissant':'Plain butter croissant; USDA has no chocolate croissant, so a chocolate one would have a little more sugar and calories.',
'pork_shoulder':'Braised pork shoulder entry used as a stand-in for pulled pork; sauce not included.',
'popcorn':'Unsalted air-popped entry; salted or oil-popped popcorn would have more sodium and fat.',
'hot_cocoa':'Homemade hot chocolate with milk used as a stand-in; mixes and café versions vary.',
'wf_pizza':'Branded entry (Whole Foods Market cheese pizza); lacks potassium and magnesium data.',
'kombucha':'Branded entry (Kroger kombucha); reports only a few nutrients. Other brands differ.',
'kefir':'Lifeway lowfat plain kefir used as a stand-in; brands and fat levels differ.',
'cod':'Pacific cod used as a stand-in for white fish; USDA lists no fiber value for it.',
'tuna':'Light tuna in water used as a stand-in for sandwich tuna.','mayo':'Regular mayonnaise.',
'lentils':'Boiled lentils without salt; home recipes and salt vary.','tortilla':'Generic shelf-stable flour tortilla; brands vary.',
'bread':'Toasted wheat bread used as a stand-in for bread in general.','wf_lentil_soup':'Branded entry (Whole Foods Market lentil soup); lacks potassium and magnesium data.',
'siggis':'Branded entry (Siggi\'s plain 0% strained yogurt); lacks calcium, potassium and magnesium data.',
'sushi_roll':'WEAK stand-in: a generic tempura shrimp roll from one brand; real rolls differ a lot. Few nutrients reported.',
'egg_fried':'Fried whole egg (includes some cooking fat); over-easy or poached eggs differ slightly.',
'broccoli':'Boiled, drained broccoli used as the closest entry to steamed.','chicken_breast':'Roasted breast meat without skin; skin or dark meat has more fat.',
'skyr':'Branded entry for plain whole-milk Icelandic skyr; brands differ. Lacks magnesium data.','corn_tortilla_fried':'Ready-to-fry corn tortilla; restaurant tortillas may differ.',
'duck_cooked':'Cooked duck meat only, no skin.','melting_cheese':'Mozzarella-type melting cheese used as the closest entry; other cheeses (cotija, queso fresco) differ.',
'veg_oil_fry':'Generic vegetable (soybean) frying oil.','salt_table':'Table salt.',
'rice_white':'Yellow (turmeric) rice entry used; USDA has one generic yellow rice entry, and homemade rice varies.',
'tikka_sauce':'Branded entry (Kroger tikka masala sauce) used as a stand-in; sodium varies a lot by brand. Lacks potassium and magnesium data.',
'chicken_thigh':'Roasted thigh meat without skin; seasoning not included.','feta':'Generic feta cheese.',
'olive_ripe':'Canned ripe olives (brined, high in sodium) used as a stand-in for olives in general.',
'spinach_cooked':'Plain boiled spinach, no salt, used as a stand-in for cooked leafy greens.',
'spinach':'Raw spinach; cooked spinach has different values per gram (see the boiled entry).','onion':'Raw onion; cooking changes values per gram.',
'eggplant':'Boiled eggplant.','curry_powder':'Generic curry powder.','yogurt_lowfat':'Generic low-fat plain yogurt.','potato_baked':'Baked potato with skin, no salt.','fairlife_2':'Branded entry (Fairlife 2% ultra-filtered milk), label values per 100 mL.','chex_mix':'Branded entry (Chex Mix Traditional); calcium and potassium are rounded label zeros, and there is no magnesium data.','kale_raw':'Raw kale; cooked kale has different values per gram (see the boiled entry).','coconut_oil':'Coconut oil.','avocado':'Raw avocado, all commercial varieties (Hass-type California avocados are close).','potato':'Boiled potato, flesh only.'}
def sr(ids):
    ids=set(ids);foods={};nv={}
    for r in csv.DictReader(open(D+'/food.csv')):
        if int(r['fdc_id']) in ids: foods[int(r['fdc_id'])]=(r['description'],'SR Legacy')
    want={n[4] for n in NUTS}
    for r in csv.DictReader(open(D+'/food_nutrient.csv')):
        i=int(r['fdc_id'])
        if i in ids and int(r['nutrient_id']) in want and r['amount']!='': nv.setdefault(i,{})[int(r['nutrient_id'])]=float(r['amount'])
    return foods,nv
def branded(ids):
    cache='/workspace/fdc/branded.json'
    if not os.path.exists(cache):
        u='https://api.nal.usda.gov/fdc/v1/foods?format=full&api_key=DEMO_KEY&fdcIds='+','.join(map(str,ids))
        open(cache,'wb').write(urllib.request.urlopen(u,timeout=60).read())
    foods={};nv={}
    for f in json.load(open(cache)):
        i=f['fdcId'];d=f['description'];br=f.get('brandOwner') or f.get('brandName')
        foods[i]=(d+(f' ({br})' if br else ''),'Branded')
        nv[i]={fn['nutrient']['id']:fn['amount'] for fn in f['foodNutrients'] if 'amount' in fn}
    return foods,nv
nut=json.load(open('nutrition.json'))['foods']
items=[(k,v['fdc_id'],v['approx'],v.get('data_type')) for k,v in nut.items() if v.get('fdc_id')]
seen={}
out=[]
allsr=[i for k,i,a,t in items if t=='SR Legacy']+[i for k,i in EXTRA]
bi=[i for k,i,a,t in items if t=='Branded']
F1,N1=sr(allsr);F2,N2=branded(bi);FF={**F1,**F2};NN={**N1,**N2}
def add(k,i,approx,note,extra):
    assert i in FF,i
    nv=NN.get(i,{})
    out.append({'key':k,'fdc_id':i,'name':nut[k]['name'] if k in nut else FF[i][0],'usda_description':FF[i][0],'data_type':FF[i][1],
      'source':f'https://fdc.nal.usda.gov/food-details/{i}/nutrients','accessed':ACC,'proxy':bool(approx),'note':note,'extra':extra,
      'per100g':{n[0]:nv[n[4]] for n in NUTS if n[4] in nv}})
for k,i,a,t in items:
    add(k,i,a,PUB.get(k,''),False)
for k,i in EXTRA: add(k,i,False,'',True)
names={'sweet_potato_raw':'Sweet potato, raw','sweet_potato_baked':'Sweet potato, baked in skin','kale_raw':'Kale, raw','kale_boiled':'Kale, boiled','bok_choy_raw':'Bok choy, raw','bok_choy_boiled':'Bok choy, boiled','collards_raw':'Collards, raw','collards_boiled':'Collards, boiled','broccoli_raw':'Broccoli, raw'}
for o in out:
    if o['key'] in names: o['name']=names[o['key']]
json.dump({'accessed':ACC,'method':'SR Legacy: USDA FoodData Central public bulk CSV download (April 2018 SR Legacy release, https://fdc.nal.usda.gov/download-datasets). Branded: FDC API v1 (https://fdc.nal.usda.gov/api-guide). Values per 100 g. A nutrient missing from per100g means USDA reports no data.',
 'nutrients':[{'key':n[0],'label':n[1],'unit':n[2],'group':n[3],'fdc_nutrient_id':n[4]} for n in NUTS],'foods':out},open('foods_full.json','w'),indent=1)
print(len(out),'foods',len(NUTS),'nutrients')
