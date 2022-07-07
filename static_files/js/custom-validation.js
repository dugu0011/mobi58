function getStates() {
    country_code = $('#customer-country').val();
     $.ajax({
        url: '/ajax/state-list/' + country_code,
        type:'GET',
        dataType: 'json',
        success: function (result) {
          let state_options;
            state_options = renderState(result);
            $('#customer-state').html(state_options);
            $('#customer-city').html('<option value="0">-----</option>');
        }
      });
}

function getCustomerStates(e) {
    $.ajax({
        url: '/ajax/state-list/' + e.value,
        type:'GET',
        dataType: 'json',
        success: function (result) {
            let state_options;
            state_options = renderState(result);
            $(".customer-state").html(state_options);
            $(".customer-district").html('<option value="0">-----</option>');
            $(".customer-city").html('<option value="0">-----</option>');
        }
        });
}

function getNewAddedStates(){
    var address_form = $('.address-form');
    country = document.getElementsByName('customer-country')[0];
    states =document.getElementsByName('customer-state');
    districts = $(".customer-district");
    cities = $(".customer-city");
    $.ajax({
        url: '/ajax/state-list/' + country.value,
        type:'GET',
        dataType: 'json',
        success: function (result) {
            let state_options;
            state_options = renderState(result);
            for(i=0; i<address_form.length;i++){
                if(!states[i].value){
                    states[i].innerHTML = state_options;
                    districts[i].innerHTML = '<option value="0">-----</option>';
                    cities[i].innerHTML = '<option value="0">-----</option>';
                }
            }
        }
    });
}


function getCustomerDistricts(e) {
    var target = e.parentNode.parentNode.parentNode;
    var districts = target.querySelector('[name="customer-district"]');
    var cities = target.querySelector('[name="customer-city"]');
     $.ajax({
        url: '/ajax/district-list/' + e.value,
        type:'GET',
        dataType: 'json',
        success: function (result) {
          let district_options;
          district_options = renderCity(result);
            districts.innerHTML = district_options;
            cities.innerHTML = '<option value="0">-----</option>';
        }
      });
}

function getCustomerCities(e) {
    var target = e.parentNode.parentNode.parentNode;
    var cities = target.querySelector('[name="customer-city"]');
    $.ajax({
        url: '/ajax/district-city-list/' + e.value,
        type:'GET',
        dataType: 'json',
        success: function (result) {
          let city_options;
            city_options = renderCity(result);
            cities.innerHTML = city_options;
        }
    });
}


function getDisrictCity(e) {
    $.ajax({
        url: '/ajax/district-city-list/' + e.value,
        type:'GET',
        dataType: 'json',
        success: function (result) {
          let city_options;
            city_options = renderCity(result);
            cities.innerHTML = city_options;
        }
    });
}


function getCities() {
    state_id = $('#customer-state').val();
     $.ajax({
        url: '/ajax/city-list/' + state_id,
        type:'GET',
        dataType: 'json',
        success: function (result) {
          let city_options;
            city_options = renderCity(result);
            $('#customer-city').html(city_options);

        }
      });
}

function getDistricts() {
    state_id = $('#customer-state').val();
     $.ajax({
        url: '/ajax/district-list/' + state_id,
        type:'GET',
        dataType: 'json',
        success: function (result) {
          let district_options;
          district_options = renderCity(result);
            $('#customer-district').html(district_options);
            $('#customer-city').html('<option value="0">-----</option>');
        }
      });
}



function renderState(states) {
    var state_options = '<option value="">-----</option>';
    for (i = 0; i < states.length; i++) {
        state_options = state_options + `<option value="` + states[i].id + `">` + states[i].name + `</option>`
    }
    return state_options
}

function renderCity(cities){
  var city_options = '<option value="">-----</option>';
  for (i = 0; i < cities.length; i++) {
    city_options = city_options + `<option value="`+ cities[i].id+`">`+ cities[i].name +`</option>`
  }
  return city_options
}



function show_message(message){
    toastr.options = {
        "preventDuplicates": true,
        "preventOpenDuplicates": true
    };
    toastr.error(message , {timeOut: 5000});
}


function validate_mobile(data , type){
    mobile  = data.value;
    var deferred = $.Deferred();
    if (mobile.length==10){
        url= '';
        if(type=='mobile'){
            url = '/ajax/validate-mobile/?mobile=' + mobile;
        }
        else{
            url = '/ajax/validate-mobile/?c_mobile=' + mobile;
        }
        
        var bool = false;
        $.ajax({
            url: url,
            type:'GET',
            dataType: 'json',
            success: function (result) {
            if(result.already_exist=='true'){
                show_message('This mobile number is already in use.');
                data.value = '';
            }
            else {
                bool= true;
            }

            },
            complete: function () {
                deferred.resolve(bool);
            }
        });
    }else{
        show_message('Please enter 10 digit valid mobile no.');
        data.value = '';
    }
        return deferred.promise();

     
}

function ValidateMobile(mobile){
    var returnData = $.ajax({
    async: true,
    type: "GET",
    url: '/ajax/validate-mobile/?mobile=' + mobile,
    dataType: "json"
});
//return returnData.then(function(response){ return response.already_exist === 'false'; }, function(){ return false; });
returnData.then(success, error);
}

function success(response) {
    if (response.already_exist ) {
        show_message('This mobile number is already in use.');
        return false;
    }
    else {
        return true;
    }
}

function error(response) {
    return false;
}

function check_mobile_number(data , msg) {
    mobile = data.value;
    if (mobile.length != 10 )
    {
       show_message('Please ' + msg);
       return false;
    }
    else {
        return true;
    }


}

function check_email_id(email , msg) {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))

    { 
            return (true);
    }
    else {
        show_message("Please "+ msg);
        return false;
    }


}

function check_data(data , name){
    if($.trim(data)){
        return true;
    }
    else{
        show_message('Please ' + name);
        return false;
    }
}

function check_file_size(data , msg){
    if(!data.value || data.files[0].size > 5242880){
        show_message('Please '+msg + '(size should be less than 5 mb)');
        return false;
    }
    else {
        return true;
    }
}

function check_msme(msme_check ,msme_file ){
    if(msme_check){
       if(msme_check == 'option1'){
        return check_file_size(msme_file , 'upload msme file');
       } 
       else {
            return true;
       }
    }
    else{
        show_message('Please select msme');
    }
}

function check_account_no(data){
    if(data && data.length >=9){
        return true;
    }
    else{
        show_message('Please enter account number(minimum length of 9)');
    }
}

function validateCustomerAddress(){
    var address_form = $(".address-form");
    console.log(address_form.length);
    var form = document.getElementById('create-customer-form').elements;
    var address = document.getElementsByName('customer-address');
    var country = document.getElementsByName('customer-country');
    var state = document.getElementsByName('customer-state');
    var district = document.getElementsByName('customer-district');
    var city = document.getElementsByName('customer-city');
    var pincode = document.getElementsByName('customer-pincode');
    var valid = false;
    for(i=0 ; i<address_form.length ; i++){
        if(check_data(country[0].value , 'select country')
        && check_data(state[i].value , 'select state')
        && check_data(district[i].value , 'select district')
        && check_data(address[i].value , 'enter address')
        && check_data(city[i].value , 'select city')
        && check_data(pincode[i].value , 'enter pincode')
        ){  
            valid= true;
        }
        else{
            valid= false;
        }
    }
    return valid;
}

function validateCustomerContact(){
    var form = document.getElementById('create-customer-form').elements;
    var contact_form = $(".contact-form");
    console.log(contact_form.length);
    var contact_name = document.getElementsByName('contact-name');
    var contact_email = document.getElementsByName('contact-email');
    var contact_mobile = document.getElementsByName('contact-mobile');
    var contact_designation = document.getElementsByName('contact-designation');
    var valid = false;
    var mobile_list = [];
    var email_list = [];
    for(i=0 ; i<contact_form.length ; i++){
        if(check_data(contact_name[i].value , 'enter contact person name')
        && check_data(contact_designation[i].value , 'enter contact person designation')
        && check_mobile_number(contact_mobile[i], 'enter valid contact mobile number')
        && check_email_id(contact_email[i].value , 'enter valid contact email-id')
        ){  
            mobile_list.push(contact_mobile[i].value);
            email_list.push(contact_email[i].value);
            valid= true;
        }
        else{
            valid= false;
        }
    }
    if(valid){
        var check = false;
        var unique_mobile_list = new Set(mobile_list);
        var unique_email_list = new Set(email_list);
        console.log(unique_mobile_list);
        if(mobile_list.length != unique_mobile_list.size){
            show_message("Please enter unique contact mobile numbers.");
            check = false;
        }
        else{
            check= true;
        }
        if(check){
            if(email_list.length != unique_email_list.size){
                show_message("Please enter unique contact email-ids.");
                return false;
            }
            else{
                return true;
            }
        }
    }
    else{
        return false;
    }

    //var contact_name = document.getElementsByTagName("contact-name");
}

function validateIndividualCustomer(){
    var form = document.getElementById('create-customer-form').elements;
    var name = form['customer-name'].value;
    var email = form['customer-email'].value;
    
    var mobile = form['customer-mobile'];
    var sale_type = form['sale_type'].value;
    // var address = form['customer-address'].value;
    // var country = form['customer-country'].value;
    // var state = form['customer-state'].value;
    // var district = form['customer-district'].value;
    // var city = form['customer-city'].value;
    // var pincode = form['customer-pincode'].value;
    var pan_number = form['customer-pan-number'].value;
    var pan_file = form['customer-pan-file'];
    
    if(check_data(name , 'enter customer name')
     && check_mobile_number(mobile , 'enter valid customer mobile number')
     && check_email_id(email , 'enter valid customer email-id')
     && check_data(sale_type, "select sale type")
     && validateCustomerAddress()
    //  && check_data(country , 'select country')
    //  && check_data(state , 'select state')
    //  && check_data(district ,'enter district')
    //  && check_data(address , 'enter address')
    //  && check_data(city , 'select city')
    //  && check_data(pincode , 'enter valid pincode')
     && check_data(pan_number , 'enter pan number')
     && check_file_size(pan_file ,'upload pan file')
    ){
        return true;
    }
    else {
        return false;
    }

}

function validateProperitorPartnerCustomer(){
    var form = document.getElementById('create-customer-form').elements;
    var gst_number = form['customer-gst-number'].value;
    var gst_file = form['customer-gst-file'];
    var msme = form['customer-msme'].value;
    //var msme = document.querySelector('input[name="customer-msme"]:checked').value;
    var msme_file = form['customer-msme-file'];

    if(validateIndividualCustomer()
      && check_data(gst_number ,'enter gst')
      && check_file_size(gst_file , 'upload gst file')
      && check_msme(msme , msme_file)
      //&& check_data(msme ,'select msme')
      //&& check_file_size(msme_file , 'upload msme file')
      && validateCustomerContact()
    ){
        return true;
    }
    else{
        return false;
    }
}

function validateLTDCustomer(){
    var form = document.getElementById('create-customer-form').elements;
    var cin_number = form['customer-cin-number'].value;
    var cin_file = form['customer-cin-file'];
    
    if(validateProperitorPartnerCustomer()
      && check_data(cin_number , 'enter cin number')
      && check_file_size(cin_file,'upload cin file')      
    ){
        return true;
    }
    else{
        return false;
    }
}

function validateCreateCustomerForm(){
    var form = document.getElementById('create-customer-form').elements;
    var remarks = form['customer-remarks'].value;
    //var company = form['customer-company-id'].value;
    var customer_type = form['customer-type'].value;
    console.log(customer_type);
    valid = false;

    if(customer_type == 'individual' || customer_type == 'client' || customer_type == 'vendor' || customer_type == 'transporter'){
        if(validateIndividualCustomer()){
            valid = true;
        }
    }
    else if(customer_type == 'properitor' || customer_type== 'partner'){
        if(validateProperitorPartnerCustomer()){
            valid = true;
        }
    }
    else if(customer_type == 'llp' || customer_type == 'pvt_ltd' || customer_type =='ltd'){
        if(validateLTDCustomer()){
            valid = true;
        }
    }
    else{
        show_message('Please select customer type');
        console.log('Something went wrong');
    }

    

    if(valid){
        if(check_data(remarks, 'enter remarks')){
            document.getElementById('create-customer-form').submit();
        }
        else{
            console.log('Something went wrong');
        }
    }


    
    /*if(validateIndividualCustomer() && check_data(remarks , 'enter remarks')){
        document.getElementById('create-customer-form').submit();
    }
    else{
        console.log('Something went wrong');
    }*/
}

function show_hide_inputs(customer_type){
    if(customer_type == 'individual' || customer_type == 'vendor' || customer_type == 'client' || customer_type == 'transporter'){
        $(".partner").addClass('d-none');
        $(".llp").addClass('d-none');
        $(".plus-icon-add").addClass('d-none');
    }
    else if(customer_type == 'properitor' || customer_type== 'partner'){
        $(".partner").removeClass('d-none');
        $(".llp").addClass('d-none');
        $(".plus-icon-add").removeClass('d-none');
    
    }
    else if(customer_type == 'llp' || customer_type == 'pvt_ltd' || customer_type =='ltd'){
        $(".partner").removeClass('d-none');
        $(".llp").removeClass('d-none');
        $(".plus-icon-add").removeClass('d-none');
    }
    else{
        show_message('Please select customer type');
        console.log('Something went wrong');
    }
}


function show_hide_category(customer_category){
    if(customer_category == 'crusher' || customer_category == 'contractor' || customer_category == 'transporter' || customer_category == 'client' || customer_category == 'supplier'){
        $(".mine").addClass('d-none');
        $(".kaata").addClass('d-none');

    }
    else if(customer_category == 'mine' || customer_category == 'minecrusher' || customer_category == 'vendor'){
        $(".mine").removeClass('d-none');
    }
    else if(customer_category == 'kaata'){
        $(".kaata").removeClass('d-none');
    }
    else{
        show_message('Please select customer category');
        console.log('Something went wrong');
    }
}



function Validate(){
    var mySelect = document.getElementById("sale_type");
    if(mySelect.value === " ") {
        show_message('Please select sale category type');
        console.log("Something went wrong");

    }
   }




function validate_company_name(data){
    c_name  = data.value;
    var deferred = $.Deferred();
    var bool = false;
    $.ajax({
        url: '/ajax/validate-company/?c_name=' + c_name,
        type:'GET',
        dataType: 'json',
        success: function (result) {
          if(result.already_exist=='true'){
            show_message('Customer with this name is already exist.');
            data.value = '';
          }
          else {
              bool= true;
          }

        },
        complete: function () {
            deferred.resolve(bool);
        }
    });
    return deferred.promise();
}

function validate_user_email(data , msg){
    email  = data.value;
    var deferred = $.Deferred();
    var bool = false;
    $.ajax({
        url: '/ajax/validate-user-email/?email=' + email,
        type:'GET',
        dataType: 'json',
        success: function (result) {
          if(result.already_exist=='true'){
            show_message(msg);
            data.value = '';
          }
          else {
              bool= true;
          }

        },
        complete: function () {
            deferred.resolve(bool);
        }
    });
    return deferred.promise();

     
}


function validate_pan_no(data , msg){
    var deferred = $.Deferred();
    if (data.value.length !=10){
        show_message(msg);
            data.value = '';
    }else{
        deferred.resolve(true);
    }
    return deferred.promise();
    
}

function check_pf(data, msg){
    var deferred = $.Deferred();
    if (data.value.length ==''){
        deferred.resolve(true);
    }
    else if (data.value.length !=12){
        show_message(msg);
            data.value = '';
    }else{
        deferred.resolve(true);
    }
    return deferred.promise();
    
}

function validate_ifsc_code(data , msg){
    var deferred = $.Deferred();
    if (data.value.length <=12){
        deferred.resolve(true);        
    }else{
        show_message(msg);
            data.value = '';
    }
    return deferred.promise();
    
}

function validate_pin_code(data , msg){
    var deferred = $.Deferred();
    if (data.value.length !=6){
        show_message(msg);
            data.value = '';
    }else{
        deferred.resolve(true);
    }
    return deferred.promise();
    
}

function validate_adhar_number(data , msg){
    var deferred = $.Deferred();
    if (data.value.length !=12){
        show_message(msg);
            data.value = '';
    }else{
        deferred.resolve(true);
    }
    return deferred.promise();
    
}


function getGSTinfo(value){
    if($.trim(value).length ==15 ){
        $.ajax({
            url: '/ajax/get-gst-info/?gst_no='+ value,
            type:'GET',
            dataType: 'json',
            success: function (result) {
                $("#customer-name").val(result.data);
            },
            error : function (result) {
                
            }
        });
    }
    else{
        show_message("Please enter a valid gst number")
    }

}

function getQualification(education_id, qualification_id){
    id = $('#'+education_id).val();
     $.ajax({
        url: '/ajax/get-qualification/' + id+"/",
        type:'GET',
        dataType: 'json',
        success: function (result) {
            console.log(result);
          let qualificationOptions;
            qualificationOptions = renderQualification(result);
            $('#'+qualification_id).html(qualificationOptions);

        }
      });
}
function renderQualification(data){
    var options = '<option value=""selected>Select Qualification</option>';
    for (i = 0; i < data.length; i++) {
      options = options + `<option value="`+ data[i].id+`">`+ data[i].name +`</option>`
    }
    return options
}


function CreateAssociateCustomerForm(){
    var form = document.getElementById('create-associate-customer-form').elements;
    var name = form['associate-customer-name'].value;
    var user_type = form['user_type_id'].value;
    var email = form['associate-customer-email'].value;
    var mobile = form['associate-customer-mobile'];
    var address = form['associate-customer-address'].value;
    var country = form['customer-country'].value;
    var state = form['customer-state'].value;
    var district = form['associate-customer-district'].value;
    var city = form['customer-city'].value;
    var pincode = form['associate-customer-pincode'].value;
    var pan_number = form['associate-customer-pan-number'].value;
    var pan_file = form['associate-customer-pan-file'];
    var account_no = form['associate-customer-account-no'].value;
    var bank_name = form['bank_name_id'].value;
    var account_holder = form['associate-customer-account-holder'].value;
    var ifsc = form['associate-customer-ifsc'].value;
    var parent = form['associate-customer-parent'].value;
    var remarks = form['associate-customer-remarks'].value;
    
    
    if(check_data(name , 'enter customer name')
     && check_mobile_number(mobile , 'enter valid customer mobile number')
     && check_data(user_type , 'select user type')
     && check_email_id(email , 'enter valid customer email-id')
     //&& check_data(sale_type,'select sale category type')
     && check_data(country , 'select country')
     && check_data(address , 'enter address')
     && check_data(state , 'select state')
     && check_data(district ,'enter district')
     && check_data(city , 'select city')
     && check_data(pincode , 'enter valid pincode')
     && check_data(pan_number , 'enter pan number')
     && check_file_size(pan_file ,'upload pan file')
     && check_data(bank_name , 'select bank name')
     && check_account_no(account_no)
     && check_data(account_holder ,'enter account holder')
     && check_data(ifsc , 'enter ifsc code')
     && check_data(parent , 'select parent customer')
     && check_data(remarks , 'enter remarks')
     
    ){
        document.getElementById('create-associate-customer-form').submit();
    }
    
    // var inputs = document.getElementsByClassName("associate-customer");
    // var mobile = document.getElementById('associate-customer-mobile');
    // var account_num = document.getElementById('associate-customer-account-no');
    // console.log(inputs , "dddddddddddd");
    // for(i=0;i<=inputs.length; i++){
    //     console.log(i);
    //     if(i==1 && valid==true){
    //         if(check_mobile_number(inputs[i] , inputs[i].placeholder)){
    //             valid = true;
    //         }
    //     }
    //     else if(i==3 && valid==true){
    //         if(check_data(inputs[i].value,'select country')){
    //             valid = true;
    //         }
    //     }
    //     else if(i==5 && valid==true){
    //         if(check_data(inputs[i].value,'select state')){
    //             valid = true;
    //         }
    //     }
    //     else if(i==7 && valid==true){
    //         if(check_data(inputs[i].value,'select city')){
    //             valid = true;
    //         }
    //     }
    //     else if(i==10 && valid==true){
    //         if(check_data(inputs[i].value,'enter account number')){
    //             valid = true;
    //         }
    //     }
    //     else{
    //         if(i ==0 || valid==true){
    //             if(check_data(inputs[i].value,inputs[i].placeholder)){
    //                 valid = true;
    //             }
    //         }
    //     }
        
    // }
}

var uploadField = document.getElementById("customFile");
if (uploadField){
uploadField.onchange = function() {
    if(this.files[0].size > 3145728){
       alert("File size should be less than 3mb!");
       this.value = "";
    };
};
}


function validateSubcategroyFormulaForm(){
    var form = document.getElementById('subcategory-formula-form').elements;
    var category = form['category'];
    var subcategory = form['subcategory'];
    var products = document.getElementsByName('product');
    var valid = false;
    var product_list = [];
    if(check_data(category.value ,'select category')
    && check_data(subcategory.value,'select subcategory')){
        for(i=0 ; i<products.length ; i++){
            if(check_data(products[i].value , 'select product')){  
                product_list.push(products[i].value);
                valid= true;
            }
            else{
                valid= false;
            }
        }
    }
    if(valid){
        var check = true;
        var unique_product_list = new Set(product_list);
        if(product_list.length != unique_product_list.size){
            show_message("Do not select same products");
            check = false;
        }
        if(check){
            $("#subcategory-formula-form").submit();
        }
    }
    else{
        return false;
    }
}
