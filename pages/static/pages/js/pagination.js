(function ($) {
    "use strict";

    $(document).ready(function () {
        const itemsPerPage = 10;

        // Function to setup pagination for a specific tab pane
        function setupPagination(paneId) {
            const pane = $('#' + paneId);
            const items = pane.find('.row > div.col-lg-6'); // Adjust selector to match product items
            const totalItems = items.length;
            const totalPages = Math.ceil(totalItems / itemsPerPage);

            if (totalItems <= itemsPerPage) return;

            // Create pagination container if it doesn't exist
            let paginationContainer = pane.find('.pagination-container');
            if (paginationContainer.length === 0) {
                paginationContainer = $('<div class="pagination-container d-flex justify-content-center mt-4"></div>');
                pane.append(paginationContainer);
            }

            // Generate pagination HTML
            function renderPagination(currentPage) {
                let html = '<nav aria-label="Page navigation"><ul class="pagination pagination-lg">';
                
                // Previous Button
                html += `<li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
                            <a class="page-link" href="#" data-page="${currentPage - 1}" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                            </a>
                         </li>`;

                // Page Numbers
                for (let i = 1; i <= totalPages; i++) {
                    html += `<li class="page-item ${i === currentPage ? 'active' : ''}">
                                <a class="page-link" href="#" data-page="${i}">${i}</a>
                             </li>`;
                }

                // Next Button
                html += `<li class="page-item ${currentPage === totalPages ? 'disabled' : ''}">
                            <a class="page-link" href="#" data-page="${currentPage + 1}" aria-label="Next">
                                <span aria-hidden="true">&raquo;</span>
                            </a>
                         </li>`;
                
                html += '</ul></nav>';
                paginationContainer.html(html);

                // Attach click events
                paginationContainer.find('.page-link').on('click', function (e) {
                    e.preventDefault();
                    const page = $(this).data('page');
                    if (page && page >= 1 && page <= totalPages && page !== currentPage) {
                        showPage(page);
                    }
                });
            }

            // Function to display items for a specific page
            function showPage(page) {
                items.hide();
                const start = (page - 1) * itemsPerPage;
                const end = start + itemsPerPage;
                items.slice(start, end).fadeIn(); // Use fadeIn for smooth transition
                
                renderPagination(page);
                
                // Scroll to top of products row to see new items if needed
                // $('html, body').animate({
                //     scrollTop: pane.offset().top - 100
                // }, 500);
            }

            // Initialize with first page
            showPage(1);
        }

        // Initialize pagination for all tabs
        $('.tab-pane').each(function () {
            setupPagination($(this).attr('id'));
        });
        
        // Optional: Re-adjust if needed when tab is switched (though each has its own independent pagination)
        $('a[data-bs-toggle="pill"]').on('shown.bs.tab', function (e) {
            // Nothing needed here strictly if logic is per-pane and independent
        });
    });

})(jQuery);
