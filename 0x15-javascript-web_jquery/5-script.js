function addLi () {
  $('UL.my_list').append('<li>Item</li>');
}

$(document).ready(function () {
  $('DIV#add_item').click(addLi);
});
