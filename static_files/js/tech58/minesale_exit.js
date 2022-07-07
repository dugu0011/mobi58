$(document).ready(function() {
    $('.select2_dropdown').select2();
    });


    $(document).ready(function(e){
        if (e.keyCode == 9) {
            e.preventDefault();
        }
        $('.sbwt').blur(function(){
       let in_var = $('#in_weight').val();
       let out_var = $('#out_weight').val();
       let b_amt = $('#billing_amt').val();
       if (parseFloat($('#out_weight').val()) < parseFloat($('#in_weight').val()))
            {
                alert("Full load should be more than "+in_var);
                $('#out_weight').val('');
                return false; 
            }

       if ($('#product').val() == '')
        {
            alert("Please Select a Product");
            $('#out_weight').val('');
            return false; //preventDefault;
        }
        let sub_weight = out_var-in_var
        
        // Empty Load - Full Load = Net Load
        $('#net_weight').val(sub_weight.toFixed(2));

        // QTY is Net Load
        $('#qty').val(sub_weight.toFixed(2));
        $('#sale_qty').val(sub_weight.toFixed(2));
        
        var selected_item = $('#product').find(':selected').attr('class');
        var saperate_data = selected_item.split(',');  
        var sale_royalty = parseFloat(saperate_data[3]);
        var sale_royal = parseFloat($('#sale_qty').val()*sale_royalty);
        $('#royalty_charges').val(sale_royal.toFixed(2));

       var finalamt = parseFloat($('#net_weight').val()) * parseFloat($('#price').val() );
        $('#amount').val(finalamt.toFixed(2));
        let bill_AMT = $('#b_price').val()*$('#qty').val();                        // sub_weight is the net_weight
        var bill_AMOUNT = bill_AMT.toFixed(2);
        $('#billing_amount').val(bill_AMOUNT);
        
        let sale_AMT = $('#sale_qty').val()*$('#sale_price').val(); // for sale quantity multyiply by sale price
        var sale_AMOUNT = sale_AMT.toFixed(2);
        $('#sale_amount').val(sale_AMOUNT);


        t_amt = sub_weight * $('#price').val();
    
        var t_amt = t_amt.toFixed(2); 
        let p_amt = t_amt-b_amt

        var dsd = parseFloat($('#gst_per').val());
        var amm = parseFloat($('#billing_amount').val());
        var total_gst = amm*dsd/100;
        
        $('#gst_amt').val(total_gst.toFixed(2));
        // Sale Detail GST Amount
        $('#sale_gst_amt').val($('#gst_amt').val());  
        
        var GST = $('#gst_amt').val(); 
        var bill = $('#billing_amount').val();
        

        var mn_GRANDTOTAL = parseFloat(GST) + parseFloat(bill);
        
        //$('.grand_total').val(mn_GRANDTOTAL.toFixed(2)); // Gst Amount + Billing Amount = Grand Total
        $('#bill_grand_total').val(mn_GRANDTOTAL.toFixed(2));
        // Sale Detail Total
        var total_sale = parseFloat($('#sale_gst_amt').val()) + parseFloat($('#sale_amount').val()); 
        $('#sale_grand_total').val(total_sale.toFixed(2));
        $('.grand_total').val($('#sale_grand_total').val());

        
        var total_pending_amount = $('.grand_total').val() - $('#advance').val();
        $('#p_amt').val(total_pending_amount.toFixed(2));

        //var up_BL = $('#grand_total').val()-$('#advance').val();
        //$('#balance').val(up_BL.toFixed(2));
           
    });
    });
    

    // $('.block-tab').on('keydown', function(e)) {
    //         if (e.keyCode == 9 )
    //         e.preventDefault();
    //     }


// grand total - advance - commission = balance 
    $('#commission').keyup(function(e){
        if (e.keyCode == 9) {       
            e.preventDefault();
        }    
        var gr = $('#grand_total').val();
        var advc = $('#advance').val();
        var com = parseFloat($('#commission').val());
        var grand_bal = gr-advc;
      parseFloat($('#balance').val(grand_bal-$('#commission').val()));
      });  

    function OtherCharges(){ 
            var o_charges = $('#other_charges').val();
            if (o_charges.length < 0 || o_charges == '')
                o_charges = 0;

            var o_grand = $('.sale_grand_total').val();
            var o_grand_total =  parseFloat(o_charges) + parseFloat(o_grand);
            
            $('.grand_total').val(o_grand_total.toFixed(2));
        }
      


    $('#pay_received').keyup(function(e){
        var c_advance = parseFloat($('#advance_recieved').val());
        var c_pay_advance = parseFloat($('#pay_received').val());
        var c_ap = c_advance + c_pay_advance; // Received Advance Plus Received Amount
        
        var c_grand = $('.grand_total').val();
        var c_receive =  c_grand - c_pay_advance - c_advance;
        $('#p_amt').val(c_receive.toFixed(2));


            
      });  


    $(function() {
        $('#internal_external').change(function(){
            $('.vendor').hide();
            $('#' + $(this).val()).show();
        });
        });


    $(function() {
        $('#product').change(function(){
             var selected_item = $(this).find(':selected').attr('class');
             var saperate_data = selected_item.split(',');  
             
             $('#price').val(saperate_data[0]);
             var sale_price = parseFloat(saperate_data[0]);
             var bill_price = parseFloat(saperate_data[1]);
     
             $('#sale_price').val(sale_price);
             $('#b_price').val(bill_price);
             $('#gst_per').val(saperate_data[2]);
             $('#royalty_charges').val(saperate_data[3]);
            
            $('#b_item_name').val($(this).find(':selected').text());
            $('#sale_item_name').val($(this).find(':selected').text());
            
            });
        });


    // $(document).ready(function(){
    //     var entry_adv = document.getElementById('advance_recieved');
    //         $('#advance').val(entry_adv).val());
    // });


// Quantity Editable
    $('#qty, #b_price').keyup(function(e){
    if (e.keyCode == 9) {       
            e.preventDefault();
        }
        var q_qty = $('#qty').val();
        var q_billing_price = $('#b_price').val();
        var q_billing_amount = $('#billing_amount').val();
        var q_gst_percentage = $('#gst_per').val();
        var q_gst_amount = parseFloat($('#gst_amt').val());
        var q_bill_grand_total = parseFloat($('#bill_grand_total').val());
        
        var total_q_billing = parseFloat(q_qty*q_billing_price);
        $('#billing_amount').val(total_q_billing.toFixed(2));

        var actual_gst = total_q_billing*q_gst_percentage/100;
        $('#gst_amt').val(actual_gst.toFixed(2));

        var actual_grand = parseFloat($('#gst_amt').val()) + parseFloat($('#billing_amount').val());
        $('#bill_grand_total').val(actual_grand.toFixed(2));

        $('#sale_gst_amt').val($('#gst_amt').val());

        // Sale Detail Total
        var total_sale = parseFloat($('#sale_gst_amt').val()) + parseFloat($('#sale_amount').val()); 
        $('#sale_grand_total').val(total_sale.toFixed(2));
        $('.grand_total').val($('#sale_grand_total').val());

        if ($('#other_charges').val() != '' || $('#other_charges').val() != 0 || $('#royalty_charges').val() != '' || $('#royalty_charges').val() != 0) 
        {
            $('.grand_total').val( parseFloat($('#sale_grand_total').val()) + parseFloat($('#other_charges').val()) + parseFloat($('#royalty_charges').val()));
        }
      });