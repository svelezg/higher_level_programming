$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const str = $('INPUT#language_code').val();
    $.ajax({
      type: 'POST',
      url: 'https://www.fourtonfish.com/hellosalut/',
      data: { lang: str },
      success: function (data) {
        const myResult = data.hello;
        $('DIV#hello').append(myResult);
      }
    });
  });
});
