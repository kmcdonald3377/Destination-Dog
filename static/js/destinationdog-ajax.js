  $( document ).ready(function() {


    $('#likes').click(function(){
    var dotmid;
    dotmid = $(this).attr("data-dotmid");
    $.get('/destinationdog/like/', {dotmid: dotmid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    });
});

});
