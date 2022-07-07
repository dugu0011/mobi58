(function($){
    $(function(){
        $("#id_item_code").on('change', function(){
        //   alert("Works");
        var dt =[]
        console.log($("#id_item_code").val())
        var id_item_code = $("#id_item_code").val();
        $.ajax({
            type:'get',
            url: "/ajax/product-raw-material?id_item_code="+id_item_code,
            success: function (data) {
               console.log(data)
               console.log("success")
               var material = data['material'];
               var product = data['product_name'];
               var base_products = data['base_products'];
               var html = 
                '<option value="" selected="">---------</option>';
                    // $("#id_subcategory").val("");
                    // $("#id_item_code").html("");
                    // $("#id_item_code").html(html);
                    // $('#id_material').html('');
                    // $("#product_name_id").val('');
                    
                    // for (i = 0; i < product.length; i++) {

                    //     var next = '<option value="'+product[i]['id']+'" data-productname = "'+product[i]['name']+'">'+product[i]['item_code']+'</option>';
                    //     console.log(next);
                    //     $("#id_item_code").append(next);
                    // }

                    for (i = 0; i < base_products.length; i++) {

                        var next = '<option value="'+base_products[i]['id']+'" >'+base_products[i]['name']+'</option>';
                        $("#id_base_product").append(next);
                    }
                    
                    console.log("material");
                    console.log(material);
                    $("#product_name_id").val(product);
                    $('#id_material').html(render_materal(material));
                    countTotal('totalSoldContentId', 'solid_content_cls')
            },
            
            error: function(err) {
               console.log("error", err)

            }
        });
        })
         
       });
})(jQuery);

function render_materal(data){
    var html = ''
    for (i = 0; i < data.length; i++) {
        
        var next = `
            <tr>
                <td>
                    ${data[i]['item_code']}
                    <div>
                        <input type="hidden" name="material" class="form-control bg-white rounded-0 fvalidation" id = "product_id${i}" value="${data[i]['id']}" data-price="${data[i]['price']}"/>
                        <span class="text-danger error-msg"></span>
                    </div>
                </td>
                <td>${data[i]['name']}</td>
                <td>
                    <div>
                        <input type="number" name="solid_content" id="id_sc${i}" class="form-control bg-white rounded-0 fvalidation" value="${data[i]['solid_content']}" readonly onchange="validateFloatKeyPress(this)"; />
                        <span class="text-danger error-msg"></span>
                    </div>

                </td>
                <td>
                    <div>
                        <input type="number" name="percentage" id="id_per${i}"  class="form-control bg-white rounded-0 fvalidation percentage_cls" 
                        onchange="validateFloatKeyPress(this),  countTotal('totalPercentageId', 'percentage_cls'), cal_sd_kg('id_sc${i}', 'id_per${i}', 'id_sc_kg${i}', 'product_id${i}', ${i})" ;/>
                        <span class="text-danger error-msg"></span>
                    </div>
                </td>
                <td>
                    <div>
                        <input type="number" name="quantity" id="id_quantity${i}"  class="form-control bg-white rounded-0 fvalidation" 
                        onchange="validateFloatKeyPress(this),  countTotal('totalPercentageId', 'percentage_cls'), cal_sd_kg('id_sc${i}', 'id_per${i}', 'id_sc_kg${i}', 'product_id${i}', ${i})" ;/>
                        <span class="text-danger error-msg"></span>
                    </div>
                </td>
                <td>
                    <div>
                        <input type="number" name="solid_content_kg" id="id_sc_kg${i}" readonly  class="form-control bg-white rounded-0 fvalidation solid_content_cls" onchange="validateFloatKeyPress(this),countTotal('totalSoldContentId', 'solid_content_cls')"/>
                        <span class="text-danger error-msg"></span>
                    </div>
                </td>
                <td>
                    <div>
                        <input type="number" name="price" class="form-control bg-white rounded-0 fvalidation per_kg_cls" id="total_price_kg_id${i}" onchange="validateFloatKeyPress(this), countTotal('totalPriceId', 'per_kg_cls')";/>
                        <span class="text-danger error-msg"></span>
                    </div>
                </td>
            </tr>
        `;
        console.log(next);
        html = html + next
    }
    return html
}


function get_product(){
    console.log($("#id_item_code option:selected").data("productname"))
    var productname = $("#id_item_code option:selected").data("productname")
    $("#product_name_id").val(productname);
}

function countTotal(id, cls){
    var price_val = 0;
    $('table').find(`input.${cls}`).each(function () {
        if(!isNaN($(this).val()) && $(this).val()!=''){
            console.log("in for", $(this).val())
            price_val =parseFloat(price_val) + parseFloat($(this).val())
            price = price_val.toFixed(2)
            $(`#${id}`).val(price)
        }
        
        
    });   
}


function validateFloatKeyPress(el) {
	var v = parseFloat(el.value);
	el.value = (isNaN(v)) ? '' : v.toFixed(2);
	console.log(v.toFixed(2))
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


function cal_sd_kg(sc_id, per_id, sc_kg_id, product_id, i){
    var sc = $(`#${sc_id}`).val()
    var per = $(`#${per_id}`).val()
    value = sc * per /100;
    $(`#${sc_kg_id}`).val(value.toFixed(2))
    countTotal('totalSoldContentId', 'solid_content_cls');
    var prod_price = $(`#${product_id}`).data('price');
    price = prod_price * per/100;
    $(`#total_price_kg_id${i}`).val(price.toFixed(2));
    countTotal('totalPriceId', 'per_kg_cls');
    var quantity = per*10;
    $(`#id_quantity${i}`).val(quantity.toFixed(2))

}

function submit_form_product(formId, submitId, msg=''){
    $('#loader').addClass("show-loader")
    var valid = submitFormValid($("#"+submitId));
        if (valid){

            if ($("#totalPercentageId").val()==100) {           
                $('#loader').addClass("show-loader")
                $('#'+formId).submit()
            }else{
                $(".total_per_err").html('* Total Percentage should be 100%')
                $('#loader').addClass("hide-loader")

            }
            
            
        }else{
            $('#loader').addClass("hide-loader")
        }
}

