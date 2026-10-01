"""Build Tiggy's ten-page local character site using the Python standard library."""
from pathlib import Path
from html import escape
import os

ROOT = Path(__file__).resolve().parents[1]
SIRE_URL = os.environ.get('SIRE_PARTNER_URL', 'https://auraofintelligence.github.io/australiansire/')
VERSION = '20261001-public'

PAGES = [
    dict(slug='index', title='Tiggy Bestmann', intro='Artist. Traveller. Happy-go-lucky fool. A taste for a little mischief.', image='opening-world', alt='Two adult women, one visibly pregnant, welcome the long-haired Tiggy at an Istanbul ferry landing and draw him into a lively conversation.', caption='An invitation on the Bosphorus. Imagined Istanbul encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">After Tiggy’s presentation, she invites him to dinner across town. Her friend knows the band; he knows a rooftop nearby. Between them, an evening begins to take shape.</p>
<p>He has three days here. They intend to make good use of the evening.</p>
<h2>Between the work and the evening</h2>
<p>Long hair, glasses, an artist’s eye and a grin that tends to arrive just before the cheeky comment. Tiggy likes women who speak their minds, places that wake up after dark and invitations that require a quick change of clothes.</p>
<p>At dinner, she notices blue paint still caught on his wrist from the morning’s installation. There is a matching streak on hers. The afternoon’s swim has washed away almost everything else. They are still laughing about it when her friend arrives with the drinks.</p>
<h2>Three days in town</h2>
<p>His travels have a purpose and a pace. There are projects to deliver, workshops to run and people expecting him. He gets involved, puts in the effort and makes room for pleasure while he is there.</p>
<p>An outback festival needs a pair of hands. A Goa retreat needs an artist. A Nairobi reception leads to a private invitation. A woman asks whether he has time to see the city with her. His flight is tomorrow evening. They start talking about breakfast.</p>
<p>Her interest is clear. So is his smile.</p>
<h2>The pleasure of being invited</h2>
<p>He wants every country and territory, and more than a glimpse of each. There are things he wants to share, people he wants to learn from and places he wants to return to because of someone he met there.</p>
<p>The route stays open. So does his romantic life. A friend from the festival joins him for the next journey. A flirtation draws him into a whole circle of people with an expansive idea of love.</p>
<h2>Earth is the beginning</h2>
<p>Tiggy belongs to a much larger science-fiction romantasy universe: humanity spreading across planets, pursuing Kardashev ambitions and meeting extraterrestrial and extra-dimensional civilisations. AI and robotics run through the work and daily life of that imagined future.</p>
<p>On an orbital festival deck, she invites him to the rehearsal. Robots are moving the lighting rig; Earth turns beyond the glass. He joins her for the opening song. Afterwards, they start talking about the next port.</p>
<p class="big-line">“We were hoping you’d join us.”<br>His evening has just improved.</p>'''),
    dict(slug='fool', title='The happy-go-lucky fool', intro='He takes the joke and adds something of his own.', image='fool-outback', alt='Tiggy and two adult event crew members laugh while moving a drooping giant bird prop at an Australian outback arts gathering.', caption='A small setback in a very large idea. Imagined outback gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">“Something memorable?” she suggests, holding up a jacket the colour of a tropical bird. Tiggy produces a shirt that could give it competition. They both start laughing.</p>
<p>He likes a playful exchange. A little teasing, a ridiculous challenge, an invitation delivered with a perfectly straight face. One joke becomes another until neither remembers who started it.</p>
<h2>There is nerve beneath the grin</h2>
<p>The fool is an artist willing to put an unusual idea in front of people. He will perform the song, wear the outfit, try the dance and ask the question everybody else is politely avoiding.</p>
<p>A joke travels around the room, picking up a new detail with each telling. By the time it returns to Tiggy, he is laughing as hard as anyone.</p>
<h2>Mischief likes company</h2>
<p>At an outback arts gathering, he helps a crew bring a giant kinetic bird to life. One of the women gives it an extravagant bow. He returns the bow to the bird. By the time the audience arrives, they have accidentally invented the opening performance.</p>
<p>That is his sort of fun: a shared idea that gets better because people keep adding to it. The work still gets done. It simply develops a personality.</p>
<p>He brings that same spirit to romance. She surprises him, invites him closer and leaves him smiling at something she said long after she has left the room.</p>
<p class="big-line">Her expression gives her away.<br>He starts laughing before she says it.</p>'''),
    dict(slug='art', title='The night it comes alive', intro='The last light comes on. Across the room, she catches his eye.', image='artist', alt='Tiggy and an adult artist assemble a colourful kinetic sculpture in a sunny workshop.', caption='One more piece. Then they will see what moves. GenAI story concept.', colour='blue', body='''
<p class="lead">At six, it is still a pile of parts. At eight, strangers are queuing to get inside.</p>
<p>Tiggy is under the frame with a light between his teeth. His collaborator is above him, testing a sequence that turns the whole structure blue. They have been refining those seven seconds of darkness all afternoon.</p>
<p>Then it works. They look at each other before they look at the thing they have made.</p>
<h2>When the doors open</h2>
<p>His art has movement, noise and somewhere for people to stand. A sculpture catches the wind. A film fills an outdoor screen. A room answers the people inside it. He wants the moment when someone stops walking, forgets their phone and comes closer.</p>
<p>The work takes him into studios, festival yards and temporary crews around the world. Ideas pass between them: a rhythm becomes a movement, her colour changes his lighting, his film gives their installation another dimension.</p>
<h2>The people who made it</h2>
<p>The first visitors stop beneath the moving lights. Across the room, his collaborator catches his eye. Between them are the experiments, the discoveries and the moment they knew it was going to work. Tiggy likes that intimacy of making something together.</p>
<p>When she asks him to stay for the next project, she mentions that her studio has a spare room. Then she tells him about the festival they could go to afterwards.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/world-builder.html">World Builder</a> takes that ambition further: entire imagined places to make, inhabit and bring to life. He wants to see what happens when the visitors start changing the story.</p>'''),
    dict(slug='retreats', title='Aura retreats', intro='Five days of bright ideas, close company and very good reasons to stay for dinner.', image='retreat', alt='A visibly pregnant adult woman shares a playful light sculpture with Tiggy and another participant at an imagined coastal Aura retreat in Goa.', caption='Colour across the table. Conversation into the evening. Imagined Goa retreat. GenAI artwork.', colour='mint', body='''
<p class="lead">She turns the light sculpture in her hands. Colour travels across the table and up Tiggy’s sleeve. “Want a go?” she asks.</p>
<p>Outside, the palms are moving and the sea is close enough to hear. Inside, an Aura retreat has brought together people who want to make things, explore ideas and get to know one another while they do it.</p>
<h2>Curiosity looks good on him</h2>
<p>Tiggy arrives with skills to share and an appetite for what everyone else knows. They build avatars, explore memory palaces, try extended reality and turn an idea into a sculpture on the table.</p>
<p>His pregnant collaborator turns the sculpture while he changes the pattern of light. Her friend suggests adding sound. By lunch, their experiment has become something none of them arrived with. By dinner, the conversation has travelled well beyond it.</p>
<h2>The company continues</h2>
<p>Over dinner, she mentions the music drifting up from the beach. Tiggy has heard it too. They wander down together, shoes in hand, talking until the conversation gives way to dancing.</p>
<p>Luke’s Aura proposal gives these fictional scenes a five-day retreat and a nine-day teacher-training format, with coastal Goa among the possible settings. Around the workshop tables, people bring their own experience, exchange skills and make something none of them had imagined alone.</p>
<p>By the end of the week, their next experiment already has a place and a date. Neither seems in much of a hurry to say goodnight.</p>'''),
    dict(slug='out-about', title='Three days in town', intro='A workshop finished. A boat arriving. An evening unfolding between them.', image='out-about-world', alt='Two adult Thai women invite Tiggy to an evening gathering beside a Bangkok canal and an arriving passenger boat.', caption='The boat is coming. The evening is open. Imagined Bangkok encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Bangkok. The workshop is finished, and the three of them are watching the evening boats slide past.</p>
<p>Earlier, she asked whether he would join them for a performance. He has sent the file, changed his shirt and found the landing. Now their conversation moves between the show, somewhere to eat and a gallery he noticed on the way.</p>
<p>When their boat arrives, they are halfway through planning tomorrow.</p>
<h2>The reason he came</h2>
<p>A residency, a research visit, a paid pilot or a presentation gives Tiggy a reason to land. He has people expecting him and something to deliver. The <a href="https://auraofintelligence.github.io/global-founder-atlas/">Global Founder Atlas</a> belongs behind those journeys, connecting projects with places that might welcome them.</p>
<p>He travels quickly, but he wants more than a photograph proving he was there. Work gets him into a room. Curiosity keeps him in the conversation. Her invitation fills the few hours left with the part he remembers.</p>
<h2>Tomorrow is taking shape</h2>
<p>A festival tonight. A woman he wants to see again tomorrow. A new project in another city on Monday. His opportunity oracle brings the options together; he chooses which one to follow.</p>
<p>He wants every country and territory, with room to meet, share, learn and teach. There is no fixed route through that ambition. Relationships, useful work and the next extraordinary experience keep redrawing it.</p>
<p>Fast travel, full days and people he wants to spend those days with. The next chapter might begin before he reaches the airport.</p>'''),
    dict(slug='water', title='Sand, salt and screen', intro='The match runs into the afternoon. The afternoon becomes an evening together.', image='water', alt='Tiggy and two adult women laugh in shallow turquoise seawater with their bodyboards after a small wave.', caption='Back in the water. GenAI story concept.', colour='mint', body='''
<p class="lead">She wants Tiggy on her volleyball team. Apparently she likes his reach. The grin she exchanges with her friend suggests there may be another reason.</p>
<p>He is enjoying both possibilities.</p>
<h2>Before sunset</h2>
<p>There is a match on the sand, a decent swell and a screening to help set up before sunset. Tiggy has a board, a job to do and enough time for a thoroughly satisfying day.</p>
<p>Beyond the break, he and the Ocean Master trade stories between sets. Then a swell lifts them, the conversation stops and they paddle. Back on shore, each has a different account of the same wave.</p>
<h2>One place, several pleasures</h2>
<p>The proposed <a href="https://auraofintelligence.github.io/ballow-road-sand-screen-hub/">Ballow Road Sand &amp; Screen Hub</a> on Minjerribah brings together sand sports, outdoor cinema, markets and festival life.</p>
<p>In Tiggy’s imagined evening, he helps with the screen and sound, then washes off the day. Food stalls are opening. Friends are arriving. The woman from the court waves him over to the seat beside her.</p>
<p>She has brought her friends; he arrives with food from the stalls. Talk of one more drink turns into talk of the band. By the time the first song starts, they are all still there.</p>'''),
    dict(slug='company', title='The invitation matters', intro='She makes room beside her. He enjoys the invitation.', image='company-world', alt='Tiggy talks closely with two adult women, one visibly pregnant, at an art-filled rooftop gathering in Mexico City.', caption='The conversation has become the best part of the evening. Imagined Mexico City gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">She could have sent him the name of the restaurant. Instead, she comes to collect him.</p>
<p>Her friend is waiting downstairs. They have been talking about an exhibition, dinner and a rooftop view since yesterday. Tiggy has been looking forward to seeing them again.</p>
<h2>A particular appetite</h2>
<p>Adult women in their twenties and thirties, very full busts, pregnancy, confidence and cheek: Tiggy’s romantic imagination has its own distinct tastes. He enjoys direct interest and the pleasure of a woman choosing his company.</p>
<p>She begins the first encounter. He responds with interest of his own. Their conversation moves easily between curiosity and flirtation, each finding something in the other that makes them want to stay.</p>
<h2>More people to love. More world to share.</h2>
<p>He wants to love and be loved while his life keeps moving. A relationship might grow through return visits, shared journeys, creative work or an invitation into an established circle of friends and lovers.</p>
<p>An invitation into a larger circle of lovers gives him another life to imagine. The <a href="https://auraofintelligence.github.io/australiansire/group-marriages.html">group marriage exploration</a> follows that possibility in depth. Tiggy meets it through the people whose company he enjoys.</p>
<p>For now, they have an evening together. The conversation is already making dinner last longer than any of them expected.</p>'''),
    dict(slug='music', title='A song between them', intro='She sings a line. He finds a harmony. The band keeps playing.', image='music-world', alt='An adult Afro-Brazilian singer performs with Tiggy and another percussionist during a lively Salvador street gathering.', caption='A rhythm shared across the stage. Imagined Salvador festival. GenAI artwork.', colour='blue', body='''
<p class="lead">During the sound check, she asks whether he sings. A little later they are trying a harmony, then another, while the percussionist keeps time.</p>
<p>By evening, they have a verse neither is prepared to leave out.</p>
<h2>Another verse</h2>
<p>At the imagined Salvador street festival, the lights come on above a crowd that has been gathering since sunset. Tiggy recognises faces from the afternoon’s set-up. Beside him, she tries the first line, and their harmony finds its place above the drums.</p>
<p>He adds a phrase. She answers with a variation that makes him smile. The percussionist carries it on, and the song grows another verse.</p>
<h2>After the applause</h2>
<p>Tiggy likes the whole life around a performance. Rehearsal, set-up, the show itself, then food with the people who made it happen. There are stories you only hear when the equipment is packed and nobody needs to watch the time quite so closely.</p>
<p>The singer has saved him a place at the table. Now he gets to hear what she sounds like when she is simply enjoying the conversation.</p>
<p>The <a href="https://auraofintelligence.github.io/i-C-infinity-music-universe/">i C. infinity music universe</a> gives this side of Tiggy room to grow: songs, characters and imagined lives with an audience to share them.</p>'''),
    dict(slug='possibilities', title='How big are we talking?', intro='Festivals between worlds. Humanity across planets. An invitation into a much larger universe.', image='possibilities-world', alt='Two Kenyan artists share a model of a floating cinema and festival venue with Tiggy at a Nairobi evening reception.', caption='A formal invitation. A much less formal conversation. Imagined Nairobi reception. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy arrives at a Nairobi reception. The model on the table suggests he has drastically underdressed his imagination.</p>
<p>A screen rises above the water. Walkways connect stages, gardens and places to sit. The artist beside him points out where the audience arrives. Her colleague asks what he would put on the opening programme.</p>
<p>He has an answer. Her expression suggests she rather likes it.</p>
<h2>An opening night on the water</h2>
<p>In Nairobi, the scene is an elegant reception and a very ambitious model. Elsewhere it could be a festival linked across cities, a responsive world built by its visitors or a performance he has travelled halfway around the planet to help deliver.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/aura-events.html">events concept</a> stretches from intimate gatherings to grand galas and global festivals. <a href="https://auraofintelligence.github.io/space-industry.html">Moonlight Frontier</a> goes further, imagining low-gravity sport and lunar adventure. Tiggy is already picturing the game, the view and the people he would like to take with him.</p>
<h2>Someone has to make it happen</h2>
<p><a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> connects the work behind these possibilities. <a href="https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html">GAJRA Earth’s Ahead</a> follows dated meetings and openings to contribute. For Tiggy, the idea comes alive around the table, talking through his part with people he wants to work with.</p>
<p>He has limited time and plenty he wants to do. The project has caught his imagination. So have the people around the table. By the time dinner arrives, he has offered to help with the opening.</p>
<p>Then someone mentions the after-party.</p>
<h2>Humanity across planets</h2>
<p>The larger universe follows humanity into life across planets, with energy ambitions reaching up the Kardashev scale. AI and robotics are part of how people build, travel, create and look after the places they share. Tiggy’s art and relationships travel through that changing world.</p>
<p>A lunar festival gives the dancers a very different leap. At an orbital cinema, the view competes with the film. A woman invites him to join a performance whose next stop is another planet. His enthusiasm arrives before he has finished reading the programme.</p>
<h2>Company from other worlds</h2>
<p>Extraterrestrial and extra-dimensional civilisations bring their own music, celebrations, histories and humour into the fiction. Tiggy meets people for whom a familiar human gesture means something entirely different. She explains why they are both laughing. He has another question, and neither is ready to leave.</p>
<p>Love, desire and larger relationships belong within that immense universe. The journey carries the pleasure of being invited, the effort of making something together and the anticipation of meeting again across worlds.</p>
<h2>The work behind the horizon</h2>
<p>Luke sees this fiction as a preview of futures taking shape through global thinkers, researchers and builders. <a href="https://www.nasa.gov/moontomarsarchitecture-strategyandobjectives/">NASA’s Moon to Mars strategy</a> develops the path towards sustained human exploration beyond Earth. <a href="https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/">Google DeepMind’s Gemini Robotics work</a> brings AI into physical tasks. The stories follow those beginnings into a much wider imagined life.</p>
<p>Contact with other civilisations and journeys across dimensions are part of that speculative horizon. These pages offer an early glimpse of the universe Luke is building.</p>'''),
    dict(slug='sitemap', title='More of Tiggy’s world', intro='Journeys, company and the things that happen along the way.', image='wayfinder', alt='Brightly coloured sculptural archways lead along a sunny seaside festival walkway towards the ocean.', caption='Plenty of ways to spend the afternoon. GenAI story concept.', colour='orange', body='''
<p class="lead">A few days in a new city. An artist with something to contribute. An invitation that becomes an evening they are all enjoying.</p>
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
<section class="partner-panel"><div><h2>Meet Australian Sire</h2><p>A writer and traveller with particular desires and a vast universe to explore. Another expression of Luke’s imagined world.</p></div><a href="{escape(SIRE_URL,quote=True)}">Visit the partner site ↗</a></section></main>
<nav class="page-turn" aria-label="Previous and next pages"><a rel="prev" href="{prev['slug']}.html"><span>← Previous</span><strong>{escape(prev['title'])}</strong></a><a rel="next" href="{nxt['slug']}.html"><span>Next →</span><strong>{escape(nxt['title'])}</strong></a></nav>
<footer><p>Tiggy Bestmann<br>A fictional character by Luke Nathan Hayes.</p><nav class="footer-links" aria-label="Related sites and licence"><a href="sitemap.html">Site map ↗</a><a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Story Forge</a><a href="https://auraofintelligence.github.io/loose-goose-comedy-engine/">Loose Goose Comedy Engine</a><a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a><a href="https://github.com/auraofintelligence/tiggy-bestmann/blob/main/LICENCE.md">Strange But True licence</a></nav></footer><a class="to-top" href="#top" aria-label="Back to top">↑</a></body></html>''',encoding='utf-8')
print(f'Built {len(PAGES)} Tiggy pages.')
