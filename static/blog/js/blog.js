$(document).ready(function() {
    // Reading Progress Bar
    $(window).scroll(function() {
        var scrollTop = $(window).scrollTop();
        var docHeight = $(document).height();
        var winHeight = $(window).height();
        var scrollPercent = (scrollTop / (docHeight - winHeight)) * 100;
        $('#reading-progress').css('width', scrollPercent + '%');

        // Active TOC Highlighting (Simple Implementation)
        $('h2[id]').each(function() {
            var top = $(this).offset().top - 100;
            var id = $(this).attr('id');
            if (scrollTop >= top) {
                $('.toc-list a').removeClass('active');
                $('.toc-list a[href="#' + id + '"]').addClass('active');
            }
        });
    });

    // Smooth Scroll for TOC
    $('.toc-list a').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top - 80
        }, 500);
    });

    // Pulse Animation for Ad Button
    setInterval(function() {
        $('.pulse-anim').animate({transform: 'scale(1.05)'}, 500).animate({transform: 'scale(1)'}, 500);
    }, 2000);
});