# GarageLogs Article Plan

## ⚠️ ANTI-DUPE RULE
Before writing any new article: check the PUBLISHED ARTICLES list below.
Match on TOPIC/ANGLE, not just title. If the same buyer question is already answered, don't repeat it — extend it or pick a different angle.

---

## Published Articles

### Batch 1
1. `used-car-red-flags` — how-to: 11 warning signs of a lemon (exterior, oil, rust, dash lights, etc.)
2. `read-used-car-oil` — how-to: reading oil condition + why new oil can be a red flag
3. `used-car-title-mistakes` — how-to: title/paperwork errors at point of PURCHASE (signing, liens, open titles)
4. `the-bike-he-waited-for` — story: dream bike purchase, subtle late product hook
5. `saturday-in-the-driveway` — story: wrenching nostalgia, maintenance-log hook
6. `used-car-test-drive-checklist` — how-to: 20-minute test drive, what to feel/hear/notice

### Batch 2 (motorcycles)
7. `used-motorcycle-red-flags` — how-to: 9 red flags specific to used bikes (forks, chain, crash damage, etc.)
8. `used-motorcycle-inspection-checklist` — how-to: 10-step pre-visit motorcycle inspection

### Batch 3
9.  `used-car-transmission-check` — how-to: transmission inspection (fluid, feel, shifts, auto vs manual)
10. `private-seller-vs-dealer-used-car` — buying guide: pros/cons of each channel, CPO trap, negotiation reality
11. `how-to-negotiate-used-car-price` — buying guide: research, inspection-as-leverage, walkaway tactics
12. `first-motorcycle-buying-guide` — buying guide: new rider mistakes, engine size, starter bike mindset
13. `used-car-vin-check` — buying guide: VIN research BEFORE the visit (Carfax, NHTSA, title brands, odometer fraud)
14. `toyota-supra-mk4-legend` — passion: history of the A80 Supra, 2JZ legend, Fast & Furious impact

### Batch 4
15. `used-car-brake-inspection` — how-to: pad thickness, rotor condition, pedal feel, fluid check, warning signs most buyers miss

---

### Batch 5
16. `nissan-skyline-r34` — passion: history of the R34 Skyline GT-R, Godzilla lineage, RB26 legend, pop culture impact, what to look for and current pricing

## Article Types & Ratios (working guidelines, not fixed Robert percentages)
- **How-to / SEO** (~60% working mix): rank for search terms; teach WHAT/WHY, never give away the full kit
- **Story / gearhead narrative** (~25% working mix): immersive, emotional, seamless late product hook — NOT a sales pitch
- **Car/bike passion ("car porn")** (~15% working mix): enthusiast deep-dives on iconic vehicles — see rules below

Robert explicitly wanted passion/"car porn" pieces **at least about 1 out of 10 over the long run** and asked Wren whether going higher would be useful. Wren recommended somewhat more (roughly 2 in 10). The current ~60/~25/~15 split is therefore an **implementation balancing guideline**, not a fixed ratio Robert personally adopted. Adjust it when current traffic/editorial evidence or a later Robert instruction supports doing so, while preserving the explicit >= roughly 1-in-10 passion-piece floor unless Robert changes it.

### Car Porn Rules
- Pick a genuinely iconic, culturally significant car or motorcycle
- Focus: history, cultural significance, interesting/little-known facts, why gearheads love it
- CTA: reveal the product naturally at the very end, but **do not narrow the audience only to someone actually shopping for the featured dream car**. Robert explicitly corrected that narrower Wren suggestion. The preferred pattern should catch both the enthusiast/dreamer reading about the iconic vehicle and the person who is realistically shopping for an ordinary used car or daily driver — e.g. the approved Supra pattern: "Whether you're hunting for a pristine MK4 Supra or shopping for your next daily driver..." before the natural GarageLogs product bridge.
- Never feel like a sales pitch. The product reveal should feel like a helpful buddy-to-buddy progression from the story, not an ad.
- Good candidates: Toyota Supra MK4, Honda NSX, Dodge Viper, air-cooled Porsche 911, Honda CB750, Kawasaki Ninja ZX-series, Yamaha R1 gen 1, Ford GT40, etc.

---

## Rules (all articles)
- **Every new article must include at least one relevant photo.** This is Robert's explicit going-forward rule from 2026-06-05. Do not publish a new text-only article.
- Normal autonomous media preference: Pexels first for lifestyle/how-to shots; Wikimedia Commons when a specific vehicle/model image is more appropriate; Unsplash remains available only after re-reading `/workspace/unsplash-rules.md` and following its hotlink + attribution + download-location-trigger requirements. Re-read `/workspace/pexels-rules.md` before every Pexels use as Robert required.
- Pexels/Wikimedia/Unsplash photos must have meaningful alt text and visible source/photographer/license attribution as required by the source. Do not use a random copyrighted web image merely because it is relevant.
- Current restored OpenAI/provider credentials are capability-only and do not authorize paid image generation during the autonomous blog cron. Paid/generated media requires separate current authority.
- Before publishing a newly drafted article, run `python3 validate_article_media.py drafts/<new-draft>.html`; failure means skip/repair rather than publish.
- Articles teach WHAT/WHY. Never reproduce the full printable kit (that's the $7 product).
- Stories/passion pieces: plant a subtle hook early or mid-article, reveal product naturally at the end.
- Each ends with a tasteful CTA (auto-added by builder for how-tos; write custom closing line for stories/passion pieces).
- Target real search phrases in titles/headings.
