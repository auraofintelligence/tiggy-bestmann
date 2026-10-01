const menuButton=document.querySelector('.menu-button');
const menu=document.querySelector('#chapter-menu');
function setMenu(open,returnFocus=false){
  menu.hidden=!open;
  menuButton.setAttribute('aria-expanded',String(open));
  menuButton.querySelector('span').textContent=open?'−':'+';
  if(returnFocus)menuButton.focus();
}
menuButton.addEventListener('click',()=>setMenu(menu.hidden));
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&!menu.hidden)setMenu(false,true);});
document.addEventListener('click',event=>{if(!menu.hidden&&!menu.contains(event.target)&&!menuButton.contains(event.target))setMenu(false);});
const moods={
  make:['Music and Glastonbury','i C. infinity is the music, Sway is the new instrument on its way, and performing at Glastonbury is the dream that began in 2004.','music.html','Music and Glastonbury'],
  wander:['Bodyboarding','An epic wave, the speed of the ride and women sharing the fun in the surf. Bodyboarding is part of the beach life behind Tiggy’s adventures.','water.html','Bodyboarding'],
  company:['World travel','Every country and territory is the ambition. Work, events, people and invitations shape a route that stays open to new opportunities.','out-about.html','World travel']
};
document.querySelectorAll('[data-mood]').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('[data-mood]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
  const [title,copy,href,label]=moods[button.dataset.mood];
  const result=document.querySelector('.play-result');
  result.replaceChildren(Object.assign(document.createElement('h3'),{textContent:title}),Object.assign(document.createElement('p'),{textContent:copy}));
  const link=document.querySelector('.round-link');link.href=href;link.setAttribute('aria-label',label);
}));
