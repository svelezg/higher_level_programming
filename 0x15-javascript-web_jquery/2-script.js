function myFunction () {
  $('HEADER').css({ color: '#FF0000' });
}
$('DIV#red_header').click(myFunction);

/*
$(function () {
  $('DIV#red_header').click(function () {
    $('HEADER').css({ color: '#FF0000' });
  });
}); */
