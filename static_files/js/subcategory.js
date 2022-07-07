(function($){
    $(document).ready(function() {
        if($("#id_sub_category").val()==''){
        $("#id_sub_category").html('').html('<option value="" selected="">---------</option>')
        }
        else{
            console.log("fdfdddfdf")
            $("#id_sub_category").html('<option value="" selected="">---------</option><option value="'+$("#id_sub_category").val()+'" selected>'+$("#id_sub_category :selected").text()+'</option>')
        }
    });
})(jQuery);

(function($){
    $(function(){
        $("#id_category").on('change', function(){
        //   alert("Works");
        var dt =[]
        console.log($("#id_category").val())
        var id_category = $("#id_category").val();
        $.ajax({
            type:'get',
            url: "/ajax/sub-category?id_category="+id_category,
            success: function (data) {
                console.log(data)
               console.log("success")
               var html = 
                '<option value="" selected="">---------</option>';
                $("#id_subcategory").val("");
                    $("#id_sub_category").html("");
                    $("#id_sub_category").html(html);
                    for (i = 0; i < data.length; i++) {
                        console.log("here for")
                        var next = '<option value="'+data[i]['id']+'">'+data[i]['name']+'</option>';
                        console.log(next);
                        $("#id_sub_category").append(next);
                    }

            },
            
            error: function(err) {
               console.log("error", err)

            }
        });
        })
         
       });
})(jQuery);