$(document).ready(function () {
  function translate () {
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
  }
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keypress(function (e) {
    const key = e.which;
    if (key === 13) {
      translate();
    }
  });
});
