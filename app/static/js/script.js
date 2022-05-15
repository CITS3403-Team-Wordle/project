$(document).ready(function() {

    $('#signup-form').on('submit', function(event) {

        $.ajax({
            data : {
                email : $('#signup-email').val(),
                password : $('#signup-password').val()
            },
            type : 'POST',
            url : '/signup'
        })
        .done(function(data) {

            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            } else {
                $('#successAlert').text(data.success).show();
                $('#errorAlert').hide();
            }
        })
        event.preventDefault();
    })

})