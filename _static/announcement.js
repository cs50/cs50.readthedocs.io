document.addEventListener('DOMContentLoaded', function () {
    // Get the element with class 'announcement'
    var announcement = document.querySelector('.announcement');

    // Add class 'alert-xxx' to the announcement element
    if (announcement) {
        announcement.classList.add('alert-warning');

        // Add class 'alert-link' to all <a> tags within the announcement element
        var links = announcement.querySelectorAll('a');
        links.forEach(function (link) {
            link.classList.add('alert-link');
        });
    }
});
