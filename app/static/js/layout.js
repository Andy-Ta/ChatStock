stock = undefined;
price = undefined;
phone = undefined;

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
                                    '<b>You: <br/></b>' + message +
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
                    if(response.output.nodes_visited[0] === 'node_3_1517084237517') {
                        stock = response.entities[0].value;
                    }
                    else if(response.output.nodes_visited[0] === 'node_3_1517112563069') {
                        price = response.entities[0].value;
                    }
                    else if(response.output.nodes_visited[0] === 'node_2_1517114042728') {
                        phone = "";
                        for(var i = 0; i < response.entities; i++) {
                            if(response.entities[i].value.charAt(0) === '-')
                                response.entities[i].value = response.entities[i].value.splice(0, 1);
                            phone += response.entities[i].value;
                        }
                    }

                    var data = response.output.text;
                    for(var i = 0; i < data.length; i++) {
                        var template = $('<div class="wrapper">' +
                            '<div class="reply-message">' +
                            '<b>Watson: <br/></b>' + data[i] +
                            '</div>' +
                            '</div>').hide();

                        template.appendTo('#conversation').show("slide", {direction: 'left'});
                        checkHeight();
                    }
                    text();
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

function text() {
    if(stock !== undefined && phone !== undefined && price !== undefined) {
        $.ajax({
            type: 'POST',
            url: '/api/v1.0/send',
            data: JSON.stringify({ stock: stock, price: price, phone: phone }),
            dataType: 'json',
            contentType: "application/json",
            success: function (response) {
                console.log(response);
            },
            error: function (result) {
                alert(result.responseText);
            }
        });
    }
}