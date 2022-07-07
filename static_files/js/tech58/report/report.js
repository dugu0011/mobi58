$('#search_report').click(function(e){
    var from_date = $('#from_date').val();
    var to_date = $('#to_date').val();
    $.ajax({
        type:"GET",
        url:"/mine/sale/report/?fromdate="+from_date+"&todate="+to_date+"",
        success: function(data){
                    setInterval('pageRefresh()',3000);
                    }
        //{console.log("working...");}
    });
});
// Page will be reload after Ajax Call success.
function pageRefresh() {
    location.reload(true);
    }