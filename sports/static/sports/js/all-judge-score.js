var flag = 1;
$(document).ready(function () {});
$("#select-sex").on("change", function () {
    if ($("#select-sex").val() == 1) {
        $("#project-male").show();
        $("#project-female").hide();
    } else if ($("#select-sex").val() == 2) {
        $("#project-male").hide();
        $("#project-female").show();
    } else {
        $("#project-male").hide();
        $("#project-female").hide();
        $("#project-group").hide();
    }
});
$("#select-project-male").on("change", function () {
    if ($("#select-project-male").val() == "" || $("#select-project-male").val() == undefined) {
        $("#project-group").hide();
    } else {
        $("#project-group").show();
        get_group_num();
    }
});
$("#select-project-female").on("change", function () {
    if ($("#select-project-female").val() == "" || $("#select-project-female").val() == undefined) {
        $("#project-group").hide();
    } else {
        $("#project-group").show();
        get_group_num();
    }
});
$("#search").on("click", function (e) {
    get_form();
});
// $("#search").on("click", function () {
//     alert(1);
//     //get_form();
// });
function get_group_num() {
    var cond = {};
    cond.sex = $("#select-sex").val();
    cond.age = $("#select-age").val();
    if (cond.sex == 1)
        cond.project = $("#select-project-male").val();
    else
        cond.project = $("#select-project-female").val();

    $.ajax({
        type: "post",
        url: "get_group_num/",
        data: cond,
        success: function (data) {
            $("#select-group").empty();
            if (data == 0) {
                var option = '<option value="">该项目无人报名，请重新选择</option>';
                $("#select-group").append(option);
            } else {
                var option = '<option value=""></option>';
                for (var i = 1; i <= data; ++i)
                    option += '<option value="' + i + '">' + i + '</option>';
                $("#select-group").append(option);
            }
        }
    });
};

function get_form() {
    // var cond = {};
    // cond.sex = $("#select-sex").val();
    // cond.age = $("#select-age").val();
    // if (cond.sex == 1)
    //     cond.project = $("#select-project-male").val();
    // else
    //     cond.project = $("#select-project-female").val();
    // cond.group = $("#select-group").val();
    // $.ajax({
    //     type: "post",
    //     url: "get_form/",
    //     data: cond,
    //     dataType: "json",
    //     success: function (data) {
    //         console.log(data);
    //         $(".form-list").empty();
    //         for (var i = 1; i <= data.number; ++i) {
    //             var tr = $("<tr />")
    //                 .append('<th>' + i + '</th>')
    //                 .append('<td>' + data.athlete[i - 1].name + '</td>')
    //                 .append('<td>' + data.athlete[i - 1].team + '</td>');
    //                 for(var i = 1;i<data.Jnumber;++i)
    //                 {.append('<td>' + data.Judge[i - 1].score + '</td>');}
    //             $(".form-list").append(tr);
    //         }
    //         $(".form").show();
    //         $("#submit").show();
    //     },
    //     error: function(){
    //         $(".form").hide();
    //         $("#submit").hide();
    //     }
    var data = {};
    data.number = 3;
    data.Jnumber = 2;
    data.athlete = [];
    data.athlete[0] ={};
    data.athlete[1] = {};
    data.athlete[2] = {};
    data.athlete[0].name = 1;
    data.athlete[1].name = 2;
    data.athlete[2].name = 3;
    data.athlete[0].team = 1;
    data.athlete[1].team = 2;
    data.athlete[2].team = 3;
    data.judge = [];
    data.judge[0] = {};
    data.judge[1] = {};
    data.judge[0].score = [];
    data.judge[1].score = [];
    data.judge[0].score[0] = 1;
    data.judge[0].score[1] = 2;
    data.judge[1].score[0] = 1;
    data.judge[1].score[1] = 1;
$(".form-list").empty();
                for (var i = 1; i <= data.number; ++i) {
                    var tr = $("<tr />")
                        .append('<th>' + i + '</th>')
                        .append('<td>' + data.athlete[i - 1].name + '</td>')
                        .append('<td>' + data.athlete[i - 1].team + '</td>');
                        for(var j = 1;j<data.Jnumber;++j)
                        {tr.append('<td>' + data.judge[j - 1].score[i - 1] + '</td>');}
                    $(".form-list").append(tr);
                }
                $(".form").show();
                $("#submit").show();

       }

