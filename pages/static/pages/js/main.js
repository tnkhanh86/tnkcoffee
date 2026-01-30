(function ($) {
    "use strict";

    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 40) {
            $('.navbar').addClass('sticky-top');
        } else {
            $('.navbar').removeClass('sticky-top');
        }
    });

    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });


    // Modal Video
    $(document).ready(function () {
        var $videoSrc;
        $('.btn-play').click(function () {
            $videoSrc = $(this).data("src");
        });
        console.log($videoSrc);

        $('#videoModal').on('shown.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
        })

        $('#videoModal').on('hide.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc);
        })
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        margin: 45,
        dots: true,
        loop: true,
        center: true,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });


    // Tab Switching Logic for Dropdown Menu
    function activateTabFromHash() {
        var hash = window.location.hash;
        if (hash) {
            var tabTriggerEl = $('.nav-pills a[href="' + hash + '"]');
            if (tabTriggerEl.length) {
                var tab = new bootstrap.Tab(tabTriggerEl[0]);
                tab.show();
                // Optional: Scroll to the tab section
                $('html, body').animate({
                    scrollTop: $('.tab-class').offset().top - 100
                }, 500);
            }
        }
    }

    // Activate on load
    $(document).ready(function () {
        activateTabFromHash();
    });

    // Activate on hash change
    $(window).on('hashchange', function () {
        activateTabFromHash();
    });

    // Ensure dropdown links also trigger the hash change event or direct update
    $('.dropdown-menu .dropdown-item').on('click', function (e) {
        var href = $(this).attr('href');
        if (href && href.indexOf('#') !== -1) {
            var hash = href.substring(href.indexOf('#'));
            // If we are already on the page, the hash change happens naturally,
            // but we might want to force the tab switch or scroll immediately
            // if logic above catches it, fine.
        }
    });

})(jQuery);

