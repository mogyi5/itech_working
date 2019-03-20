// $('#suggestion').keyup(function(){ var query;
//     query = $(this).val();
//     $.get('/yumyum/suggest/', {suggestion: query}, function(data){
//         $('#cats').html(data);
//     });
// });

$(document).ready(function() {
  // JQuery code to be added in here.
  $('#suggestion2').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/yumyum/suggest2/', {suggestion2: query}, function(data){
      $('#cats1').html(data);
    });
  });
});
