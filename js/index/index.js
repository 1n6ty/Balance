$(document).ready(function(){
    $('nav.top_nav .nav_btn').on('click', function(e){
        e.preventDefault();
        $('nav.top_nav').toggleClass('active');
    });

    $('.quest .q img').on('click', function(e){
        let el = $(e.target).parent().parent();

        e.preventDefault();

        if(el.hasClass('active')){
            $('.quest .q').removeClass('active');
        } else{
            $('.quest .q').removeClass('active');
            el.toggleClass('active');
        }
    });

    $('.swiper').slick({
        arrows: true,
        autoplay: true,
        prevArrow: $('.btn-prev'),
        nextArrow: $('.btn-next'),
        slidesToShow: 1,
        centerMode: true,
        variableWidth: true,
        autoplaySpeed: 5000
    });
});