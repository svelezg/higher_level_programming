function addLi () {
  $('UL.my_list').append('<li>Item</li>');
}

function remLi () {
  $('UL.my_list li:first-child').remove();
}

function clLi () {
  $('UL.my_list').empty();
}

$(document).ready(function () {
  $('DIV#add_item').click(addLi);
  $('DIV#remove_item').click(remLi);
  $('DIV#clear_list').click(clLi);
});
