function ToggleClass () {
  $('HEADER').toggleClass('red');
  $('HEADER').toggleClass('green');
}

$(document).ready(function () {
  $('DIV#toggle_header').click(ToggleClass);
});
