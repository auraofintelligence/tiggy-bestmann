"""Build Tiggy's ten-page local character site using the Python standard library."""
from pathlib import Path
from html import escape
import os

ROOT = Path(__file__).resolve().parents[1]
SIRE_URL = os.environ.get('SIRE_PARTNER_URL', 'http://127.0.0.1:4173/')
VERSION = '20260929-4'

PAGES = [
    dict(slug='index', title='Tiggy Bestmann', intro='Artist. Traveller. Happy-go-lucky fool. A taste for a little mischief.', image='opening-world', alt='Two adult women, one visibly pregnant, welcome the long-haired Tiggy at an Istanbul ferry landing and draw him into a lively conversation.', caption='An invitation on the Bosphorus. Imagined Istanbul encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy has finished the presentation. She has booked a table on the other side of the city. Her friend knows the band. Nobody has told him about the dancing yet.</p>
<p>He has three days here. They intend to make good use of the evening.</p>
<h2>Between the work and the evening</h2>
<p>Long hair, glasses, an artist’s eye and a grin that tends to arrive just before the cheeky comment. Tiggy likes women who speak their minds, places that wake up after dark and invitations that require a quick change of clothes.</p>
<p>He can spend the morning building a festival installation, the afternoon playing in the surf and the evening quite comfortably out of his depth at a splendid dinner. He enjoys having something to learn. Especially when his teacher is enjoying herself too.</p>
<h2>Three days in town</h2>
<p>His travels have a purpose and a pace. There are projects to deliver, workshops to run and people expecting him. He gets involved, puts in the effort and makes room for pleasure while he is there.</p>
<p>An outback festival needs a pair of hands. A Goa retreat needs an artist. A Nairobi reception leads to a private invitation. Somewhere between the work and the next departure, a woman decides he should see her part of the world.</p>
<p>Her interest is clear. So is his smile.</p>
<h2>The pleasure of being invited</h2>
<p>He wants every country and territory, and more than a glimpse of each. There are things he wants to share, people he wants to learn from and places he wants to return to because of someone he met there.</p>
<p>The route stays open. So does his romantic life. A festival friendship can become a travelling companion; a flirtation can introduce him to a whole circle of people with an expansive idea of love.</p>
<p class="big-line">“We were hoping you’d join us.”<br>His evening has just improved.</p>'''),
    dict(slug='fool', title='The happy-go-lucky fool', intro='He can take a joke. He can usually improve it.', image='fool-outback', alt='Tiggy and two adult event crew members laugh while moving a drooping giant bird prop at an Australian outback arts gathering.', caption='A small setback in a very large idea. Imagined outback gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">She tells Tiggy the dress code is “something memorable”. He asks how memorable. Her smile suggests he should have asked earlier.</p>
<p>He likes people who can play. A little teasing, a ridiculous challenge, an invitation delivered with a perfectly straight face. He is quite capable of joining in without needing to run the show.</p>
<h2>There is nerve beneath the grin</h2>
<p>The fool is an artist willing to put an unusual idea in front of people. He will perform the song, wear the outfit, try the dance and ask the question everybody else is politely avoiding.</p>
<p>He knows a joke can open a room. He also knows when to stop talking and enjoy what someone else brings to it.</p>
<h2>Mischief likes company</h2>
<p>At an outback arts gathering, he helps a crew bring a giant kinetic bird to life. One of the women gives it an extravagant bow. He returns the bow to the bird. By the time the audience arrives, they have accidentally invented the opening performance.</p>
<p>That is his sort of fun: a shared idea that gets better because people keep adding to it. The work still gets done. It simply develops a personality.</p>
<p>He brings that same spirit to romance. He enjoys a woman who can surprise him, invite him closer and leave him smiling at something she said long after she has left the room.</p>
<p class="big-line">Her expression gives her away.<br>He starts laughing before she says it.</p>'''),
    dict(slug='art', title='The night it comes alive', intro='The last light comes on. Across the room, she catches his eye.', image='artist', alt='Tiggy and an adult artist assemble a colourful kinetic sculpture in a sunny workshop.', caption='One more piece. Then they will see what moves. GenAI story concept.', colour='blue', body='''
<p class="lead">At six, it is still a pile of parts. At eight, strangers are queuing to get inside.</p>
<p>Tiggy is under the frame with a light between his teeth. His collaborator is above him, testing a sequence that turns the whole structure blue. They have been refining those seven seconds of darkness all afternoon.</p>
<p>Then it works. They look at each other before they look at the thing they have made.</p>
<h2>When the doors open</h2>
<p>His art has movement, noise and somewhere for people to stand. A sculpture catches the wind. A film fills an outdoor screen. A room answers the people inside it. He wants the moment when someone stops walking, forgets their phone and comes closer.</p>
<p>The work takes him into studios, festival yards and temporary crews around the world. There is always something he can bring, something he has to learn and someone whose way of seeing makes his own work less predictable.</p>
<h2>The people who made it</h2>
<p>The first visitors stop beneath the moving lights. Across the room, his collaborator catches his eye. Between them are the experiments, the discoveries and the moment they knew it was going to work. Tiggy likes that intimacy of making something together.</p>
<p>When she asks him to stay for the next project, she mentions that her studio has a spare room. Then she tells him about the festival they could go to afterwards.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/world-builder.html">World Builder</a> takes that ambition further: entire imagined places to make, inhabit and bring to life. He wants to see what happens when the visitors start changing the story.</p>'''),
    dict(slug='retreats', title='Aura retreats', intro='Five days of bright ideas, close company and very good reasons to stay for dinner.', image='retreat', alt='A visibly pregnant adult woman demonstrates a playful light sculpture to Tiggy and another participant at an imagined coastal Aura retreat in Goa.', caption='Something to learn. Someone worth listening to. Imagined Goa retreat. GenAI artwork.', colour='mint', body='''
<p class="lead">She turns the light sculpture in her hands. Colour travels across the table and up Tiggy’s sleeve. “Want a go?” she asks.</p>
<p>Outside, the palms are moving and the sea is close enough to hear. Inside, an Aura retreat has brought together people who want to make things, explore ideas and get to know one another while they do it.</p>
<h2>Curiosity looks good on him</h2>
<p>Tiggy arrives with skills to share and an appetite for what everyone else knows. They build avatars, explore memory palaces, try extended reality and turn an idea into something they can hold.</p>
<p>The woman leading this demonstration is pregnant, quick-witted and clearly enjoying his questions. By lunch they have a new experiment in mind. By dinner the conversation has travelled well beyond it.</p>
<h2>The company continues</h2>
<p>There is music to hear, food to share and a dance he would like to learn from the woman offering to teach him. Repeated company has its pleasures: familiar faces at breakfast, a joke that carries through the day, someone finding him when the group heads out.</p>
<p>Luke’s Aura proposal gives these fictional scenes a five-day retreat and a nine-day teacher-training format, with coastal Goa among the possible settings. Tiggy gets to be an artist, a student and someone with a useful thing to pass on.</p>
<p>By the end of the week, their next experiment already has a place and a date. Neither seems in much of a hurry to say goodnight.</p>'''),
    dict(slug='out-about', title='Three days in town', intro='A good reason to travel. A woman with local knowledge. A few days worth filling.', image='out-about-world', alt='Two adult Thai women invite Tiggy to an evening gathering beside a Bangkok canal and an arriving passenger boat.', caption='The boat is coming. The evening is open. Imagined Bangkok encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Bangkok. The boat is coming, the workshop is finished and she says there is time.</p>
<p>He has finished the workshop, sent the file and changed his shirt in a room barely wider than the bed. Now she is holding up two tickets. Her friend is already waving to the boat.</p>
<p>He can ask the rest on the way.</p>
<h2>The reason he came</h2>
<p>A residency, a research visit, a paid pilot or a presentation gives Tiggy a reason to land. He has people expecting him and something to deliver. The <a href="https://auraofintelligence.github.io/global-founder-atlas/">Global Founder Atlas</a> belongs behind those journeys, connecting projects with places that might welcome them.</p>
<p>He travels quickly, but he wants more than a photograph proving he was there. Work gets him into a room. Curiosity keeps him in the conversation. Someone who lives there can turn the few hours left into the part he remembers.</p>
<h2>Tomorrow is taking shape</h2>
<p>A festival tonight. A woman he wants to see again tomorrow. A new project in another city on Monday. His opportunity oracle can bring the options together; he chooses which one to follow.</p>
<p>He wants every country and territory, with room to meet, share, learn and teach. There is no fixed route through that ambition. Relationships, useful work and the next extraordinary experience keep redrawing it.</p>
<p>Fast travel, full days and people he wants to spend those days with. The next chapter might begin before he reaches the airport.</p>'''),
    dict(slug='water', title='Sand, salt and screen', intro='The match runs into the afternoon. The afternoon becomes an evening together.', image='water', alt='Tiggy and two adult women laugh in shallow turquoise seawater with their bodyboards after a small wave.', caption='Back in the water. GenAI story concept.', colour='mint', body='''
<p class="lead">She wants Tiggy on her volleyball team. Apparently she likes his reach. The grin she exchanges with her friend suggests there may be another reason.</p>
<p>He is enjoying both possibilities.</p>
<h2>Before sunset</h2>
<p>There is a match on the sand, a decent swell and a screening to help set up before sunset. Tiggy has a board, a job to do and enough time for a thoroughly satisfying day.</p>
<p>Bodyboarding gives him speed, timing and the pleasure of being completely absorbed in the next wave. The Ocean Master in his story world has skills he wants to learn. He likes that there is always a better line to take, and someone worth watching take it.</p>
<h2>One place, several pleasures</h2>
<p>The proposed <a href="https://auraofintelligence.github.io/ballow-road-sand-screen-hub/">Ballow Road Sand &amp; Screen Hub</a> on Minjerribah brings together sand sports, outdoor cinema, markets and festival life.</p>
<p>In Tiggy’s imagined evening, he helps with the screen and sound, then washes off the day. Food stalls are opening. Friends are arriving. The woman from the court waves him over to the seat beside her.</p>
<p>She has brought her friends, remembered his drink and decided they are all staying for the music afterwards. He is beginning to appreciate how well she organises a team.</p>'''),
    dict(slug='company', title='The invitation matters', intro='She makes room beside her. He enjoys the invitation.', image='company-world', alt='Tiggy talks closely with two adult women, one visibly pregnant, at an art-filled rooftop gathering in Mexico City.', caption='The conversation has become the best part of the evening. Imagined Mexico City gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">She could have sent him the name of the restaurant. Instead, she comes to collect him.</p>
<p>Her friend is waiting downstairs. There is an exhibition first, dinner afterwards and a rooftop view they think he ought to see. Tiggy has been looking forward to this since she suggested it.</p>
<h2>A particular appetite</h2>
<p>Adult women in their twenties and thirties, very full busts, pregnancy, confidence and cheek: Tiggy’s romantic imagination has its own distinct tastes. He enjoys direct interest and the pleasure of a woman choosing his company.</p>
<p>She takes the lead in the first encounter. He listens, responds and brings his own warmth to what they discover together. Sometimes the flirting is wonderfully obvious. Sometimes she enjoys letting him catch up.</p>
<h2>More people to love. More world to share.</h2>
<p>He wants to love and be loved while his life keeps moving. A relationship might grow through return visits, shared journeys, creative work or an invitation into an established circle of friends and lovers.</p>
<p>The <a href="https://auraofintelligence.github.io/global-group-marriages/">Global Group Marriages</a> exploration belongs near the heart of that possibility. Several people can choose a shared life with room for travel, affection, family and their own pursuits. Tiggy is interested in what that could feel like from the inside.</p>
<p>For now, she has arranged an evening. He is looking forward to finding out what she wants to show him.</p>'''),
    dict(slug='music', title='They gave him a microphone', intro='The singer has noticed him. Now she wants to hear him.', image='music-world', alt='An adult Afro-Brazilian singer cues Tiggy and another percussionist during a lively Salvador street gathering.', caption='He appears to have become part of the performance. Imagined Salvador festival. GenAI artwork.', colour='blue', body='''
<p class="lead">The singer changes a line and looks straight at Tiggy. He laughs. She points to the microphone beside her.</p>
<p>Fair enough. He has been singing along for the last three songs.</p>
<h2>Another verse</h2>
<p>In an imagined Salvador street festival, he has spent the afternoon helping the crew. Now the lights are on, the percussion fills the street and the woman on stage has decided he should be part of the evening’s entertainment.</p>
<p>He wants this: a live audience, a rhythm he can feel in his feet and the chance to give a song something of his own. He takes the cue. She answers. The band gives them another verse.</p>
<h2>After the applause</h2>
<p>Tiggy likes the whole life around a performance. Rehearsal, set-up, the show itself, then food with the people who made it happen. There are stories you only hear when the equipment is packed and nobody needs to watch the time quite so closely.</p>
<p>The singer has saved him a place at the table. Now he gets to hear what she sounds like when she is simply enjoying the conversation.</p>
<p>The <a href="https://auraofintelligence.github.io/i-C-infinity-music-universe/">i C. infinity music universe</a> gives this side of Tiggy room to grow: songs, characters and imagined lives with an audience to share them.</p>'''),
    dict(slug='possibilities', title='How big are we talking?', intro='A floating festival. A lunar playground. An invitation to help make it happen.', image='possibilities-world', alt='Two Kenyan artists share a model of a floating cinema and festival venue with Tiggy at a Nairobi evening reception.', caption='A formal invitation. A much less formal conversation. Imagined Nairobi reception. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy arrives at a Nairobi reception. The model on the table suggests he has drastically underdressed his imagination.</p>
<p>A screen rises above the water. Walkways connect stages, gardens and places to sit. The artist beside him points out where the audience arrives. Her colleague asks what he would put on the opening programme.</p>
<p>He has an answer. Her expression suggests she rather likes it.</p>
<h2>An opening night on the water</h2>
<p>In Nairobi, the scene is an elegant reception and a very ambitious model. Elsewhere it could be a festival linked across cities, a responsive world built by its visitors or a performance he has travelled halfway around the planet to help deliver.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/aura-events.html">events concept</a> stretches from intimate gatherings to grand galas and global festivals. <a href="https://auraofintelligence.github.io/space-industry.html">Moonlight Frontier</a> goes further, imagining low-gravity sport and lunar adventure. Tiggy can already imagine the game, the view and the people he would like to take with him.</p>
<h2>Someone has to make it happen</h2>
<p><a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> connects the work behind these possibilities. <a href="https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html">GAJRA Earth’s Ahead</a> follows dated meetings and openings to contribute. For Tiggy, an idea becomes interesting when there is a room he can enter, a part he can play and people he wants to work with.</p>
<p>He has limited time and plenty he wants to do. The project has caught his imagination. So have the people around the table. By the time dinner arrives, he has offered to help with the opening.</p>
<p>Then someone mentions the after-party.</p>'''),
    dict(slug='sitemap', title='More of Tiggy’s world', intro='Journeys, company and the things that happen along the way.', image='wayfinder', alt='Brightly coloured sculptural archways lead along a sunny seaside festival walkway towards the ocean.', caption='Plenty of ways to spend the afternoon. GenAI story concept.', colour='orange', body='''
<p class="lead">A few days in a new city. An artist with something to contribute. A woman who has decided he should stay for the evening.</p>
<p>Tiggy’s world unfolds through ten connected pages of travel, art, work, romance and playful possibilities. Each opens a different part of the life he wants to enjoy.</p>
<h2>Behind the stories</h2>
<p>The <a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Australian Sire Story Forge</a> holds the developing characters and possibilities. <a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a> introduces Luke Nathan Hayes, their creator.</p>
<p>The <a href="https://auraofintelligence.github.io/sitemap.html">Aura site map</a> and <a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> open the wider collection of projects and imagined futures that give these stories their settings and ambitions.</p>'''),
]

PLAY = '''<section class="play-panel" aria-labelledby="play-title"><div><h2 id="play-title">An evening with Tiggy</h2><p>Three glimpses of the company he keeps.</p><div class="mood-buttons" role="group" aria-label="Choose a scene"><button type="button" data-mood="make" aria-pressed="true">Red dust</button><button type="button" data-mood="wander" aria-pressed="false">Sand and screen</button><button type="button" data-mood="company" aria-pressed="false">Dress up</button></div><div class="play-result" aria-live="polite" aria-atomic="true"><h3>The bird takes a bow.</h3><p>She bows back. Tiggy joins her, and the crew starts laughing. Their outback stage build has acquired an opening act. Afterwards, she asks whether he is staying for dinner.</p></div></div><a class="round-link" href="fool.html" aria-label="Meet the happy-go-lucky fool">↗</a></section>'''

def chapter_links():
    return '<div class="chapter-index">'+''.join(f'<a href="{p["slug"]}.html"><span>{escape(p["title"])}</span><span aria-hidden="true">↗</span></a>' for p in PAGES[:-1])+'</div>'

for i,p in enumerate(PAGES):
    prev=PAGES[(i-1)%len(PAGES)];nxt=PAGES[(i+1)%len(PAGES)]
    nav=''.join(f'<a href="{q["slug"]}.html"'+(' aria-current="page"' if q==p else '')+f'>{escape(q["title"])}</a>' for q in PAGES)
    extra=PLAY if i==0 else chapter_links() if p['slug']=='sitemap' else ''
    (ROOT/(p['slug']+'.html')).write_text(f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(p['intro'],quote=True)}"><meta name="theme-color" content="#f7ff67"><title>{escape(p['title'])}{' | Tiggy Bestmann' if i else ' | Artist, fool and student of life'}</title><link rel="icon" href="assets/favicon.ico"><link rel="apple-touch-icon" href="assets/icon-180.png"><link rel="stylesheet" href="assets/site.css?v={VERSION}"><script defer src="assets/site.js?v={VERSION}"></script></head>
<body id="top" class="theme-{p['colour']} {'home' if i==0 else ''}"><a class="skip" href="#main">Skip to content</a>
<header class="site-header"><a class="brand" href="index.html">Tiggy Bestmann<span class="brand-dot" aria-hidden="true"></span></a><div class="header-actions"><a class="partner-short" href="{escape(SIRE_URL,quote=True)}">Meet Sire ↗</a><button class="menu-button" type="button" aria-expanded="false" aria-controls="chapter-menu">Explore <span aria-hidden="true">+</span></button></div><nav id="chapter-menu" aria-label="Chapters" hidden>{nav}</nav></header>
<main id="main"><section class="opening"><h1>{escape(p['title'])}</h1><p>{escape(p['intro'])}</p></section><figure class="hero"><img src="assets/{p['image']}.webp" alt="{escape(p['alt'],quote=True)}" width="1536" height="1024" fetchpriority="high"><figcaption>{escape(p['caption'])}</figcaption></figure>
<article class="prose" aria-label="{escape(p['title'],quote=True)}">{p['body']}</article>{extra}
<section class="partner-panel"><div><h2>Meet Australian Sire</h2><p>A writer whose travels open into desire, shared lives and global group marriages. Another expression of Luke’s imagined world.</p></div><a href="{escape(SIRE_URL,quote=True)}">Visit the partner site ↗</a></section></main>
<nav class="page-turn" aria-label="Previous and next pages"><a rel="prev" href="{prev['slug']}.html"><span>← Previous</span><strong>{escape(prev['title'])}</strong></a><a rel="next" href="{nxt['slug']}.html"><span>Next →</span><strong>{escape(nxt['title'])}</strong></a></nav>
<footer><p>Tiggy Bestmann<br>A fictional character by Luke Nathan Hayes.</p><a href="sitemap.html">Site map ↗</a></footer><a class="to-top" href="#top" aria-label="Back to top">↑</a></body></html>''',encoding='utf-8')
print(f'Built {len(PAGES)} Tiggy pages.')
