$.ajax({
    type: 'POST',
    url: '/articles/postComment/',
    data: {
       'comment': $('#articleCommentForm textarea').val(),
       csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },
    dataType: 'json',
    success: function(data){
         $('.commentStyle').append(data)
   }
});
