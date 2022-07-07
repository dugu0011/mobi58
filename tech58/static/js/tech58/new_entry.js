$(document).ready(function(){
    $('.vehicle_no').change(function(e){
            var vehicle = $('.vehicle_no').val();
            selected_driver = $('#driver_name');   
            $.ajax({
                url:"/mine/vehicle/driver/select/?vehicle="+vehicle+"",
                success: function(data)
                    {
                        selected_driver.empty();
                        selected_driver.append("<option value='0' selected='selected'> Choose a value</option>");
                            for (i = 0; i<Object.keys(data).length;i++)
                        {
                            {
                            selected_driver.append("<option value="+Object.keys(data)[i]+">" +Object.values(data)[i] + "</option>");
                            }
                        }            
                    }
                })
        }); 
    });

    $(document).ready(function(e){
        var vehicle = $('.vehicle_no').val();
        //alert(vehicle);
        var driver_add = $('#alldrivers').val();
        selected_driver = $('#driver_name'); 
        $.ajax({
            url:"/mine/vehicle/driver/select/?vehicle="+vehicle+"",
            success: function(data)
                {
                    selected_driver.empty();
                    selected_driver.append("<option value='0' selected='selected'> Choose a value</option>");
                   for (i = 0; i<Object.keys(data).length;i++) 
                    {
                    
                    if ((Object.keys(data)[i]*1) == (driver_add*1))
                    
                    {
                        selected_driver.append("<option value="+Object.keys(data)[i]+" selected='selected'>" +Object.values(data)[i] + "</option>");
                    }
                    else
                    {
                        selected_driver.append("<option value="+Object.keys(data)[i]+">" +Object.values(data)[i] + "</option>");   
                    }
                    }

                }

            })
    });

$(document).ready(function(){
    $('.driver_name').change(function(e){
            var driver = $('.driver_name').val();
            selected_mobile = $('#mobile');
            $.ajax({
                url:"/mine/vehicle/driver/mobile/?driver="+driver+"",
                success: function(data)
                    {

                        for (i = 0; i<Object.keys(data).length;i++)
                        {
                            {
                            selected_mobile.val(Object.values(data)[i]);
                            
                            }
                        }            
                    }
                })
        }); 
    });

    $(document).ready(function(e){
        var driver = $('.driver_name').val();
        var mobile_add = $('#allmobiles').val();
        selected_mobile = $('#mobile'); 
        $.ajax({
            url:"/mine/vehicle/driver/mobile/?driver="+driver+"",
            success: function(data)
                {
                    selected_mobile.empty();
                    selected_mobile.append("<option value='0' selected='selected'> Choose a value</option>");
                   for (i = 0; i<Object.keys(data).length;i++) 
                    {
                    
                    if ((Object.keys(data)[i]*1) == (mobile_add*1))
                    
                    {
                        selected_driver.append("<option value="+Object.keys(data)[i]+" selected='selected'>" +Object.values(data)[i] + "</option>");
                    }
                    else
                    {
                        selected_driver.append("<option value="+Object.keys(data)[i]+">" +Object.values(data)[i] + "</option>");   
                    }
                    }

                }

            })
    });