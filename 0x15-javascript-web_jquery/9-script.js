$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      const myResult = data.hello;
      $('DIV#hello').text(myResult);
    }
  });
});
