$(document).ready(function(){
    function stopScroll(){
        document.body.style.top = `-${window.scrollY}px`;
        document.body.style.position = 'fixed';
    }
    function enableScroll(){
        const scrollY = document.body.style.top;

        document.body.style.position = '';
        document.body.style.top = '';
        window.scrollTo(0, parseInt(scrollY || window.scrollY) * -1);
    }

    $('nav.top_nav .nav_btn').on('click', function(e){
        e.preventDefault();
        if($('nav.top_nav').hasClass('active')){
            enableScroll();
        } else{
            stopScroll();
        }
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

    $('#about_btn').click(function(e){
        e.preventDefault();
        if($('nav.top_nav').hasClass('active')){
            enableScroll();
            $('nav.top_nav').removeClass('active');
        }
        $([document.documentElement, document.body]).animate({
            scrollTop: $(".about").offset().top
        }, 2000);
    });

    $('#rates_btn').click(function(e){
        e.preventDefault();
        if($('nav.top_nav').hasClass('active')){
            enableScroll();
            $('nav.top_nav').removeClass('active');
        }
        $('nav.top_nav').removeClass('active');
        $([document.documentElement, document.body]).animate({
            scrollTop: $(".rates").offset().top
        }, 2000);
    });

    $('#take_part_btn').click(function(e){
        e.preventDefault();
        if($('nav.top_nav').hasClass('active')){
            enableScroll();
            $('nav.top_nav').removeClass('active');
        }
        $([document.documentElement, document.body]).animate({
            scrollTop: $(".rates").offset().top
        }, 2000);
    });

    $('#quest_btn').click(function(e){
        e.preventDefault();
        if($('nav.top_nav').hasClass('active')){
            enableScroll();
            $('nav.top_nav').removeClass('active');
        }
        $('nav.top_nav').removeClass('active');
        $([document.documentElement, document.body]).animate({
            scrollTop: $(".quest").offset().top
        }, 2000);
    });

    $('#email_btn').click(function(e){
        if($('nav.top_nav').hasClass('active')){
            enableScroll();
            $('nav.top_nav').removeClass('active');
        }
        $('nav.top_nav').removeClass('active');
    });

    $('#sug_btn').click(function(e){
        e.preventDefault();
        
        if($('nav.top_nav').hasClass('active')){
            $('nav.top_nav').removeClass('active');
        } else{
            stopScroll();
        }

        $('nav.top_nav').removeClass('active');
        $('.suggestions').addClass('active');
        $('.suggestions').css({
            height: '100vh',
            opacity: 1
        });
    });

    $('.suggestions .close img').click(function(e){
        e.preventDefault();
        $('.suggestions').removeClass('active');
        $('.suggestions').css({
            opacity: 0
        });
        setTimeout(function(){
            $('.suggestions').css({
                height: '0'
            });
            enableScroll();
        }, 300);
    });

    $('.rates .choose').click(function(e){
        e.preventDefault();

        const el = $(e.target).parent().parent();
        const rate_id = el.attr('data-rate-id'),
            rate_cost = el.attr('data-rate-cost'),
            rate_name = el.attr('data-rate-name');

        $('.cart .rate .choose h3').html(rate_name);
        $('.cart .rate .cost span').html(rate_cost + ' рублей');
        $('.cart form .sum').html(rate_cost + ' рублей');
        $('#id_rate').attr('value', rate_id);

        $('.cart').addClass('active');
        $('.cart').css({
            height: '100vh',
            opacity: 1
        });

        stopScroll();
    });

    $('.cart .close').click(function(e){
        e.preventDefault();

        $('.cart').removeClass('active');
        $('.cart').css({
            opacity: 0
        });
        setTimeout(function(){
            $('.cart').css({
                height: '0'
            });
            enableScroll();
        }, 300);
    });

    $('.cart .cost img').click(function(e){
        e.preventDefault();

        $('.cart').removeClass('active');
        $('.cart').css({
            opacity: 0
        });
        setTimeout(function(){
            $('.cart').css({
                height: '0'
            });
            enableScroll();
        }, 300);
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