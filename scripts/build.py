"""Build Tiggy's ten-page local character site using the Python standard library."""
from pathlib import Path
from html import escape
import os

ROOT = Path(__file__).resolve().parents[1]
SIRE_URL = os.environ.get('SIRE_PARTNER_URL', 'https://auraofintelligence.github.io/australiansire/')
VERSION = '20261001-history-music'

PAGES = [
    dict(slug='index', title='Tiggy Bestmann', intro='Artist. Traveller. Happy-go-lucky fool. A taste for a little mischief.', image='opening-world', alt='Two adult women, one visibly pregnant, welcome the long-haired Tiggy at an Istanbul ferry landing and draw him into a lively conversation.', caption='An invitation on the Bosphorus. Imagined Istanbul encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy Bestmann is the happy-go-lucky fool, artist and student of life. He wants love in abundance, a world to explore and plenty of fun along the way.</p>
<p>Cheeky, inventive and sometimes awkward, he brings a playful spirit to big ideas. His name began with Luke’s childhood dog, a street and a game of tag. <a href="fool.html#the-name">That story still lives in him.</a></p>
<h2>Between the work and the evening</h2>
<p>Long hair, glasses and an artist’s curiosity. His interests run through philosophy, art, science, music, bodyboarding and the technologies he wants to help bring into being.</p>
<p>He is open to adult women of many forms and personalities. Joyful, energetic and exploratory companionship draws him in. Women begin his first encounters; what follows grows through their mutual interest.</p>
<h2>A long-held music ambition</h2>
<p>In 2004, Luke helped set up Glastonbury during his UK working holiday. He wanted to return one day as a performer. Now he has bought an Audima Labs Sway MIDI controller, and Tiggy will explore learning to perform his i C. infinity music with it.</p>
<p><a href="music.html">From the festival crew to the ambition of a stage ↗</a></p>
<h2>Fast travel, full days</h2>
<p>His travels have a purpose and a pace. There are projects to deliver, workshops to run and people expecting him. He gets involved, puts in the effort and makes room for pleasure while he is there.</p>
<p>Outback gatherings, beach culture, sports, festivals and high society give his travels their variety. Work is part of the journey; so are comedy, risk, enjoyment and the people he meets.</p>
<h2>The pleasure of being invited</h2>
<p>He wants every country and territory, and more than a glimpse of each. There are things he wants to share, people he wants to learn from and places he wants to return to because of someone he met there.</p>
<p>The route stays open. So does his romantic life. The desire to love and be loved reaches through shared journeys, returning to people he misses and exploring larger relationships.</p>
<h2>Earth is the beginning</h2>
<p>Tiggy belongs to a much larger science-fiction romantasy universe: humanity spreading across planets, pursuing Kardashev ambitions and meeting extraterrestrial and extra-dimensional civilisations. AI and robotics run through the work and daily life of that imagined future.</p>
<p>His history travels with him too. Flashbacks open earlier work, places and ambitions within the adventure. <a href="art.html#remembering">Body, mind and place/soul story</a> connect the remembered life with the future he is exploring.</p>'''),
    dict(slug='fool', title='The happy-go-lucky fool', intro='He takes the joke and adds something of his own.', image='fool-outback', alt='Tiggy and two adult event crew members laugh while moving a drooping giant bird prop at an Australian outback arts gathering.', caption='A small setback in a very large idea. Imagined outback gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">The innocent fool wants to play. Tiggy’s humour is cheeky, his curiosity is lively and his romantic life is open to discovery.</p>
<p>He likes a playful exchange. A little teasing, a ridiculous challenge, an invitation delivered with a perfectly straight face. One joke becomes another until neither remembers who started it.</p>
<h2 id="the-name">A dog, a street and a game</h2>
<p>Luke’s childhood dog was called Tiggy. Tiggy was also the name for the game of tag he played then: running, laughing and wanting another turn. Bestmann Road was his childhood street.</p>
<p>First pet plus first street: the old make-your-porn-star-name game produced Tiggy Bestmann. The joke also asks for two familiar account-recovery answers. Luke tells the origin openly. The name joins childhood play with an adult sense of mischief.</p>
<p>That playful spirit lives in the character: the innocent fool with love in abundance, wanting joyful, energetic and exploratory companionship. He is an adult artist and traveller, still delighted when someone wants to play.</p>
<p><a href="https://auraofintelligence.github.io/australiansire/writer.html#three-personas">Luke, Tiggy and Australian Sire</a> opens the fuller story of the three personalities in Luke’s romantasy.</p>
<h2>There is nerve beneath the grin</h2>
<p>The fool is an artist willing to put an unusual idea in front of people. He will perform the song, wear the outfit, try the dance and ask the question everybody else is politely avoiding.</p>
<p>A joke travels around the room, picking up a new detail with each telling. By the time it returns to Tiggy, he is laughing as hard as anyone.</p>
<h2>Mischief likes company</h2>
<p>Art, music, festivals and shared adventures give his mischief plenty of company. He enjoys the moment an idea becomes something people want to join.</p>
<p>That is his sort of fun: a shared idea that gets better because people keep adding to it. The work still gets done. It simply develops a personality.</p>
<p>He brings that same spirit to romance. She surprises him, invites him closer and leaves him smiling at something she said long after she has left the room.</p>
<p class="big-line">Her expression gives her away.<br>He starts laughing before she says it.</p>'''),
    dict(slug='art', title='Art, memory and imagined worlds', intro='A life remembered. An idea taking form. A world still opening.', image='artist', alt='Tiggy and an adult artist assemble a colourful kinetic sculpture in a sunny workshop.', caption='Making something together. GenAI visual interpretation.', colour='blue', body='''
<p class="lead">Art, philosophy and science meet in Tiggy’s imagination. He is interested in making things, experiencing them with other people and exploring what they reveal.</p>
<h2>Making Aura</h2>
<p>Building Aura O.Z. with a team is one of the ambitions in the Story Forge. Digital twins, immersive environments and ways of reflecting on experience give that work both a practical and a personal life.</p>
<p>Web, design, mechanical, electrical and event work form part of the history behind the dream. Music and worldbuilding bring other ways to express it.</p>
<h2 id="remembering">Body, mind and place/soul story</h2>
<p>Luke is mapping his history to help remember the experiences that shaped him. His <a href="https://auraofintelligence.github.io/Lukes-world-of-work-experience/">work history map</a> is already public. A travel history map is planned.</p>
<p>Work, travel, music, places, memories and reflection contribute to his digital twins of body, mind and place/soul story. The maps connect those experiences so an earlier part of life is easier to find and revisit.</p>
<h2>Flashbacks through a life</h2>
<p>Any part of Luke’s history is available for exploration in flashbacks. Tiggy’s story moves between remembered experience, present intentions and fantasy. A long-held ambition, such as <a href="music.html#glastonbury">performing at Glastonbury</a>, carries its history into the next chapter.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/world-builder.html">World Builder</a> takes that ambition further: entire imagined places to make, inhabit and bring to life. He wants to see what happens when the visitors start changing the story.</p>'''),
    dict(slug='retreats', title='Aura retreats', intro='Five days of bright ideas, close company and very good reasons to stay for dinner.', image='retreat', alt='A visibly pregnant adult woman shares a playful light sculpture with Tiggy and another participant at an imagined coastal Aura retreat in Goa.', caption='Colour across the table. Conversation into the evening. Imagined Goa retreat. GenAI artwork.', colour='mint', body='''
<p class="lead">Aura retreats bring creative technology, reflection, culture and company into the same stretch of time. Tiggy is interested in the ideas and the people exploring them.</p>
<p>Avatars, memory palaces, extended reality and practical making sit alongside music, food and adventure in Luke’s retreat proposal.</p>
<h2>Curiosity looks good on him</h2>
<p>Tiggy has skills to share and an appetite for what other people know. His interest in learning belongs with his pleasure in making, playing and spending time together.</p>
<h2>The company continues</h2>
<p>The Story Forge’s retreat pod explores a group growing close over a fortnight, then discovering what that connection becomes after the stay ends.</p>
<p>Luke’s separate Aura retreat proposal sets out five days of creative exploration, with a nine-day teacher-training format for a longer stay. Coastal Goa is one proposed setting.</p>
<p>The workshop, the friendships and the possibility of romance reach into the same imagined experience. Who meets and how those relationships unfold remain open.</p>'''),
    dict(slug='out-about', title='Fast travel, full days', intro='Useful work, unfamiliar places and time worth enjoying.', image='out-about-world', alt='Two adult Thai women invite Tiggy to an evening gathering beside a Bangkok canal and an arriving passenger boat.', caption='The boat is coming. The evening is open. Imagined Bangkok encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy wants to visit every country and territory: to meet, share, learn and teach, and enjoy the life happening around him.</p>
<p>The travel is fast and action-packed, with limited time, work involved and plenty of fun. Different continents and cultures take him from the outback to high society, beach life, sports and festivals.</p>
<h2>The reason he came</h2>
<p>A residency, a research visit, a paid pilot or a presentation gives Tiggy a reason to land. He has people expecting him and something to deliver. The <a href="https://auraofintelligence.github.io/global-founder-atlas/">Global Founder Atlas</a> belongs behind those journeys, connecting projects with places that might welcome them.</p>
<p>He travels quickly, but he wants more than a photograph proving he was there. Work gets him into a room. Curiosity keeps him in the conversation. Her invitation fills the few hours left with the part he remembers.</p>
<h2>Tomorrow is taking shape</h2>
<p>The travel oracle brings work, gatherings, relationships and other opportunities together. It leaves the route open to changing interests and serendipity.</p>
<p>He wants every country and territory, with room to meet, share, learn and teach. There is no fixed route through that ambition. Relationships, useful work and the next extraordinary experience keep redrawing it.</p>
<p>Fast travel, full days and people he wants to spend those days with. The next chapter might begin before he reaches the airport.</p>'''),
    dict(slug='water', title='Sand, salt and screen', intro='The match runs into the afternoon. The afternoon becomes an evening together.', image='water', alt='Tiggy and two adult women laugh in shallow turquoise seawater with their bodyboards after a small wave.', caption='Back in the water. GenAI story concept.', colour='mint', body='''
<p class="lead">Bodyboarding and powerful waves belong to Tiggy’s adventure. Beach life, sand sports, outdoor cinema and festivals bring other pleasures to the shore.</p>
<h2>Before sunset</h2>
<p>The Story Forge names an ambition to ride an epic wave. Reading the ocean, timing and physical skill give that ambition its substance.</p>
<p>The Ocean Master is one of the Forge’s possible companions: an experienced wave rider with knowledge of the break and its seasons. That connection opens bodyboarding culture within the larger story.</p>
<h2>One place, several pleasures</h2>
<p>The proposed <a href="https://auraofintelligence.github.io/ballow-road-sand-screen-hub/">Ballow Road Sand &amp; Screen Hub</a> on Minjerribah brings together sand sports, outdoor cinema, markets and festival life.</p>
<p>For Tiggy, that combination connects outdoor play, creative work and social life. The water, the sport, the films and the company each give him a reason to enjoy being there.</p>'''),
    dict(slug='company', title='The invitation matters', intro='She makes room beside her. He enjoys the invitation.', image='company-world', alt='Tiggy talks closely with two adult women, one visibly pregnant, at an art-filled rooftop gathering in Mexico City.', caption='The conversation has become the best part of the evening. Imagined Mexico City gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">Tiggy wants to love and be loved, with fun, joy, energy and exploratory companionship running through his romantic life.</p>
<h2>The pleasure of her company</h2>
<p>Tiggy is drawn to adult women of many forms and personalities. A shared laugh, lively curiosity and the pleasure of exploring together draw him closer. There is no fixed body type at the heart of his attraction; he wants to enjoy the woman he is with.</p>
<p>She begins the first encounter. He responds with interest of his own. Their conversation moves easily between curiosity and flirtation, each finding something in the other that makes them want to stay.</p>
<h2>More people to love. More world to share.</h2>
<p>He wants to love and be loved while his life keeps moving. A relationship might grow through return visits, shared journeys, creative work or an invitation into an established circle of friends and lovers.</p>
<p>An invitation into a larger circle of lovers gives him another life to imagine. The <a href="https://auraofintelligence.github.io/australiansire/group-marriages.html">group marriage exploration</a> follows that possibility in depth. Tiggy meets it through the people whose company he enjoys.</p>
'''),
    dict(slug='music', title='From Glastonbury to Sway', intro='He helped build the festival. He wanted to return as a performer. The ambition is still alive.', image='music-world', alt='An adult Afro-Brazilian singer performs with Tiggy and another percussionist during a lively Salvador street gathering.', caption='Music and shared performance. GenAI visual interpretation, imagined in Salvador.', colour='blue', body='''
<p class="lead">Tiggy’s music ambition has a long memory. It begins on the crew side of Glastonbury, with Luke wondering about a future on stage.</p>
<h2 id="glastonbury">The UK working holiday, 2004</h2>
<p>Luke worked with W.A.A.P. Wing and a Prayer Event Services during his UK working holiday, helping set up major music festivals, including Glastonbury. One of his goals from that time was to perform at Glastonbury someday.</p>
<p>His <a href="https://auraofintelligence.github.io/Lukes-world-of-work-experience/">work history map</a> records that festival season. The ambition travels from that history into Tiggy’s story.</p>
<h2 id="sway">Sway is on its way</h2>
<p>Luke has bought an <a href="https://audima.com.au/">Audima Labs Sway MIDI controller</a> from batch 4. He expects it to arrive in November or December 2026.</p>
<p>Once it arrives, Tiggy will explore learning to perform Luke’s i C. infinity music with it. The learning is ahead: getting familiar with the instrument, experimenting and finding his own way into performance.</p>
<h2>Performing i C. infinity</h2>
<p>The songs already carry characters, ideas and imagined lives. Performing them adds another way to explore that universe, with movement and musical expression becoming part of the experience.</p>
<p>The Story Forge includes performing music for a living audience among its ambitions. Sway gives that interest a present starting point in Luke’s life.</p>
<h2>Where fantasy takes it</h2>
<p>Glastonbury remains a real ambition. Beyond it, the fiction opens festivals, journeys and encounters across a much larger universe. Where the music begins to take Tiggy is still an open story.</p>
<p>A flashback to the 2004 festival season brings the earlier hope into the present. Other parts of Luke’s history offer their own entrances into the music and the adventure.</p>
<p>More songs, characters and imagined lives await in the <a href="https://auraofintelligence.github.io/i-C-infinity-music-universe/">i C. infinity music universe</a>.</p>'''),
    dict(slug='possibilities', title='How big are we talking?', intro='Festivals between worlds. Humanity across planets. An invitation into a much larger universe.', image='possibilities-world', alt='Two Kenyan artists share a model of a floating cinema and festival venue with Tiggy at a Nairobi evening reception.', caption='A formal invitation. A much less formal conversation. Imagined Nairobi reception. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy’s imagination reaches from music and travel into whole civilisations. Art, technology, relationships and joyful responsible abundance run through the worlds he wants to explore.</p>
<h2>The Worldbuilding Challenge Festival</h2>
<p>The Story Forge imagines teams pitching whole civilisations at a futures festival. A pitch arena leads into a build sprint: a short film, a working simulation and a world bible, with an island campus residency in view.</p>
<p>It brings philosophy, science, art and filmmaking into one of the universe’s larger adventures.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/aura-events.html">events concept</a> stretches from intimate gatherings to grand galas and global festivals. <a href="https://auraofintelligence.github.io/space-industry.html">Moonlight Frontier</a> goes further, imagining low-gravity sport and lunar adventure. Tiggy is already picturing the game, the view and the people he would like to take with him.</p>
<h2>Someone has to make it happen</h2>
<p><a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> connects the work behind these possibilities. <a href="https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html">GAJRA Earth’s Ahead</a> follows dated meetings and openings to contribute. For Tiggy, the idea comes alive around the table, talking through his part with people he wants to work with.</p>
<h2>Humanity across planets</h2>
<p>The larger universe follows humanity into life across planets, with energy ambitions reaching up the Kardashev scale. AI and robotics are part of how people build, travel, create and look after the places they share. Tiggy’s art and relationships travel through that changing world.</p>
<h2>Company from other worlds</h2>
<p>Extraterrestrial and extra-dimensional civilisations bring unfamiliar experiences of life into the fiction. The Forge includes envoys from hidden and sub-oceanic societies, visitors with different lineages and a Starmind Interpreter.</p>
<p>Love, desire and larger relationships belong within that immense universe. The journey carries the pleasure of being invited, the effort of making something together and the anticipation of meeting again across worlds.</p>
<h2>The work behind the horizon</h2>
<p>Luke sees this fiction as a preview of futures taking shape through global thinkers, researchers and builders. <a href="https://www.nasa.gov/moontomarsarchitecture-strategyandobjectives/">NASA’s Moon to Mars strategy</a> develops the path towards sustained human exploration beyond Earth. <a href="https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/">Google DeepMind’s Gemini Robotics work</a> brings AI into physical tasks. The stories follow those beginnings into a much wider imagined life.</p>
<p>Contact with other civilisations and journeys across dimensions are part of that speculative horizon. These pages offer an early glimpse of the universe Luke is building.</p>'''),
    dict(slug='sitemap', title='More of Tiggy’s world', intro='Journeys, company and the things that happen along the way.', image='wayfinder', alt='Brightly coloured sculptural archways lead along a sunny seaside festival walkway towards the ocean.', caption='Plenty of ways to spend the afternoon. GenAI story concept.', colour='orange', body='''
<p class="lead">Play, art, music, work, travel and relationships open different parts of Tiggy’s life.</p>
<p>Tiggy’s world unfolds through ten connected pages of travel, art, work, romance and playful possibilities. Each opens a different part of the life he wants to enjoy.</p>
<h2>Behind the stories</h2>
<p>The <a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Australian Sire Story Forge</a> holds the developing characters and possibilities. <a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a> introduces Luke Nathan Hayes, their creator.</p>
<p><a href="fool.html#the-name">Where Tiggy’s name began</a> leads back to Luke’s childhood. <a href="https://auraofintelligence.github.io/australiansire/writer.html#three-personas">Luke, Tiggy and Sire</a> introduces their different romantic personalities.</p>
<p><a href="music.html#glastonbury">The Glastonbury ambition</a> connects the 2004 working holiday with learning to perform i C. infinity. <a href="art.html#remembering">Art, memory and imagined worlds</a> connects the history maps with body, mind and place/soul story.</p>
<p>The <a href="https://auraofintelligence.github.io/sitemap.html">Aura site map</a> and <a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> open the wider collection of projects and imagined futures that give these stories their settings and ambitions.</p>'''),
]

PLAY = '''<section class="play-panel" aria-labelledby="play-title"><div><h2 id="play-title">Follow an interest</h2><p>Music, waves and the next journey.</p><div class="mood-buttons" role="group" aria-label="Choose an interest"><button type="button" data-mood="make" aria-pressed="true">Music</button><button type="button" data-mood="wander" aria-pressed="false">Waves</button><button type="button" data-mood="company" aria-pressed="false">Travel</button></div><div class="play-result" aria-live="polite" aria-atomic="true"><h3>From Glastonbury to Sway.</h3><p>The wish to perform began while Luke was helping set up Glastonbury in 2004. Learning to perform i C. infinity with Sway is the next exploration.</p></div></div><a class="round-link" href="music.html" aria-label="From Glastonbury to Sway">↗</a></section>'''

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
<section class="partner-panel"><div><h2>Meet Australian Sire</h2><p>A writer and traveller with particular desires and a vast universe to explore. Another expression of Luke’s imagined world.</p></div><a href="{escape(SIRE_URL,quote=True)}">Visit the partner site ↗</a></section></main>
<nav class="page-turn" aria-label="Previous and next pages"><a rel="prev" href="{prev['slug']}.html"><span>← Previous</span><strong>{escape(prev['title'])}</strong></a><a rel="next" href="{nxt['slug']}.html"><span>Next →</span><strong>{escape(nxt['title'])}</strong></a></nav>
<footer><p>Tiggy Bestmann<br>A fictional character by Luke Nathan Hayes.</p><nav class="footer-links" aria-label="Related sites and licence"><a href="sitemap.html">Site map ↗</a><a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Story Forge</a><a href="https://auraofintelligence.github.io/loose-goose-comedy-engine/">Loose Goose Comedy Engine</a><a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a><a href="https://github.com/auraofintelligence/tiggy-bestmann/blob/main/LICENCE.md">Strange But True licence</a></nav></footer><a class="to-top" href="#top" aria-label="Back to top">↑</a></body></html>''',encoding='utf-8')
print(f'Built {len(PAGES)} Tiggy pages.')
