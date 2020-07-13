const nav=document.getElementById('nav');
const menu=document.getElementById('nav_menu');

const logoMenu = document.querySelectorAll('.header_icon');


menu.addEventListener('click',(event)=>{
    event.preventDefault();
    nav.classList.toggle('nav_active');
    logoMenu.forEach(item=>item.classList.remove('header_active'))
    if(nav.classList.contains('nav_active')){
        logoMenu[1].classList.add('header_active')
    }else{
        logoMenu[0].classList.add('header_active')
    }
})