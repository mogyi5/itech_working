
$(document).ready( function() {
  $("#add-btn").click( function() {
    $( "#ing" ).clone().appendTo( $( "#ings" ) );
  });
});

// $('#suggestion').keyup(function(){ var query;
//   query = $(this).val();
//   $.get('/rango/suggest/', {suggestion: query}, function(data){
//     $('#cats').html(data);
//   });
// });

function removeDiv(elem){
  $(elem).parent('div').remove();
}
