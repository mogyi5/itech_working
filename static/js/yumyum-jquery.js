//  I don't think we use this anywhere actually? The problem was solved with formfactory.
function removeDiv(elem){
  $(elem).parent('div').remove();
}

// The function to change serving sizes.
$(window).bind("load", function() {
  $(function() {
    $('.serving').bind('keyup', function(event) {
      var previousValue = parseFloat($("#previousServing").val());
      var newValue = parseFloat($(event.target).val());
      if (previousValue && newValue) {
        $('.ingredient').each(function(index, elem) {
          var ingredientNow = $('.amount', elem);
          var oldIngredientAmount = ingredientNow.text();
          var newIngredientAmount = oldIngredientAmount * newValue / previousValue;
          ingredientNow.text(newIngredientAmount);
        });
        $('#previousServing').val(newValue);
      }
    });
  });
});
