$(document).ready(function () {
    // Add active class to the currently displayed page linked in the navbar
    var url = window.location["href"];
    $('ul.nav a').filter(function() {
         return this.href == url;
    }).addClass('active');
});