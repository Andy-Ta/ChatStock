$(function() {
    $.ajax({
        type: 'GET',
        url: '/api/v1.0/start',
        contentType: "application/json",
        success: function (response) {
            console.log(response)
        },
        error: function (result) {
            alert(result.responseText);
        }
    });

    $('#send').click(function() {
        var message = $('#message').val();
        if(message !== '') {
            var template = $('<div class="user-wrapper">' +
                                '<div class="user-message">' +
                                    '<span>You: <br/></span>' + message +
                                '</div>' +
                           '</div>').hide();

            template.appendTo('#conversation').fadeIn();
            $('#message').val('');

            $.ajax({
                type: 'POST',
                url: '/api/v1.0/send',
                data: JSON.stringify({ message: message }),
                dataType: 'json',
                contentType: "application/json",
                success: function (response) {
                    console.log(response);

                    var data = response.output.text;
                    var concat = "";
                    for(var i = 0; i < data.length; i++) {
                        concat += data[i] + "<br />";
                    }
                    var template = $('<div class="wrapper">' +
                    '<div class="reply-message">' +
                    '<span>Watson: <br/></span>' + concat +
                    '</div>' +
                    '</div>').hide();
                    template.appendTo('#conversation').show("slide", {direction: 'left'});
                    checkHeight();
                },
                error: function (result) {
                    alert(result.responseText);
                }
            });
        }
    });

    $('#message').keydown(function(e) {
        if (e.which === 13) {
            $('#send').click();
        }
    });
});

function checkHeight() {
    if ($('body').height() > $('#conversation').height()) {
        $('#conversation').animate({
            scrollTop: $('#conversation')[0].scrollHeight
        }, 500);
    }
}