# Eaten vs absorbed: research notes (typical adult man 51+)
Compiled 2026-10-17. RESEARCH ONLY: not committed, not pushed, no site edits.
All figures are typical-adult population figures, not personal measurements. Where I could not find a sourced number, it says GAP.

## Summary table

| Nutrient | Headline figure | Range / variation (sourced) | Verdict |
|---|---|---|---|
| Calcium (already built) | NIH ODS, per-food % in mock | already in site | done |
| Potassium | ~85-90% absorbed | ~94% from potassium gluconate supplement, similar to potatoes (2016 trial) | **Show split** (sourced). Gap between bars is small (10-15%). |
| Sodium | ~98% absorbed | 96-98.5% across a huge intake range | **Don't show split** (eaten ≈ absorbed; a 2% sliver is invisible). Put "~98% absorbed" in tooltip text. |
| Magnesium | 30-40% of food Mg absorbed | Falls as dose rises (65% at 3 mEq/meal down to 11% at 80 mEq in one study); organic salts > oxide; older adults absorb less | **Show with caveat**: food 30-40% (sourced, shown as a range or 35% midpoint); supplement form has NO sourced % for healthy adults, so use the same 30-40% flagged as assumed. |
| Protein | Digestibility by food: animal ~90-99%, plant ~70-90% (varies a lot) | See per-food table below; DIAAS is quality, not amount | **Show with caveat**: "digestible protein" by food group, only where a sourced % exists; mark others as assumed. |
| Fiber | Not absorbed by definition; >half fermented in colon, rest excreted | cellulose 20-80% fermented, pectin 100%, wheat bran 50%, resistant starch 100% | **Don't show split.** "Absorbed" is meaningless. Optional tooltip: "about 2 kcal/g reaches you as fermentation products". |

## 1. Potassium
- Figure: "It is estimated that the body absorbs about 85%-90% of dietary potassium." Also "About 90% of ingested potassium is absorbed" (via passive diffusion, small intestine).
- Supplement form: "A 2016 dose-response trial found that humans absorb about 94% of potassium gluconate in supplements, and this absorption rate is similar to that of potassium from potatoes." Enteric-coated KCl tablets are absorbed more slowly than liquid (rate, not amount).
- Per-food: GAP. No per-food potassium percentages found; ODS gives one range for all foods. Use 85-90% (midpoint ~87.5%) for everything; potatoes ~94% (Macdonald-Clarke 2016, cited by ODS) is the only food-specific hint.
- Caveat: absorbed ≠ retained. Kidneys excrete the excess in healthy people.
- Source: NIH ODS, Potassium Health Professional Fact Sheet. https://ods.od.nih.gov/factsheets/Potassium-HealthProfessional/ . Updated June 2, 2022 (accessed 2026-10-17). Primary refs it cites: Stone, Martyn, Weaver, Nutrients 2016; Macdonald-Clarke et al., Am J Clin Nutr 2016;104:346-53; IOM DRI 2005.
- Verdict: **Show split.**

## 2. Sodium
- Figure: NASEM/IOM 2005 DRI (Water, Potassium, Sodium, Chloride, Sulfate): "Absorption of sodium and chloride occurs primarily in the small intestine and is approximately 98 percent across a wide intake range." https://www.nationalacademies.org/read/10925/chapter/8 (published 2005).
- EFSA Dietary Reference Values for sodium (EFSA Journal 2019;17(9):5778) https://doi.org/10.2903/j.efsa.2019.5778 , https://pmc.ncbi.nlm.nih.gov/articles/PMC7009309/ : 98.5% absorbed in four 7-day balance studies over a year (Holbrook 1984, mean intake 3.4 g/day); 97.8 ± 1.9% at 2.2-6.8 g/day (Kodama 2005); ~96% at 34.5 g/day (Luft 1979).
- NIH ODS has no sodium health-professional fact sheet (the URL returned 404 on 2026-10-17). The 2019 NASEM Sodium and Potassium DRI report (https://doi.org/10.17226/25353) did not show an absorption % in what I could read: GAP, so I cite the 2005 report and EFSA.
- Per-food variation: none sourced (GAP). Not expected to matter.
- Note: the kidney excretes nearly all absorbed sodium, so "absorbed" says little about what the body keeps.
- Verdict: **Don't show split**. Tooltip line "~98% absorbed (NASEM 2005, EFSA 2019)".

## 3. Magnesium
- Food figure: "In general, approximately 30% to 40% of the magnesium obtained from food and beverages is absorbed by the body." NIH ODS Magnesium Health Professional Fact Sheet, updated January 6, 2026. https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/ (accessed 2026-10-17). Primary refs cited: Fine et al. 1991; Rude (Encyclopedia of Dietary Supplements 2010).
- Dose dependence (Fine KD et al., J Clin Invest 1991;88:396-402, https://jci.org/articles/view/115317 ): standard meal (steak, cheese, rice) plus magnesium acetate; fractional absorption 65% at 3 mEq total, 30% at 13.3 mEq, 21% at 22.3 mEq, 15.4% at 42 mEq, 11.4% at 80.2 mEq. Almonds were as bioavailable as soluble magnesium acetate. Enteric-coated MgCl was much less absorbed. (Small study of normal subjects; this is the source of the ODS 30-40%.) 1 mEq Mg = 12.15 mg, so 200 mg ≈ 16.5 mEq. I did not interpolate a percentage for his dose.
- Age: ODS says "magnesium absorption from the gut decreases and renal magnesium excretion increases with age" (no number given: GAP).
- Supplement forms (ODS): "Forms of magnesium that dissolve well in liquid are more completely absorbed" and "aspartate, citrate, lactate, and chloride forms ... absorbed more completely and ... more bioavailable than magnesium oxide and magnesium sulfate." Glycinate is not listed by ODS.
- Glycinate/bisglycinate-specific evidence:
  - Ileal-resection trial, 1994 (author not confirmed) (PubMed 7815675, https://pubmed.ncbi.nlm.nih.gov/7815675/ ): 12 ileal-resection patients, 100 mg 26Mg-labelled diglycinate vs oxide: 23.5% vs 22.8% absorbed overall (no difference); 23.5% vs 11.8% in the 4 worst absorbers. Patients with surgery, not healthy adults, so NOT usable as his percentage.
  - Walker et al., Magnes Res 2003;16:183-91 (https://pubmed.ncbi.nlm.nih.gov/14596323/ ): 46 healthy adults, 300 mg/day for 60 days; citrate and amino-acid chelate showed greater absorption than oxide by 24-h urine Mg; citrate gave the highest serum Mg; oxide was no different from placebo. Indirect markers, no % absorbed.
  - Systematic review (authors not confirmed) of 14 studies, Nutrition 2021 (ScienceDirect PII S0899900721001568): organic forms more bioavailable than inorganic; % absorbed is dose dependent (falls as dose rises); all forms can maintain normal levels in healthy people. No fractional ranking of glycinate vs citrate.
- His supplement (supplements.json #4): Nature Made "Magnesium (Bisglycinate)", 2 capsules = 200 mg elemental Mg, taken in the evening. Form = bisglycinate (an amino-acid chelate).
- Gaps: no sourced fractional absorption for magnesium bisglycinate in healthy older men. No per-food Mg % (phytate/oxalate effects not quantified in the sources I read).
- Practical implication (supported by Fine 1991 and the 2021 review): a smaller dose is typically absorbed at a higher percentage, so 100 mg may absorb a larger fraction than 200 mg, but I have no sourced number for either. Don't state one.
- Verdict: **Show with caveat.** Use 30-40% for food (ODS). For the supplement, either (a) apply the same 30-40% labelled "assumed, form-specific data lacking" or (b) leave the supplement unsplit. I recommend (a) with the caveat in the tooltip.

## 4. Protein
Two different ideas: **digestibility** (how much protein/amino acid is absorbed) and **quality** (DIAAS/PDCAAS: does it contain enough of every essential amino acid). Only digestibility is "eaten vs absorbed". Do not multiply grams by DIAAS to get "absorbed grams"; the FAO 2013 report uses DIAAS for quality scoring and claims, not for absorbed grams.

- FAO Expert Consultation, "Dietary protein quality evaluation in human nutrition", FAO Food and Nutrition Paper 92, 2013. https://www.fao.org/4/i3124e/i3124e.pdf . Recommends DIAAS (true ileal digestibility of each indispensable amino acid, human data first, then pig, then rat) to replace PDCAAS. Its Table 6 examples (child 6 mo-3 y pattern): wheat DIAAS 40, peas 64, whole milk powder 122. Table 1 gives milk true ileal digestibility: Lys 0.95, SAA 0.94, Thr 0.90, Trp 0.90.
- FAO sub-committee collation (Gilani, Tomé, Moughan, Burlingame; 2011/2012, https://www.fao.org/ag/humannutrition/36216-04a2f02ec02eafd4f457dd2c9851b4c45.pdf ): true ileal N digestibility in healthy humans ranged 84-95% (stable-isotope studies); fish (Chinese) protein ileal digestibility 90-91% (column labelled for human application; data origin per table footnote unclear); kidney beans 73-74%; field beans (cooked) 73-77%; jack beans 58-61%; rat faecal crude protein digestibility: pea flour 88, lentil (autoclaved) 85, peanut 96, wheat 93, soyabean 90.
- Review table (Nutrients 2019;11(8):1825, https://pmc.ncbi.nlm.nih.gov/articles/PMC6723444/ ; compiles Hoffman & Falvo, ANSES, Rutherfurd, Sarwar): protein digestibility milk 96%, egg 98%, green lentil 84%, yellow split pea 88%, cooked pea 89%, cooked black bean 83%, chickpea 89%, roasted peanuts 98%, wheat 91%, white bread 93%, white rice 93%. DIAAS: milk 114, egg 113, green lentil 65, cooked pea 58, wheat 45 (Lys-limited). (Column layout in the web table is ambiguous for red meat; I did not use red-meat numbers from it.)
- True ileal digestibility used in a DIAAS spreadsheet (Nutrients 2019;11(12):3016, Table A2, https://pmc.ncbi.nlm.nih.gov/articles/PMC6950041/table/nutrients-11-03016-t0A2/ ; digestibility from Gilani 2011 and Evenepoel 1998): lysine/SAA/Thr/Trp: milk 0.91/0.93/0.92/0.93; egg 0.91 all; cheese 0.85-0.91; cooked beans 0.94/0.77/0.72/0.77; cooked peas 0.90/0.74/0.91/0.89; dry-roasted peanuts 0.84-0.96; sunflower seeds 0.77-0.81; wheat flour 0.80-0.88; popcorn 0.76-0.86; corn tortilla 0.76-0.86; baked potato 0.47-0.52; "meat (all animal flesh)" set to 1.00 (an assumption in that spreadsheet, not a measurement).
- Pig-based DIAAS: Herreman et al., Compr Rev Food Sci Food Saf 2020;19(6), https://pmc.ncbi.nlm.nih.gov/articles/PMC7590266/ : with the 0.5-3 y pattern, pork meat, casein, egg and potato protein average DIAAS above 100; wheat, pea, rice etc. are well below 75; ANFs (phytate, protease inhibitors) and cooking change values. Large variation within a food.
- Gaps: no human-measured digestibility found for chicken, cod/white fish (only "fish, Chinese" 90-91%), walnuts, pumpkin seeds, lentils (cooked, human), broccoli, cabbage, spinach, kefir/yogurt specifically (dairy given as milk/cheese). Cooking/processing effects are not quantified.
- Verdict: **Show with caveat.** Offer "digestible protein" using: dairy 91-96%, egg 91-98%, fish ~90%, legumes ~83-89% (lentil 84%), wheat/bread ~91-93%; flag everything else (poultry, nuts/seeds, vegetables) as assumed. The visual difference is modest (animal ~5-10% loss, plants ~10-20%). Show a range, not a single point. Note the supplement items (collagen, 11 g) are a hydrolysed collagen protein with very low DIAAS quality but no sourced digestibility: GAP.

## 5. Fiber
- By definition fibre is the part of carbohydrate not digested/absorbed in the small intestine, so "eaten vs absorbed" does not apply. What is sourced is how much is **fermented** in the colon.
- FAO/WHO, Carbohydrates in human nutrition (FAO Food and Nutrition Paper 66, 1998), "Physiological Effects of Dietary Fibre" https://www.fao.org/4/w8079e/w8079e0l.htm : "More than half of the usually consumed fibres are degraded in the large intestine, the rest being excreted in the stool." Fermentability: cellulose 20-80%, hemicelluloses 60-90%, pectin 100%, guar gum 100%, ispaghula 55%, wheat bran 50%, resistant starch 100%. Fermentation yields short-chain fatty acids (energy absorbed from them), gases and bacterial mass.
- Energy: FAO recommends ~2 kcal/g for carbohydrate reaching the colon (https://www.fao.org/4/W8079E/w8079e0c.htm); Livesey, Nutr Res Rev 1992 gives 2 kcal/g digestible, ~1.5 kcal/g net energy for mixed diets.
- Per-food fermented %: GAP (only per-fibre-type). USDA fibre numbers don't separate types in nutrition.json.
- Verdict: **Don't show split.** Reason: fibre's job is not to be absorbed; a "not absorbed" bar would look like a defect. Optional note: "mostly fermented by gut bacteria (more than half), rest leaves in stool; that's the point."

## 6. Which nutrition.json foods could get sourced percentages
nutrition.json has 43 foods; per-100 g values only, no absorption fields.
- **Potassium**: all foods can use 85-90% (ODS). Potato (potato) and potassium-gluconate-type supplements ~94%.
- **Sodium**: all foods ~98% (NASEM 2005).
- **Magnesium**: all foods 30-40% (ODS). Per-food: almonds ≈ acetate (Fine 1991) but almonds are not in the log; pumpkin_seeds (the big Mg source) have no sourced specific %, treat as the general range.
- **Protein**: 
  - milk_2, kefir, kefir_maplehill, skyr, siggis, melting_cheese, hot_cocoa, wf_pizza (dairy part): dairy 91-96% (milk 96% in Nutrients 2019; milk ileal 0.91-0.93; cheese 0.85-0.91).
  - egg_fried: 98% (Nutrients 2019) / ~0.91 ileal (Evenepoel 1998).
  - cod, tuna, sushi_roll (shrimp): fish ~90-91% (FAO sub-committee, "fish, Chinese" only; applies to cod/tuna loosely, flag).
  - lentils, wf_lentil_soup: 84% (green lentil, Nutrients 2019) with Lys 0.94-type bean values; sulfur amino acids lower.
  - bread, tortilla (wheat), croissant: wheat 91%, white bread 93%.
  - corn_tortilla_fried, popcorn: corn ileal 0.76-0.86 (amino-acid specific, not whole protein %).
  - potato: baked potato ileal 0.47-0.52 for amino acids (low) but protein content is tiny.
  - chicken_breast, duck_cooked, pork_shoulder, polish_sausage: only "meat" assumed ~100% in one spreadsheet (weak); red-meat table value ambiguous. Treat as GAP/assumed.
  - walnuts, pumpkin_seeds: no direct data; sunflower seeds 0.77-0.81 and peanuts 0.84-0.96 are the nearest. GAP.
  - vegetables (cabbage, spinach, broccoli, eggplant, tomato, onion etc.): GAP; protein contribution small.
- **Fiber**: none.
- Existing calcium percentages (milk 27%, spinach 5%, cabbage/broccoli 27%, default 25%) stay as built.
- Supplement items: collagen (protein), fish oil, magnesium, glucosamine's potassium/sodium: potassium and sodium amounts there are small; only Mg (200 mg) matters for the split.

## 7. Recommendation
1. Build splits for **potassium** (85-90%) and **magnesium** (30-40%, shown as a range with the caveat) first: both have an authoritative NIH ODS number, and magnesium is the one with a meaningful gap, which is what he cares about.
2. Add **protein** "digestible" split with per-food sourced %, falling back to a flagged default (e.g. 90%) where food data are missing; show ranges.
3. **Sodium**: no split, tooltip line only (~98%).
4. **Fiber**: no split; tooltip line about fermentation.
5. For the magnesium supplement: do not claim a bisglycinate-specific %. If he lowers to 100 mg, say fraction absorbed tends to rise at lower doses (Fine 1991; 2021 review) without a number.
6. Every tooltip should say "typical adult, estimate, not personal".

Caveats on my process: I read ODS Potassium and Magnesium fact sheets and the FAO PDFs directly; the NASEM 2005 sodium, EFSA, JCI/PubMed abstracts and the PMC tables came from search-result extracts (not full papers), and the authorship/journal for the Nutrients 2019 1825 table and the 2021 systematic review were not shown on the extracts, so they are cited by title/ID only. The 1994 ileal-resection trial and the 2021 systematic review are cited by PMID/PII only; confirm authors before publishing.
