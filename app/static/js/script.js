$(document).ready(function() {

    $('#signup-form').on('submit', function(event) {
        event.preventDefault();

        data = {
            email : $('#signup-email').val() ,
            password : $('#signup-password').val(),
        }
        $.ajax({
            type: 'POST',
            url: '/signup',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(data),
            context: Form,
            success: function(callback) {
                console.log(callback);
                // Watch out for Cross Site Scripting security issues when setting dynamic content!
                $('#successAlert').text('Hello ' + callback.first_name + ' ' + callback.last_name  + '!');
            },
            error: function() {
                $('#errorAlert').html("error!");
            }
        });
    })

})

