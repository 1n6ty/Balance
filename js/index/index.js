var top_nav_btn = document.querySelector('nav.top_nav .nav_btn'),
    top_nav = document.querySelector('nav.top_nav');

top_nav_btn.addEventListener('click', (e) => {
    top_nav.classList.toggle('active');
}, false);

$(document).ready(function(){
    $('.swiper').slick({
        arrows: true,
        autoplay: true,
        prevArrow: $('.btn-prev'),
        nextArrow: $('.btn-next'),
        slidesToShow: 1,
        centerMode: true,
        variableWidth: true
    });
});