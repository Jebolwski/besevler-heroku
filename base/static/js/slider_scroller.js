let slider = document.querySelector(".slidernav");
let icon = document.querySelector(".fa-bars");
icon.addEventListener("click", () => {
    slider.classList.toggle("slidernavmargin");
});
window.onscroll = function() {
    scrollfunc();
};
let scrollnav = document.querySelector(".scroll-nav");
let scrolltop = document.querySelector(".fa-arrow-up");

function scrollfunc() {
    if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
        scrollnav.style.top = "0";
    } else {
        scrollnav.style.top = "-50px";
    }
    scrolltop.addEventListener("click", () => {
        window.scrollTo(0, 0);
    });
}

let filtre = document.querySelector("#filtre");
let filtretablo = document.querySelector(".filtretablo");
filtre.addEventListener("click", () => {
    filtretablo.classList.toggle("displayed");
});