$(".submit_ajax").click(function(){ 
    var cond = {}
    cond.name = $(".name").val();
    $.ajax({
        type: "post",
        url: "submit/",
        data: cond,
        dataType: "json",
        success: function (data) {
            $(".name").val(data.hi);
        }
    });
});
