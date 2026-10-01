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
  make:['From Glastonbury to Sway.','The festival crew days left a lasting dream: to return as a performer. Sway is on its way, and i C. infinity is the music he wants to bring to life.','music.html','From Glastonbury to Sway'],
  wander:['Bodyboarding epic waves.','An epic ride is on his wish list. Back on shore, the afternoon is still open: teasing, a game on the sand and a film after sunset.','water.html','Sand, salt and screen'],
  company:['Fast travel, full days.','Every country and territory is the ambition. Work brings him into new places; people he wants to see again help shape the next journey.','out-about.html','Fast travel, full days']
};
document.querySelectorAll('[data-mood]').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('[data-mood]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
  const [title,copy,href,label]=moods[button.dataset.mood];
  const result=document.querySelector('.play-result');
  result.replaceChildren(Object.assign(document.createElement('h3'),{textContent:title}),Object.assign(document.createElement('p'),{textContent:copy}));
  const link=document.querySelector('.round-link');link.href=href;link.setAttribute('aria-label',label);
}));
