$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, textStatus) => {
    $('DIV#hello').text(data.hello);
  });
});
