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
  make:['The bird takes a bow.','She bows back. Tiggy joins her, and the crew starts laughing. Their outback stage build has acquired an opening act. Afterwards, she asks whether he is staying for dinner.','fool.html','The happy-go-lucky fool'],
  wander:['She has saved him a seat.','The volleyball net is down, the screen is lit and there is salt drying in his hair. She waves him over. Her friends have brought food; someone has remembered his drink.','water.html','Sand, salt and screen'],
  company:['There is a band downstairs.','The artist has shown him the floating festival model. Now she mentions a singer she thinks he would enjoy. Her colleague is already smiling at the prospect of all three going together.','possibilities.html','An evening in Nairobi']
};
document.querySelectorAll('[data-mood]').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('[data-mood]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
  const [title,copy,href,label]=moods[button.dataset.mood];
  const result=document.querySelector('.play-result');
  result.replaceChildren(Object.assign(document.createElement('h3'),{textContent:title}),Object.assign(document.createElement('p'),{textContent:copy}));
  const link=document.querySelector('.round-link');link.href=href;link.setAttribute('aria-label',label);
}));
