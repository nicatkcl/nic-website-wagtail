// $(function(){
//     console.log('ready');
    
//     $('.navbar-nav a').click(function(e) {
//         // e.preventDefault()
        
//         $that = $(this);
        
//         $('.navbar-nav').find('a').removeClass('active');
//         $that.addClass('active');
//     });
// })

! function (e) {
    "use strict";
    e('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (location.pathname.replace(/^\//, "") == this.pathname.replace(/^\//, "") && location.hostname == this.hostname) {
            var a = e(this.hash);
            console.log(a)
            if ((a = a.length ? a : e("[name=" + this.hash.slice(1) + "]")).length) return e("html, body").animate({
                scrollTop: a.offset().top - 54
            }, 1e3, "easeInOutExpo"), !1
        }
    }), e(".js-scroll-trigger").click(function () {
        e(".navbar-collapse").collapse("hide")
    }), e("body").scrollspy({
        target: "#mainNav",
        offset: 56
    });

    // function a() {
    //     100 < e("#mainNav").offset().top ? e("#mainNav").addClass("navbar-shrink") : e("#mainNav").removeClass("navbar-shrink")
    // }
    // e(window).scroll(a)
}(jQuery);