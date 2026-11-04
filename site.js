const root=document.documentElement,$=s=>document.querySelector(s);
const tbtn=$('#theme');
const setTheme=d=>{root.classList.toggle('dark',d);tbtn.textContent=d?'☀':'☾';try{localStorage.setItem('theme',d?'dark':'light')}catch(e){}};
let sv=null;try{sv=localStorage.getItem('theme')}catch(e){}
setTheme(sv?sv==='dark':matchMedia('(prefers-color-scheme: dark)').matches);
tbtn.addEventListener('click',()=>setTheme(!root.classList.contains('dark')));
const ring=$('#ring');addEventListener('mousemove',e=>{ring.style.transform=`translate(${e.clientX}px,${e.clientY}px)`});
const mb=$('#menu'),mn=$('#mnav');
const mset=o=>{mb.innerHTML=o?'<span>CLOSE</span><span aria-hidden="true" class="text-xl leading-none">✕</span>':'<span>MENU</span><span aria-hidden="true" class="text-xl leading-none">≡</span>'};
mb.addEventListener('click',()=>{const h=mn.classList.toggle('hidden');mb.setAttribute('aria-expanded',String(!h));mset(!h)});
// Certificate viewer
const modal=$('#modal');
if(modal){
  const img=$('#mi'),note=$('#mn'),close=()=>{modal.classList.add('hidden');modal.classList.remove('flex')};
  document.querySelectorAll('.view').forEach(b=>b.addEventListener('click',()=>{
    $('#mt').textContent=b.dataset.title;note.classList.add('hidden');img.classList.remove('hidden');
    img.onerror=()=>{img.classList.add('hidden');note.textContent='Add the certificate image at site/'+b.dataset.img+' to show it here.';note.classList.remove('hidden')};
    img.src=b.dataset.img;modal.classList.remove('hidden');modal.classList.add('flex');}));
  $('#mx').addEventListener('click',close);
  modal.addEventListener('click',e=>{if(e.target===modal)close()});
  addEventListener('keydown',e=>{if(e.key==='Escape')close()});
}
// Contact form → opens the visitor's email app with the message filled in
const f=$('#cform');
if(f)f.addEventListener('submit',async e=>{e.preventDefault();const d=new FormData(f),ep=f.dataset.endpoint,st=$('#fstat');
  if(ep){st.textContent='Sending…';
    try{const r=await fetch(ep,{method:'POST',body:d,headers:{Accept:'application/json'}});if(!r.ok)throw 0;f.reset();st.textContent='Thanks! Your message is on its way.'}
    catch(x){st.textContent='Could not send. Please email me directly.'}return}
  location.href='mailto:aharikarthik7124@gmail.com?subject='+encodeURIComponent('Portfolio message from '+d.get('name'))+'&body='+encodeURIComponent(d.get('msg')+'\n\n'+d.get('name')+' ('+d.get('email')+')');});
// Marquee: always drifts left to right; scrolling gives it a push (down = faster, up = slower), then it settles back. Never pauses.
document.querySelectorAll('.track').forEach(t=>{
  t.style.animation='none';
  let x=0,last=scrollY,prev=performance.now();
  const tick=now=>{
    const dt=Math.max(0,Math.min(now-prev,64))/1000;prev=now;
    const dy=scrollY-last;last=scrollY;
    const half=t.scrollWidth/2;
    if(half){
      x+=45*dt+Math.max(-60,Math.min(60,dy))*.9;
      t.style.transform=`translateX(${((x%half)+half)%half-half}px)`;
    }
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
});

// Projects: search, technology filter, screenshot sliders
const pq=$('#q');
if(pq){
  const items=[...document.querySelectorAll('.proj')],sel=$('#tech'),cnt=$('#cnt'),chips=[...document.querySelectorAll('.chip')];let tag='all';
  const run=()=>{const term=pq.value.trim().toLowerCase();let n=0;
    items.forEach(a=>{const ok=(tag==='all'||a.dataset.tags.split('|').includes(tag))&&(!term||a.dataset.text.includes(term));a.classList.toggle('hidden',!ok);if(ok)n++});
    cnt.textContent=n+(n===1?' project':' projects');$('#none').classList.toggle('hidden',n>0);
    chips.forEach(c=>c.classList.toggle('on',c.dataset.tag===tag));sel.value=tag;};
  pq.addEventListener('input',run);sel.addEventListener('change',()=>{tag=sel.value;run()});
  chips.forEach(c=>c.addEventListener('click',()=>{tag=c.dataset.tag;run()}));run();
}
document.querySelectorAll('.shot').forEach(s=>{
  const imgs=(s.dataset.imgs||'').split(',').filter(Boolean);if(!imgs.length)return;
  const im=s.querySelector('img'),ph=s.querySelector('.ph'),ctl=s.querySelector('.ctl'),num=s.querySelector('.num');let i=0;
  const show=()=>{im.src='img/projects/'+imgs[i];num.textContent=(i+1)+' / '+imgs.length};
  im.onerror=()=>{im.classList.add('hidden');ph.classList.remove('hidden')};
  im.onload=()=>{im.classList.remove('hidden');ph.classList.add('hidden')};
  if(imgs.length>1){ctl.classList.remove('hidden');ctl.classList.add('flex')}
  s.querySelector('.prev').onclick=()=>{i=(i-1+imgs.length)%imgs.length;show()};
  s.querySelector('.next').onclick=()=>{i=(i+1)%imgs.length;show()};show();
});

// Project demo videos: YouTube / Google Drive / direct .mp4 play in a popup; other links open in a new tab
const vm=$('#vmodal');
if(vm){
  const box=$('#vbox'),vclose=()=>{vm.classList.add('hidden');vm.classList.remove('flex');box.innerHTML=''};
  const embed=u=>{let m;
    if((m=u.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/|shorts\/))([\w-]{11})/)))return{t:'f',s:'https://www.youtube.com/embed/'+m[1]};
    if((m=u.match(/drive\.google\.com\/file\/d\/([\w-]+)/)))return{t:'f',s:'https://drive.google.com/file/d/'+m[1]+'/preview'};
    if(/\.(mp4|webm|mov)(\?|$)/i.test(u))return{t:'v',s:u};
    return null};
  document.querySelectorAll('.vid').forEach(b=>b.addEventListener('click',()=>{
    const u=b.dataset.video,e=u&&embed(u);
    if(u&&!e){window.open(u,'_blank','noopener');return}
    $('#vt').textContent=b.dataset.title+' · demo video';
    box.innerHTML=!u?'<p class="py-16 text-center opacity-70">The demo video link has not been added yet.</p>':e.t==='f'
      ?'<iframe src="'+e.s+'" class="aspect-video w-full" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Demo video"></iframe>'
      :'<video src="'+e.s+'" class="w-full" controls playsinline></video>';
    vm.classList.remove('hidden');vm.classList.add('flex');}));
  $('#vx').addEventListener('click',vclose);
  vm.addEventListener('click',e=>{if(e.target===vm)vclose()});
  addEventListener('keydown',e=>{if(e.key==='Escape')vclose()});
}
