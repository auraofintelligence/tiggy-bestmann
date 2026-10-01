"""Build Tiggy's ten-page local character site using the Python standard library."""
from pathlib import Path
from html import escape
import os

ROOT = Path(__file__).resolve().parents[1]
SIRE_URL = os.environ.get('SIRE_PARTNER_URL', 'https://auraofintelligence.github.io/australiansire/')
VERSION = '20261001-footer-links'

PAGES = [
    dict(slug='index', title='Tiggy Bestmann', intro='Artist, traveller and happy-go-lucky fool. Love in abundance, a little mischief and a world to explore.', image='opening-world', alt='Two adult women, one visibly pregnant, welcome the long-haired Tiggy at an Istanbul ferry landing and draw him into a lively conversation.', caption='An invitation on the Bosphorus. Imagined Istanbul encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy Bestmann is an artist and student of life with a cheeky sense of humour and an appetite for adventure. He enjoys making things, meeting people and discovering how much pleasure fits into a busy life.</p>
<p>Long hair, glasses, a lively mind. He moves between practical work and ambitious ideas, with music, bodyboarding and romance woven through his travels.</p>
<h2>The pleasure of being invited</h2>
<p>A woman starts a conversation. He enjoys her wit, her warmth and the interest she takes in him. Curiosity becomes flirtation; neither is in a hurry to leave. Tiggy is drawn to women of many forms and personalities, and to the fun of discovering each other.</p>
<p>His romantic life stays open as he travels. Affection grows through shared adventures, return visits and people who miss one another. <a href="company.html">The invitation matters.</a></p>
<h2>A full life, on the move</h2>
<p>Every country and territory is the ambition. Work brings him into unfamiliar places; the people he meets give him reasons to linger and return. Outback gatherings, beach culture, festivals and splendid evenings offer very different pleasures.</p>
<p>The route follows opportunities rather than a fixed itinerary. There is effort involved, limited time and a great deal he wants to enjoy. <a href="out-about.html">Fast travel, full days.</a></p>
<h2>A tune carried since 2004</h2>
<p>Luke helped set up Glastonbury during his UK working holiday and dreamed of performing there someday. That hope travels into Tiggy’s life. An Audima Labs Sway is on order, ready for the next adventure: learning to perform i C. infinity music.</p>
<p><a href="music.html">From Glastonbury to Sway ↗</a></p>
<h2>A much wider horizon</h2>
<p>His adventures reach into a science-fiction romantasy universe of planetary settlements, AI, robotics and encounters with extraterrestrial and extra-dimensional civilisations. Art, desire and joyful responsible abundance travel with him.</p>
<p>Luke’s lived history feeds this imagined life. Tiggy’s name begins with <a href="fool.html#the-name">a childhood dog, a street and a game</a>; flashbacks lead through earlier work, places and hopes. <a href="art.html#remembering">Memory opens another way into the adventure.</a></p>'''),
    dict(slug='fool', title='The happy-go-lucky fool', intro='A quick grin, an honest thought and a joke getting better in company.', image='fool-mischief-v2', alt='Long-haired Tiggy laughs with adult friends as a woman playfully tilts his orange hat at an imagined outdoor festival.', caption='The joke is shared. Imagined festival company. GenAI artwork.', colour='orange', body='''
<p class="lead">The innocent fool wants to play. Tiggy is cheeky, inventive and occasionally awkward, with an honest thought that sometimes arrives before the polished version.</p>
<p>He enjoys teasing, a ridiculous suggestion and the delight of someone adding a better joke. His humour makes company lively. His curiosity keeps him interested long after the laughter.</p>
<h2 id="the-name">A dog, a street and a game</h2>
<p>Tiggy was the name of Luke’s childhood dog, and the name he used for the game of tag. Bestmann Road was his childhood street. Together they became Tiggy Bestmann through the old first-pet-plus-first-street porn-star-name game.</p>
<p>Luke tells the origin openly, including the trick tucked inside that game: those names are also familiar account-recovery questions. Childhood play and adult mischief meet in a name that still makes him smile.</p>
<h2>Love in abundance</h2>
<p>Tiggy carries that playful spirit into his adult life. He enjoys women of many forms and personalities, with fun, energy and exploratory companionship at the heart of his attraction.</p>
<p>She begins the encounter. He is delighted by her interest, and brings plenty of his own. A shared joke stays with him; so does the anticipation of seeing her again.</p>
<h2>The artist beneath the grin</h2>
<p>Playfulness runs through his art, music and travels. He is serious about making things, and enjoys the surprises that arrive when other people join in. There is nerve in putting an unusual idea into the world, and pleasure in seeing it take on a life beyond him.</p>
<p><a href="https://auraofintelligence.github.io/australiansire/writer.html#three-personas">Luke, Tiggy and Australian Sire</a> introduces the three romantic personalities growing from the same life.</p>'''),
    dict(slug='art', title='Art, memory and imagined worlds', intro='Work, travel and remembered places become material for another life.', image='memory-atlas-v2', alt='Tiggy and two adult artists explore a place-and-memory timeline beside a globe and human digital twin in a bright harbour studio.', caption='Body, mind and remembered places. GenAI interpretation of a future memory studio.', colour='blue', body='''
<p class="lead">Tiggy’s art grows from a life spent making, travelling and asking questions. Philosophy and science feed his imagination; practical skills help give an idea form.</p>
<h2>Making Aura</h2>
<p>Web, design, mechanical, electrical and event work sit behind his ambition to build Aura O.Z. with a team. Immersive places and digital twins bring together his interest in technology and the experience of being alive.</p>
<h2 id="remembering">Body, mind and place/soul story</h2>
<p>Luke is mapping his history to remember where he has been and what he has lived. His <a href="https://auraofintelligence.github.io/Lukes-world-of-work-experience/">work history map</a> is public; a travel history map is still to come.</p>
<p>These histories feed digital twins of body, mind and place/soul story: connected representations of physical life, thought, and the places and experiences that carry personal meaning. Work, music, travel and reflection become easier to revisit together.</p>
<h2>Earlier lives, future worlds</h2>
<p>Flashbacks lead through any part of that history. The <a href="music.html#glastonbury">2004 Glastonbury season</a> brings an old performance dream into the present. Other memories open other paths through Tiggy’s adventures.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/world-builder.html">World Builder</a> carries the imagination into entire places to inhabit. Remembered experience feeds the making of unfamiliar worlds.</p>'''),
    dict(slug='retreats', title='Aura retreats', intro='Bright ideas, shared discoveries and conversation that carries on over dinner.', image='retreat', alt='A visibly pregnant adult woman shares a playful light sculpture with Tiggy and another participant at an imagined coastal Aura retreat in Goa.', caption='Colour across the table. Conversation into the evening. Imagined Goa retreat. GenAI artwork.', colour='mint', body='''
<p class="lead">An Aura retreat draws Tiggy through creative work, reflection and the pleasure of spending time with people who are curious about life.</p>
<p>Avatars, memory palaces and extended reality meet practical making, music, food and adventure. He arrives with experience to share and questions he has not finished asking.</p>
<h2>A few days together</h2>
<p>Luke’s retreat concept imagines five days of exploration, or nine days for teacher training. Coastal Goa is one proposed setting, with room in the day for the surrounding culture and landscape as well as the work.</p>
<p>For Tiggy, ideas and company are closely entwined. A conversation begun over a project continues at dinner. Familiarity grows; so does the interest between people.</p>
<h2>After the stay</h2>
<p>A longer retreat story follows a group becoming close over a fortnight. Leaving raises a new question: where does that affection go next? Return visits, shared journeys and romance carry the relationships beyond the retreat.</p>'''),
    dict(slug='out-about', title='Fast travel, full days', intro='A reason to land, a busy few days and someone he hopes to see again.', image='out-about-world', alt='Two adult Thai women invite Tiggy to an evening gathering beside a Bangkok canal and an arriving passenger boat.', caption='The boat is coming. The evening is open. Imagined Bangkok encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy wants to visit every country and territory: to meet, share, learn and teach, with plenty of life in between.</p>
<p>The journeys are fast and action-packed. Work is involved, time is limited and unfamiliar places keep his senses awake. He enjoys the change from the outback to high society, from beach life and sport to festivals and late conversations.</p>
<h2>A reason to be there</h2>
<p>A festival job, residency, research visit or presentation brings people and practical work into the journey. The <a href="https://auraofintelligence.github.io/global-founder-atlas/">Global Founder Atlas</a> connects projects with places that might welcome them.</p>
<p>He gets involved in the work, then enjoys the hours around it. The person who invites him somewhere brings a different view of the place: her interests, her company and the life she shares with him.</p>
<h2>The route keeps changing</h2>
<p>His travel oracle brings work, gatherings, relationships and opportunities into view together. There is no predetermined itinerary. An opening in one place, a project in another and someone he wants to see again all influence the next journey.</p>
<p>He enjoys moving quickly without losing the pleasure of where he is. Some connections continue across distance; others bring him back. Each visit adds another place and another memory to his life.</p>'''),
    dict(slug='water', title='Sand, salt and screen', intro='Bodyboards in the water. Games on the sand. A film after sunset.', image='water-carry-waves-v4', alt='Tiggy and two adult women laugh in shallow surf with bodyboards tucked under their arms and coiled bicep leashes attached. A blue-green wave peels across the break behind them.', caption='After the ride. GenAI story concept.', colour='mint', body='''
<p class="lead">Salt water, an approaching swell and the concentration of catching a wave: bodyboarding brings a physical thrill to Tiggy’s travels.</p>
<h2>An epic wave</h2>
<p>Riding an epic wave is one of his ambitions. Timing, skill and an understanding of the ocean matter as much as nerve. The Ocean Master, an experienced rider familiar with the break and its seasons, is among the companions in that adventure.</p>
<h2>Back on shore</h2>
<p>The proposed <a href="https://auraofintelligence.github.io/ballow-road-sand-screen-hub/">Ballow Road Sand &amp; Screen Hub</a> on Minjerribah draws sand sports, outdoor cinema, markets and festivals into one place.</p>
<p>That mix appeals to Tiggy’s love of outdoor play, creative work and company. A game, a shared film and an evening conversation give the shore a life of its own.</p>'''),
    dict(slug='company', title='The invitation matters', intro='She starts the conversation. Curiosity becomes flirtation.', image='company-world', alt='Tiggy talks closely with two adult women, one visibly pregnant, at an art-filled rooftop gathering in Mexico City.', caption='The conversation has become the best part of the evening. Imagined Mexico City gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">Tiggy wants love in abundance: affection, laughter, sensuality and the pleasure of discovering someone who enjoys him too.</p>
<h2>The woman he is with</h2>
<p>His attraction reaches across many forms and personalities. Wit, warmth, energy and curiosity draw him in. He enjoys learning what she loves, what makes her laugh and where their desires meet.</p>
<p>Women initiate his first encounters. He responds with interest and affection; the exchange grows through what they enjoy together. With a pregnant lover, tenderness and desire mingle with the anticipation of a new life.</p>
<h2>Affection across distance</h2>
<p>Travel gives his relationships a wide geography. A visit becomes a shared journey; a friendship deepens; missing someone becomes a reason to return. He enjoys an open, moving life and the relationships that grow within it.</p>
<h2>A larger circle</h2>
<p>An invitation into an established circle of friends and lovers opens another kind of relationship. <a href="https://auraofintelligence.github.io/australiansire/group-marriages.html">Global Group Marriages and the United Nations of Love</a> explore those larger connections across cultures and places. For Tiggy, the attraction begins with the people, their mutual desire and the life they enjoy sharing.</p>'''),
    dict(slug='music', title='From Glastonbury to Sway', intro='A dream from the festival crew days. A new instrument on its way.', image='music-sway-v2', alt='Tiggy experiments with an Audima Sway-inspired MIDI controller while two adult women, one visibly pregnant, enjoy the music in an imagined rehearsal space.', caption='Finding the first phrase. Imagined Sway rehearsal. GenAI artwork.', colour='blue', body='''
<p class="lead">Before the thought of a stage came the work of building a festival. Tiggy’s music dream reaches back to Luke’s UK working holiday in 2004.</p>
<h2 id="glastonbury">Glastonbury, 2004</h2>
<p>Luke worked with W.A.A.P. Wing and a Prayer Event Services, helping set up major music festivals, including Glastonbury. He wanted to return someday as a performer. The years have passed; the wish is still there.</p>
<p>That festival season lives on in Luke’s <a href="https://auraofintelligence.github.io/Lukes-world-of-work-experience/">work history map</a> and in the dream he carries into Tiggy’s story.</p>
<h2 id="sway">Sway is on its way</h2>
<p>Luke has bought an <a href="https://audima.com.au/op/sway-b4/">Audima Labs Sway MIDI controller</a> from batch 4, with arrival expected in November or December 2026. Once it arrives, Tiggy’s next musical adventure is learning to perform i C. infinity with it.</p>
<p>Sway responds to gestures as well as touch. Finding a phrase, shaping a sound and hearing an experiment come alive are part of the pleasure ahead.</p>
<h2>Music in company</h2>
<p><a href="https://auraofintelligence.github.io/i-C-infinity-music-universe/">i C. infinity</a> carries songs, characters and imagined lives. Performance brings that music into a room with other people: rhythm, movement and a response he feels as it happens.</p>
<p>Glastonbury remains an ambition. The fiction reaches further, into festivals and encounters across worlds, while flashbacks return to the crew days when the dream began.</p>'''),
    dict(slug='possibilities', title='How big are we talking?', intro='A festival of whole civilisations. A life reaching beyond Earth.', image='worldbuilding-festival-v2', alt='Tiggy and two adult worldbuilders, one visibly pregnant, share a civilisation model at an imagined future festival, with lunar and city simulations behind them.', caption='Whole worlds on the table. Imagined Worldbuilding Challenge Festival. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy’s curiosity reaches far beyond the next destination. His universe follows humanity across planets and into encounters with extraterrestrial and extra-dimensional civilisations.</p>
<h2>The Worldbuilding Challenge Festival</h2>
<p>Teams bring entire imagined civilisations to a futures festival. A pitch arena leads into a build sprint: a short film, a working simulation and a world bible. An island campus residency lies ahead.</p>
<p>Philosophy, science, art and filmmaking meet in the work. Tiggy is drawn to the scale of the ideas and the people giving them life.</p>
<h2>Adventure on a larger scale</h2>
<p>Aura’s <a href="https://auraofintelligence.github.io/aura-events.html">events universe</a> stretches from close gatherings to grand galas and global festivals. <a href="https://auraofintelligence.github.io/space-industry.html">Moonlight Frontier</a> imagines low-gravity sport and lunar adventure. His love of play travels well beyond a beach on Earth.</p>
<p>Planetary settlements and energy ambitions reaching up the Kardashev scale form the wider horizon. AI and robotics help people build, travel and create within that imagined future.</p>
<h2>Unfamiliar company</h2>
<p>Hidden mountain societies, sub-oceanic civilisations, visitors with different lineages and a Starmind Interpreter open unfamiliar experiences of life. Tiggy brings his curiosity and affection into those encounters. Art, desire and the wish to love and be loved follow him across worlds.</p>
<h2>From present work to future fiction</h2>
<p>Luke draws on the work of global thinkers and builders as he imagines what follows. <a href="https://www.nasa.gov/moontomarsarchitecture-strategyandobjectives/">NASA’s Moon to Mars strategy</a> and <a href="https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/">Gemini Robotics</a> offer present-day starting points; contact with other civilisations and travel across dimensions remain speculative adventures.</p>
<p><a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> opens the wider collection. <a href="https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html">GAJRA Earth’s Ahead</a> connects current meetings and opportunities with work towards that larger future.</p>'''),
    dict(slug='sitemap', title='More of Tiggy’s world', intro='Play, art, music, travel and relationships. Follow a thread through his world.', image='wayfinder', alt='Brightly coloured sculptural archways lead along a sunny seaside festival walkway towards the ocean.', caption='Plenty of ways to spend the afternoon. GenAI story concept.', colour='orange', body='''
<p class="lead">Meet Tiggy through his humour, his company and the adventures that draw him onward.</p>
<h2>The life behind the character</h2>
<p>The <a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Australian Sire Story Forge</a> brings together the developing characters and story possibilities. <a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a> introduces Luke Nathan Hayes, their creator.</p>
<p><a href="https://auraofintelligence.github.io/australiansire/writer.html#three-personas">Luke, Tiggy and Australian Sire</a> explores the three romantic personalities growing from his life: Tiggy’s playful openness, Sire’s refined and particular desires, and Luke’s balance between them.</p>
<h2>The wider universe</h2>
<p>The <a href="https://auraofintelligence.github.io/sitemap.html">Aura site map</a> and <a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> lead into the work, music and imagined futures surrounding these stories.</p>'''),
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
