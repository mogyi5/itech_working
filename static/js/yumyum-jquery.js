$(document).ready( function() {
  $("#add-btn").click( function() {
    $( "#ing" ).clone().appendTo( $( "#ings" ) );
  });
});

function removeDiv(elem){
  $(elem).parent('div').remove();
}
