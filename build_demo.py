from pathlib import Path
from html import escape

ROOT=Path('site')
NAV=[('chi-sono.html','Chi sono'),('corsi.html','Corsi online'),('contatti.html','Contatti')]
def link(url,label,outline=False):
 return f'<a class="button{" secondary" if outline else ""}" href="{url}">{label}<span aria-hidden="true">→</span></a>'
def section(id,title,content,kicker=''):
 return f'<section class="content-section" id="{id}"><div class="section-heading">{f"<p class=eyebrow>{kicker}</p>" if kicker else ""}<h2>{title}</h2></div>{content}</section>'
def item(title,text):
 return f'<article class="text-item"><h3>{title}</h3><p>{text}</p></article>'
def pending(title,text):
 return f'<div class="pending"><span class="pending-label">Materiale da inserire</span><h3>{title}</h3><p>{text}</p></div>'
def photo(file,alt,caption='Fotografia illustrativa · Demo'):
 return f'<figure class="demo-photo"><img src="assets/{file}" alt="{escape(alt,quote=True)}" width="1536" height="1024" loading="lazy" decoding="async"><figcaption>{caption}</figcaption></figure>'

FLUTE_PHOTO=photo('flute-score-demo.jpg','Flauto traverso argentato appoggiato su uno spartito, in un ambiente dai toni caldi')
ROOM_PHOTO=photo('music-room-demo.jpg','Ambiente illustrativo con due poltrone, un tamburo, uno xilofono e piccoli strumenti in legno','Ambiente illustrativo · Non è uno studio reale di Yasmin')

def video_placeholder(file,title,description):
 return f'<article class="video-example"><div class="video-preview"><img src="assets/{file}" alt="" width="1536" height="1024" loading="lazy" decoding="async"><span class="video-play" aria-hidden="true">▶</span><span class="video-label">Segnaposto video · Demo</span></div><h3>{title}</h3><p>{description}</p><span class="video-availability">Video non ancora disponibile</span></article>'

def page(file,title,body,lead='',motto=''):
 menu=''.join(f'<a href="{u}"'+(' aria-current="page"' if file==u else '')+f'>{l}</a>' for u,l in NAV)
 activities=[('musicoterapia.html','Musicoterapia'),('musicista.html','Musicista'),('flauto.html','Lezioni di flauto')]
 sublinks=''.join(f'<a href="{u}"'+(' aria-current="page"' if file==u else '')+f'>{l}</a>' for u,l in activities)
 group=f'<div class="activity-group"><button class="activity-toggle{" active" if file in dict(activities) else ""}" type="button" aria-expanded="false" aria-controls="activity-submenu">Attività <span aria-hidden="true">⌄</span></button><div id="activity-submenu" hidden>{sublinks}</div></div>'
 menu=menu.replace('<a href="corsi.html"',group+'<a href="corsi.html"',1)
 if file!='index.html':
  body=f'<div class="page-shell"><section class="page-intro"><p class="eyebrow">{title}</p><h1>{motto or title}</h1><p class="intro-copy">{lead}</p></section>{body}</div>'
 cta='' if file=='contatti.html' else f'<section class="closing"><img src="assets/mark.svg" alt=""><h2>Ogni incontro comincia da qui.</h2><p>Per un percorso, una lezione o una collaborazione musicale.</p>{link("contatti.html","Contatta Yasmin")}</section>'
 html=f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{escape(title)} · Dott.ssa Yasmin Khreiwesh</title><meta name="description" content="Yasmin Khreiwesh: musicoterapia, progetti musicali e lezioni di flauto traverso. Demo del sito."><link rel="icon" type="image/svg+xml" href="assets/mark.svg"><link rel="stylesheet" href="styles.css?v=5"><script src="app.js?v=5" defer></script></head><body><a class="skip" href="#main">Vai al contenuto</a><header class="site-header"><div class="header-inner"><a class="brand" href="index.html" aria-label="Yasmin Khreiwesh, homepage"><img src="assets/mark.svg" alt=""><span>Dott.ssa Yasmin Khreiwesh<small>Musicoterapista · Flautista · Insegnante di flauto</small></span></a><button class="menu" type="button" aria-expanded="false" aria-controls="navigation">Menu <span aria-hidden="true">☰</span></button><nav id="navigation" aria-label="Navigazione principale">{menu}</nav></div></header><main id="main">{body}</main>{cta}<footer><p>© 2026 Dott.ssa Yasmin Khreiwesh</p><a href="note-demo.html">Informazioni sulla demo</a></footer></body></html>'''
 html=html.replace('styles.css?v=5','styles.css?v=20').replace('app.js?v=5','app.js?v=11')
 html=html.replace('<link rel="stylesheet"', '<link rel="preload" href="assets/Allura.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="assets/Manrope.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet"',1)
 html=html.replace('<span>Dott.ssa Yasmin Khreiwesh<small>', '<span><span class="brand-honorific">Dott.ssa </span>Yasmin Khreiwesh<small>')
 html=html.replace('<body>', '<body class="home-page">' if file=='index.html' else '<body>')
 html=html.replace('<a href="contatti.html"', '<a class="nav-contact" href="contatti.html"',1)
 if file=='index.html':
  html=html.replace(cta, '<section class="closing"><img src="assets/mark.svg" alt=""><h2>Non sai da dove cominciare?</h2><p>Raccontami cosa stai cercando: possiamo partire da un primo contatto.</p>'+link('contatti.html','Scrivimi')+'</section>')
 (ROOT/file).write_text(html,encoding='utf-8')

paths=[
 ('01','musicoterapia.html','Musicoterapia','Cerchi uno spazio di ascolto? Scopri i percorsi per bambini, adolescenti e adulti.','Esplora la musicoterapia'),
 ('02','musicista.html','Musicista','Vuoi conoscere la mia musica? Esplora esecuzioni, progetti e possibilità di collaborazione.','Scopri i progetti'),
 ('03','flauto.html','Lezioni di flauto','Vuoi iniziare o continuare a suonare? Scopri le lezioni in presenza e online.','Scopri le lezioni'),
]
doors=''.join(f'<a class="activity-door" href="{u}"><span class="number">{n}</span><h3>{t}</h3><p>{d}</p><span class="door-link">{label} <b aria-hidden="true">→</b></span></a>' for n,u,t,d,label in paths)
page('index.html','Home',f'''
<section class="home-hero" aria-label="Benvenuti nel sito di Yasmin">
 <div class="hero-photo"><img src="assets/flute-hero.jpg" alt="Dettaglio illustrativo di mani su un flauto traverso" fetchpriority="high"></div>
 <div class="hero-copy">
  <h1 class="hero-name">Yasmin Khreiwesh</h1>
  <p class="hero-tagline">La musica, uno spazio di incontro.</p>
  <p>Musicoterapia, lezioni di flauto<br>e progetti musicali.</p>
  <div class="hero-actions">{link('#attivita','Scopri i percorsi')}{link('contatti.html','Parliamone',True)}</div>
 </div>
</section>
<section class="home-paths" id="attivita" aria-labelledby="paths-title">
 <div class="paths-intro">
  <p class="eyebrow">Benvenuti</p>
  <h2 id="paths-title">Tre modi di incontrare la musica.</h2>
  <p>Sono Yasmin, musicoterapista, flautista e insegnante di flauto. Il mio lavoro unisce l’ascolto, l’espressione e il piacere di fare musica.</p>
 </div>
 <div class="paths-heading"><h3>Da dove vuoi iniziare?</h3><p>Qui puoi esplorare le mie attività e trovare le informazioni per un percorso, una lezione o una collaborazione.</p></div>
 <div class="activity-doors">{doors}</div>
</section>
<section class="home-about" aria-labelledby="about-title">
 <div class="about-sign"><img src="assets/mark.svg" alt=""><p>Ogni persona ha<br>il proprio tempo.</p></div>
 <div class="about-copy"><p class="eyebrow">Chi sono</p><h2 id="about-title">Conosciamoci meglio.</h2>
  <p>Dietro ogni percorso c’è una persona. Nella pagina dedicata a me puoi conoscere la mia formazione, le esperienze e il modo in cui lavoro.</p>
  {link('chi-sono.html','Il mio percorso',True)}
 </div>
</section>
<section class="home-course" aria-labelledby="course-title">
 <div><p class="eyebrow">Corsi online · In preparazione</p><h2 id="course-title">Anche a distanza.</h2>
  <p>Uno spazio per approfondire musica, ascolto e respiro. Il primo corso sarà dedicato alla respirazione.</p>
  <p>Scopri la proposta e le anteprime delle lezioni nella pagina dei corsi.</p>
  {link('corsi.html','Esplora i corsi online',True)}
 </div>
 {FLUTE_PHOTO}
</section>''')

page('chi-sono.html','Chi sono',
 section('presentazione','Tre modi di vivere la musica.', '<div class="two-columns">'+item('Musicoterapia','La musica come esperienza di ascolto e relazione, nei percorsi rivolti a bambini, adolescenti e adulti.')+item('Musica e insegnamento','L’attività artistica e le lezioni di flauto traverso: il suono, la pratica e il piacere di condividere la musica.')+'</div>')+
 section('biografia','Il mio percorso.','<div class="two-columns photo-block">'+FLUTE_PHOTO+pending('Biografia e ritratto','Questo spazio accoglierà il racconto personale di Yasmin e una sua fotografia. Il dettaglio musicale accanto è un’immagine illustrativa per la demo.')+'</div>')+
 section('formazione','Formazione ed esperienze.',pending('Curriculum di Yasmin','La formazione e le esperienze saranno inserite a partire dai curriculum originali. Nessuna qualifica aggiuntiva è stata attribuita nella demo.')+'<div class="inline-links"><a href="musicoterapia.html#curriculum">Area musicoterapia →</a><a href="musicista.html#curriculum">Area artistica →</a><a href="flauto.html#curriculum">Area didattica →</a></div>'),
 'Sono Yasmin Khreiwesh, musicoterapista, flautista e insegnante di flauto. Questo è il luogo in cui si incontrano le tre anime del mio lavoro.','La persona, prima delle note.')

page('musicoterapia.html','Musicoterapia',
 section('percorsi','A ogni età, uno spazio di ascolto.','<div class="three-columns">'+item('Bambini','Percorsi dedicati ai più piccoli. Qui saranno presentati destinatari, attività e modalità di coinvolgimento delle famiglie.')+item('Adolescenti','Percorsi dedicati agli adolescenti, con spazio all’espressione personale e alla relazione attraverso l’esperienza musicale.')+item('Adulti','Incontri e percorsi per adulti. Yasmin descriverà modalità, destinatari e obiettivi delle proposte individuali o di gruppo.')+'</div>')+
 section('studi','Dove ricevo.','<div class="two-columns photo-block">'+ROOM_PHOTO+pending('Gli studi','Qui troverai le fotografie reali degli ambienti, le sedi e le informazioni per raggiungere gli studi. La foto accanto è solo un esempio per la demo; indirizzi e disponibilità sono da confermare.')+'</div>')+
 section('curriculum','Il curriculum professionale.',pending('Formazione in musicoterapia','In questa sezione sarà possibile consultare e scaricare il curriculum originale di Yasmin.'))+
 section('corsi','Un percorso anche a distanza.','<div class="two-columns">'+item('Musica e respirazione','Il corso online sulla respirazione è in preparazione. La pagina dedicata raccoglierà il programma, i destinatari e le modalità di accesso.')+f'<div class="section-action">{link("corsi.html","Vai ai corsi online",True)}</div></div>')+
 section('testimonianze','Dicono di me.',pending('Le esperienze di chi partecipa','Qui saranno inserite le testimonianze reali, dopo aver raccolto l’autorizzazione alla pubblicazione.')),
 'Percorsi per bambini, adolescenti e adulti. Un primo incontro è il punto di partenza per conoscere la persona, la richiesta e le possibilità del lavoro insieme.','Uno spazio per ascoltarsi.')

page('musicista.html','Musicista',
 section('media','La musica da vedere e ascoltare.','<div class="two-columns photo-block">'+FLUTE_PHOTO+pending('Foto e video delle esecuzioni','Una galleria dedicata a Yasmin: immagini delle esibizioni e video in cui suona. La fotografia illustrativa anticipa l’atmosfera della sezione; i materiali originali sono da inserire.')+'</div>')+
 section('progetti','Progetti e incontri musicali.','<div class="two-columns">'+item('Progetti musicali','Ogni progetto avrà una presentazione, il repertorio e i musicisti coinvolti, insieme alle fotografie e ai video disponibili.')+item('Servizi e collaborazioni','Qui saranno descritte le proposte musicali di Yasmin e le possibilità di collaborazione con musicisti, associazioni e organizzatori.')+'</div>')+
 section('curriculum','Il curriculum artistico.',pending('Il percorso da musicista','Formazione, concerti e collaborazioni saranno raccontati attraverso il curriculum artistico originale.'))+
 section('collaborazioni','Hai un progetto musicale?','<p>Questo spazio è dedicato a chi desidera proporre un’esecuzione, un evento o una collaborazione.</p>'+link('contatti.html','Contatta Yasmin')),
 'Il flauto, le esecuzioni e i progetti. Uno spazio per conoscere l’attività musicale di Yasmin e immaginare nuove collaborazioni.','La musica prende vita.')

faq=[('A che età si può iniziare a suonare il flauto?','Età, strumento e percorso vanno valutati insieme all’insegnante. Qui Yasmin indicherà le fasce d’età delle sue proposte e le possibilità per i più piccoli.'),('Quanto costa un flauto?','Il prezzo dipende dal modello e dalla scelta tra nuovo e usato. Le indicazioni saranno concordate con Yasmin; prima di acquistare è utile confrontarsi con l’insegnante.'),('Serve già uno strumento per la prima lezione?','Le modalità della prima lezione e l’eventuale disponibilità di uno strumento saranno precisate da Yasmin.'),('Come si svolgono le lezioni online?','Durata, piattaforma e attrezzatura necessaria saranno indicate nella proposta didattica definitiva.'),('Posso cominciare da adulto?','La richiesta può essere approfondita con Yasmin per conoscere le possibilità e il percorso più adatto.')]
page('flauto.html','Lezioni di flauto',
 section('metodo','Un metodo, il tuo percorso.','<div class="two-columns photo-block">'+FLUTE_PHOTO+'<div><p>Qui Yasmin racconterà come organizza le lezioni: ascolto, respirazione, tecnica e pratica musicale, con attenzione alle esigenze dello studente.</p>'+link('contatti.html','Informazioni sulle lezioni',True)+'</div></div>')+
 section('lezioni','In presenza oppure online.','<div class="two-columns">'+item('Lezioni in presenza','Sedi, frequenza, durata e destinatari saranno descritti nell’offerta didattica di Yasmin.')+item('Lezioni online','Una sezione dedicata alle lezioni a distanza: modalità, strumenti necessari e organizzazione degli incontri.')+'</div>')+
 section('curriculum','Il curriculum didattico.',pending('Formazione e insegnamento','Il curriculum e l’offerta di corsi e lezioni saranno inseriti con le informazioni originali di Yasmin.'))+
 section('testimonianze','Dicono di me.',pending('La voce degli studenti','Qui troveranno spazio le testimonianze degli allievi che desiderano condividere la propria esperienza.'))+
 section('faq','Prima di iniziare.','<div class="faq">'+''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q,a in faq)+'</div>'),
 'Un percorso per conoscere il flauto traverso e trovare il proprio suono. Metodo didattico, lezioni, formazione e risposte alle domande più comuni.','Il tuo tempo, il tuo suono.')

page('corsi.html','Corsi online',
 section('respirazione','Musica e respirazione.','<span class="status">In preparazione</span><p>Il primo corso previsto sarà dedicato alla respirazione. Programma, durata e materiali saranno definiti da Yasmin prima dell’apertura delle iscrizioni.</p><div class="two-columns">'+item('Il programma','Qui saranno presentati gli argomenti, i destinatari e ciò che comprende il corso.')+item('Come partecipare','Modalità, date e prezzo saranno pubblicati quando il corso sarà pronto.')+'</div>')+
 section('video','Uno sguardo al corso.','<p>Un esempio di come appariranno le lezioni video. Le anteprime sono illustrative: i filmati saranno aggiunti quando il corso sarà pronto.</p><div class="two-columns course-videos">'+video_placeholder('flute-score-demo.jpg','Presentazione del corso','Qui troverai il video introduttivo di Yasmin, con il programma e le informazioni per iniziare.')+video_placeholder('music-room-demo.jpg','Un esempio di lezione','Uno spazio dedicato a un estratto del corso, per conoscere il modo in cui saranno presentati i contenuti.')+'</div>')+
 section('accesso','I contenuti, a casa tua.','<p>In una fase successiva sarà possibile acquistare i corsi e accedere ai contenuti in un’area riservata. Per ora puoi esplorare la proposta e chiedere informazioni.</p>'+link('contatti.html','Informazioni sui corsi',True)),
 'Corsi da seguire a distanza, per approfondire la relazione tra musica, ascolto e respiro.','Uno spazio per approfondire.')

page('contatti.html','Contatti',
 section('scrivi','Un primo contatto.','<div class="two-columns"><div><p>Per un percorso di musicoterapia, una lezione di flauto o una collaborazione artistica.</p>'+pending('Recapiti e sedi','Email, telefono, social e indirizzi saranno inseriti dopo la conferma di Yasmin.')+'<div class="contact-photo">'+ROOM_PHOTO+'</div>'+'</div><form class="form-demo"><p class="form-note">Modulo di prova: non invia né salva dati. Usa informazioni inventate.</p><label for="name">Il tuo nome</label><input id="name" placeholder="Nome di esempio" required autocomplete="off"><label for="interest">Di cosa vorresti parlare?</label><textarea id="interest" rows="4" placeholder="Un percorso, una lezione, un progetto…" required></textarea><button class="button" type="submit">Prova il modulo <span aria-hidden="true">→</span></button><p class="form-message" role="status" hidden></p></form></div>'),
 'Ogni richiesta ha il suo punto di partenza. Raccontami cosa stai cercando.','Cominciamo da un incontro.')

page('note-demo.html','Informazioni sulla demo',section('info','Una proposta da completare.','<p>Il sito segue il brand book approvato di Yasmin. Testi, fotografie e segno musicale sono dimostrativi. I materiali originali, i recapiti e i curriculum saranno inseriti prima del lancio.</p><p>Allura è utilizzato per firma e titoli brevi. Manrope sostituisce temporaneamente Nourd, in attesa del font con licenza web.</p><p>Il modulo di prova non invia o salva dati. Non sono integrati analytics, cookie, video esterni, pagamenti o account. GitHub Pages può trattare dati tecnici secondo la propria informativa.</p>'),'Questa è una demo grafica e navigabile, con fotografie illustrative.','Informazioni sulla demo')
print('Rebuilt 8 pages from shared templates')
