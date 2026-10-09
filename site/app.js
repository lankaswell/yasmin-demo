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

// Content stays visible without JavaScript or animation support.
const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
if(!reducedMotion.matches && 'IntersectionObserver' in window && 'animate' in Element.prototype){
 const animations=new Set();
 const observer=new IntersectionObserver(entries=>{
  for(const entry of entries){
   if(!entry.isIntersecting)continue;
   observer.unobserve(entry.target);
   if(reducedMotion.matches)continue;
   const animation=entry.target.animate(
    [{opacity:0,transform:'translateY(18px)'},{opacity:1,transform:'translateY(0)'}],
    {duration:580,easing:'cubic-bezier(.22,1,.36,1)'}
   );
   animations.add(animation);
   animation.finished.then(()=>animations.delete(animation),()=>animations.delete(animation));
  }
 },{threshold:0.01,rootMargin:'0px 0px -32px 0px'});
 document.querySelectorAll('.home-paths,.home-about,.home-course,.content-section,.closing').forEach(section=>{
  if(section.getBoundingClientRect().top>=window.innerHeight-32)observer.observe(section);
 });
 reducedMotion.addEventListener('change',event=>{
  if(!event.matches)return;
  observer.disconnect();
  for(const animation of animations)animation.cancel();
  animations.clear();
 });
}
