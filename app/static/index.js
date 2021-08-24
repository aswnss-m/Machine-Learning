function reveal(){
    var intro = document.getElementById('intro');
    intro.style.transform = 'translateX(-100%)';
    // intro.style.-webkit-transform = "translateX(-100%)";
    // intro.style.-moz-transform = "translateX(-100%)";
    // intro.style.-o-transform = "translateX(-100%)";
    // intro.style.-ms-transform = "translateX(-100%)";
    // intro.style.transform = "translateX(-100%)";
    intro.classList.remove('shadow');
}