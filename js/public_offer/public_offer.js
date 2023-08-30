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
});