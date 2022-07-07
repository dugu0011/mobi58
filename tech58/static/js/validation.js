
	var validation = {
		validate_submit_action: function(b) {
			var submitAttemp = true;
			
			$(b).parents('form').find('.fvalidation').each((i, e) => {
			 	if($(e).attr('type')=='number' ){

					if( $(e).val()!='' )
					{
						$(e).removeClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('');
						submitAttemp = true;
					}
					else{
						$(e).focus();
						$(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* Please enter valid number.');
						return submitAttemp = false;
						event.preventDefault();
					}
				}

				else if($(e).attr('type')=='email'){

					if( /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test($(e).val()))
					{
						$(e).removeClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('');
						submitAttemp = true;
					}
					else{
						$(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* Invalid email');
						return submitAttemp = false;
						event.preventDefault();

					}
				}
				else if($(e).attr('type')=='password'){

					if( $(e).val()!='' )
					{
						$(e).removeClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('');
						submitAttemp = true;
					}
					else{
						$(e).focus();
						$(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* This field cannot be blank.');
						return submitAttemp = false;
						event.preventDefault();
					}
				}
                
                else if($(e).attr('type')=='radio'){
                    if($("input[type='radio'][name='user_type']:checked"))
                    {
						$(e).removeClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('');
						submitAttemp = true;
					}
					else{
                        $(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* Select one of them');
                        $('.user-type').empty().html('* Select one of them');
						return submitAttemp = false;
						event.preventDefault();

					}
				}
				else if($(e).attr('type')=='checkbox'){
                    if($("input[type='checkbox'][name='check']:checked").length)
                    {
						$(e).removeClass('input-error').parent('div').parent('div').css('position', 'relative').find('span.error-msg').html('');
						submitAttemp = true;
					}
					else{
                        $(e).addClass('input-error').parent('div').parent('div').css('position', 'relative').find('span.error-msg').html('* This field cannot be uncheck.');
                        //$('.user-type').empty().html('* Select one of them');
						return submitAttemp = false;
						event.preventDefault();

					}
				}
				else if($(e).attr('type')=='file'){
					if ($(e).val() == '') {
						$(e).focus();
						$(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* This field cannot be blank.');
						return submitAttemp = false;
						event.preventDefault();
					  } else {
						$(e).removeClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('');
						submitAttemp = true;
					  }
				}
				

				// else if( $(e).hasClass( "custom-select") ){

				// 	if ( $.trim($(e).val()) == '') {
				// 		$(e).addClass('input-error').parents('.form-group').css('position', 'relative').find('span.error-msg').html('* This field cannot be blank.');
				// 		return submitAttemp = false;
				// 		event.preventDefault();
				// 	} else {
				// 		$(e).removeClass('input-error').parents('.form-group').css('position', 'relative').find('span.error-msg').html('');
				// 		submitAttemp = true;
				// 	}

				// }
				else if( $(e).hasClass( "custom-select") ){

					if ($(e).val() == '') {
					  $(e).focus();
					  $(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* This field cannot be blank.');
					  return submitAttemp = false;
					  event.preventDefault();
					} else {
					  $(e).removeClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('');
					  submitAttemp = true;
					}
			
				  }
				  

				else{
					if ( ($.trim($(e).val()) == '') && !($(e).hasClass( "bootstrap-select")) ) {
						$(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* This field cannot be blank.');
						return submitAttemp = false;
						event.preventDefault();
					} else {
						$(e).removeClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('');
						submitAttemp = true;
					}

				}

			});
			return submitAttemp;
		}
	}


	function submitFormValid(el){
		if (!validation.validate_submit_action(el)) {
				toastr.error('Please fill all the required information correctly.','Alert')
				return false
			} else {
				//showLoader();
				return true
			}
		}

	function submit_form(formId, submitId, msg=''){
		var valid = submitFormValid($("#"+submitId));
			if (valid){
				if (msg){
				function show_popup(){
					$('#'+formId).submit()
			
					};
					setTimeout( show_popup, 1000 );
					toastr.success(msg,'Success')
				}else{
					$('#'+formId).submit()
				}
				
			}
	}

	function submit_offical_form(formId, submitId, msg=''){
		var valid = submitFormValid($("#"+submitId));
			if (valid){
				var prime = $('#prime_num_id').val();
				var alter = $('#alter_num_id').val();

				if(prime!=alter){
					if (msg){
					function show_popup(){
						$('#'+formId).submit()
				
						};
						setTimeout( show_popup, 1000 );
						toastr.success(msg,'Success')
					}else{
						$('#'+formId).submit()
					}
				}else{
					$('.alter_num').html('* Alternate mobile no. should be different from primary mobile no.');
				}
			}
	}



