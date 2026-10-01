"""Build Tiggy's ten-page local character site using the Python standard library."""
from pathlib import Path
from html import escape
import os

ROOT = Path(__file__).resolve().parents[1]
SIRE_URL = os.environ.get('SIRE_PARTNER_URL', 'https://auraofintelligence.github.io/australiansire/')
VERSION = '20261001-reader-prose'

PAGES = [
    dict(slug='index', title='Tiggy Bestmann', intro='Artist, traveller and happy-go-lucky fool. Love in abundance, a little mischief and a world to explore.', image='opening-world', alt='Two adult women, one visibly pregnant, welcome the long-haired Tiggy at an Istanbul ferry landing and draw him into a lively conversation.', caption='An invitation on the Bosphorus. Imagined Istanbul encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy Bestmann wants a full life: making art, travelling the world, falling for women and laughing often. He is the happy-go-lucky fool in Luke Nathan Hayes’s science-fiction romantasy universe, with long hair, an inventive mind and an honest thought that sometimes escapes before he has dressed it properly.</p>
<h2>The pleasure of being invited</h2>
<p>She starts talking to him. Something in her humour catches his attention; something in his reply makes her stay. He loves that first stretch of discovery, when neither knows quite where the conversation is going.</p>
<p>His attraction is broad. Different bodies, temperaments and ways of looking at life interest him. He wants affection, desire and <a href="company.html">company that enjoys him back</a>. Romance travels with him, through new encounters and people he is very glad to see again.</p>
<h2>There is a lot he wants to do</h2>
<p>Every country and territory is on his wish list. The days are busy: work, art, music, the surf, an invitation somewhere unfamiliar. He enjoys the distance between an outback gathering and a splendid dinner, and the discovery that he feels at home in both.</p>
<p><a href="out-about.html">His route follows openings as they arrive</a>. A festival job, a promising swell or someone he misses gives the next journey a reason.</p>
<h2>A dream from the festival field</h2>
<p>In 2004, Luke helped set up Glastonbury and wished he would return someday to perform. Tiggy carries that wish. An Audima Labs Sway is on order, and learning to play <a href="music.html">i C. infinity live</a> is the next adventure.</p>
<h2>Earth is the beginning</h2>
<p>The horizon reaches across planets, into unfamiliar civilisations and encounters beyond the dimensions he knows. Tiggy’s appetite for <a href="possibilities.html">adventure and romance</a> reaches with it.</p>
<p>His name begins with <a href="fool.html#the-name">a childhood dog, a street and a game</a>. Luke’s remembered life supplies the flashbacks; Tiggy takes that history somewhere new.</p>'''),
    dict(slug='fool', title='The happy-go-lucky fool', intro='A quick grin, an honest thought and a joke getting better in company.', image='fool-mischief-v2', alt='Long-haired Tiggy laughs with adult friends as a woman playfully tilts his orange hat at an imagined outdoor festival.', caption='The joke is shared. Imagined festival company. GenAI artwork.', colour='orange', body='''
<p class="lead">Tiggy says what he actually thinks. Sometimes it is funny. Sometimes the pause afterwards is funnier. He is cheeky, inventive and occasionally awkward, with enough honesty to leave the awkward bit in.</p>
<p>He likes a woman who adds something outrageous to his ridiculous suggestion. A joke becomes a game between them, and the game is often more interesting than whatever started it.</p>
<h2 id="the-name">A dog, a street and a game</h2>
<p>Tiggy was Luke’s childhood dog. Tiggy was also what he called the game of tag. Bestmann Road was his childhood street. The old first-pet-plus-first-street porn-star-name game put the two names together.</p>
<p>There is a trick in that game: it asks people to reveal two familiar account-recovery answers. Luke tells the origin openly. The name carries the dog, the street, childhood play and an adult joke all at once.</p>
<h2>The fool in love</h2>
<p>Tiggy wants to play, and to love and be loved. He has no fixed ideal of a woman’s body or personality. Energy, affection and the pleasure of exploring each other draw him towards very different women.</p>
<p>She begins the encounter. His delight is easy to see. He remembers what made them laugh, and finds himself looking forward to the next conversation.</p>
<h2>Making something of it</h2>
<p>His inventiveness runs through practical work, art and music. An unusual idea interests him enough to try it. Other people bring their own ideas, and he enjoys discovering what they make together.</p>
<p><a href="https://auraofintelligence.github.io/australiansire/writer.html#three-personas">Luke, Tiggy and Australian Sire</a> share an origin, with different appetites for romance and adventure. Tiggy is the playful, open-hearted one.</p>'''),
    dict(slug='art', title='Art, memory and imagined worlds', intro='Work, travel and remembered places become material for another life.', image='memory-atlas-v2', alt='Tiggy and two adult artists explore a place-and-memory timeline beside a globe and human digital twin in a bright harbour studio.', caption='Body, mind and remembered places. GenAI interpretation of a future memory studio.', colour='blue', body='''
<p class="lead">Tiggy’s imagination has a working history. Web, mechanical, electrical, design and event work have left him with things to make, places to remember and more ideas than one life is likely to finish.</p>
<h2>Making Aura</h2>
<p>Aura O.Z. is among his largest ambitions: building with a team, drawing art, science and philosophy into places people experience together. He wants to make worlds that people enter, explore and bring something of themselves to.</p>
<p>He enjoys the work as well as the idea. There are materials, tools and other people’s contributions involved. His art grows through that contact.</p>
<h2 id="remembering">Body, mind and place/soul story</h2>
<p>An old job or a remembered place opens a flashback. Luke is mapping those memories through his <a href="https://auraofintelligence.github.io/Lukes-world-of-work-experience/">work history map</a>, with a travel history map still to come.</p>
<p>His digital twins connect body, mind and place/soul story: the physical person, the thinking person, and the life remembered through places. For Tiggy, that history is rich material. A festival field in 2004 still holds <a href="music.html#glastonbury">a dream of getting on stage</a>.</p>
<h2>A remembered life, an unfamiliar world</h2>
<p>Flashbacks reach through any part of Luke’s history. The future opens in another direction, through Aura’s <a href="https://auraofintelligence.github.io/world-builder.html">World Builder</a> and imagined civilisations. Tiggy’s art follows his curiosity into both.</p>'''),
    dict(slug='retreats', title='Aura retreats', intro='Bright ideas, shared discoveries and conversation that carries on over dinner.', image='retreat', alt='A visibly pregnant adult woman shares a playful light sculpture with Tiggy and another participant at an imagined coastal Aura retreat in Goa.', caption='Colour across the table. Conversation into the evening. Imagined Goa retreat. GenAI artwork.', colour='mint', body='''
<p class="lead">At an Aura retreat, there is time to become absorbed in an idea and in the people around the table. Tiggy enjoys both. The creative work gives them something to share; dinner gives the conversation room to wander.</p>
<h2>Getting absorbed</h2>
<p>Light, music, avatars and imagined spaces fill the work. Tiggy arrives with practical experience and plenty he still wants to explore. He enjoys seeing what happens when someone else takes an idea somewhere he had not thought of.</p>
<p>Luke’s retreat concept includes five-day explorations and nine-day teacher training, with coastal Goa among the proposed settings. Making, reflection, food and the life outside the retreat sit alongside the sessions.</p>
<h2>Getting close</h2>
<p>Repeated meals and unfinished conversations make strangers familiar. Attraction has time to show itself. The joke from the first evening acquires a history; the person beside him becomes someone he hopes will stay a little longer.</p>
<h2>When the fortnight ends</h2>
<p>One retreat story follows a group becoming close over a fortnight. Then departure arrives. There are flights to catch and people who have grown used to being together. The affection follows them home, and the question of seeing one another again becomes much more interesting than it was when they arrived.</p>'''),
    dict(slug='out-about', title='Fast travel, full days', intro='A reason to land, a busy few days and someone he hopes to see again.', image='out-about-world', alt='Two adult Thai women invite Tiggy to an evening gathering beside a Bangkok canal and an arriving passenger boat.', caption='The boat is coming. The evening is open. Imagined Bangkok encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy wants to visit every country and territory. He wants to meet people, share what he knows, learn, teach and enjoy being there. The ambition is enormous; the time between arrival and departure is often short.</p>
<h2>Busy days, open evenings</h2>
<p>Work is part of the journey. Festival crews, creative projects, research and presentations give him reasons to land and people to work beside. The <a href="https://auraofintelligence.github.io/global-founder-atlas/">Global Founder Atlas</a> is one doorway into that working travel.</p>
<p>He also wants the hours after work: the beach, a gathering, a meal he has never tried, the invitation he is pleased he accepted. Outback life, high society, sport and festivals offer very different company. He enjoys discovering how he fits into each.</p>
<h2>The next place</h2>
<p>His travel oracle follows opportunities as they come into view. Work, events, a swell and a woman he wants to see again all matter to the route. Each new opening changes the journey.</p>
<p>A few busy days leave him with a new place in his memory and people he misses. Sometimes the next journey takes him further away. Sometimes it brings him back for a very good reason.</p>'''),
    dict(slug='water', title='Sand, salt and screen', intro='A good wave, salt on his skin and company he wants to keep.', image='water-photo-carry-v6', alt='Long-haired Tiggy walks through shallow surf with two smiling adult women. Each carries a bodyboard under an arm and a pair of short swim flippers in the same hand. A blue-green wave peels behind them.', caption='After the ride. GenAI story concept.', colour='mint', body='''
<p class="lead">Tiggy comes ashore with his board under his arm, flippers in hand and a grin still on his face. The women beside him are laughing. He is enjoying the walk back almost as much as the surf.</p>
<h2>The wave he wants</h2>
<p>An epic ride is high on his wish list. He wants the speed, the exhilaration and a wave worth remembering years later. A promising swell gives his travel oracle another reason to look towards the coast.</p>
<p>One of his companions is the Ocean Master, who knows the island’s water intimately. Her body is beginning to argue with her, and she is deciding who receives what she knows while she is still riding.</p>
<h2>The afternoon is still open</h2>
<p>Back on the sand, the teasing continues. A game draws them in; a film after sunset gives them a reason to stay. Tiggy enjoys the warmth of being beside a woman who is enjoying him too, with the conversation growing more personal as the beach empties.</p>
<p>The next pleasure might be another wave, another shared joke or an invitation into <a href="company.html">a much closer evening</a>.</p>'''),
    dict(slug='company', title='The invitation matters', intro='She starts the conversation. Curiosity becomes flirtation.', image='company-world', alt='Tiggy talks closely with two adult women, one visibly pregnant, at an art-filled rooftop gathering in Mexico City.', caption='The conversation has become the best part of the evening. Imagined Mexico City gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">Tiggy likes being wanted. She starts the conversation, and he feels the pleasure of her attention. Her wit, her body, the way she looks at him: he wants to find out more.</p>
<h2>Getting to know her</h2>
<p>His attraction reaches across women of many forms and personalities. A quick laugh, a bold thought or a quieter warmth catches him. The discovery is personal: what she loves, what excites her, what they enjoy together.</p>
<p>He welcomes affection and sex into that exploration. With a pregnant lover, her changing curves and the closeness between them hold their own attraction. He enjoys the woman he is with and the desire they share.</p>
<h2>Someone he wants to see again</h2>
<p>A return visit carries anticipation. They have things to tell each other, memories to laugh over and the pleasure of finding that the attraction is still there.</p>
<p>Tiggy’s life keeps moving. Romance grows across places, through new encounters and continuing relationships. He wants the freedom to travel and the warmth of being missed.</p>
<h2>A larger circle</h2>
<p>An invitation from women who already share a life opens a wider intimacy. Friendship, desire and affection cross between several people, each bringing something of their own.</p>
<p><a href="https://auraofintelligence.github.io/australiansire/group-marriages.html">Global Group Marriages and the United Nations of Love</a> reach into that possibility on an international scale. Tiggy’s interest begins with the people he is drawn to and the pleasure of joining a life they want to share with him.</p>'''),
    dict(slug='music', title='From Glastonbury to Sway', intro='A dream from the festival crew days. A new instrument on its way.', image='music-sway-v2', alt='Tiggy experiments with an Audima Sway-inspired MIDI controller while two adult women, one visibly pregnant, enjoy the music in an imagined rehearsal space.', caption='Finding the first phrase. Imagined Sway rehearsal. GenAI artwork.', colour='blue', body='''
<p class="lead">In 2004, Luke helped build Glastonbury and wanted to return someday as a performer. Tiggy carries the same unfinished wish: to hear his own music come alive in front of a crowd.</p>
<h2 id="glastonbury">Glastonbury, 2004</h2>
<p>Luke’s UK working holiday included festival work with W.A.A.P. Wing and a Prayer Event Services. Glastonbury was among the events he helped set up. The wish to perform there has lasted far longer than that season.</p>
<p>The crew days are part of his <a href="https://auraofintelligence.github.io/Lukes-world-of-work-experience/">work history map</a> and the flashbacks behind Tiggy’s musical ambition.</p>
<h2 id="sway">Sway is on its way</h2>
<p>Luke has bought an <a href="https://audima.com.au/op/sway-b4/">Audima Labs Sway MIDI controller</a> from batch 4, with arrival expected in November or December 2026. Once it arrives, Tiggy’s adventure is learning to perform i C. infinity with it.</p>
<p>The music is already there; the performance is something to discover. Touch, gestures and practice give him a new way to explore a phrase and hear what he does with it.</p>
<h2>From a room to a festival</h2>
<p><a href="https://auraofintelligence.github.io/i-C-infinity-music-universe/">i C. infinity</a> carries songs, characters and whole imagined lives. Tiggy wants to play that music in company, feel the response and enjoy what happens between the sound and the people hearing it.</p>
<p>Glastonbury is still the dream. Beyond it, his science-fiction romantasy opens festivals across worlds, with unfamiliar audiences and a great deal of room to play.</p>'''),
    dict(slug='possibilities', title='How big are we talking?', intro='A festival of whole civilisations. A life reaching beyond Earth.', image='worldbuilding-festival-v2', alt='Tiggy and two adult worldbuilders, one visibly pregnant, share a civilisation model at an imagined future festival, with lunar and city simulations behind them.', caption='Whole worlds on the table. Imagined Worldbuilding Challenge Festival. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy wants to see every country and territory. His universe keeps opening beyond them: other planets, ocean civilisations, hidden mountain societies and encounters with beings whose lives are unlike anything he has known.</p>
<h2>The Worldbuilding Challenge Festival</h2>
<p>At this imagined festival, teams pitch whole civilisations. One week holds a pitch arena, a build sprint, a short film, a working simulation and a world bible. An island campus residency is the next possibility.</p>
<p>That is a week Tiggy wants to be part of. Art, philosophy, filmmaking and science have something enormous to work on, with people getting absorbed in worlds they have made together.</p>
<h2>Play beyond Earth</h2>
<p><a href="https://auraofintelligence.github.io/space-industry.html">Moonlight Frontier</a> imagines low-gravity sport and lunar adventure. <a href="https://auraofintelligence.github.io/aura-events.html">Aura’s events universe</a> reaches from intimate gatherings to galas and global festivals. Tiggy’s appetite for a good time follows that expanding horizon.</p>
<p>Humanity grows across planets and towards energy ambitions on the Kardashev scale. AI and robotics are part of building that future. The distance between places becomes immense, and so does the scope for a life spent exploring.</p>
<h2>Who is out there?</h2>
<p>Extraterrestrial and extra-dimensional civilisations bring unfamiliar art, ideas and ways of being together. A Starmind Interpreter is among the figures in that universe. Tiggy wants to meet, learn, share and discover where affection and desire find a response.</p>
<h2>Work behind the horizon</h2>
<p>Luke draws on today’s thinkers and builders when he imagines what follows. <a href="https://www.nasa.gov/moontomarsarchitecture-strategyandobjectives/">NASA’s Moon to Mars strategy</a> and <a href="https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/">Gemini Robotics</a> are present-day starting points. Contact with other civilisations and travel across dimensions belong to the speculative adventures.</p>
<p><a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> and <a href="https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html">GAJRA Earth’s Ahead</a> lead into the wider work behind that horizon.</p>'''),
    dict(slug='sitemap', title='More of Tiggy’s world', intro='Play, art, music, travel and relationships. Follow a thread through his world.', image='wayfinder', alt='Brightly coloured sculptural archways lead along a sunny seaside festival walkway towards the ocean.', caption='Plenty of ways to spend the afternoon. GenAI story concept.', colour='orange', body='''
<p class="lead">Tiggy’s world begins with a playful man, an appetite for love and a long list of places he wants to see. These chapters follow his humour, art, music, relationships and adventures.</p>
<h2>The man and the characters</h2>
<p><a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a> introduces Luke Nathan Hayes. <a href="https://auraofintelligence.github.io/australiansire/writer.html#three-personas">Luke, Tiggy and Australian Sire</a> explores the three romantic personalities growing from his life: Tiggy’s broad, playful attraction, Sire’s more particular desires, and Luke’s balance between them.</p>
<p>The <a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Australian Sire Story Forge</a> opens the developing characters, settings and possible stories. The <a href="https://auraofintelligence.github.io/loose-goose-comedy-engine/">Loose Goose Comedy Engine</a> follows the humour.</p>
<h2>Beyond the chapters</h2>
<p>The proposed <a href="https://auraofintelligence.github.io/ballow-road-sand-screen-hub/">Ballow Road Sand &amp; Screen Hub</a> brings Luke’s beach-hub idea into view: sand sports, outdoor cinema, markets and festivals on Minjerribah.</p>
<p>The <a href="https://auraofintelligence.github.io/sitemap.html">Aura site map</a> and <a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> open the wider collection of work, music and imagined futures.</p>'''),
]

PLAY = '''<section class="play-panel" aria-labelledby="play-title"><div><h2 id="play-title">Follow an interest</h2><p>Music, waves and the next journey.</p><div class="mood-buttons" role="group" aria-label="Choose an interest"><button type="button" data-mood="make" aria-pressed="true">Music</button><button type="button" data-mood="wander" aria-pressed="false">Waves</button><button type="button" data-mood="company" aria-pressed="false">Travel</button></div><div class="play-result" aria-live="polite" aria-atomic="true"><h3>From Glastonbury to Sway.</h3><p>The festival crew days left a lasting dream: to return as a performer. Sway is on its way, and i C. infinity is the music he wants to bring to life.</p></div></div><a class="round-link" href="music.html" aria-label="From Glastonbury to Sway">↗</a></section>'''

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
</main>
<nav class="page-turn" aria-label="Previous and next pages"><a rel="prev" href="{prev['slug']}.html"><span>← Previous</span><strong>{escape(prev['title'])}</strong></a><a rel="next" href="{nxt['slug']}.html"><span>Next →</span><strong>{escape(nxt['title'])}</strong></a></nav>
<footer><p>Tiggy Bestmann<br>A fictional character by Luke Nathan Hayes.</p><nav class="footer-links" aria-label="Related sites and licence"><a href="sitemap.html">Site map ↗</a><a href="{escape(SIRE_URL,quote=True)}">Australian Sire</a><a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Story Forge</a><a href="https://auraofintelligence.github.io/loose-goose-comedy-engine/">Loose Goose Comedy Engine</a><a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a><a href="https://github.com/auraofintelligence/tiggy-bestmann/blob/main/LICENCE.md">Strange But True licence</a></nav></footer><a class="to-top" href="#top" aria-label="Back to top">↑</a></body></html>''',encoding='utf-8')
print(f'Built {len(PAGES)} Tiggy pages.')
