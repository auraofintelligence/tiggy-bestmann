"""Build Tiggy's ten-page local character site using the Python standard library."""
from pathlib import Path
from html import escape
import os

ROOT = Path(__file__).resolve().parents[1]
SIRE_URL = os.environ.get('SIRE_PARTNER_URL', 'http://127.0.0.1:4173/')
VERSION = '20260929-3'

PAGES = [
    dict(slug='index', title='Tiggy Bestmann', intro='Happy-go-lucky fool. Artist. Student of life. Out in the world, seeing who he meets.', image='opening-world', alt='Two adult women, one visibly pregnant, welcome the long-haired Tiggy at an Istanbul ferry landing and draw him into a lively conversation.', caption='An invitation on the Bosphorus. Imagined Istanbul encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy wants a big, interesting life: world travel, relationships, comedy, a bit of risk and a great deal of enjoyment.</p>
<p>He is an artist and a happy-go-lucky fool with an appetite for places and people. Long hair, glasses, a cheeky curiosity and enough confidence to find himself somewhere he has absolutely no idea how to behave.</p>
<h2>From red dust to the reception</h2>
<p>An outback gathering. A beach full of wave riders. A street festival on another continent. An elegant evening where the woman beside him has a much more interesting invitation than the one printed on the card.</p>
<p>He likes that range. Different cultures, different company, different ways of enjoying life. The journey changes with the people he meets and the relationships that begin to matter.</p>
<h2>Fast trips. Full days.</h2>
<p>There is work involved and only so much time. A workshop to help deliver, a festival to get running, a presentation to finish before the evening begins. Tiggy wants to do his part and still squeeze in the match, the swim, the conversation and the invitation he did not see coming.</p>
<p>Sand sports in the afternoon, outdoor cinema at dusk, music afterwards. He likes a place that can hold all three, with people moving between the action and the company.</p>
<h2>Follow the chemistry</h2>
<p>Attraction is part of the adventure. He is drawn to younger adult women, very full busts, pregnancy, warmth and a playful spark. He wants to love and be loved, share experiences and discover where an unexpected connection might lead.</p>
<p>Art and curiosity give him ways into a place. Humour helps when his grand entrance goes slightly wrong. An Aura retreat, a sporting challenge or a spectacular creative gathering can open a whole new chapter.</p>
<p class="big-line">The world is big. He would like a look.</p>'''),
    dict(slug='fool', title='The happy-go-lucky fool', intro='Curiosity is winning. Dignity can catch up later.', image='fool-outback', alt='Tiggy and two adult event crew members laugh while moving a drooping giant bird prop at an Australian outback arts gathering.', caption='A small setback in a very large idea. Imagined outback gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">Tiggy has a cheerful willingness to look a bit silly. An interesting idea gets a chance before he has worked out how impressive he will look doing it.</p>
<p>The Forge calls him the honest fool: awkward, cheeky, inventive and inclined to say what he actually thinks. His timing can be excellent. It can also be entertaining for entirely different reasons.</p>
<h2>Give the idea a go</h2>
<p>A spectacular event in the middle of the outback. A dance he nearly understands. A moment on stage before he has quite worked out what he agreed to. Tiggy enjoys that leap between wondering and trying.</p>
<p>If it goes sideways, there is a pause, a look at whoever is standing next to him and often a laugh. Then someone suggests a much better way of doing it.</p>
<h2>Good company helps</h2>
<p>He likes people who can tease him, surprise him and bring their own ridiculous idea. A shared joke can make a new place feel familiar very quickly.</p>
<p>There is room for risk in his stories: creative nerve, physical adventure and the emotional leap of letting someone see what he really wants. He can get it wrong. That is often where the comedy, and the next interesting conversation, begins.</p>
<p>Being the fool leaves him plenty of room to be curious. He can ask the obvious question, admit he has no idea and discover that the answer is far more interesting than his first guess.</p>
<p class="big-line">That seemed like a much better idea ten seconds ago.</p>'''),
    dict(slug='art', title='Make a glorious mess', intro='Colour. Movement. Sound. Something that did not exist this morning.', image='artist', alt='Tiggy and an adult artist assemble a colourful kinetic sculpture in a sunny workshop.', caption='One more piece. Then they will see what moves. GenAI story concept.', colour='blue', body='''
<p class="lead">Tiggy makes things because an idea has got into his head and he wants to see what happens when it comes out.</p>
<p>It might become an object, a tune, a performance or a whole strange little world. He likes work you can walk around, listen to, play with or talk about while somebody puts the kettle on.</p>
<h2>Follow the interesting part</h2>
<p>A moving shape becomes a character. A sound suggests a scene. Somebody turns a piece the wrong way around and suddenly it is the best part of the thing.</p>
<p>He enjoys those accidental discoveries. Making gives him a reason to experiment, change his mind and keep one beautiful bit from an otherwise questionable attempt.</p>
<h2>Bring someone else into it</h2>
<p>Another artist sees a different possibility. A musician hears something he missed. A friend arrives to have a look and is soon holding one end while he tries to find the right tool.</p>
<p>The work can become a social occasion before it becomes a finished object. Tiggy is quite happy about that. He likes the making, the company and the moment somebody says, “What if we tried this?”</p>
<h2>Make something worth travelling for</h2>
<p>An installation for a festival, a short film for an outdoor screening, a performance built with artists he has just met. There is a deadline, a place to open and an audience on its way. That gives the experimenting a useful kick.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/world-builder.html">World Builder</a> stretches that impulse into imagined worlds people can explore. Tiggy would like to help make one, then see who turns up to play.</p>'''),
    dict(slug='retreats', title='Aura retreats', intro='Meet for the experience. Stay curious about each other.', image='retreat', alt='A visibly pregnant adult woman demonstrates a playful light sculpture to Tiggy and another participant at an imagined coastal Aura retreat in Goa.', caption='Something to learn. Someone worth listening to. Imagined Goa retreat. GenAI artwork.', colour='mint', body='''
<p class="lead">An Aura retreat gives Tiggy a reason to spend more than an afternoon with an interesting group of people. There is something to make, plenty to try and time for the conversation to get personal.</p>
<p>Luke’s retreat proposal has a five-day retreat and a nine-day teacher-training format. It brings creative technology, self-reflection, learning and cultural experiences into the same gathering.</p>
<h2>Have a go together</h2>
<p>They might build a digital avatar, explore a memory palace, try extended reality, make a smart object or turn an idea into a 3D print. Tiggy brings art, practical curiosity and the occasional confidently wrong guess.</p>
<p>Someone shows him a better way. He finds something he can help with. The group starts to know one another through what they make, what they laugh at and where their conversations wander.</p>
<h2>The day continues outside</h2>
<p>The source proposal includes music, dance, cuisine, languages, storytelling and adventure, with a coastal Goa setting among its possibilities. A workshop can lead into a swim, a shared meal, a performance or a quiet conversation that neither person wants to end.</p>
<p>Attraction and relationships can develop through the repeated company. The retreat becomes part of the travel story, with its own friendships, chemistry and reasons to meet again.</p>
<h2>Student, then someone with something to share</h2>
<p>The teacher-training idea includes maintaining tools, presenting to a group and helping someone one to one. That suits a student of life who enjoys passing something on when he has got the hang of it.</p>
<p>For this fictional world, the retreat is a setting for learning, enjoyment and human connection, drawn from Luke’s proposal.</p>'''),
    dict(slug='out-about', title='Out in the world', intro='Different continents. Different cultures. A very personal journey.', image='out-about-world', alt='Two adult Thai women invite Tiggy to an evening gathering beside a Bangkok canal and an arriving passenger boat.', caption='The boat is coming. The evening is open. Imagined Bangkok encounter. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy travels with a lively interest in what is going on around the next corner. A place becomes interesting through its people, sounds, food and small surprises.</p>
<p>He likes markets, waterfronts, local music, working studios and the sort of gathering where somebody makes room for another person at the table.</p>
<p>A city festival in Brazil feels different from an outback gathering in Australia. A canal-side invitation in Bangkok opens a different evening from a formal reception in Nairobi. The people, language, atmosphere and possibilities change with the place.</p>
<h2>A good reason to wander</h2>
<p>A friend mentions a festival. A conversation leads to a workshop. Someone points out a beach he would have walked straight past. He follows the possibility far enough to see what is there.</p>
<p>The travelogue follows his own interests: romance, sport, art, laughter and big experiences. A relationship can change where he wants to go next, who travels with him or which place he is looking forward to seeing again.</p>
<h2>Meet, share, learn, enjoy</h2>
<p>He brings his own stories and curiosity, lends a hand where he can and enjoys being shown something through another person’s eyes.</p>
<p>A return visit can have its own pleasure: a familiar laugh, a place that has changed, a half-finished conversation suddenly picking up again. There is always another way to spend the day.</p>
<h2>A window opens. Get moving.</h2>
<p>A creative residency, a research visit, a paid pilot or an invitation to present can give a journey its purpose and its time limit. The <a href="https://auraofintelligence.github.io/global-founder-atlas/">Global Founder Atlas</a> is part of that wider opportunity picture. Tiggy’s story follows the work, the people and what happens around the edges.</p>
<p>There might be three days between arrival and the next departure. Finish the session, help pack up, change clothes and meet the woman who said she would show him the city. A short trip can still carry a lot of life.</p>
<p>An opportunity oracle brings together invitations, project needs, events, travel time and the relationships he wants to make time for. The ambition reaches every country and territory; the next move stays open to what actually comes together.</p>'''),
    dict(slug='water', title='Just add water', intro='A board, a bit of sunshine and a very good reason to get wet.', image='water', alt='Tiggy and two adult women laugh in shallow turquoise seawater with their bodyboards after a small wave.', caption='Back in the water. GenAI story concept.', colour='mint', body='''
<p class="lead">The ocean gets Tiggy out of his own head. There is water moving, a board under him and something happening right now.</p>
<p>Bodyboarding belongs in his world. So do sandy feet, salt in his hair, the laugh after a missed wave and the conversation that carries on when everybody comes back to shore.</p>
<h2>One more wave</h2>
<p>He enjoys the rhythm of it: watch, wait, paddle, go. A good ride can keep him smiling long after it is over.</p>
<p>The Forge gives him an Ocean Master to learn from, someone who reads water with a skill he wants to understand. The shared interest makes room for curiosity, company and another reason to return.</p>
<h2>The rest of the beach day</h2>
<p>Afterwards there might be food, a shady place to sit or somebody suggesting a completely unnecessary competition. He is open to hearing the rules.</p>
<p>The beach gives his stories room to breathe. People relax, conversations wander and a day that began with a swim can turn into a much longer adventure.</p>
<h2>Sand sports, then a film under the sky</h2>
<p>The proposed <a href="https://auraofintelligence.github.io/ballow-road-sand-screen-hub/">Ballow Road Sand &amp; Screen Hub</a> on Minjerribah gives this idea a home-ground connection: sand sport by day, outdoor cinema, markets and festival energy as the evening arrives.</p>
<p>Picture a sand sports, outdoor cinema and festival hub. Beach volleyball gets competitive, a casual team needs one more player and Tiggy discovers that enthusiasm only gets him halfway to the ball.</p>
<p>Later he helps with the screen and sound check. The courts quieten, the food starts arriving and a woman he met during the game saves him a seat. The same place holds sport, work, films, music and a night that keeps getting better.</p>'''),
    dict(slug='company', title='Chemistry across cultures', intro='A particular attraction. A shared laugh. An invitation to see more.', image='company-world', alt='Tiggy talks closely with two adult women, one visibly pregnant, at an art-filled rooftop gathering in Mexico City.', caption='The conversation has become the best part of the evening. Imagined Mexico City gathering. GenAI artwork.', colour='orange', body='''
<p class="lead">Tiggy likes the spark between people: a quick look, a cheeky remark, the feeling that somebody is enjoying the same small absurdity.</p>
<p>He is drawn to warmth, beauty, humour and people who bring a bit of life with them. Flirtation can sit quite comfortably beside making something, sharing food or finding out that neither of them knows the words.</p>
<p>His attraction is specific: adult women in their twenties and thirties, very full busts and visibly pregnant women belong in the romantic life he imagines. He likes confidence, cheek, direct interest and the pleasure of being wanted.</p>
<h2>Love and be loved</h2>
<p>That is one of the personal hopes behind his wandering. He enjoys affection, romance and the possibility that a chance meeting might become part of a much larger life.</p>
<p>His imagined social world includes pregnant women enjoying the music, company and play alongside everybody else. Pregnancy, attraction and the pleasure of being together have a place in these stories.</p>
<h2>More life together</h2>
<p>Tiggy is curious about how people share love across cultures and places. <a href="https://auraofintelligence.github.io/global-group-marriages/">Global Group Marriages</a> gives that curiosity a wider set of possibilities to explore.</p>
<p>The story can begin with a woman inviting him into her evening, a shared experience at a retreat or a conversation after a festival. What they enjoy together, and what they want next, gives the journey its personal direction.</p>'''),
    dict(slug='music', title='Turn it up', intro='Festivals, music and the people who make the night.', image='music-world', alt='An adult Afro-Brazilian singer cues Tiggy and another percussionist during a lively Salvador street gathering.', caption='He appears to have become part of the performance. Imagined Salvador festival. GenAI artwork.', colour='blue', body='''
<p class="lead">Music gives Tiggy another way to join in. A rhythm catches, somebody starts singing and suddenly the gathering has become something else.</p>
<p>The Forge includes performing for a living audience among his creative ambitions. He wants to feel an idea leave his own head and become something people can enjoy together.</p>
<h2>Make a bit of noise</h2>
<p>A tune can be tender, funny, grand or completely ridiculous. Tiggy has time for all of those moods. He likes a surprising lyric and a moment that makes the person beside him grin.</p>
<p>A friend adds a rhythm. Somebody changes the line. The chorus becomes easier once nobody is too worried about getting it exactly right.</p>
<p>A festival gives his travels scale: unfamiliar sounds, a whole place alive after dark, performers and visitors crossing paths. He might end up in the audience, helping backstage or discovering that the singer has a question for him after the show.</p>
<h2>Let the evening find its feet</h2>
<p>There might be dancing, a second song or a good conversation at the edge of the music. Sound gives the scene somewhere to go.</p>
<p>The <a href="https://auraofintelligence.github.io/i-C-infinity-music-universe/">i C. infinity music universe</a> opens another part of Luke’s creative world, where songs, characters and possible lives meet.</p>'''),
    dict(slug='possibilities', title='Go a little bigger', intro='Big experiences. Bold company. The occasional leap into the unknown.', image='possibilities-world', alt='Two Kenyan artists share a model of a floating cinema and festival venue with Tiggy at a Nairobi evening reception.', caption='A formal invitation. A much less formal conversation. Imagined Nairobi reception. GenAI artwork.', colour='lemon', body='''
<p class="lead">Tiggy wants experiences big enough to surprise him: spectacular festivals, adventurous sport, ambitious art and evenings that open doors into lives very different from his own.</p>
<p>He can enjoy a dusty outback camp and dress for a high-society reception. The people make both interesting. An invitation might lead to a performance, a private view of something extraordinary or a journey he had not imagined taking.</p>
<p>The wider story world gives him intelligent companions, strange instruments, responsive spaces and places that stretch what an ordinary day can hold. He wants to know what they do. He also wants to have a go.</p>
<h2>A future worth enjoying</h2>
<p>Imagine a floating performance venue, a festival spread across an entire future city or a gathering where artists and explorers turn an outrageous idea into an experience people can share.</p>
<p>Those are possibilities for scenes: people trying something, surprising each other and finding unexpected pleasure in a world they help create.</p>
<p>Aura’s <a href="https://auraofintelligence.github.io/aura-events.html">events concept</a> stretches from small gatherings to grand galas and festivals connected across the world. Its <a href="https://auraofintelligence.github.io/space-industry.html">Moonlight Frontier</a> imagines low-gravity sport and lunar adventure. Give Tiggy a new way to fall over and he will probably find an audience.</p>
<h2>Something worth showing up for</h2>
<p><a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> connects the projects behind this world. <a href="https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html">GAJRA Earth’s Ahead</a> brings attention to dated meetings and opportunities to contribute. They give the travel a wider purpose: bring an idea, meet the people working on it and do something useful while there is a chance.</p>
<p>In the fiction, that might put a demanding work session, a rooftop reception and a spontaneous invitation into the same short visit. Joyful responsible abundance includes the effort that makes the good stuff possible.</p>
<h2>One creative world, different expressions</h2>
<p>Tiggy Bestmann and Australian Sire are connected expressions within Luke Nathan Hayes’ story world. This site gives Tiggy room for his own personality: the playful artist, romantic wanderer and student of life.</p>
<p>Australian Sire’s partner site explores his particular desires, continuing travels and global group marriages. The <a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Story Forge</a> holds the settings, characters and possibilities behind both.</p>
<p>The fiction is still being developed. These pages are a character profile and a collection of imagined scenes, with plenty of room for the next good idea.</p>'''),
    dict(slug='sitemap', title='Pick your next bit', intro='Follow a curiosity. You can come back for the rest.', image='wayfinder', alt='Brightly coloured sculptural archways lead along a sunny seaside festival walkway towards the ocean.', caption='Plenty of ways to spend the afternoon. GenAI story concept.', colour='orange', body='''
<p class="lead">Ten connected pages. Travel with Tiggy, join an Aura retreat, head for the sand sports or follow the festival into the night.</p>
<p>Every page has a previous and next link, and a way back to the top. The menu opens the whole site whenever another bit catches your eye.</p>
<h2>Keep exploring</h2>
<p>The <a href="https://auraofintelligence.github.io/australian-sire-story-forge/">Australian Sire Story Forge</a> opens the story workshop. <a href="https://auraofintelligence.github.io/luke-nathan-hayes-man-and-mind/">Man and Mind</a> introduces Luke, the person behind the characters.</p><p>The <a href="https://auraofintelligence.github.io/sitemap.html">Aura site map</a> opens the wider world of creative technology, events, travel and imagined futures. <a href="https://auraofintelligence.github.io/project-atlas/site-map.html">Project Atlas</a> connects the projects that give those ideas somewhere to go.</p>''')
]

PLAY = '''<section class="play-panel" aria-labelledby="play-title"><div><h2 id="play-title">Where is the action?</h2><p>Three imagined turns in a busy journey. Pick a scene.</p><div class="mood-buttons" role="group" aria-label="Choose a scene"><button type="button" data-mood="make" aria-pressed="true">Red dust</button><button type="button" data-mood="wander" aria-pressed="false">Sand and screen</button><button type="button" data-mood="company" aria-pressed="false">Dress up</button></div><div class="play-result" aria-live="polite" aria-atomic="true"><h3>The crowd arrives in two hours.</h3><p>Red dust, a touring stage and a very large prop with a mind of its own. She has a better way to rig it. Tiggy has a question about dinner after the show.</p></div></div><a class="round-link" href="fool.html" aria-label="Meet the happy-go-lucky fool">↗</a></section>'''

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
<section class="partner-panel"><div><h2>Meet Australian Sire</h2><p>Another expression in Luke’s story world. Follow his travels, desires and exploration of global group marriages.</p></div><a href="{escape(SIRE_URL,quote=True)}">Visit the partner site ↗</a></section></main>
<nav class="page-turn" aria-label="Previous and next pages"><a rel="prev" href="{prev['slug']}.html"><span>← Previous</span><strong>{escape(prev['title'])}</strong></a><a rel="next" href="{nxt['slug']}.html"><span>Next →</span><strong>{escape(nxt['title'])}</strong></a></nav>
<footer><p>Tiggy Bestmann<br>A fictional character by Luke Nathan Hayes.</p><a href="sitemap.html">Site map ↗</a></footer><a class="to-top" href="#top" aria-label="Back to top">↑</a></body></html>''',encoding='utf-8')
print(f'Built {len(PAGES)} Tiggy pages.')
