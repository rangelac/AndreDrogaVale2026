'use strict';
document.documentElement.classList.add('js');
const menuButton=document.querySelector('.menu-toggle');
const navigation=document.querySelector('#menu');
function closeMenu(){menuButton.setAttribute('aria-expanded','false');navigation.classList.remove('is-open');}
menuButton.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));navigation.classList.toggle('is-open',open);});
navigation.querySelectorAll('a').forEach(link=>link.addEventListener('click',closeMenu));
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&menuButton.getAttribute('aria-expanded')==='true'){closeMenu();menuButton.focus();}});
document.addEventListener('click',event=>{if(!event.target.closest('.site-header'))closeMenu();});
window.matchMedia('(min-width:681px)').addEventListener('change',closeMenu);
const privacyDialog=document.querySelector('#privacy-dialog');
document.querySelector('[data-open-privacy]').addEventListener('click',()=>privacyDialog.showModal());
privacyDialog.querySelector('.close-dialog').addEventListener('click',()=>privacyDialog.close());
privacyDialog.addEventListener('click',event=>{if(event.target===privacyDialog){const box=privacyDialog.getBoundingClientRect();if(event.clientX<box.left||event.clientX>box.right||event.clientY<box.top||event.clientY>box.bottom)privacyDialog.close();}});
