// ########### AJAX  ###########

$(document).ready(function() {

    function myReload(time=1000){
        setTimeout(function(){
            location.reload()
        }, time)
    }

    // ajax login
    $('#login-form').on('submit', function (event) {
        loginForm = {
            Email: $('#login-email').val(),
            Password: $('#login-password').val(),
            Remember_me: $('#flexCheckDefault').val(),  // NEED HELP
        }
        console.log(loginForm)
        // post ajax data
        $.ajax({
            type: 'POST',
            url: '/login',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(loginForm),

        })
        .done(function(data) {
            if (data.error) {
                $('#loginError').text(data.error).show();
                $('#loginSuccess').hide();
            } else {
                $('#loginSuccess').text(data.success).show();
                $('#loginError').hide();
                myReload()

            }
        });
        event.preventDefault();

    })

    // ajax signin
    $('#signup-form').on('submit', function(event) {

        signupForm = {
            Username: $('#signup-username').val(),
            Email: $('#signup-email').val(),
            Password: $('#signup-password').val(),
            Password_confirm: $('#signup-password-confirm').val(),
        }

        console.log(signupForm)

        // post ajax data
        $.ajax({
            type: 'POST',
            url: '/signup',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(signupForm),

        })
        .done(function(data) {
            if (data.error) {
                $('#signError').text(data.error).show();
                $('#signSuccess').hide();
            } else {
                $('#signSuccess').text(data.success).show();
                $('#signError').hide();
                myReload()
            }
        });
        event.preventDefault();
    })

    // ajax logout 
    $('#logout-btn').on('click', function(event){
        console.log('hellow world')
        $.ajax({
            url: '/logout',
            dataType: 'json',
        })
        .done(function(data){
            console.log(data)
            myReload()
        })
    })

})

