$(document).ready(function() {
    // Filter Functionality
    $('.btn-filter').click(function() {
        // Remove active class from all
        $('.btn-filter').removeClass('active');
        $(this).addClass('active');

        const filterValue = $(this).attr('data-filter');

        if (filterValue === 'all') {
            $('.blog-item').fadeIn(400);
        } else {
            $('.blog-item').hide(); // Hide all first
            $('.blog-item[data-category="' + filterValue + '"]').fadeIn(400);
        }
    });

    // Smooth entrance for elements as they scroll into view (Simple Observer)
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                entry.target.style.opacity = 1;
            }
        });
    });

    // Optional: You can attach this to elements if you remove the initial classes
});
