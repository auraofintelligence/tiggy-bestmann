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
  make:['From Glastonbury to Sway.','The wish to perform began while Luke was helping set up Glastonbury in 2004. Learning to perform i C. infinity with Sway is the next exploration.','music.html','From Glastonbury to Sway'],
  wander:['Bodyboarding epic waves.','The wave ambition brings physical skill, timing and the Ocean Master into the adventure. Beach life, sand sports and outdoor cinema give the shore its own pleasures.','water.html','Sand, salt and screen'],
  company:['Fast travel, full days.','Every country and territory, with room to meet, share, learn and teach. Work, relationships and opportunities keep the route open.','out-about.html','Fast travel, full days']
};
document.querySelectorAll('[data-mood]').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('[data-mood]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
  const [title,copy,href,label]=moods[button.dataset.mood];
  const result=document.querySelector('.play-result');
  result.replaceChildren(Object.assign(document.createElement('h3'),{textContent:title}),Object.assign(document.createElement('p'),{textContent:copy}));
  const link=document.querySelector('.round-link');link.href=href;link.setAttribute('aria-label',label);
}));
