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
  make:['Music and Glastonbury','A Glastonbury crew pass, i C. infinity and a Sway controller on its way. Tiggy wants to take the music on stage.','music.html','Music and Glastonbury'],
  wander:['Bodyboarding','Speed along a clean face, company in the surf and Sunshine Coast memories. Tiggy is still dreaming of an epic ride.','water.html','Bodyboarding'],
  company:['World travel','Bangkok boats, Darwin departures and a working traveller’s memories. Every country and territory is on his wish list.','out-about.html','World travel']
};
document.querySelectorAll('[data-mood]').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('[data-mood]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
  const [title,copy,href,label]=moods[button.dataset.mood];
  const result=document.querySelector('.play-result');
  result.replaceChildren(Object.assign(document.createElement('h3'),{textContent:title}),Object.assign(document.createElement('p'),{textContent:copy}));
  const link=document.querySelector('.round-link');link.href=href;link.setAttribute('aria-label',label);
}));
