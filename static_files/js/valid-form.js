
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
						$(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* This field cannot be blank.');
						return submitAttemp = false;
						event.preventDefault();
					}
				}

				else if($(e).attr('type')=='text' ){

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

                else if($(e).attr('type')=='email'){

					if( /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test($(e).val()))
					{
						$(e).removeClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('');
						submitAttemp = true;
					}
					else{
						$(e).focus();
						$(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* Invalid email');
						return submitAttemp = false;
						event.preventDefault();

					}
				}

                else if($(e).attr('type')=='date' ){

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

				else if($(e).attr('type')=='time' ){

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

			    else if( $(e).hasClass( "custom-select") ){
					console.log($(e))
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
                
                else if( $(e).hasClass( "textarea") ){
					console.log($(e))
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
				});
			return submitAttemp;
		}
    }