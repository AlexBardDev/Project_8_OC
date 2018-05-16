$("#about button").on("click", function () {
	$("#about form").submit();
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

if ($(".special_message")) {
  setTimeout(function () {
    $(".special_message").remove();
  }, 3000);
};
