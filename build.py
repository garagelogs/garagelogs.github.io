#!/usr/bin/env python3
"""Minimal site updater: rebuild only index.html, articles.html, and sitemap.xml.

Does NOT touch existing article HTML pages — those retain their original
publication dates and metadata forever once written.  Only the new article
page is generated from draft HTML; old pages are left completely untouched."""
import os, re, html, datetime, json
import template as T

SITE = os.path.dirname(os.path.abspath(__file__))
ART_OUT = os.path.join(SITE, 'articles')
os.makedirs(ART_OUT, exist_ok=True)

# (filename-slug, H1 title, meta description, tag, excerpt)
ARTICLES = [
 ("used-car-red-flags","Used Car Red Flags: 11 Warning Signs of a Lemon",
  "Spot a bad used car before you buy. 11 red flags — from hidden bodywork and bad oil to title trouble — explained in plain English.",
  "Buying Guide","The 11 warning signs that separate a solid used car from an expensive mistake."),
 ("read-used-car-oil","How to Read a Used Car's Oil Like a Mechanic",
  "What engine oil tells you about a used car — and the counterintuitive reason brand-new oil can be a red flag.",
  "Inspection","Your dipstick is a confession. Here's how to read what the last owner won't tell you."),
 ("used-car-title-mistakes","Used Car Title Mistakes That Cost Buyers Thousands",
  "The paperwork — not the engine — is what bites many used-car buyers. Avoid the title and signing mistakes that cost weeks and thousands.",
  "Paperwork","The signing mistake that can void a title and leave you unable to drive the car you just paid for."),
 ("the-bike-he-waited-for","The Bike He Waited 12 Years For",
  "A story for anyone who's ever chased a dream machine — and the small, careful moment that made all the difference.",
  "Story","Twelve years of wanting. A few hours' drive. One careful look that changed everything."),
 ("saturday-in-the-driveway","Saturday in the Driveway",
  "Scraped knuckles, a stuck bolt, and the quiet pride of bringing an old car back to life. A story for anyone who wrenches.",
  "Story","Some of the best days happen with a wrench in your hand and the radio on."),
 ("used-car-test-drive-checklist","The 20-Minute Used Car Test Drive Checklist",
  "Most buyers waste the test drive. Here's how to use 20 minutes to catch hidden problems before you buy.",
  "Inspection","The test drive is your single best chance to catch a hidden problem. Don't waste it."),
 ("used-motorcycle-red-flags","Used Motorcycle Red Flags: 9 Warning Signs Before You Buy",
  "Nine red flags that reveal a crashed, neglected, or misrepresented used motorcycle — and what each one actually means for your wallet.",
  "Buying Guide","A bike wears its history in the open. Here's how to read it before you hand over any cash."),
 ("used-motorcycle-inspection-checklist","How to Inspect a Used Motorcycle: The 10-Step Pre-Purchase Checklist",
  "A step-by-step used motorcycle inspection checklist — fluids, frame, forks, suspension, electrics, and the test ride — so you know exactly what you're buying.",
  "Inspection","Most people who lose money on a used motorcycle do it in the first 20 minutes. Or rather, because they didn't spend 20 minutes looking."),
 ("used-car-transmission-check","Used Car Transmission Check: What to Feel, Hear, and Look For Before You Buy",
  "How to check a used car's transmission before buying — what slipping, hard shifts, and bad fluid actually mean, and when to walk away.",
  "Inspection","The transmission is one of the most expensive things that can go wrong. Here's how to check it before you hand over any money."),
 ("private-seller-vs-dealer-used-car","Private Seller vs. Dealer: Which Is the Better Deal on a Used Car?",
  "The real pros and cons of buying a used car from a private seller vs. a dealer — including the warranty trap, negotiation reality, and when each makes sense.",
  "Buying Guide","Both have advantages. Both have landmines. Here's how to decide which is right for your situation."),
 ("how-to-negotiate-used-car-price","How to Negotiate a Used Car Price Without Feeling Like a Pushover",
  "A practical guide to negotiating a used car price — how to research, use the inspection as leverage, and walk away without burning the deal.",
  "Buying Guide","Most people leave money on the table because they don't know what to say. Here's exactly how to handle it."),
 ("first-motorcycle-buying-guide","First Motorcycle: What New Riders Get Wrong When Buying Used",
  "The most common first motorcycle buying mistakes — too much bike, too much money, and ignoring the real cost of ownership. A straight-talk guide for new riders.",
  "Buying Guide","The biggest mistake new riders make isn't stalling it. It's buying the wrong bike in the first place."),
 ("used-car-vin-check","How to Run a Used Car VIN Check (And What It Won't Tell You)",
  "A plain-English guide to VIN checks — free vs. paid options, what title brands actually mean, and the critical caveat every buyer needs to know.",
  "Buying Guide","A clean history report does not mean a clean car. Here's what a VIN check actually tells you — and what it doesn't."),
 ("toyota-supra-mk4-legend","The Toyota Supra MK4: Why the Legend Never Died",
  "The history, cultural significance, and enduring legend of the fourth-generation Toyota Supra — the 2JZ, the movie, the myth, and what one costs today.",
  "Story","There are fast cars, and then there are cars that changed what people thought was possible."),

 ("used-car-brake-inspection","Used Car Brake Inspection: What to Listen For, Look For, and Feel Before You Buy",
  "A practical guide to checking used car brakes — pad thickness, rotor condition, pedal feel, brake fluid, and the warning signs most buyers miss.",
  "Inspection","Brakes are the most important safety system in any car. Here's how to check them before you hand over cash."),
]

DRAFT_MAP = {
 "used-car-red-flags":"01-red-flags.html",
 "read-used-car-oil":"02-read-oil.html",
 "used-car-title-mistakes":"03-title-mistakes.html",
 "the-bike-he-waited-for":"04-story-bike.html",
 "saturday-in-the-driveway":"05-story-driveway.html",
 "used-car-test-drive-checklist":"06-test-drive.html",
 "used-motorcycle-red-flags":"07-moto-red-flags.html",
 "used-motorcycle-inspection-checklist":"08-moto-inspection.html",
 "used-car-transmission-check":"09-used-car-transmission.html",
 "private-seller-vs-dealer-used-car":"10-private-vs-dealer.html",
 "how-to-negotiate-used-car-price":"11-negotiate-used-car.html",
 "first-motorcycle-buying-guide":"12-first-motorcycle.html",
 "used-car-vin-check":"13-used-car-vin-check.html",
 "toyota-supra-mk4-legend":"14-toyota-supra-mk4.html",
 "used-car-brake-inspection":"15-used-car-brake-inspection.html",
}

def clean_body(raw):
    raw = raw.strip()
    raw = re.sub(r'^```html\s*','',raw); raw = re.sub(r'```\s*$','',raw)
    raw = re.sub(r'(?is)<!DOCTYPE.*?>','',raw)
    raw = re.sub(r'(?is)</?html[^>]*>','',raw)
    raw = re.sub(r'(?is)<head>.*?</head>','',raw)
    raw = re.sub(r'(?is)</?body[^>]*>','',raw)
    raw = re.sub(r'(?is)<h1[^>]*>.*?</h1>','',raw,count=1)
    return raw.strip()

def build_single_article(slug, title, desc):
    """Generate only NEW article pages from draft HTML. Old pages are never overwritten."""
    if os.path.exists(os.path.join(ART_OUT, slug+".html")):
        return None  # already exists; preserve as-is
    body_raw = open(os.path.join(SITE,'drafts',DRAFT_MAP[slug])).read()
    body = clean_body(body_raw)
    canonical = f"{T.BASE_URL}/articles/{slug}.html"
    today = datetime.date.today().strftime("%B %d, %Y")
    if '</h2>' in body:
        body = body.replace('</h2>', '</h2>'+T.ad_unit("in-article"), 1)
    page = (T.head(title+" | GarageLogs", desc, canonical) + T.header() +
        f'<main><div class="wrap"><article>'
        f'<span class="posts"></span>'
        f'<h1>{html.escape(title)}</h1>'
        f'<div class="meta">{""} &middot; {today} &middot; GarageLogs</div>'
        f'{body}'
        f'{T.cta_block()}'
        f'{T.ad_unit("below-article")}'
        f'</article></div></main>' + T.footer())
    open(os.path.join(ART_OUT, slug+".html"),"w").write(page)
    return canonical

def build_index():
    cards = ""
    for slug,title,desc,tag,excerpt in ARTICLES:
        cards += (f'<li><span class="tag">{tag}</span>'
                  f'<a class="title" href="/articles/{slug}.html">{html.escape(title)}</a>'
                  f'<div class="ex">{html.escape(excerpt)}</div></li>')
    hero = (f'<div class="hero"><div class="wrap">'
            f'<h1>Buy your next used car or bike with confidence.</h1>'
            f'<p>{T.TAGLINE}. Honest guides, real-world stories, and a field-ready inspection kit.</p>'
            f'<a class="btn" href="{T.PRODUCT_URL}" target="_blank" rel="noopener">Get the Inspection Kit &rarr; $7</a> '
            f'<a class="btn ghost" href="/articles.html">Read the guides</a>'
            f'</div></div>')
    body = (T.head("GarageLogs — "+T.TAGLINE, "Honest used-car and motorcycle buying guides, gearhead stories, and a printable pre-purchase inspection & maintenance kit.", T.BASE_URL+"/index.html")
            + T.header() + hero +
            '<main><div class="wrap">' + T.ad_unit("top") +
            '<h2>Latest from the garage</h2><ul class="posts">' + cards + '</ul>' +
            T.cta_block() + '</div></main>' + T.footer())
    open(os.path.join(SITE,"index.html"),"w").write(body)

def build_articles_page():
    cards = ""
    for slug,title,desc,tag,excerpt in ARTICLES:
        cards += (f'<li><span class="tag">{tag}</span>'
                  f'<a class="title" href="/articles/{slug}.html">{html.escape(title)}</a>'
                  f'<div class="ex">{html.escape(excerpt)}</div></li>')
    body = (T.head("All Articles | GarageLogs","Browse all GarageLogs guides and stories on buying, inspecting, and maintaining used cars and motorcycles.",T.BASE_URL+"/articles.html")
            + T.header() +
            '<main><div class="wrap"><h1>Articles</h1>'
            '<p class="meta">Guides &amp; stories for smart used-vehicle buyers.</p>'
            + T.ad_unit("top") + '<ul class="posts">'+cards+'</ul>'
            + T.cta_block() + '</div></main>' + T.footer())
    open(os.path.join(SITE,"articles.html"),"w").write(body)

def build_sitemap(urls):
    today = datetime.date.today().isoformat()
    items = "".join(f"<url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in urls)
    xml = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>'
    open(os.path.join(SITE,"sitemap.xml"),"w").write(xml)
    open(os.path.join(SITE,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {T.BASE_URL}/sitemap.xml\n")

if __name__ == "__main__":
    urls = [T.BASE_URL+"/index.html", T.BASE_URL+"/articles.html"]
    new_canonicals = []
    for a in ARTICLES:
        c = build_single_article(*a[:3])  # slug, title, desc only
        if c:
            urls.append(c)
            new_canonicals.append(c)
    build_index()
    build_articles_page()
    build_sitemap(urls)
    print(f"BUILT index + articles page + sitemap + robots")
    if new_canonicals:
        print(f"NEW article pages generated: {new_canonicals}")
    else:
        print("All articles already built; only aggregation files updated.")
