$(document).ready(function() {
  // On typing, suggestions for recipes are automatically generated
  $('#suggestion2').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/yumyum/suggest2/', {suggestion2: query}, function(data){
      $('#cats1').html(data);
    });
  });
});
