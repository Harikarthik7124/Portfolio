# Generates every page from shared parts. Edit content here, then run: python3 build.py
PAGES=[('work','Work'),('projects','Projects'),('toolkit','Toolkit'),('credentials','Credentials'),('about','About'),('contact','Contact')]
COL={'home':('#3358E8','#F6F1E7'),'work':('#DFC87A','#1d1b26'),'projects':('#D9D0E8','#1d1b26'),'toolkit':('#B9E4CC','#1d1b26'),
     'credentials':('#9CC9F2','#1d1b26'),'about':('#F4C9A0','#1d1b26'),'contact':('#D98574','#1d1b26')}
EMAIL='aharikarthik7124@gmail.com'; GH='https://github.com/Harikarthik7124'
HEAD='''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>@T@ · Harikarthik A</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;800;900&family=Instrument+Serif:ital@1&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com/3.4.17"></script><script src="tw.js"></script><link rel="stylesheet" href="style.css"></head>
<body style="--c-l:@C@;--fg-l:@F@"><div id="ring" aria-hidden="true"></div>
<header id="hdr" class="sticky top-0 z-50 border-b-2 border-[#1d1b26]"><div class="mx-auto flex h-14 max-w-7xl items-center justify-between gap-3 px-4 sm:px-5 md:h-16">
<a href="index.html" class="logo font-serif text-2xl italic leading-none md:text-3xl">Harikarthik</a>
<nav class="nav hidden gap-5 font-mono text-[11px] font-bold uppercase tracking-wider lg:flex xl:gap-7">@NAV@</nav>
<div class="flex items-center gap-3"><a href="Harikarthik_A_Updated_Resume.pdf" class="hidden rounded-full border-2 border-current px-5 py-2 font-mono text-xs font-bold shadow-[3px_3px_0_rgba(0,0,0,.3)] lg:inline-flex">Resume ↗</a><div class="ctrl flex items-center rounded-full">
<button id="theme" aria-label="Toggle dark mode" class="grid h-11 w-11 place-items-center text-xl">☾</button><span class="h-7 w-px bg-current opacity-30 lg:hidden"></span>
<button id="menu" aria-label="Menu" aria-expanded="false" aria-controls="mnav" class="flex h-11 items-center gap-3 px-4 font-mono text-xs font-bold tracking-widest lg:hidden"><span>MENU</span><span aria-hidden="true" class="text-xl leading-none">≡</span></button></div></div></div>
<nav id="mnav" class="hidden grid grid-cols-2 px-4 pb-4 pt-2 font-mono text-sm font-bold uppercase tracking-wider lg:hidden">@MNAV@</nav></header>
'''
LINKEDIN='https://linkedin.com/in/harikarthik-a-14a71527a'
_ex=''.join(f'<li><a class="hover:underline" href="{s}.html">{n}</a></li>' for s,n in [('index','Home')]+PAGES)
_el=''.join(f'<li><a class="hover:underline" href="{h}">{l} ↗</a></li>' for l,h in [('GitHub',GH),('LinkedIn',LINKEDIN),('Email','mailto:'+EMAIL),('Resume','Harikarthik_A_Updated_Resume.pdf')] if h)
_lab=lambda t:f'<p class="flex items-center gap-2 font-mono text-[11px] font-bold uppercase tracking-wider"><span class="h-2 w-2 rounded-full bg-[#e07a6a]"></span>{t}</p>'
FOOT=f'''<footer class="bg-[#23212b] text-[#F6F1E7]"><div class="mx-auto grid max-w-7xl gap-12 px-5 pb-12 pt-14 md:pt-20 lg:grid-cols-[1.4fr_1fr_1fr]">
<div><h2 class="font-serif text-[clamp(3rem,9vw,5rem)] italic leading-none">Get in touch.</h2><p class="mt-6 max-w-md text-lg text-[#F6F1E7]/70 md:text-xl">Multi-agent AI, computer vision, and the APIs around them. Open to AI/ML Engineer roles.</p><a href="contact.html" class="mt-8 inline-block font-mono text-sm font-bold hover:underline">Contact me ↗</a></div>
<nav aria-label="Footer" class="grid grid-cols-2 gap-10 lg:contents"><div>{_lab('Explore')}<ul class="mt-6 space-y-3 text-lg text-[#F6F1E7]/75">{_ex}</ul></div><div>{_lab('Elsewhere')}<ul class="mt-6 space-y-3 text-lg text-[#F6F1E7]/75">{_el}</ul></div></nav></div>
<div class="border-t border-white/10"><div class="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-x-6 gap-y-3 px-5 py-6 font-mono text-[11px] uppercase tracking-wider text-[#F6F1E7]/80"><span>© 2026 Harikarthik A</span><a href="#" class="hover:underline">Back to top ↑</a><span>Made with <span class="text-[#ee5a86]" role="img" aria-label="love">♥</span></span></div></div></footer><script src="site.js"></script></body></html>'''
def page(slug,title,body):
    c,f=COL[slug]
    nav=''.join(f'<a href="{s}.html" class="{"on" if s==slug else ""}">{n}</a>' for s,n in PAGES)
    mnav=''.join(f'<a class="mlink block px-3 py-5 {"on" if s==slug else ""}" href="{s}.html">{n}</a>' for s,n in PAGES)+'<a class="mlink block px-3 py-5" href="Harikarthik_A_Updated_Resume.pdf">Resume ↗</a>'
    h=HEAD.replace('@T@',title).replace('@C@',c).replace('@F@',f).replace('@NAV@',nav).replace('@MNAV@',mnav)
    h=h.replace('<script src="tw.js"></script><link rel="stylesheet" href="style.css">','<script>'+open('tw.js',encoding='utf-8').read()+'</script><style>'+open('style.css',encoding='utf-8').read()+'</style>')
    ft=FOOT.replace('<script src="site.js"></script>','<script>'+open('site.js',encoding='utf-8').read()+'</script>')
    open(f'{slug if slug!="home" else "index"}.html','w',encoding='utf-8').write(h+body+ft)
def band(num,label,h2,intro):
    return f'''<section class="band relative overflow-hidden"><div class="gl absolute inset-0"></div><span class="ghost">{num}</span>
<div class="relative mx-auto max-w-7xl px-5 pb-12 pt-10 md:pb-20 md:pt-16"><p class="font-mono text-[11px] font-bold uppercase tracking-wider">● {label}</p>
<h1 class="mt-6 text-[clamp(2.75rem,12vw,7.5rem)] font-black leading-[.9] tracking-tighter">{h2}</h1><p class="mt-5 max-w-2xl text-lg md:text-xl">{intro}</p></div></section>'''
def pills(xs): return ''.join(f'<span class="pill">{x}</span> ' for x in xs)
MAIN='<main class="mx-auto max-w-7xl px-5 py-12 md:py-16">'

# ---------- HOME ----------
tiles=[('work','01','Work','Internship at Infosys Springboard.'),('projects','02','Projects','Multi-agent AI, computer vision, 5G.'),
('toolkit','03','Toolkit','Languages, frameworks and cloud I use.'),('credentials','04','Credentials','Certificates and hackathon wins.'),
('about','05','About','Who I am and what I’m after.'),('contact','06','Contact','Say hello or send a message.')]
tl=''.join(f'<a href="{s}.html" class="pop block p-6 text-[#1d1b26]" style="background:{COL[s][0]}"><span class="font-mono text-xs font-bold">{n}</span><h3 class="mt-8 text-4xl font-black tracking-tighter">{t}</h3><p class="mt-2">{d}</p><p class="mt-6 font-mono text-sm font-bold">Open ↗</p></a>' for s,n,t,d in tiles)
def lab(t): return f'<p class="flex items-center gap-2 font-mono text-[11px] font-bold uppercase tracking-wider"><span class="h-2 w-2 rounded-full bg-current"></span>{t}</p>'
cols=[('01','Applied AI','Multi-agent pipelines, LLM scoring and semantic search with pgvector.'),('02','Computer vision','CNN image and audio classification, from preprocessing to a Flask API.'),('03','Backend and deployment','FastAPI and Flask services, containerized with Docker and shipped on Railway and Render.')]
cl=''.join(f'<div class="border-b-2 border-ink/30 p-6 last:border-b-0 md:border-b-0 md:border-l-2 md:border-ink/60 md:px-8 md:py-10 md:first:border-l-0 md:first:pl-0"><p class="font-mono text-xs">{n}</p><h3 class="mt-8 text-3xl font-black leading-none tracking-tighter md:mt-24 md:text-4xl">{t}</h3><p class="mt-4 leading-relaxed opacity-80">{d}</p></div>' for n,t,d in cols)
persp=f'''<section class="relative overflow-hidden bg-[var(--s-cream)] text-ink"><div class="gl absolute inset-0"></div><div class="relative mx-auto max-w-7xl px-5 pt-12 md:pt-16">{lab('01 · Perspective')}
<div class="mt-6 grid items-end gap-10 lg:grid-cols-[1.3fr_1fr]"><h2 class="text-[clamp(3.2rem,13vw,8.5rem)] font-black leading-[.85] tracking-tighter">Train it.<br>Ship it.<br><span class="font-serif font-normal italic tracking-normal text-[var(--acc)]">Make it useful.</span></h2>
<div class="pb-4"><p class="text-2xl leading-snug md:text-3xl">I like turning models into products people can use. <b class="text-[var(--acc)]">Data, APIs, deployment, and a UI on top.</b> AI that holds up outside the notebook and stays easy to reason about.</p><a href="about.html" class="mt-8 inline-block border-b border-ink pb-1 font-mono text-xs font-bold uppercase">More about me ↗</a></div></div>
<div class="mt-12 grid border-t-2 border-ink/60 md:mt-20 md:grid-cols-3">{cl}</div></div></section>'''
builds=[('AutoEval','Multi-agent developer assessment','Two LLMs score GitHub profiles across 8 rubrics, with a consensus layer and pgvector search.',['LangGraph','FastAPI','pgvector'],'#BFE8D8'),('Cat Emotion Detection','Image + audio classification','A CNN and an audio model served through a Flask web app.',['TensorFlow','OpenCV','Flask'],'#F7E08A'),('5G Session Manager','Network test automation','Automates UE and gNodeB sessions with a live monitoring dashboard.',['Flask','Open5GS','UERANSIM'],'#CFE3F7')]
bl=''.join(f'<a href="projects.html" class="pop block p-6 text-[#1d1b26]" style="background:{c}"><h3 class="text-3xl font-black tracking-tighter">{n}</h3><p class="font-serif text-xl italic">{s}</p><p class="mt-3 leading-relaxed">{d}</p><div class="mt-5 flex flex-wrap gap-2">{pills(t)}</div></a>' for n,s,d,t,c in builds)
bsec=f'''<section class="bg-[var(--s-rose)] text-ink"><div class="mx-auto max-w-7xl px-5 py-14 md:py-20"><div class="flex flex-wrap items-end justify-between gap-4">{lab('02 · Selected builds')}<a href="projects.html" class="border-b border-ink pb-1 font-mono text-xs font-bold uppercase">All projects ↗</a></div>
<h2 class="mt-6 text-[clamp(2.5rem,9vw,5.5rem)] font-black leading-[.9] tracking-tighter">Things I’ve built.</h2><div class="mt-10 grid gap-7 md:grid-cols-2 lg:grid-cols-3">{bl}</div></div></section>'''
mq2=''.join(f'<span class="px-5 text-4xl font-black tracking-tighter sm:text-6xl">{w}</span><span class="text-3xl text-[var(--acc)] sm:text-5xl">✦</span>' for w in ['Python','Flask','FastAPI','TensorFlow','PyTorch','OpenCV','LangGraph','React','PostgreSQL','pgvector','Docker','AWS']*2)
tsec=f'''<section class="relative overflow-hidden bg-[var(--s-butter)] text-ink"><div class="gl absolute inset-0"></div><div class="relative mx-auto max-w-7xl px-5 pt-14 md:pt-20">{lab('03 · Toolkit')}
<div class="mt-6 grid items-end gap-8 lg:grid-cols-[1.3fr_1fr]"><h2 class="text-[clamp(3rem,11vw,7rem)] font-black leading-[.9] tracking-tighter">Tools change.<br><span class="font-serif font-normal italic tracking-normal text-[var(--acc)]">Thinking scales.</span></h2><p class="text-lg md:text-xl">I pick technology around the system: the constraints, the failure modes, and what will still be understandable six months later.</p></div></div>
<div class="relative overflow-hidden py-14"><div class="strip py-3" style="background:transparent;border-color:var(--ink)"><div class="track items-center">{mq2}</div></div></div></section>'''
cta=f'''<section class="relative overflow-hidden bg-[var(--s-tang)] text-ink"><div class="gl absolute inset-0"></div><div class="relative mx-auto grid max-w-7xl items-end gap-10 px-5 py-16 lg:grid-cols-[1.4fr_1fr] md:py-24"><div>{lab('04 · Let’s build')}<h2 class="mt-6 text-[clamp(3rem,12vw,8rem)] font-black leading-[.85] tracking-tighter">Have a hard problem in mind?</h2></div>
<div class="pb-4"><p class="text-xl md:text-2xl">I’m always interested in reliable systems, useful AI, and products that make technical work feel simpler.</p><a href="contact.html" class="mt-8 inline-block rounded-full border-2 border-black bg-[#3358E8] px-7 py-4 font-mono text-sm font-bold text-cream shadow-[4px_4px_0_#000]">Start a conversation ↗</a></div></div></section>'''
exp=f'''<section class="bg-[var(--s-cream)] text-ink"><div class="mx-auto max-w-7xl px-5 py-14 md:py-20">{lab('05 · Explore the site')}<h2 class="mt-6 text-[clamp(2.5rem,9vw,5.5rem)] font-black leading-[.9] tracking-tighter">Pick a page.</h2><div class="mt-10 grid gap-7 sm:grid-cols-2 lg:grid-cols-3">{tl}</div></div></section>'''
REST=persp+bsec+tsec+cta+exp
home=f'''<section class="band relative overflow-hidden"><div class="gl absolute inset-0"></div>
<div class="relative mx-auto grid max-w-7xl items-end gap-8 px-5 pt-12 lg:grid-cols-[1.4fr_1fr] md:pt-24"><div class="pb-10 md:pb-16">
<p class="mb-6 flex items-center gap-2 font-mono text-[11px] font-bold uppercase tracking-wider"><span class="h-2 w-2 rounded-full bg-cream"></span>AI/ML Engineer · Chennai, India</p>
<h1 class="text-[clamp(3.2rem,11vw,9rem)] font-black leading-[.85] tracking-tighter">Hey, I’m<br><span class="font-serif font-normal italic tracking-normal text-sun">Harikarthik.</span></h1>
<p class="mt-10 max-w-lg text-2xl font-extrabold leading-tight md:text-3xl">I build multi-agent AI systems, computer vision models, and the APIs around them.</p>
<div class="mt-8 flex flex-wrap gap-3 font-mono text-sm font-bold"><a href="work.html" class="rounded-full border-2 border-black bg-sun px-6 py-3 text-[#1d1b26] shadow-[3px_3px_0_#000]">Explore my work ↓</a><a href="{GH}" aria-label="GitHub" class="grid h-12 w-12 place-items-center rounded-full border-2 border-cream"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/></svg></a><a href="{LINKEDIN}" aria-label="LinkedIn" class="grid h-12 w-12 place-items-center rounded-full border-2 border-cream"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg></a><a href="mailto:{EMAIL}" aria-label="Email" class="grid h-12 w-12 place-items-center rounded-full border-2 border-cream"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg></a></div></div>
<div class="relative mx-auto w-full max-w-[17rem] self-end sm:max-w-sm"><div class="relative mx-auto mb-6 w-fit max-w-[18rem] -rotate-2 rounded-2xl border-2 border-black bg-cream p-4 font-extrabold leading-snug text-black shadow-[6px_6px_0_#000] lg:absolute lg:-left-16 lg:-top-24 lg:right-6 lg:mx-0 lg:mb-0 lg:w-auto lg:max-w-none">I like turning models into products people can actually use.</div>
<!-- Replace with <img src="photo.png" alt="Harikarthik" class="h-full w-full object-cover"> -->
<div class="flex aspect-[4/5] items-end justify-center overflow-hidden border-2 border-black bg-[#0c3a8a] shadow-[8px_8px_0_#F2C230] md:shadow-[14px_12px_0_#F2C230]" style="border-radius:50% 50% 0 0/38% 38% 0 0"><span class="font-serif text-[6.5rem] italic leading-none text-sun md:text-[9rem]">HA</span></div><div class="absolute -bottom-4 right-0 flex items-center gap-3 rounded-2xl border-2 border-black bg-[#14110f] px-4 py-3 text-cream shadow-[4px_4px_0_#000] md:-right-6"><span class="h-3 w-3 rounded-full bg-[#3ddc84]"></span><div><p class="font-mono text-[9px] uppercase tracking-wider opacity-70">Currently</p><p class="font-extrabold">Open to AI/ML roles</p></div></div></div></div></section>
{REST}'''
page('home','Home',home)

# ---------- WORK ----------
def bandbox(num,label,h2,intro,extra=''):
    return f'''<div class="mx-auto max-w-7xl px-5 pt-8 md:pt-12"><section class="relative overflow-hidden border-2 border-ink shadow-[6px_6px_0_var(--shadow)] md:shadow-[12px_12px_0_var(--shadow)]" style="background:var(--c);color:var(--fg)"><div class="gl absolute inset-0"></div><span class="ghost">{num}</span>
<div class="relative p-6 sm:p-10 md:p-16"><div class="flex justify-between gap-4 font-mono text-[11px] font-bold uppercase tracking-wider"><p>● {label}</p><p class="hidden sm:block">{num} / Harikarthik</p></div>
<h1 class="mt-10 text-[clamp(3rem,13vw,8.5rem)] font-black leading-[.9] tracking-tighter md:mt-16">{h2}</h1><p class="mt-5 max-w-2xl text-lg opacity-80 md:text-xl">{intro}</p>{extra}</div></section></div>'''
BOX='border-2 border-ink bg-panel shadow-[6px_6px_0_var(--shadow)] md:shadow-[12px_12px_0_var(--shadow)]'
W=[dict(i='01',dates='Nov 2025 – Jan 2026',loc='Remote',pill='Internship',logo='IS',co='Infosys Springboard',title='Artificial Intelligence Intern',
 b=['Built a Cat Emotion Recognition System: a MobileNetV2 CNN for facial emotion classification and an audio model for feline vocalizations, with data augmentation and MFCC features from Librosa.',
    'Integrated the trained models into a Flask web app with separate REST endpoints for image and audio predictions, plus file upload handling, input validation, and pipeline testing.'],
 stats=[('2','REST endpoints'),('2','Model types'),('3 mo','Duration')],tags=['Python','Deep Learning','MobileNetV2','Librosa','Flask','REST APIs','Data Augmentation'],link='https://www.infosys.com/about/springboard.html',img='img/logos/infosys.png')]
def role(w):
    st=''.join(f'<div><p class="text-3xl font-black sm:text-5xl">{a}</p><p class="mt-1 font-mono text-[10px] sm:text-xs">{b}</p></div>' for a,b in w['stats'])
    bl=''.join(f'<li class="sq">{x}</li>' for x in w['b'])
    href=w['link']; co=w['co']; im=w.get('img')
    limg=f'<img src="{im}" alt="{co} logo" class="absolute inset-0 h-full w-full bg-white object-contain p-1.5" onerror="this.remove()">' if im else ''
    lk=f'<a href="{href}" target="_blank" rel="noopener" class="mt-8 inline-block font-mono text-sm font-bold hover:underline">Visit {co} ↗</a>' if href else ''
    return f'''<article class="grid gap-5 border-t-2 border-ink py-8 first:border-t-0 first:pt-0 md:grid-cols-[13rem_1fr] md:gap-10">
<div class="flex flex-wrap items-center gap-x-4 gap-y-2 font-mono md:block md:space-y-3"><p class="text-xs">{w['i']}</p><p class="font-sans text-lg md:text-xl">{w['dates']}</p><p class="text-sm opacity-70">{w['loc']}</p><span class="pill">{w['pill']}</span></div>
<div class="min-w-0"><div class="flex items-center gap-4"><div class="relative grid h-14 w-14 shrink-0 place-items-center overflow-hidden border-2 border-ink bg-[#DFC87A] font-black text-[#1d1b26] shadow-[4px_4px_0_var(--shadow)] sm:h-16 sm:w-16">{w['logo']}{limg}</div>
<div class="min-w-0"><p class="font-mono text-[11px] font-bold uppercase tracking-wider">{co}</p><h2 class="text-2xl font-black leading-[.95] tracking-tighter sm:text-4xl md:text-5xl">{w['title']}</h2></div></div>
<ul class="mt-6 space-y-4 text-base leading-relaxed opacity-90 sm:text-lg">{bl}</ul>
<div class="mt-8 grid grid-cols-3 gap-3 border border-ink/40 bg-[#F3E9CC] p-4 text-[#1d1b26] sm:gap-6 sm:p-6">{st}</div>
<div class="mt-6 flex flex-wrap gap-2">{pills(w['tags'])}</div>{lk}</div></article>'''
work=bandbox('01','Experience','Work','Where I’ve shipped models into real applications.')+f'<main class="mx-auto max-w-7xl px-5 py-12 md:py-16"><div class="{BOX} p-5 sm:p-8 md:p-12">'+''.join(role(w) for w in W)+'</div></main>'
page('work','Work',work)

# ---------- PROJECTS ----------
# Add screenshots to img/projects/ and list the file names in imgs; add src/demo links to show them.
P=[dict(n='AutoEval',e='Multi-agent AI · Developer assessment',c='#D9D0E8',t=['Python','FastAPI','LangGraph','Groq','pgvector','React','Docker'],imgs=[],src=None,demo=None,
 d='Two LLMs (Llama 3.3-70B and 3.1-8B on Groq) score a developer’s GitHub profile across 8 rubrics. A consensus layer flags conflicts above 1.5 points, and pgvector powers similar-candidate search. Smart caching skips re-evaluation unless the profile meaningfully changed.'),
dict(n='Trustloop AI – Student Grievance',e='Hackathon · AI Impact Hackathon',c='#F7B7C8',t=['AI','Hackathon'],imgs=[],src=None,demo=None,d='A student grievance platform built at the AI Impact Hackathon.'),
dict(n='Cat Emotion Detection',e='Deep learning · Image + audio',c='#B9E4CC',t=['Python','OpenCV','TensorFlow','Flask'],imgs=[],src=None,demo=None,
 d='A CNN trained on labeled cat facial expressions, with OpenCV preprocessing to improve accuracy. Extended with audio classification and served through Flask.'),
dict(n='5G Session Manager',e='Networking · Test automation',c='#F4C9A0',t=['Flask','Open5GS','UERANSIM','JavaScript','Shell'],imgs=[],src=None,demo=None,
 d='A web app that automates UE and gNodeB operations in a 5G test network. Shell scripts start and stop sessions, and a live dashboard shows logs and active nodes.'),
dict(n='Water Leakage Detection',e='Machine learning · Detection',c='#DFC87A',t=['Python','Machine Learning'],imgs=[],src=None,demo=None,d='A machine learning system for detecting water leakage.')]
# Project links: src = source code, live = deployed app, demo = video/walkthrough (leave out any you don't have)
def link(n,**k): next(p for p in P if p['n']==n).update(**k)
link('AutoEval',src='https://github.com/Harikarthik7124/autoeval',live='https://autoeval-frontend.onrender.com')
link('Cat Emotion Detection',src='https://github.com/Harikarthik7124/cat-emotion-detection-system')
link('5G Session Manager',video='img/projects/5G.mp4',imgs=['task-preview.png'])   # video: a file in img/projects, or a YouTube / Google Drive link
link('AutoEval',imgs=['autoeval-preview.png'])
link('Trustloop AI – Student Grievance',imgs=['trustloop-preview.png'])
link('Cat Emotion Detection',imgs=['cat-preview.png'])
# link('Trustloop AI – Student Grievance',src='...',live='...',demo='...')
from collections import Counter
cnt=Counter(x for p in P for x in p['t']); alltags=sorted(cnt,key=str.lower); popular=[k for k,_ in cnt.most_common(6)]
def proj(i,p):
    tags='|'.join(x.lower() for x in p['t']); text=(p['n']+' '+p['e']+' '+p['d']+' '+' '.join(p['t'])).lower().replace('"','')
    lk=''.join(f'<a href="{u}" target="_blank" rel="noopener" class="font-mono text-sm font-bold hover:underline">{l} ↗</a>' for l,u in (('Source code',p['src']),('Live site',p.get('live')),('Watch demo',p['demo'])) if u)
    vu=p.get('video')
    if vu is not None: lk+=f'<button class="vid font-mono text-sm font-bold hover:underline" data-video="{vu}" data-title="{p["n"]}">Watch video ▶</button>'
    lk=f'<div class="mt-8 flex flex-wrap gap-x-6 gap-y-3 border-t border-ink/40 pt-5">{lk}</div>' if lk else ''
    name=p['n']; imgs=','.join(p['imgs'])
    return f'''<article class="proj grid gap-6 border-t-2 border-ink py-10 first:border-t-0 first:pt-0 lg:grid-cols-[3.5rem_1fr_1fr] lg:gap-10" data-tags="{tags}" data-text="{text}">
<div class="flex items-center gap-2 font-mono text-sm lg:block"><span class="inline-block h-4 w-4 rounded-full border-2 border-ink align-middle"></span> {i:02d}</div>
<div class="min-w-0"><p class="font-mono text-[11px] uppercase tracking-wider opacity-70">{p['e']}</p><h2 class="mt-5 inline-block border-b-2 border-[var(--pacc)] pb-2 text-4xl font-black leading-[.95] tracking-tighter text-[var(--pacc)] md:text-5xl">{name}</h2>
<div class="mt-6 flex flex-wrap gap-2">{pills(p['t'])}</div><p class="mt-6 text-lg leading-relaxed opacity-80">{p['d']}</p>{lk}</div>
<div class="shot relative self-start border-2 border-ink bg-[#EADFCB] shadow-[6px_6px_0_var(--shadow)] md:shadow-[8px_8px_0_var(--shadow)]" data-imgs="{imgs}"><div class="aspect-[16/10] overflow-hidden"><img class="hidden h-full w-full object-contain" alt="{name} screenshot"><div class="ph grid h-full place-items-center p-6 text-center font-serif text-3xl italic text-[#1d1b26] md:text-4xl" style="background:{p['c']}">{name}</div></div>
<div class="ctl absolute bottom-3 right-3 hidden items-center gap-3 rounded-full bg-[#FFFBF1] px-4 py-2 font-mono text-sm text-[#1d1b26]"><button class="prev" aria-label="Previous screenshot">←</button><span class="num"></span><button class="next" aria-label="Next screenshot">→</button></div></div></article>'''
opts='<option value="all">All technologies</option>'+''.join(f'<option value="{t.lower()}">{t}</option>' for t in alltags)
chips=''.join(f'<button class="chip" data-tag="{t.lower()}">{t}</button>' for t in ['All']+popular).replace('data-tag="all"','data-tag="all"')
fld='border-2 border-ink bg-paper px-4 py-4 text-ink'
arch=f'''<section class="{BOX} mb-10 md:mb-14"><div class="flex flex-wrap items-start justify-between gap-4 border-b border-ink/40 bg-[#F0E9EE] p-5 text-[#1d1b26] sm:p-8"><div><p class="font-mono text-[11px] font-bold uppercase tracking-wider"><span class="text-[#c8553d]">●</span> Explore the archive</p><p class="mt-3 opacity-80">Search by project, idea, or tool, or narrow the collection by technology.</p></div><span id="cnt" class="rounded-full bg-[#EADFCB] px-4 py-2 font-mono text-sm">{len(P)} projects</span></div>
<div class="p-5 sm:p-8"><div class="grid gap-5 md:grid-cols-[1fr_20rem]"><label class="block font-mono text-[11px] uppercase tracking-wider">Search projects<span class="relative mt-3 block"><svg class="absolute left-4 top-1/2 -translate-y-1/2 opacity-60" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg><input id="q" type="search" placeholder="Try “AI”, “Flask”, or “docker”…" class="{fld} w-full pl-12 font-sans text-base normal-case tracking-normal placeholder:opacity-50"></span></label>
<label class="block font-mono text-[11px] uppercase tracking-wider">Technology<select id="tech" class="{fld} mt-3 w-full font-sans text-base normal-case tracking-normal">{opts}</select></label></div>
<div class="mt-5 flex flex-wrap items-center gap-2"><span class="mr-2 font-mono text-[11px] uppercase tracking-wider">Popular</span>{chips}</div></div></section>'''
projects=bandbox('02','Selected work','Projects','End-to-end applications across AI, backend and networking. Each one a chance to solve a problem and learn something new.')+f'<main class="mx-auto max-w-7xl px-5 py-12 md:py-16">{arch}<div class="{BOX} p-5 sm:p-8 md:p-12">'+''.join(proj(i+1,p) for i,p in enumerate(P))+'<p id="none" class="hidden py-10 text-center font-mono">No projects match that search.</p></div></main>'
vmodal='<div id="vmodal" class="fixed inset-0 z-[70] hidden items-center justify-center bg-black/70 p-4"><div class="w-full max-w-4xl rounded-xl bg-[#14110f] p-5 text-cream"><div class="flex items-start justify-between gap-4"><h3 id="vt" class="text-xl font-extrabold"></h3><button id="vx" class="shrink-0 rounded-full bg-cream px-5 py-2 font-bold text-black">Close ✕</button></div><div id="vbox" class="mt-5"></div></div></div>'
page('projects','Projects',projects+vmodal)

# ---------- TOOLKIT ----------
T=[('Languages and web',['Python','HTML','CSS','JavaScript','React'],'#D9D0E8'),('Machine learning',['TensorFlow / Keras','PyTorch','OpenCV','LangChain','LangGraph','RAG'],'#F4C9A0'),
('Backend and data',['Flask','FastAPI','REST APIs','MySQL','PostgreSQL','pgvector'],'#9CC9F2'),('Cloud and tooling',['Docker','AWS','Git / GitHub','Postman','Railway','Render','Vercel'],'#DFC87A')]
words=['Python','Flask','FastAPI','TensorFlow','PyTorch','OpenCV','LangGraph','React','PostgreSQL','pgvector','Docker','AWS','Git']
mq=''.join(f'<span class="px-5 text-4xl font-black tracking-tighter sm:text-6xl">{w}</span><span class="text-3xl text-[#3358E8] sm:text-5xl">✦</span>' for w in words*2)
tc=''.join(f'<section class="pop p-5 text-[#1d1b26]" style="background:{c}"><h2 class="text-2xl font-black tracking-tighter">{n}</h2><div class="mt-4 flex flex-wrap gap-2">{pills(x)}</div></section>' for n,x,c in T)
tool=band('03','Toolkit','Tools change.<br><span class="font-serif font-normal italic tracking-normal text-[#3358E8]">Thinking scales.</span>','I pick technology around the system: the constraints, the failure modes, and what will still be understandable six months later.')
tool+=f'<div class="overflow-hidden py-14"><div class="strip py-3"><div class="track items-center">{mq}</div></div></div>'
page('toolkit','Toolkit',tool+f'<main class="mx-auto max-w-7xl px-5 pb-16"><div class="grid gap-7 sm:grid-cols-2">{tc}</div></main>')

# ---------- CREDENTIALS ----------
C=[('IITM Pravartak','LEAP Program Winner','Built an Arduino-based smart heater with automatic control.','leap.png','#D9D0E8',''),
('AWS','AWS ML Foundations','Learned core machine learning concepts and AWS basics.','aws-ml.png','#B9E4CC',''),
('Nunnari Labs','Generative AI Prompt Engineering','Learned generative AI concepts and LLM-based applications.','genai.png','#F4C9A0',''),
('Vaan Megam','5G Networks','Learned the core of 5G wireless networks and topologies.','5g.png','#9CC9F2',''),
('Hackathon','AI Agent Hackathon','Developed an NLP-based Q&amp;A assistant.','ai-agent.png','#DFC87A',''),
('GDG','TechImpact Hackathon','Built a solution in a team-based hackathon.','techimpact.png','#D98574',''),
('McKinsey','McKinsey Forward Program','Completed the McKinsey Forward program.','mckinsey.png','#F7B7C8','')]
def cert(i,t,d,im,c,dt):
    return f'''<article class="flex flex-col border-2 border-ink bg-panel shadow-[5px_5px_0_var(--sh)] md:shadow-[8px_8px_0_var(--sh)]" style="--sh:{c}"><div class="flex aspect-[4/3] items-center justify-center border-b-2 border-ink bg-[#EADFCB] p-5">
<img src="certs/{im}" alt="{t} certificate" loading="lazy" class="max-h-full max-w-full object-contain" onerror="this.style.display='none';this.nextElementSibling.style.display='grid'">
<div class="h-full w-full place-items-center text-center font-serif text-3xl italic text-[#1d1b26]" style="display:none;background:{c}">{i}</div></div>
<div class="flex flex-1 flex-col p-6"><p class="font-mono text-[11px] uppercase tracking-wider opacity-70">{i}</p><h2 class="mt-4 text-3xl font-black leading-[1.05] tracking-tighter">{t}</h2><p class="mt-4 flex-1 leading-relaxed opacity-80">{d}</p>
<div class="mt-6 flex items-center justify-between border-t border-ink/40 pt-5 font-mono text-sm"><span>{dt}</span><button class="view font-bold" data-title="{t}" data-img="certs/{im}">View ↗</button></div></div></article>'''
modal='''<div id="modal" class="fixed inset-0 z-[70] hidden items-center justify-center bg-black/70 p-4"><div class="max-h-[90vh] w-full max-w-3xl overflow-auto rounded-xl bg-[#14110f] p-5 text-cream"><div class="flex items-start justify-between gap-4"><div><h3 id="mt" class="text-xl font-extrabold"></h3><p class="text-sm opacity-70">Press Esc or click outside to close</p></div><button id="mx" class="shrink-0 rounded-full bg-cream px-5 py-2 font-bold text-black">Close ✕</button></div><img id="mi" class="mx-auto mt-5 max-h-[70vh] w-auto" alt="Certificate"><p id="mn" class="mt-8 hidden text-center opacity-70"></p></div></div>'''
cc=''.join(cert(*x) for x in C)
page('credentials','Credentials',bandbox('04','Achievements and certifications','Credentials','Certificates and hackathons. Click View to open the certificate.')+f'<main class="mx-auto max-w-7xl px-5 py-12 md:py-16"><div class="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">{cc}</div></main>'+modal)

# ---------- ABOUT ----------
paras='''<div class="mt-8 max-w-2xl space-y-5 text-lg leading-relaxed md:text-xl"><p>I’m Harikarthik, a Computer Science student at Prince Shri Venkateshwara Padmavathy Engineering College in Chennai (2022–2026), focused on AI/ML engineering. Most recently I interned at Infosys Springboard, building a cat emotion recognition system from computer vision and audio models.</p>
<p>I enjoy taking ideas from model to product: preparing data, training and evaluating models, exposing them through APIs, and shipping a UI someone can use. AutoEval, a multi-agent assessment platform, is where I’ve pushed that furthest.</p>
<p>I’m looking for AI/ML Engineer, Computer Vision, and Data Science roles, and I keep learning in the open: AWS ML Foundations, generative AI prompt engineering, and the McKinsey Forward program.</p></div>'''
def fact(bg,label,inner): return f'<div class="pop p-6 text-[#1d1b26]" style="background:{bg}"><p class="font-mono text-[11px] font-bold uppercase tracking-wider">{label}</p>{inner}</div>'
sk=''.join(f'<div><dt class="font-bold">{a}</dt><dd>{b}</dd></div>' for a,b in [('Languages','Python · HTML · CSS · JavaScript'),('Frameworks','Flask · FastAPI · React'),('Data','MySQL · PostgreSQL · pgvector'),('AI','Machine Learning · GenAI · RAG · Multi-agent systems'),('Tools','Git · Docker · Postman')])
facts=(fact('#F4C9A0','Education','<p class="mt-3 text-2xl font-black leading-tight">Bachelor of Science in Computer Science</p><p class="mt-2">2022 – 2026 · CGPA 8.2 / 10</p><p class="font-serif text-lg italic">Prince Shri Venkateshwara Padmavathy Engineering College, Chennai</p>')
 +fact('#B9E4CC','Skills',f'<dl class="mt-3 space-y-2 font-mono text-sm">{sk}</dl>')
 +fact('#D9D0E8','Looking for','<p class="mt-3 text-2xl font-black leading-tight">AI/ML Engineer · Computer Vision · Data Science</p><p class="mt-2">Based in Chennai, open to Chennai and Bengaluru.</p><a href="contact.html" class="mt-5 inline-block border-b border-[#1d1b26] font-mono text-xs font-bold uppercase">Get in touch ↗</a>'))
page('about','About',bandbox('05','Profile','About Me','',paras)+f'<main class="mx-auto max-w-7xl px-5 py-12 md:py-16"><div class="grid gap-7 md:grid-cols-2 lg:grid-cols-3">{facts}</div></main>')

# ---------- CONTACT ----------
FORM_ENDPOINT=''  # optional: paste a Formspree URL (https://formspree.io/f/xxxx) so messages arrive in your inbox without opening an email app
GOLD='shadow-[6px_6px_0_#C9AE6B] md:shadow-[12px_12px_0_#C9AE6B]'
inp='w-full border-2 border-ink bg-paper px-4 py-3 text-base text-ink placeholder:opacity-50'
rows=''.join(f'<a class="flex items-center justify-between py-4" href="{h}">{l}<span aria-hidden="true">↗</span></a>' for l,h in (('LinkedIn',LINKEDIN),('GitHub',GH),('Resume','Harikarthik_A_Updated_Resume.pdf'),('Phone · +91 72001 54153','tel:+917200154153')))
note='Your message goes directly to my inbox.' if FORM_ENDPOINT else 'Opens your email app with the message ready to send.'
contact=bandbox('06','Get in touch','Contact','Have an interesting opportunity, a challenging problem, or something you’d like to build together? I’d love to hear about it.')+f'''<main class="mx-auto max-w-7xl px-5 py-12 md:py-16"><div class="grid gap-8 lg:grid-cols-2 lg:gap-12">
<section class="border-2 border-ink p-6 text-[#1d1b26] {GOLD} sm:p-10" style="background:#D98574"><p class="font-mono text-[11px] font-bold uppercase tracking-wider">● Direct line</p>
<a href="mailto:{EMAIL}" class="mt-8 block break-all text-3xl font-black leading-tight tracking-tighter sm:text-5xl">{EMAIL} ↗</a><p class="mt-8 text-lg">Based in India · IST (UTC+5:30)</p>
<div class="mt-10 divide-y divide-[#1d1b26]/30 border-t border-[#1d1b26]/30 font-mono text-sm">{rows}</div></section>
<form id="cform" data-endpoint="{FORM_ENDPOINT}" class="border-2 border-ink bg-panel p-6 {GOLD} sm:p-10"><p class="font-mono text-[11px] font-bold uppercase tracking-wider"><span class="text-[#c8553d]">●</span> Leave a message</p>
<div class="mt-8 grid gap-5 sm:grid-cols-2"><label class="block">Your name<input name="name" required class="{inp} mt-3" placeholder="Alex Morgan"></label><label class="block">Email address<input name="email" type="email" required class="{inp} mt-3" placeholder="alex@example.com"></label></div>
<label class="mt-6 block">What’s on your mind?<textarea name="msg" required rows="7" class="{inp} mt-3" placeholder="A little about your idea, project, or opportunity..."></textarea></label>
<div class="mt-8 flex flex-wrap items-center gap-4"><button class="rounded-full border-2 border-ink bg-ink px-6 py-3 font-mono text-sm font-bold text-paper shadow-[4px_4px_0_#C9AE6B]">Send message ↗</button><p class="text-sm opacity-70">{note}</p></div><p id="fstat" role="status" class="mt-4 font-mono text-sm"></p></form></div></main>'''
page('contact','Contact',contact)
