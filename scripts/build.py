"""Build Tiggy's ten-page local character site using the Python standard library."""
from pathlib import Path
from html import escape
import os

ROOT = Path(__file__).resolve().parents[1]
SIRE_URL = os.environ.get('SIRE_PARTNER_URL', 'https://auraofintelligence.github.io/australiansire/')
VERSION = '20261001-chapter-coherence-2'

PAGES = [
    dict(slug='index', title='Tiggy Bestmann', intro='Artist, traveller and happy-go-lucky fool. Love in abundance, a little mischief and a world to explore.', image='opening-world', alt='Two adult women, one visibly pregnant, welcome the long-haired Tiggy at an Istanbul ferry landing and draw him into a lively conversation.', caption='Imagined encounter at an Istanbul ferry landing. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy Bestmann is Luke Nathan Hayes’s happy-go-lucky fool: an artist, traveller and romantic with love in abundance and a taste for big experiences. Cheeky, inventive and sometimes awkward, he says what he thinks and enjoys the comedy that follows.</p>
<h2>Love and a life in motion</h2>
<p>Women begin his first encounters. Tiggy meets their interest with his own. His attraction reaches across women of many forms and personalities, with affection, sex, laughter and shared curiosity at the heart of <a href="company.html">his romantic life</a>.</p>
<h2>A world to get amongst</h2>
<p>Every country and territory is on his wish list. Outback gatherings, beach life, high society, sport and festivals give his travels their variety. There is work involved, limited time and a lot he wants to fit in.</p>
<p><a href="out-about.html">His travel oracle follows opportunities</a>: people, creative work, events and the chance to be somewhere interesting while something is happening.</p>
<h2>The life behind the fiction</h2>
<p>Luke’s work, travel and memories feed Tiggy’s adventures. <a href="art.html">Art and life mapping</a> connect that history to imagined worlds. <a href="music.html">Music carries a Glastonbury dream</a> that began during Luke’s festival crew days in 2004.</p>
<h2>Beyond Earth</h2>
<p>The science-fiction romantasy reaches across planets and into encounters with extraterrestrial and extra-dimensional civilisations. Tiggy’s appetite for <a href="possibilities.html">adventure, art and romance</a> reaches with it.</p>
<p><a href="fool.html">A childhood dog, a street and a game</a> are behind his name.</p>'''),
    dict(slug='fool', title='The happy-go-lucky fool', intro='Cheeky, inventive and occasionally awkward. Honest first, dignified second.', image='fool-mischief-v2', alt='Long-haired Tiggy laughs with adult friends as a woman playfully tilts his orange hat at an imagined outdoor festival.', caption='Shared mischief at an imagined outdoor festival. GenAI artwork.', colour='orange', body='''
<p class="lead">Tiggy says what he actually thinks. His honesty sometimes gets out ahead of his dignity. He is cheeky, inventive and occasionally awkward, with an appetite for play and the unexpected.</p>
<h2 id="the-name">A dog, a street and a game</h2>
<p>Tiggy was Luke’s childhood dog. Tiggy was also his name for the game of tag. Bestmann Road was his childhood street. The first-pet-plus-first-street porn-star-name game put the two names together: childhood affection, play and a grown-up joke.</p>
<h2>Three faces of the same life</h2>
<p>Tiggy is the open-hearted romantic, drawn to joyful, energetic and exploratory companionship with women of many forms and personalities. Australian Sire is the older, more refined and selective expression, exploring fertility and particular deep desires. Luke Nathan Hayes, also known as Luke Catalyst, is the middle ground where both meet.</p>
<p>These are three creative personalities growing from Luke’s life. <a href="https://auraofintelligence.github.io/australiansire/writer.html#three-personas">Their shared origin</a> gives each a different way into the romantasy.</p>
<h2>A student of life</h2>
<p>Tiggy’s curiosity runs through art, music, practical work and relationships. He enjoys making something with other people and discovering what their different ideas bring to it. Learning, laughter and desire are all part of that enjoyment.</p>
<p>He wants to love and be loved, with room for fun, frivolity and the next experience. Joyful responsible abundance is the spirit of that life.</p>'''),
    dict(slug='company', title='Love, desire and company', intro='Affection, sex, laughter and exploratory companionship. Love in abundance across a travelling life.', image='company-world', alt='Tiggy talks closely with two adult women, one visibly pregnant, at an art-filled rooftop gathering in Mexico City.', caption='Imagined rooftop company in Mexico City. GenAI artwork.', colour='orange', body='''
<p class="lead">Tiggy wants to love and be loved. Affection, sex, humour and adventure run through his romantic life, with attraction reaching across women of many forms and personalities.</p>
<h2>The first encounter</h2>
<p>Women initiate his first encounters. Tiggy responds with his own curiosity and desire. Flirtation grows through mutual interest, shared choices and the pleasure of finding out more about each other.</p>
<h2>Desire in many forms</h2>
<p>He enjoys playful, joyful, energetic and exploratory companionship. Different bodies and personalities interest him, along with the individual woman’s humour, ideas and appetite for experience.</p>
<p>Pregnant women are among those he hopes to share affection, sex and adventure with.</p>
<h2>Relationships across places</h2>
<p>World travel and romance belong to the same life for Tiggy. He wants the discovery of new encounters and the warmth of continuing relationships, with people staying connected across distance.</p>
<h2>Global Group Marriages</h2>
<p>His romantic horizon includes <a href="https://auraofintelligence.github.io/australiansire/group-marriages.html">Global Group Marriages</a>, exploring marriages involving several partners across countries. The United Nations of Love imagines the UN as one loving, sexually alive, cross-cultural marriage raising children together. GAJRA Earth gives that thought experiment a wider planetary setting. Shared affection, pleasure and travel are part of its appeal for Tiggy.</p>'''),
    dict(slug='out-about', title='World travel', intro='Every country and territory. Fast trips, busy days, work to do and plenty of fun.', image='out-about-world', alt='Two adult Thai women invite Tiggy to an evening gathering beside a Bangkok canal and an arriving passenger boat.', caption='Imagined canal-side encounter in Bangkok. GenAI artwork.', colour='lemon', body='''
<p class="lead">Every country and territory is Tiggy’s travel ambition. He wants to meet, share, learn and teach. Work is part of the journey, time is limited and his appetite for experience is large.</p>
<h2>Different worlds on Earth</h2>
<p>Outback gatherings, high society, beach cultures, sport and festivals draw him into very different settings. He wants the variety of places and people, along with the humour, attraction and enjoyment of getting amongst it.</p>
<h2>Work on the way</h2>
<p>Practical skills, creative projects and festival work give his travels another dimension. Making something with people brings him into the life of a place, even during a short visit.</p>
<p>The <a href="https://auraofintelligence.github.io/global-founder-atlas/">Global Founder Atlas</a> leads into possible working journeys through research, residencies and projects. Tiggy’s travels draw on Luke’s work history and his interest in sharing knowledge.</p>
<h2>The travel oracle</h2>
<p>His travel oracle keeps the route responsive to opportunities: work, events, creative collaborations, surf conditions and invitations. People, place and timing come together as the journey develops.</p>
<p>The ambition spans the whole world. The next destination grows from what is happening in his life, with room for serendipity, <a href="water.html">a promising swell</a> and company worth travelling to meet.</p>'''),
    dict(slug='water', title='Bodyboarding', intro='An epic wave, a fast ride and two women sharing the fun in the surf.', image='water-photo-carry-v6', alt='Long-haired Tiggy walks through shallow surf with two smiling adult women. Each carries a bodyboard under an arm and a pair of short swim flippers in the same hand. A blue-green wave peels behind them.', caption='After the ride. GenAI story concept.', colour='mint', body='''
<p class="lead">Tiggy is in his element with a board, a pair of flippers and two women enjoying the waves beside him. The pleasure is physical: the burst of speed, the ride itself and the company out there with him.</p>
<h2>An epic ride</h2>
<p>Riding an epic wave is one of his ambitions. He wants the speed along an open face, a ride that holds his whole attention and the exhilaration of coming out of it. Bodyboarding gives his travels a thrill he wants more of.</p>
<h2>Company in the surf</h2>
<p>Sun, salt, wet hair and laughter give beach life its own sensuality. Tiggy enjoys the excitement of being there with women who are enjoying the day with him. Shared play and attraction are part of the same pleasure.</p>
<h2>A beach life behind the story</h2>
<p>Luke’s own history includes frequent bodyboarding and an early social life around the beach. Those memories feed Tiggy’s adventures, alongside the desire for bigger waves and <a href="out-about.html">new coasts to explore</a>.</p>'''),
    dict(slug='art', title='Art, memory and Aura', intro='Practical skills, remembered places and an imagination reaching into new worlds.', image='memory-atlas-v2', alt='Tiggy and two adult artists explore a place-and-memory timeline beside a globe and human digital twin in a bright harbour studio.', caption='Imagined memory and digital-twin studio. GenAI artwork.', colour='blue', body='''
<p class="lead">Web, design, mechanical, electrical and event work give Tiggy a practical imagination. He is interested in the life of an idea: making it, sharing it and seeing what people bring to it.</p>
<h2>Building Aura together</h2>
<p>Building Aura O.Z. with a team is one of his largest ambitions. Art, science and philosophy meet in that work, through digital twins, imagined spaces and experiences people share.</p>
<p>His creative life includes tools, materials and other people’s ideas. The enjoyment is in making something together as well as imagining it.</p>
<h2 id="remembering">Body, mind and place/soul story</h2>
<p>Luke’s life mapping connects the physical person, the thinking person and the story remembered through places. His <a href="https://auraofintelligence.github.io/Lukes-world-of-work-experience/">work history map</a> is already part of that record; a travel history map is planned.</p>
<p>Digital twins of body, mind and place/soul story are part of his exploration of Aura: ways of remembering and mapping a life, its experiences and its intentions.</p>
<h2>Flashbacks and imagined worlds</h2>
<p>Any part of Luke’s history is material for a Tiggy flashback. Jobs, journeys and remembered places connect the fiction to a lived past. The <a href="music.html#glastonbury">Glastonbury dream from 2004</a> is one thread that reaches into his future.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/world-builder.html">World Builder</a> explores landscapes, planets, moons, stars and galaxies. Places remembered and worlds imagined are both material for Tiggy’s art.</p>'''),
    dict(slug='music', title='Music and Glastonbury', intro='i C. infinity, a Sway controller on its way and a dream of performing at Glastonbury.', image='music-sway-v2', alt='Tiggy experiments with an Audima Sway-inspired MIDI controller while two adult women, one visibly pregnant, enjoy the music in an imagined rehearsal space.', caption='Imagined Sway rehearsal. GenAI artwork.', colour='blue', body='''
<p class="lead">Tiggy wants to perform i C. infinity for a living audience. The music is Luke’s; the wish to take it on stage reaches back to a festival field in 2004.</p>
<h2 id="glastonbury">Glastonbury, 2004</h2>
<p>Luke’s UK working holiday included festival work with W.A.A.P. Wing and a Prayer Event Services. He helped set up Glastonbury, where the ambition to return someday as a performer began.</p>
<p>Those crew days are recorded in his <a href="https://auraofintelligence.github.io/Lukes-world-of-work-experience/">work history map</a>. Tiggy carries the performance dream into the romantasy.</p>
<h2 id="sway">Sway is on its way</h2>
<p>Luke has bought an <a href="https://audima.com.au/op/sway-b4/">Audima Labs Sway MIDI controller</a> from batch 4, with arrival expected in November or December 2026. Once it arrives, the goal is to learn to perform i C. infinity with it.</p>
<p>An unfamiliar instrument gives Tiggy something new to play with. The ambition is a live performance shaped by his own hands and the response of the people listening.</p>
<h2>Music that travels</h2>
<p><a href="https://auraofintelligence.github.io/i-C-infinity-music-universe/">i C. infinity</a> is Luke’s music universe. Tiggy’s ambition brings that music into his life as an artist and traveller, with a crowd to play for and the enjoyment of a shared performance.</p>
<p>Glastonbury remains the dream venue. The science-fiction romantasy opens a further horizon of <a href="possibilities.html">festivals and audiences beyond Earth</a>.</p>'''),
    dict(slug='retreats', title='Aura retreats', intro='Making Aura, sharing ideas and enjoying a few days in good company.', image='retreat', alt='A visibly pregnant adult woman shares a playful light sculpture with Tiggy and another participant at an imagined coastal Aura retreat in Goa.', caption='Imagined Aura retreat in Goa. GenAI artwork.', colour='mint', body='''
<p class="lead">An Aura retreat brings creativity and company into the same few days. Tiggy’s interests meet there: art and technology, music and movement, learning through experience and the enjoyment of being together.</p>
<h2>Aura in the making</h2>
<p>Luke’s proposed formats are a five-day exploration and a nine-day teacher-training retreat. Both explore the Aura of Intelligence and digital twins through AI, extended reality, avatars, body mapping and remembered places.</p>
<p>The concept also includes making things with generative AI, 3D modelling and printing, alongside reflection and creative work. That combination fits Tiggy’s practical skills and artistic curiosity.</p>
<h2>Life around the retreat</h2>
<p>Goa is among the proposed locations. Local culture, food, music, dance and adventure are part of the wider experience, with shared meals and time together beyond the workshops.</p>
<p>For Tiggy, the appeal includes meeting people absorbed in ideas he enjoys, making something together and the possibilities of friendship and attraction. Retreats bring another rhythm to <a href="out-about.html">his travelling life</a>, with time for shared discovery.</p>'''),
    dict(slug='possibilities', title='Beyond Earth', intro='Planetary adventures, whole civilisations and encounters beyond the familiar world.', image='worldbuilding-festival-v2', alt='Tiggy and two adult worldbuilders, one visibly pregnant, share a civilisation model at an imagined future festival, with lunar and city simulations behind them.', caption='Imagined Worldbuilding Challenge Festival. GenAI artwork.', colour='lemon', body='''
<p class="lead">Earth is the beginning. Tiggy’s science-fiction romantasy reaches towards humanity across planets, growing ambitions on the Kardashev scale and contact with extraterrestrial and extra-dimensional civilisations.</p>
<h2>Other civilisations</h2>
<p>Hidden mountain societies, ocean civilisations and unfamiliar worlds widen the scope of his travels. Their art, ideas and ways of living give his curiosity much more to explore.</p>
<p>He wants to meet, share, learn and teach. Adventure, companionship and romance reach into that larger universe with him.</p>
<h2>The Worldbuilding Challenge Festival</h2>
<p>This imagined festival devotes a week to teams pitching and developing whole civilisations. The Pitch Arena leads into a Build Sprint, with a 12-minute film, a working simulation and a world bible. An island campus residency is among the possibilities at the end.</p>
<p>It brings art, science, philosophy and filmmaking into one enormous creative experience, connecting Tiggy’s <a href="art.html">worldbuilding interests</a> with his love of festivals.</p>
<h2>Play across worlds</h2>
<p><a href="https://auraofintelligence.github.io/space-industry.html">Moonlight Frontier</a> imagines low-gravity sport and lunar adventure. <a href="https://auraofintelligence.github.io/aura-events.html">Aura’s events universe</a> reaches through gatherings, galas and festivals. The scale of the setting grows with the scope for work, art and enjoyment.</p>
<h2>The work feeding the fiction</h2>
<p>Luke draws inspiration from today’s work in spaceflight, AI and robotics when he imagines these futures. <a href="https://www.nasa.gov/moontomarsarchitecture-strategyandobjectives/">NASA’s Moon to Mars strategy</a> and <a href="https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/">Gemini Robotics</a> are starting points for that curiosity.</p>
<p><a href="https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html">GAJRA Earth’s Ahead</a> leads into the wider work. Planetary life, contact and travel across dimensions extend the imagined horizon beyond it.</p>'''),
    dict(slug='sitemap', title='Site map', intro='Tiggy’s chapters and the wider life, music and story universe behind them.', image='wayfinder', alt='Brightly coloured sculptural archways lead along a sunny seaside festival walkway towards the ocean.', caption='An imagined seaside festival walkway. GenAI artwork.', colour='orange', body='''
<p class="lead">Behind Tiggy’s adventures are Luke’s life, music, practical work and evolving Aura universe. These links lead into that wider ecosystem.</p>
<h2>The creator and the fiction</h2>
<p><a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a> introduces Luke Nathan Hayes. His <a href="https://auraofintelligence.github.io/australiansire/writer.html#three-personas">three creative personalities</a> share that history. <a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Story Forge</a> holds developing characters, settings and possible stories; <a href="https://auraofintelligence.github.io/loose-goose-comedy-engine/">Loose Goose Comedy Engine</a> follows the humour.</p>
<h2>Life, travel and music</h2>
<p>Luke’s <a href="https://auraofintelligence.github.io/Lukes-world-of-work-experience/">work history map</a> follows the lived past. <a href="https://auraofintelligence.github.io/right-place-right-time/">Right Place, Right Time</a> connects work and future travel. <a href="https://auraofintelligence.github.io/i-C-infinity-music-universe/">i C. infinity</a> opens the music universe.</p>
<h2>Beach life and wider projects</h2>
<p>The proposed <a href="https://auraofintelligence.github.io/ballow-road-sand-screen-hub/">Ballow Road Sand &amp; Screen Hub</a> brings sand sports, outdoor cinema, markets and festivals into Luke’s beach-hub idea for Minjerribah.</p>
<p>The <a href="https://auraofintelligence.github.io/sitemap.html">Aura site map</a> and <a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> connect the wider collection of projects and imagined futures.</p>'''),
]

PLAY = '''<section class="play-panel" aria-labelledby="play-title"><div><h2 id="play-title">Follow an interest</h2><p>Music, bodyboarding and world travel.</p><div class="mood-buttons" role="group" aria-label="Choose an interest"><button type="button" data-mood="make" aria-pressed="true">Music</button><button type="button" data-mood="wander" aria-pressed="false">Waves</button><button type="button" data-mood="company" aria-pressed="false">Travel</button></div><div class="play-result" aria-live="polite" aria-atomic="true"><h3>Music and Glastonbury</h3><p>i C. infinity is the music, Sway is the new instrument on its way, and performing at Glastonbury is the dream that began in 2004.</p></div></div><a class="round-link" href="music.html" aria-label="Music and Glastonbury">↗</a></section>'''

def chapter_links():
    return '<nav class="chapter-index" aria-label="Tiggy’s chapters"><h2>Chapters</h2>'+''.join(f'<a href="{p["slug"]}.html"><span>{escape(p["title"])}</span><span aria-hidden="true">↗</span></a>' for p in PAGES[:-1])+'</nav>'

for i,p in enumerate(PAGES):
    prev=PAGES[(i-1)%len(PAGES)];nxt=PAGES[(i+1)%len(PAGES)]
    nav=''.join(f'<a href="{q["slug"]}.html"'+(' aria-current="page"' if q==p else '')+f'>{escape(q["title"])}</a>' for q in PAGES)
    extra=PLAY if i==0 else ''
    chapter_index=chapter_links() if p['slug']=='sitemap' else ''
    (ROOT/(p['slug']+'.html')).write_text(f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(p['intro'],quote=True)}"><meta name="theme-color" content="#f7ff67"><title>{escape(p['title'])}{' | Tiggy Bestmann' if i else ' | Artist, fool and student of life'}</title><link rel="icon" href="assets/favicon.ico"><link rel="apple-touch-icon" href="assets/icon-180.png"><link rel="stylesheet" href="assets/site.css?v={VERSION}"><script defer src="assets/site.js?v={VERSION}"></script></head>
<body id="top" class="theme-{p['colour']} {'home' if i==0 else ''}"><a class="skip" href="#main">Skip to content</a>
<header class="site-header"><a class="brand" href="index.html">Tiggy Bestmann<span class="brand-dot" aria-hidden="true"></span></a><div class="header-actions"><a class="partner-short" href="{escape(SIRE_URL,quote=True)}">Meet Sire ↗</a><button class="menu-button" type="button" aria-expanded="false" aria-controls="chapter-menu">Explore <span aria-hidden="true">+</span></button></div><nav id="chapter-menu" aria-label="Chapters" hidden>{nav}</nav></header>
<main id="main"><section class="opening"><h1>{escape(p['title'])}</h1><p>{escape(p['intro'])}</p></section><figure class="hero"><img src="assets/{p['image']}.webp" alt="{escape(p['alt'],quote=True)}" width="1536" height="1024" fetchpriority="high"><figcaption>{escape(p['caption'])}</figcaption></figure>{chapter_index}
<article class="prose" aria-label="{escape(p['title'],quote=True)}">{p['body']}</article>{extra}
</main>
<nav class="page-turn" aria-label="Previous and next pages"><a rel="prev" href="{prev['slug']}.html"><span>← Previous</span><strong>{escape(prev['title'])}</strong></a><a rel="next" href="{nxt['slug']}.html"><span>Next →</span><strong>{escape(nxt['title'])}</strong></a></nav>
<footer><p>Tiggy Bestmann<br>A fictional character by Luke Nathan Hayes.</p><nav class="footer-links" aria-label="Related sites and licence"><a href="sitemap.html">Site map ↗</a><a href="{escape(SIRE_URL,quote=True)}">Australian Sire</a><a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Story Forge</a><a href="https://auraofintelligence.github.io/loose-goose-comedy-engine/">Loose Goose Comedy Engine</a><a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a><a href="https://github.com/auraofintelligence/tiggy-bestmann/blob/main/LICENCE.md">Strange But True licence</a></nav></footer><a class="to-top" href="#top" aria-label="Back to top">↑</a></body></html>''',encoding='utf-8')
print(f'Built {len(PAGES)} Tiggy pages.')
