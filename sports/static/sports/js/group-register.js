var athlete_num = 1;
$(document).ready(function () {

});
$(document).on("change", ".select-sex", function () {
    var id = $(this).attr("id");
    var num = id.substring(10, id.length);
    if ($("#select-sex" + num).val() == 1) {
        $("#athlete-project-man" + num).show();
        $("#athlete-project-woman" + num).hide();
    } else if ($("#select-sex" + num).val() == 2) {
        $("#athlete-project-man" + num).hide();
        $("#athlete-project-woman" + num).show();
    } else {
        $("#athlete-project-man" + num).hide();
        $("#athlete-project-woman" + num).hide();
    }
});

$(".add-athlete").on("click", function () {
    athlete_num++;
    $.ajax({
        type: "post",
        data: {
            "number": athlete_num
        },
        url: "../get_athlete_div/",
        success: function (data) {
            $(".athlete-form").append(data);
        }
    });
});
$("#submit").on("click", function () {
    var cond = {}
    cond.captain_name = $("#captain-name").val();
    cond.captain_id = $("#captain-id").val();
    cond.captain_phone = $("#captain-phone").val();
    cond.doctor_name = $("#doctor-name").val();
    cond.doctor_id = $("#doctor-id").val();
    cond.doctor_phone = $("#doctor-phone").val();
    cond.athlete_name = [];
    cond.athlete_id = [];
    cond.athlete_sex = [];
    cond.athlete_age = []; 
    cond.athlete_project = [];
    for(var i = 0; i < athlete_num; ++i)
    {
        cond.athlete_name[i] = $("#athlete-name" + i).val();
        cond.athlete_id[i] = $("#athlete-id" + i).val();
        cond.athlete_sex[i] = $("#select-sex" + i).val()
        cond.athlete_age[i] = $("#select-age" + i).val();    
        cond.athlete_project[i] = [];
        if (cond.athlete_sex[i] == "1")
        {
            $("#select-project-man" + i + " input:checked").each(function(){
                console.log(1);
                cond.athlete_project[i].push($(this).val());
            });
        }
        else
            $("#select-project-woman" + i + " input:checked").each(function(){
                cond.athlete_project[i].push($(this).val());
            });
    }
    console.log(cond); 
    $.ajax({
        type: "method",
        url: "submit",
        data: cond,
        success: function (data) {
            console.log(data);
            swal({
                title: "Success!",
                text: "",
                type: "success",
                confirmButtonText: "OK"
            },
            function () {
               // window.location.href = "../index";
            });     
        },
        error: function () {
            swal({
                title: "ggsmd...",
                text: "",
                type: "error",
                confirmButtonText: "OK"
            },
            function () {
               // window.location.href = "../index";
            });  
        }
    });
})