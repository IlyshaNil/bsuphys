const ru=document.getElementById('RU');
const en=document.getElementById('EN');
const blr=document.getElementById('BLR');

ru.classList.add('change-language__active');
const addLine=(event)=>{

    ru.classList.remove("change-language__active");
    en.classList.remove("change-language__active");
    blr.classList.remove("change-language__active");

    event.target.classList.toggle("change-language__active");
};

ru.addEventListener('click',addLine);
en.addEventListener('click',addLine);
blr.addEventListener('click',addLine);