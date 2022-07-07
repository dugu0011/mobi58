$('#id_company').on('change', function() {
    // alert( this.value );
    //$("#id_partner").html('{{form.partner}}')
    $("#id_product").html('{{form.product}}')

    $.ajax({
        url: '/ajax/company-partners/' + this.value,
        type:'GET',
        dataType: 'json',
        success: function (result) {
            console.log(result)
            let partner_option;
            let product_option;
            //partner_option = renderHTML(result['partner_dict']);
            product_option = renderHTML(result['product_dict']);
            //$("#id_partner").html(partner_option);
            $("#id_product").html(product_option);
        }
        });
});



function renderHTML(states) {
    var state_options = '<option value="">---------</option>';
    // for (i = 0; i < states.length; i++) {
    //     state_options = state_options + `<option value="`+states[i].id+`">`+states[i].name+`</option>`
    // }
    states.forEach(element => {
        state_options += `<option value="${element.id}">${element.name}</option>`
    });
    return state_options
}


function getEditForm(id) {
    // alert( this.value );
    console.log('edit')
    $("#edit-form-id").html('')

    $.ajax({
        url: '/ajax/edit-orc/' + id,
        type:'GET',
        dataType: 'json',
        success: function (result) {
            console.log(result)
            $("#edit-form-id").html(result);
            // $('#create-orc-edit').modal('show');

            
            
        }
        });
}