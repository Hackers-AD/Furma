$(function (e) {
	var togglecount = 0;

	$(".preloader-container").fadeOut("slow");
	document.onscroll=function (e) {
	    if (window.pageYOffset > 235) {
	      $(".navbar-menu").addClass("fixed-top");
	    }else{
	      $(".navbar-menu").removeClass("fixed-top");
	    }
	    if (window.pageYOffset > 150) {
	      $(".scrolltopbtn").css({'display': 'block'});
	    }else{
	      $(".scrolltopbtn").css({'display': 'none'});
	    }
	   if ($(window).width() < 768) {
	   		if (window.pageYOffset > 235) {
		   		$(".navbar-menu").removeClass("fixed-top");
		   		$(".navbar-container").addClass("fixed-top");
		   	}else{
		      $(".navbar-container").removeClass("fixed-top");
		    }
	   }else{
	   		$(".navbar-container").removeClass("fixed-top");
	   }
	}

	$(".scrolltopbtn").click(function (e) {
		$('html, body').animate({
	        scrollTop: 0
	    }, 600);
	});


	$(".contactform").submit(function (e) {
		e.preventDefault();
		$.ajax({
			url: '/contact/',
			method: 'POST',
			data: new FormData(this),
	  		cache: false,
	      	contentType: false,
      		processData: false,
			success: function (data) {
				if (data['success']=='1') {
					window.open('/contact/','_self');
				}
				if (data['success']=='0') {

				}
			},
			error: function (error_data) {
				console.log(error_data);
			}
		});
	});

	$(".chevron-toggler span").click(function (e) {
		if ($(this).attr('class')=="fa fa-chevron-down") {
			$(this).removeClass("fa fa-chevron-down");
			$(this).addClass("fa fa-chevron-right");
		}else{
			$(this).removeClass("fa fa-chevron-right");
			$(this).addClass("fa fa-chevron-down");
		}
	});

	if($("#bank-payment").prop("checked")){
		$(".card-details").show();
	}
	$("#bank-payment").click(function (e) {
		$("#cash-payment").prop("checked",false);
		$(".card-details").toggle();
	});

	$("#cash-payment").click(function (e) {
		$("#bank-payment").prop("checked",false);
		if ($(this).prop("checked")) {
			$(".card-details").hide();
		}
	});
	$(".item-heart").click(function (e) {
		item_heart_cont = $(this);
		product_id = item_heart_cont.attr('id').split("-")[1]; 
		$.ajax({
			url: '/product/liked',
			method: 'GET',
			data: {
				'product_id' : product_id,
			},
			success: function (data) {
				item_heart_cont.html(data['img']);
			
				if(data['liked'] == true){
					$(".wishlists-count").html((parseInt($(".wishlists-count").html())+1));	
				}
				if(data['liked'] == false){
					$(".wishlists-count").html((parseInt($(".wishlists-count").html())-1));
				}
			},
			error: function (error_data) {
				console.log(error_data);
			}
		});
	});

	$(".addtocart-btn").click(function (e) {
		addcartbtn = $(this);
		product_id = addcartbtn.attr('id').split("-")[1]; 
		$.ajax({
			url: '/product/addtocart',
			method: 'GET',
			data: {
				'product_id' : product_id,
			},
			success: function (data) {
				addcartbtn.html(data['btncontent']);
			
				if(data['liked'] == true){
					
				}
				if(data['liked'] == false){
					
				}
			},
			error: function (error_data) {
				console.log(error_data);
			}
		});
	});

});