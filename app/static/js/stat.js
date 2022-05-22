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
        	if(data.error){
        		$('#statError').text(data.error).show();
        	}else{
        		$('#span-average-mistake').text(data.average_mistake).show();
        		$('#span-average-wpm').text(data.average_wpm).show();
        		$('#span-average-cpm').text(data.average_cpm).show();
        	}
        });
        event.preventDefault();
	})
})