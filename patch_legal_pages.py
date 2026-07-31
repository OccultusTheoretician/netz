#!/usr/bin/env python3
"""
patch_legal_pages.py - the un-sue-able pass, STANDALONE. From C:\\netz.
Default REPORTS; --apply writes. Idempotent. Never stages, never commits.
No site-wide notice campaign - legal pages + links only.

  A. Creates docs/terms.html and docs/privacy.html in the site shell:
     no-advice disclaimer (the forecasts touch securities), AS-IS / no
     warranty, corrections-printed-not-repaired policy stated as policy,
     nominative-use note for named third parties, allegation-attribution
     standard, governing law. Privacy states what the audit proves: static
     site, zero trackers, zero collection, host-level logs per GitHub/
     Cloudflare policies, Guest Kalls governed by GitHub's terms.
  B. Links them: appended to the notice line in netz.py (emitted pages) and
     the marks.html ipnotice block, plus index.html's footer - reachable
     from the front page, so the orphan check stays green.
  C. Sitemap entries for both.

  python patch_legal_pages.py            # report
  python patch_legal_pages.py --apply    # write
"""
import argparse
from pathlib import Path

SITE = "https://retroprescientaudit.com"
GEN_OLD = ("        \"<div class='byline'>NEBELKR\u00c4HE \u00b7 THE PRESCIENT DESK</div>\"\n"
           "        \"<div class='colophon'>Machine-collated open-source intelligence. Every synthesized \"")
GEN_NEW = ("        \"<div class='byline'>NEBELKR\u00c4HE \u00b7 THE PRESCIENT DESK</div>\"\n"
           "        \"<div class='legalline' style='font-size:.72rem;opacity:.7;margin:.2rem 0 .5rem'>"
           "<a href='terms.html'>Terms</a> \u00b7 <a href='privacy.html'>Privacy</a></div>\"\n"
           "        \"<div class='colophon'>Machine-collated open-source intelligence. Every synthesized \"")

SHELL_TOP = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} \u00b7 Nebelkr\u00e4he</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} &middot; The Prescient Desk">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{site}/og_nebelkraehe.png">
<meta property="og:url" content="{site}/{slug}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="crow_mark.svg">
<link rel="stylesheet" href="brand.css">
<link rel="canonical" href="{site}/{slug}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebPage","name":"{title}","description":"{desc}","url":"{site}/{slug}","isPartOf":{{"@type":"WebSite","name":"Retro-Prescient Audit","url":"{site}"}},"publisher":{{"@type":"Organization","name":"The Prescient Desk"}}}}</script>
<style>body{{max-width:46rem;margin:0 auto;padding:0 1.1rem 3rem}}
h1{{font-size:1.6rem;margin:1.6rem 0 .4rem}}h2{{font-size:1.05rem;margin:1.6rem 0 .3rem}}
p{{line-height:1.55;margin:.55rem 0}}.kicker{{color:#8a8a84;font:600 .68rem 'IBM Plex Mono',monospace;letter-spacing:.12em;text-transform:uppercase;margin-top:1.4rem}}
footer{{margin-top:2.5rem;padding-top:1rem;border-top:1px solid #26292f;font-size:.8rem;opacity:.8}}
body{{color:#c9c9c2}}h1{{color:#e8eaed}}strong{{color:#e8eaed}}a{{color:#dcb65e}}</style>
</head><body>
<div class="kicker">{kicker}</div>
<h1>{title}</h1>
"""

SHELL_BOT = """<footer>NEBELKR\u00c4HE \u00b7 THE PRESCIENT DESK \u2014 {footline}
<br>\u00a9 2026 Nebelkr\u00e4he \u00b7 <a href="https://github.com/OccultusTheoretician/netz/blob/main/LICENSE">LICENSE</a> \u00b7 <a href="terms.html">Terms</a> \u00b7 <a href="privacy.html">Privacy</a></footer>
</body></html>
"""

TERMS_BODY = """
<p><strong>Effective 2026-07-31.</strong> This site is a publication: an
open-source-intelligence desk, a self-scoring forecast ledger, and a family of
published verification standards with reference implementations. Using it
means these terms.</p>

<h2>Informational only \u2014 no advice</h2>
<p>Nothing here is investment, financial, trading, legal, tax, accounting,
medical, or any other professional advice, and nothing creates any advisory or
fiduciary relationship. Ledger entries that reference securities, commodities,
indices, rates, or any market are <strong>probabilistic records kept for
calibration scoring</strong> \u2014 they exist so this desk's accuracy can be
measured against its own misses, not so anyone acts on them. Do not trade on
them. Decisions you make from anything published here are yours alone.</p>

<h2>As is, no warranty</h2>
<p>Everything on this site \u2014 reports, forecasts, standards, code,
verifiers \u2014 is provided <strong>as is and as available</strong>, without
warranty of any kind, express or implied, including accuracy, completeness,
merchantability, fitness for a particular purpose, and non-infringement. To
the fullest extent permitted by law, the publisher is not liable for any
damages arising from use of, or reliance on, anything published here. Software
is additionally governed by its <a
href="https://github.com/OccultusTheoretician/netz/blob/main/LICENSE">LICENSE</a>,
whose warranty disclaimer controls for the instruments.</p>

<h2>Accuracy and corrections</h2>
<p>The desk's standing discipline: <strong>corrections are printed, never
silently substituted</strong>. Sealed ledger rows are never edited; errors are
resolved as misses or corrected by new entries that cite the old. Intelligence
reports grade their sources mechanically and print what the method rejected.
If something is wrong, the record will say so on its face \u2014 that is the
product. Report errors to audit@retroprescientaudit.com.</p>

<h2>Third parties, names, and allegations</h2>
<p>Reports and forecasts reference real people, companies, and institutions by
name because open-source intelligence is about the world. Such references are
nominative: trademarks belong to their owners and no affiliation or endorsement
is implied. Where an item concerns an allegation, the desk reports <strong>the
existence and sourcing of the allegation</strong>, attributed to the cited
reporting \u2014 not its truth. Forecast resolution criteria adjudicate what
public reporting states by a deadline, not underlying facts.</p>

<h2>Intellectual property</h2>
<p>\u00a9 2026 Nebelkr\u00e4he. The repository <a
href="https://github.com/OccultusTheoretician/netz/blob/main/LICENSE">LICENSE</a>
governs reuse: the standards are citable and conformable but not forkable
under their names; the instruments are free to run. Marks are listed on the
<a href="marks.html">marks page</a>.</p>

<h2>Housekeeping</h2>
<p>External links are provided for sourcing; their content is theirs. These
terms may be revised; revisions are dated and the old text remains in the
repository history \u2014 the same rule as everything else here. Governing law:
Utah, United States, without regard to conflicts rules. If any provision is
unenforceable, the rest stand. Contact: audit@retroprescientaudit.com.</p>
"""

PRIVACY_BODY = """
<p><strong>Effective 2026-07-31.</strong> The honest version is short because
the architecture is the policy.</p>

<h2>What this site collects: nothing</h2>
<p>This is a static site. <strong>No cookies. No analytics. No trackers. No
accounts. No forms.</strong> No third-party stylesheet, script, or font loads
from anywhere \u2014 a claim the desk's own published site audit checks by
enumeration on every ship, not by assertion. The browser verifiers on this
site make <strong>no network requests</strong>: anything you paste into them
stays on your machine.</p>

<h2>What the infrastructure sees</h2>
<p>The site is served by GitHub Pages behind Cloudflare. Like every web host,
they receive standard access data (IP address, user agent, requested URL) and
handle it under their own policies: <a
href="https://docs.github.com/en/site-policy/privacy-policies">GitHub</a> \u00b7
<a href="https://www.cloudflare.com/privacypolicy/">Cloudflare</a>. This desk
receives no analytics from either and keeps no visitor logs of its own.</p>

<h2>What you choose to send</h2>
<p>Email to audit@retroprescientaudit.com is used to respond and for the
desk's correspondence records, and is never sold or shared for marketing.
Guest Kall submissions are made as <strong>public GitHub issues</strong> in a
public repository: they are public by design, permanent by design, and
governed by GitHub's terms. Submit accordingly.</p>

<h2>Children</h2>
<p>This site is not directed to children and collects nothing from anyone,
children included.</p>

<h2>Changes</h2>
<p>Revisions are dated; prior text persists in repository history. Questions:
audit@retroprescientaudit.com.</p>
"""

SITEMAP_BLOCK = ("  <url>\n    <loc>{site}/{slug}</loc>\n"
                 "    <lastmod>2026-07-31</lastmod>\n"
                 "    <changefreq>yearly</changefreq>\n"
                 "    <priority>0.3</priority>\n  </url>\n")


def make_page(slug, title, kicker, desc, body, footline):
    return (SHELL_TOP.format(site=SITE, slug=slug, title=title, kicker=kicker,
                             desc=desc)
            + body + SHELL_BOT.format(footline=footline))


def run(apply):
    print(("APPLYING" if apply else "PROPOSED (nothing written)") + "\n" + "-" * 56)
    res = []
    pages = [
        ("terms.html", "Terms of Use",
         "the desk \u00b7 legal", 
         "Terms for an OSINT publication and self-scoring forecast ledger: informational only, no advice, as-is, corrections printed not repaired.",
         TERMS_BODY, "read the record; decide for yourself."),
        ("privacy.html", "Privacy",
         "the desk \u00b7 legal",
         "A static site that collects nothing: no cookies, no analytics, no trackers \u2014 checked by enumeration on every ship.",
         PRIVACY_BODY, "the architecture is the policy."),
    ]
    for slug, title, kicker, desc, body, footline in pages:
        p = Path("docs") / slug
        if p.exists():
            res.append(f"ALREADY DONE  docs/{slug}")
            continue
        if apply:
            p.write_text(make_page(slug, title, kicker, desc, body, footline),
                         encoding="utf-8")
        res.append(f"{'CREATED' if apply else 'WILL CREATE':13s} docs/{slug}")

    gp = Path("netz.py")
    gt = gp.read_text(encoding="utf-8")
    if "legalline" in gt:
        res.append("ALREADY DONE  netz.py: footer legal links")
    elif gt.count(GEN_OLD) == 1:
        if apply:
            gp.write_text(gt.replace(GEN_OLD, GEN_NEW, 1), encoding="utf-8")
        res.append(f"{'EDITED' if apply else 'WILL EDIT':13s} netz.py: footer legal links (emitted pages)")
    else:
        res.append(f"MISSING STR   netz.py byline/colophon anchor ({gt.count(GEN_OLD)}x)")

    mp = Path("docs/marks.html")
    mt = mp.read_text(encoding="utf-8")
    if "terms.html" in mt:
        res.append("ALREADY DONE  marks.html links")
    elif "<footer" in mt:
        if apply:
            mp.write_text(mt.replace("<footer",
                "<div style='font-size:.8rem;opacity:.75;margin:1.2rem 0'>"
                "<a href='terms.html'>Terms</a> \u00b7 "
                "<a href='privacy.html'>Privacy</a></div>\n<footer", 1),
                encoding="utf-8")
        res.append(f"{'EDITED' if apply else 'WILL EDIT':13s} marks.html: legal links above footer")
    else:
        res.append("MISSING STR   marks.html: no <footer")

    # index footer link
    ip = Path("docs/index.html")
    it = ip.read_text(encoding="utf-8")
    if "terms.html" in it:
        res.append("ALREADY DONE  index.html footer")
    elif "<footer>" in it:
        if apply:
            ip.write_text(it.replace(
                "<footer>",
                "<footer><div style='font-size:.78rem;opacity:.75;margin-bottom:.5rem'>"
                "<a href='terms.html'>Terms</a> \u00b7 "
                "<a href='privacy.html'>Privacy</a> \u00b7 "
                "<a href='marks.html'>Marks</a></div>", 1), encoding="utf-8")
        res.append(f"{'EDITED' if apply else 'WILL EDIT':13s} index.html: footer legal line")
    else:
        res.append("MISSING STR   index.html: no <footer>")

    # sitemap
    sp = Path("docs/sitemap.xml")
    st = sp.read_text(encoding="utf-8")
    if "terms.html" in st:
        res.append("ALREADY DONE  sitemap")
    else:
        blocks = (SITEMAP_BLOCK.format(site=SITE, slug="terms.html")
                  + SITEMAP_BLOCK.format(site=SITE, slug="privacy.html"))
        idx = st.find("  <url>")
        if idx == -1:
            res.append("MISSING STR   sitemap: no <url> anchor")
        else:
            if apply:
                sp.write_text(st[:idx] + blocks + st[idx:], encoding="utf-8")
            res.append(f"{'EDITED' if apply else 'WILL EDIT':13s} sitemap: + terms, privacy")

    for line in res:
        print(line)
    print()
    if apply:
        print("Done. navgen stamps the nav onto both new pages at next ship.")
        print("Stage by name, ship, re-run site_audit.py.")
    else:
        print("Apply with: python patch_legal_pages.py --apply")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    run(ap.parse_args().apply)
