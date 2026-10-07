"""Builds the Rose companion site (GitHub Pages: RoseCompanion/rose-companion). Run: python3 build.py"""
import html

BOT = "https://t.me/EveningCompany_bot"
UPDATED = "6 October 2026"
PRICES = [("20 extra messages", "0.99", "50"), ("Full chat for 24 hours", "2.49", "125"),
          ("Monthly companion", "14.99", "750"), ("VIP companion (30 days)", "49.99", "2500"),
          ("Private photo album (card or crypto)", "9.99", "-"), ("Special photo request (card or crypto)", "24.99", "-"), ("Close Friends, 30 days (card or crypto)", "2.99", "-")]
GALLERY = [("rose_48", "Red bikini days"), ("rose_55", "Turquoise water"), ("rose_47", "Coconut o'clock"),
           ("rose_52", "Sunbathing"), ("rose_43", "Pool float"), ("rose_37", "By the pool"), ("rose_45", "Sunset walks"), ("rose_42", "Beach reads")]


def page(path, title, desc, body):
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in
                  [("./", "Home"), ("terms.html", "Terms"), ("privacy.html", "Privacy"), ("refunds.html", "Refunds")])
    out = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://rosecompanion.github.io/s/rose_48.jpg">
<link rel="icon" href="img/hero.jpg"><link rel="stylesheet" href="style.css"></head>
<body><header class="top"><a class="brand" href="./"><img src="img/hero.jpg" alt="">Rose<span>AI companion</span></a>
<nav>{nav}</nav></header>
<main>{body}</main>
<footer><p>Rose is an AI companion by Evening Company. Not a real person. Adults 18+ only. Not therapy, medical, legal
or financial advice. If you're in crisis, please contact local emergency services or a helpline.</p>
<p><a href="terms.html">Terms</a> · <a href="privacy.html">Privacy</a> · <a href="refunds.html">Refunds</a> ·
<a href="{BOT}">Chat on Telegram</a> · Updated {UPDATED}</p></footer></body></html>
"""
    open(path, "w").write(out)


cta = f'<a class="btn" href="chat.html">Chat with Rose 🌹</a><p class="small">Right here in your browser, nothing to install. Prefer Telegram? <a href="{BOT}">Chat on Telegram</a>.</p>'
gallery = "".join(f'<figure><img src="s/{f}.jpg" alt="Illustration of Rose: {c}" loading="lazy"><figcaption>{c}</figcaption></figure>'
                  for f, c in GALLERY)
prices = "".join(f"<tr><td>{t}</td><td>${usd}</td><td>{stars + " ⭐" if stars != "-" else "-"}</td></tr>" for t, usd, stars in PRICES)

page("index.html", "Rose · AI companion for good conversation",
     "Rose is a warm, witty AI companion on Telegram. Good conversation any time of day. Adults 18+.", f"""
<section class="newoffers" aria-label="New from Rose"><span class="tag">New 💗</span>
<a href="chat.html#album"><img src="s/rose_48.jpg" alt=""><span><b>My private album</b> $9.99</span></a>
<a href="chat.html#request"><img src="s/rose_52.jpg" alt=""><span><b>Special request</b> $24.99 · a photo made just for you</span></a>
<a href="chat.html#close"><img src="s/rose_master.jpg" alt=""><span><b>Close Friends 💚</b> $2.99 · my cheekiest photos</span></a></section>
<section class="hero"><img src="img/main.jpg" alt="Illustrated portrait of Rose in a bikini, an AI companion">
<div><h1>Chat with Rose</h1>
<p class="lead">A warm, witty companion who's always up for a proper conversation, any time of day. Tell her about your
garden, the rugby, the old days or that trip you've been dreaming of. She listens, asks good questions and remembers
what matters to you ❤️</p>
<p class="ai">Rose is an AI companion · friendly, never explicit · 18+</p>
{cta}</div></section>

<section><h2>How it works</h2><ol class="steps">
<li><strong>Tap "Chat with Rose".</strong> The chat opens right here in your browser, on any phone or computer. (Rose is on Telegram too.)</li>
<li><strong>Confirm you're 18 or older</strong> and say hello. Your first 5 messages each day cost nothing.</li>
<li><strong>Want more time together?</strong> Choose a plan inside the chat and pay by card, Apple Pay or Google Pay (or Telegram Stars on Telegram).</li>
</ol></section>

<section><h2>Rose's beach diary</h2><p>Sun, salt water and a little mischief. The full set lives in her private
Rose Garden album. These pictures are AI-generated illustrations of her character.</p>
<div class="gallery">{gallery}</div></section>

<section><h2>Prices</h2><table class="prices"><thead><tr><th>Plan</th><th>By card</th><th>Telegram Stars</th></tr></thead>
<tbody><tr><td>5 messages every day</td><td>Free</td><td>Free</td></tr>{prices}</tbody></table>
<p class="small">Card payments are processed securely by Yoco, a South African payment provider, and charged in South
African rand at the day's exchange rate (shown before you pay); your bank converts it to your currency. Plans are
one-off payments, not subscriptions: nothing renews automatically. See <a href="refunds.html">refunds</a>.</p></section>

<section><h2>Questions</h2>
<details><summary>Is Rose a real person?</summary><p>No. Rose is an AI companion. The chat tells you this when you start,
and Rose will always say so if you ask.</p></details>
<details><summary>What can we talk about?</summary><p>Anything a good friend would chat about: your day, family, hobbies,
sport, travel, books, memories. Rose keeps things friendly and never explicit.</p></details>
<details><summary>Does Rose remember me?</summary><p>Yes. She keeps short notes from your conversations (like your
name and interests) so she can ask how things went. You can ask for your data to be deleted at any time.</p></details>
<details><summary>Will Rose ask me for money or personal details?</summary><p>Never. Rose won't ask for gifts, money, bank
details or your address. Payments only happen through the plan buttons in the chat.</p></details>
<details><summary>I'm going through a hard time.</summary><p>Rose will listen, but she isn't a counsellor. If you're in
crisis please contact a helpline (South Africa: SADAG 0800 456 789, UK: Samaritans 116 123, US: 988, Australia:
Lifeline 13 11 14) or your local emergency number.</p></details>
<details><summary>How do I get help with a payment?</summary><p>In the chat, send <code>/paysupport</code> and describe the
problem. We reply within 48 hours.</p></details></section>
<section class="end">{cta}</section>""")

page("terms.html", "Terms · Rose AI companion", "Terms of use for Rose, an AI companion on Telegram.", f"""
<article><h1>Terms of use</h1><p class="small">Last updated {UPDATED}</p>
<h2>1. The service</h2><p>Rose is an AI companion chat ("the service") operated by Evening Company and provided through
Telegram. Rose is software, not a person. Conversations are generated by an AI model and may sometimes be inaccurate.</p>
<h2>2. Who can use it</h2><p>You must be 18 or older. By confirming your age in the chat you agree to these terms.</p>
<h2>3. Acceptable use</h2><p>Be respectful. Explicit, abusive, illegal or harmful requests will not be answered, and we
may pause or end access for accounts that misuse the service. Rose never offers meetings, calls, photos or any service
outside the chat.</p>
<h2>4. Not professional advice</h2><p>Rose gives friendly, general conversation only. It is not therapy, medical, legal or
financial advice. In an emergency, contact local emergency services.</p>
<h2>5. Plans and payment</h2><p>5 messages a day are free. Paid plans unlock extra messages or unlimited chat for the
stated time (20 messages, 24 hours, or 30 days). Prices are shown in US dollars; card payments are processed by Yoco
and charged in South African rand at the exchange rate shown before you pay. Telegram Stars payments are processed by
Telegram. Plans are one-off purchases and do not renew automatically.</p>
<h2>6. Refunds</h2><p>See our <a href="refunds.html">refund policy</a>.</p>
<h2>7. Availability</h2><p>We aim to keep Rose available around the clock but can't guarantee uninterrupted service. If
an outage stops you using time you paid for, contact us for a refund or extension.</p>
<h2>8. Changes</h2><p>We may update these terms; the date above shows the latest version.</p>
<h2>9. Contact</h2><p>In the <a href="chat.html">website chat</a>, send a message starting with "Support:" (on Telegram, send <code>/paysupport</code>). We reply within 48 hours.</p></article>""")

page("privacy.html", "Privacy · Rose AI companion", "How Rose handles your data.", f"""
<article><h1>Privacy policy</h1><p class="small">Last updated {UPDATED}</p>
<h2>What we collect</h2><ul><li>Your Telegram user ID and first name (from Telegram).</li>
<li>Your messages with Rose and short notes Rose keeps to remember you (for example your name and interests).</li>
<li>Payment records: which plan, when, and the payment reference. We never see or store card numbers; Yoco and
Telegram handle card details.</li></ul>
<h2>How we use it</h2><p>Only to run the chat: to reply, remember context, apply your plan, and give support. We don't
sell your data or use it for advertising.</p>
<h2>Who processes it</h2><p>Messages are sent to our AI model provider (Anthropic) to generate replies. Payments are
processed by Yoco (cards) and Telegram (Stars). Conversations happen on Telegram, which has its own privacy policy.</p>
<h2>How long we keep it</h2><p>While you use Rose. You can ask for your data to be deleted at any time.</p>
<h2>Your choices</h2><p>To see or delete your data, send <code>/paysupport</code> in the <a href="{BOT}">Rose chat</a> and
start your message with "Privacy:". We'll act within 7 days.</p>
<h2>Safety</h2><p>Rose never asks for passwords, bank details, your address or money outside the plan buttons.</p></article>""")

page("refunds.html", "Refunds · Rose AI companion", "Refund policy for Rose plans.", f"""
<article><h1>Refund policy</h1><p class="small">Last updated {UPDATED}</p>
<p>We want you to be happy with your time with Rose.</p><ul>
<li><strong>Not what you expected?</strong> Ask within 7 days of buying a plan and we'll refund it in full.</li>
<li><strong>Charged twice, or the plan didn't unlock?</strong> We'll refund or fix it, whenever you notice.</li>
<li><strong>Service outage</strong> that stopped you using paid time: we'll refund or extend your plan.</li></ul>
<h2>How to ask</h2><p>Send <code>/paysupport</code> in the <a href="{BOT}">Rose chat</a>, then a message starting with
"Support:" saying which plan and roughly when you paid. We reply within 48 hours. Card refunds go back to the same
card through Yoco (allow 5 to 10 business days). Telegram Stars refunds are returned as Stars.</p>
<p>Plans never renew automatically, so there's nothing to cancel.</p></article>""")
print("built")
