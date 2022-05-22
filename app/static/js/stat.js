// ################ AJAX for Statistic ################
$(document).ready(function(){
	$('#stat-header').on('click', function(event){
		
		console.log('test stat')


		$.ajax({
            type: 'GET',
            url: '/stat',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
        })
        .done(function(data) {

        });
        event.preventDefault();
	})
})