// Script that fetches & prints how to say “Hello” depending on language
$('document').ready(function () {
  const URL = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('INPUT#btn_translate').click(function () {
    $.get(URL + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
