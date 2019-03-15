$('#suggestion').keyup(function(){ var query;
    query = $(this).val();
    $.get('/yumyum/suggest/', {suggestion: query}, function(data){
        $('#cats').html(data);
    });
});

$('#suggestion2').keyup(function(){ var query;
    query = $(this).val();
    $.get('/yumyum/suggest2/', {suggestion2: query}, function(data){
        $('#cats1').html(data);
    });
});
