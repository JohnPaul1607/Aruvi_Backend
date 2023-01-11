let button = document.querySelector(".menu-btn");
let links = document.querySelector(".mob-nav");
let line1 = document.querySelector(".line1"),
line2 = document.querySelector(".line2"),
line3 = document.querySelector(".line3");

button.addEventListener("click",function(){
    links.classList.toggle("navdisp")
    line1.classList.toggle("act")
    line2.classList.toggle("act")
    line3.classList.toggle("act")
})