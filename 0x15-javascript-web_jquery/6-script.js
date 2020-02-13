function changeText () {
  $('HEADER').text('New Header!!!');
}

$(document).ready(function () {
  $('DIV#update_header').click(changeText);
});
