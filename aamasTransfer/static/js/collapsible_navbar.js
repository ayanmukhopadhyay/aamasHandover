/*Version added*/
$(document).ready(function () {
	/*Menu-toggle*/
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("active");
    });

    $('.stop-propagation').click(function (e) {
        e.stopPropagation();
    });
});