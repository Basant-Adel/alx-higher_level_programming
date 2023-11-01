// Script that fetches from URL and displays the value of hello
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
  $('DIV#hello').text(data.hello);
});
