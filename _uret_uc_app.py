"""
Uc yeni app icin gizlilik ve destek sayfalarini uretir.

Metinler KODA BAKILARAK yazildi, sablondan kopyalanmadi:
- gravurgunu  : gorseller uzak sunucudan geliyor -> AG ISTEGI VAR, beyan edildi
- 72 Hours    : liste pakete gomulu, yalnizca kullanici link acinca ag
- Fee Finder  : hicbir ag cagrisi yok; defter alintisi 24+24/120 karakterle
                sinirli ve kisisel tanimlayicilar MASKELENIYOR (lib/engine/gizlilik.ts)
"""
import os
import io

TARIH = "7 August 2026"

SAYFA = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tur} - {ad}</title>
<meta name="description" content="{ozet}">
<link rel="stylesheet" href="../styles.css">
</head>
<body>
<header class="site-header">
  <a href="../index.html" class="back-link">&larr; All Apps</a>
</header>
<main>
  <span class="badge">{rozet}</span>
  <h1>{ad}</h1>
  <p class="meta">Effective: {tarih}</p>
{govde}
</main>
</body>
</html>
"""

GRAVUR_GIZLILIK = """
  <p>Gravur Gunu shows one antique engraving a day. There is no account, no sign-in
    and no analytics.</p>

  <h2>What leaves your device</h2>
  <p>Two things, and only these:</p>
  <ul>
    <li><strong>Engraving images.</strong> The catalogue text ships inside the app, but
      the pictures are downloaded from an image host as you view them. That request
      carries what any web request carries &mdash; your IP address and the image being
      requested. It carries no identifier of you, because the app has none.</li>
    <li><strong>Links you tap.</strong> If you open a source link, your browser goes to
      that website. What happens next is between you and that site.</li>
  </ul>
  <p>There is nothing else. No usage reporting, no crash reporting, no advertising
    identifier, no third-party analytics SDK.</p>

  <h2>What stays on your device</h2>
  <p>Which engravings you have seen and which you have saved are written to the
    device's own storage under a single key and stay there. Deleting the app deletes
    them. There is no copy anywhere else, so there is nothing for us to export or
    delete on request &mdash; we never had it.</p>

  <h2>Children</h2>
  <p>The app collects nothing from anyone, of any age.</p>

  <h2>Contact</h2>
  <p><a href="mailto:gurbuzer1@gmail.com">gurbuzer1@gmail.com</a></p>
"""

GRAVUR_DESTEK = """
  <h2>What the app does</h2>
  <p>One antique engraving each day &mdash; the picture, its title, its date, its
    category and whatever else is genuinely recorded about it. Past days stay in the
    archive.</p>

  <h2>Why some fields say &ldquo;unknown&rdquo;</h2>
  <p>The catalogue is a real archive, not a generated one, and real archives have gaps.
    The engraver is recorded for about 59% of pieces and the painter for about 56%.
    Where a field is missing the app says so instead of guessing. That is deliberate.</p>

  <h2>The picture will not load</h2>
  <p>Images are downloaded as you view them, so they need a connection. Without one the
    app still opens and still shows the day's title, date and details &mdash; only the
    picture is missing, and it will appear when you are back online.</p>

  <h2>Contact</h2>
  <p><a href="mailto:gurbuzer1@gmail.com">gurbuzer1@gmail.com</a></p>
"""

SAAT_GIZLILIK = """
  <p>72 Hours is a checklist for the first days after someone close to you goes into
    hospital. There is no account, no sign-in, no analytics and no server.</p>

  <h2>What leaves your device</h2>
  <p><strong>Nothing the app sends.</strong> The whole checklist ships inside the app and
    works with no connection at all. The only time anything goes out is when
    <em>you</em> tap a source link &mdash; then your browser opens that page on GOV.UK,
    the NHS, Carers UK or Age UK. The app tells no one that you tapped it.</p>

  <h2>What stays on your device</h2>
  <p>Which items you have ticked, when you started, and how many times you have opened
    the app. These are written to the device's own storage under a single key. Deleting
    the app deletes them. We never receive them, so there is nothing for us to hand over
    or erase.</p>

  <h2>A health-adjacent app that stores no health data</h2>
  <p>The app never asks who is ill, what they have, or anything about them. It does not
    ask for your name. A ticked box is a ticked box.</p>

  <h2>Contact</h2>
  <p><a href="mailto:gurbuzer1@gmail.com">gurbuzer1@gmail.com</a></p>
"""

SAAT_DESTEK = """
  <h2>What the app does</h2>
  <p>It lists what to do, in the order it needs doing, across three windows: the first
    72 hours, the first week, and the first month. Every item says why it matters now,
    how to do it, and what is lost if it is skipped.</p>

  <h2>Every item links to its source</h2>
  <p>Each item carries a link to the official page it came from &mdash; GOV.UK, the NHS,
    Carers UK or Age UK. If the app and the source ever disagree, the source is right.
    Tell us and we will fix the app.</p>

  <h2>What the app deliberately does not do</h2>
  <ul>
    <li><strong>It gives no medical or legal advice.</strong> It tells you which official
      process exists and where to start it. Nothing more.</li>
    <li><strong>It states no amounts, thresholds or rates.</strong> Those change every
      year, and a stale number in an app is worse than no number. It points you at the
      page that carries the current figure.</li>
  </ul>

  <h2>Scope</h2>
  <p>The United Kingdom. Social care rules differ between the nations, so each item
    carries a region note taken from what its own source page says.</p>

  <h2>Contact</h2>
  <p><a href="mailto:gurbuzer1@gmail.com">gurbuzer1@gmail.com</a></p>
"""

FEE_GIZLILIK = """
  <p>Fee Finder reads a bill you paste in and points out charges worth questioning.
    It has no account, no server, and <strong>no network code at all</strong>.</p>

  <h2>What leaves your device</h2>
  <p><strong>Nothing.</strong> Not the bill, not the findings, not a count of how often
    you used it. The app makes no network requests of any kind, so your bill physically
    cannot reach us or anyone else. It is not that we promise not to look &mdash; there
    is no channel to look through.</p>

  <h2>The optional history, and what it stores</h2>
  <p>You can keep a record of past checks. It is written to the device's own storage and
    goes nowhere. Two rules apply to it, and both are enforced in code and covered by
    tests:</p>
  <ul>
    <li><strong>Only a short excerpt is kept</strong> &mdash; at most 24 characters
      either side of the matched phrase, and never more than 120 characters in total.
      An earlier version kept a wider window, which meant a short bill could be stored
      almost in full. That was fixed.</li>
    <li><strong>Personal identifiers in that excerpt are masked</strong> &mdash; email
      addresses, sort codes, postcodes, long digit sequences, names and addresses are
      replaced, not hidden. The replacement is not reversible.</li>
  </ul>
  <p>Deleting the app deletes the history.</p>

  <h2>Contact</h2>
  <p><a href="mailto:gurbuzer1@gmail.com">gurbuzer1@gmail.com</a></p>
"""

FEE_DESTEK = """
  <h2>What the app does</h2>
  <p>Paste the text of a bill. The app matches it against a catalogue of documented UK
    charge patterns &mdash; telecoms, energy and banking &mdash; and shows you what it
    found, with the regulator's own page as the source.</p>

  <h2>It is not a lawyer and does not pretend to be</h2>
  <p>The app never says &ldquo;you can claim this back&rdquo;. It says which regulator's
    rule exists and suggests comparing it with your own contract. It states no amounts
    or rates, because those vary by provider and by year.</p>

  <h2>Two kinds of finding, shown differently</h2>
  <p>Findings backed by a regulator's published page are shown normally. Practices that
    are common but that we could not source are shown separately and more faintly, and
    labelled as a suggestion to check rather than a claim. The distinction is
    deliberate; do not read the second kind as the first.</p>

  <h2>Nothing found</h2>
  <p>An empty result is not a clean bill of health &mdash; it means none of the
    catalogue's patterns appeared in the text you pasted. The app offers a short list of
    things worth checking by hand.</p>

  <h2>Contact</h2>
  <p><a href="mailto:gurbuzer1@gmail.com">gurbuzer1@gmail.com</a></p>
"""

APPS = {
    "gravurgunu": ("Gravur Gunu",
                   "Gravur Gunu privacy policy - no account, no analytics, no tracking. Images are fetched from a read-only image host.",
                   GRAVUR_GIZLILIK, GRAVUR_DESTEK),
    "seventytwohours": ("72 Hours",
                        "72 Hours privacy policy - no account, no analytics, no server. The checklist ships inside the app and your progress never leaves the device.",
                        SAAT_GIZLILIK, SAAT_DESTEK),
    "feefinder": ("Fee Finder",
                  "Fee Finder privacy policy - your bill never leaves the device. The app makes no network requests of any kind.",
                  FEE_GIZLILIK, FEE_DESTEK),
}

if __name__ == "__main__":
    kok = os.path.dirname(os.path.abspath(__file__))
    for slug, (ad, ozet, gizlilik, destek) in APPS.items():
        os.makedirs(os.path.join(kok, slug), exist_ok=True)
        for dosya, tur, rozet, govde in (
            ("privacy.html", "Privacy Policy", "PRIVACY POLICY", gizlilik),
            ("support.html", "Support", "SUPPORT", destek),
        ):
            yol = os.path.join(kok, slug, dosya)
            io.open(yol, "w", encoding="utf-8").write(
                SAYFA.format(tur=tur, ad=ad, ozet=ozet, rozet=rozet, tarih=TARIH, govde=govde))
            print(f"  {slug}/{dosya}  ({os.path.getsize(yol)} bayt)")
