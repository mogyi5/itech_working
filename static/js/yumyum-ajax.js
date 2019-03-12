$('#suggestion').keyup(function(){ var query;
    query = $(this).val();
    $.get('/yumyum/suggest/', {suggestion: query}, function(data){
        $('#cats').html(data);
    });
});
