var flag = 1, number = 0;
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
$("#submit").on("click", function (e) {
    submit_form();
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
    var cond = {};
    cond.sex = $("#select-sex").val();
    cond.age = $("#select-age").val();
    if (cond.sex == 1)
        cond.project = $("#select-project-male").val();
    else
        cond.project = $("#select-project-female").val();
    cond.group = $("#select-group").val();
    $.ajax({
        type: "post",
        url: "get_form/",
        data: cond,
        dataType: "json",
        success: function (data) {
            console.log(data);
            $(".form-list").empty();
            number = data.number;
            for (var i = 1; i <= data.number; ++i) {
                var tr = $("<tr />")
                    .append('<th>' + i + '</th>')
                    .append('<td>' + data.athlete[i - 1].name + '</td>')
                    .append('<td>' + data.athlete[i - 1].team + '</td>')
                    .append('<td><input type="text" class="form-control" id="athlete-grade' + i + '">');
                $(".form-list").append(tr);
            }
            $(".form").show();
            $("#submit").show();
        },
        error: function () {
            $(".form").hide();
            $("#submit").hide();
        }
    });
}

function submit_form() {
    var cond = {};
    cond.sex = $("#select-sex").val();
    cond.age = $("#select-age").val();
    if (cond.sex == 1)
        cond.project = $("#select-project-male").val();
    else
        cond.project = $("#select-project-female").val();
    cond.group = $("#select-group").val();
    cond.athlete_score = [];
    for (var i = 1; i <= number; ++i){
        cond.athlete_score[i - 1] = $("#athlete-grade" + i).val();
    }
    console.log(cond);
    $.ajax({
        type: "post",
        url: "update_score/",
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
};