document.addEventListener('DOMContentLoaded', function() {
    var dropdownLinks = document.getElementsByClassName('sidebar-dropdown');

    for (var i = 0; i < dropdownLinks.length; i++) {
        dropdownLinks[i].addEventListener('click', function(event) {
            event.preventDefault();
            var submenu = this.nextElementSibling;
            submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
        });
    }
});