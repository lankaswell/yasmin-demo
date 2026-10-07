const menu=document.querySelector('.menu');
const nav=document.querySelector('#navigation');
const toggle=document.querySelector('.activity-toggle');
const submenu=document.querySelector('#activity-submenu');
function closeActivities(){toggle?.setAttribute('aria-expanded','false');if(submenu)submenu.hidden=true}
function closeMenu(){menu?.setAttribute('aria-expanded','false');nav?.classList.remove('open');closeActivities()}
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);if(!open)closeActivities()});
toggle?.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));submenu.hidden=!open});
nav?.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu()});
document.addEventListener('click',e=>{if(!e.target.closest('.activity-group'))closeActivities()});
document.addEventListener('keydown',e=>{if(e.key!=='Escape')return;if(toggle?.getAttribute('aria-expanded')==='true'){closeActivities();toggle.focus()}else if(menu?.getAttribute('aria-expanded')==='true'){closeMenu();menu.focus()}});
document.querySelector('.activity-group')?.addEventListener('focusout',e=>{if(!e.currentTarget.contains(e.relatedTarget))closeActivities()});
document.querySelector('.form-demo')?.addEventListener('submit',e=>{e.preventDefault();const m=document.querySelector('.form-message');m.hidden=false;m.textContent='Questa è una demo: il messaggio non è stato inviato né salvato. Il modulo sarà collegato ai recapiti di Yasmin nella versione definitiva.';m.scrollIntoView({block:'nearest',behavior:'smooth'})});
