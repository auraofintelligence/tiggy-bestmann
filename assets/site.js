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
  make:['The crowd arrives in two hours.','Red dust, a touring stage and a very large prop with a mind of its own. She has a better way to rig it. Tiggy has a question about dinner after the show.','fool.html','Meet the happy-go-lucky fool'],
  wander:['One match before the sound check.','She needs another player. He has forty minutes, questionable volleyball skills and a screening to help set up. They are already arguing cheerfully about the score.','water.html','Explore sand sports and outdoor cinema'],
  company:['The presentation is done. The evening is not.','At a Nairobi reception, an artist shows him a floating festival venue. Then she suggests they leave the model alone and go and hear the band.','possibilities.html','Explore bigger experiences']
};
document.querySelectorAll('[data-mood]').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('[data-mood]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
  const [title,copy,href,label]=moods[button.dataset.mood];
  const result=document.querySelector('.play-result');
  result.replaceChildren(Object.assign(document.createElement('h3'),{textContent:title}),Object.assign(document.createElement('p'),{textContent:copy}));
  const link=document.querySelector('.round-link');link.href=href;link.setAttribute('aria-label',label);
}));
