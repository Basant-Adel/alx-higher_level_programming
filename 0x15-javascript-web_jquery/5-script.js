// Script to add <li> element to list when user clicks on tag DIV#add_item
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
