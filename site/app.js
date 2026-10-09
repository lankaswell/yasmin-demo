const menu=document.querySelector('.menu');
const nav=document.querySelector('#navigation');
const toggle=document.querySelector('.activity-toggle');
const submenu=document.querySelector('#activity-submenu');
function closeActivities(){toggle?.setAttribute('aria-expanded','false');if(submenu)submenu.hidden=true}
function closeMenu(){menu?.setAttribute('aria-expanded','false');nav?.classList.remove('open');closeActivities()}
window.matchMedia('(max-width: 800px)').addEventListener('change',closeMenu);
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);if(!open)closeActivities()});
toggle?.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));submenu.hidden=!open});
nav?.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu()});
document.addEventListener('click',e=>{if(!e.target.closest('.activity-group'))closeActivities();if(!e.target.closest('.site-header'))closeMenu()});
document.addEventListener('keydown',e=>{if(e.key!=='Escape')return;if(toggle?.getAttribute('aria-expanded')==='true'){closeActivities();toggle.focus()}else if(menu?.getAttribute('aria-expanded')==='true'){closeMenu();menu.focus()}});
document.querySelector('.activity-group')?.addEventListener('focusout',e=>{if(!e.currentTarget.contains(e.relatedTarget))closeActivities()});
document.querySelector('.form-demo')?.addEventListener('submit',e=>{e.preventDefault();const m=document.querySelector('.form-message');m.hidden=false;m.textContent='Questa è una demo: il messaggio non è stato inviato né salvato. Il modulo sarà collegato ai recapiti di Yasmin nella versione definitiva.';m.scrollIntoView({block:'nearest',behavior:'smooth'})});

// Prepare off-screen content before observing it, so it never flashes before entering.
const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
if(!reducedMotion.matches && 'IntersectionObserver' in window && 'animate' in Element.prototype){
 const mobileReveal=window.matchMedia('(max-width: 800px)').matches;
 const pending=new Set();
 const animations=new Map();
 function show(target){
  observer.unobserve(target);
  pending.delete(target);
  target.classList.remove('reveal-pending');
  target.style.removeProperty('--reveal-x');
  animations.get(target)?.cancel();
  animations.delete(target);
 }
 const observer=new IntersectionObserver(entries=>{
  for(const entry of entries){
   if(!entry.isIntersecting)continue;
   observer.unobserve(entry.target);
   const target=entry.target;
   if(reducedMotion.matches){show(target);continue;}
   const activityIndex=[...document.querySelectorAll('.activity-door')].indexOf(target);
   const animation=target.animate(
    [{opacity:0,transform:`translateX(${target.style.getPropertyValue('--reveal-x')})`},{opacity:1,transform:'translateX(0)'}],
    {duration:800,delay:!mobileReveal && activityIndex>=0 ? activityIndex*100 : 0,easing:'cubic-bezier(.22,1,.36,1)',fill:'both'}
   );
   animations.set(target,animation);
   animation.finished.then(()=>show(target),()=>{});
  }
 },{threshold:0,rootMargin:'0px 0px -24px 0px'});
 document.querySelectorAll('.paths-intro,.paths-heading,.activity-door,.home-about,.home-course,.content-section,.closing').forEach((target,index)=>{
  // Anything already visible (including an anchor destination) stays visible.
  if(target.getBoundingClientRect().top<window.innerHeight)return;
  target.style.setProperty('--reveal-x',`${(index%2 ? 1 : -1)*(mobileReveal ? 32 : 44)}px`);
  target.classList.add('reveal-pending');
  pending.add(target);
  observer.observe(target);
 });
 document.addEventListener('focusin',event=>{
  for(const target of pending)if(target.contains(event.target))show(target);
 });
 reducedMotion.addEventListener('change',event=>{
  if(!event.matches)return;
  observer.disconnect();
  for(const target of pending)show(target);
 });
}
