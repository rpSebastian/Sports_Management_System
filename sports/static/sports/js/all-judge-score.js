var flag = 1, Data = {};
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
            Data = data;
            $(".form-list").empty();
            number = data.number;
            num = data.num;
            for (var i = 1; i <= 2*data.number; i=i+2) {
                var tr = $("<tr />")
                    .append('<th>' + (i+1)/2 + '</th>')
                    .append('<td>' + data.athlete[i - 1].name + '</td>')
                    .append('<td>' + data.athlete[i - 1].team + '</td>');
                for (var j = 1; j <= data.num; j++) {
                    tr.append('<td>' + data.athlete[i].judge[j - 1] + '</td>');
                }
                tr.append('<td><input type="text" class="form-control" id="reward-point' + i + '">');
                tr.append('<td><input type="text" class="form-control" id="punish-point' + i + '">');
                $(".form-list").append(tr);
            }
            $(".form").show();
            $("#submit").show();
            $(".form-list2").empty();
            var tr2 = $("<tr/>")
                .append('<th>' + '小组编号' + '</th>')
                .append('<th>' + '运动员姓名' + '</th>')
                .append('<th>' + '运动员代表队' + '</th>');
            for (var i = 1; i <= data.num; i++) {
                tr2.append('<th>' + '成绩' + i + '</th>');
                tr2.append('<th>' + '奖励分' + '</th>');
                tr2.append('<th>' + '惩罚分' + '</th>');
            }
            $(".form-list2").append(tr2);
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
    cond.athlete_reward = [];
    cond.athlete_punish = [];
    for (var i = 1; i <= 2*Data.number; i=i+2){
        var reward;
        reward = $("#reward-point" + i).val();
        cond.athlete_reward[(i+1)/2] = reward;
        var punish;
        punish = $("#punish-point" + i).val();
        cond.athlete_punish[(i+1)/2] = punish;
        var max = Data.athlete[i].judge[0];
        var min = Data.athlete[i].judge[0];
        var sum = Data.athlete[i].judge[0];
        var avg = 0;
        for(var j = 1; j < Data.num; j++){
             if(Data.athlete[i].judge[j] > max){
                 max = Data.athlete[i].judge[j];
             }
             if(Data.athlete[i].judge[j] < min){
                 min = Data.athlete[i].judge[j];
             }
             sum += Data.athlete[i].judge[j];
        }
        avg = sum / Data.num;
        if (Data.num > 2){
            sum -= max + min;
            avg = sum / (Data.num-2);
        }
        cond.athlete_score[(i+1)/2] = Number(avg) * Number(Data.num) + Number(reward) - Number(punish);
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

    // var data = {};
    // data.number = 3;
    // data.Jnumber = 2;
    // data.athlete = [];
    // data.athlete[0] ={};
    // data.athlete[1] = {};
    // data.athlete[2] = {};
    // data.athlete[0].name = 1;
    // data.athlete[1].name = 2;
    // data.athlete[2].name = 3;
    // data.athlete[0].team = 1;
    // data.athlete[1].team = 2;
    // data.athlete[2].team = 3;
    // data.judge = [];
    // data.judge[0] = {};
    // data.judge[1] = {};
    // data.judge[0].score = [];
    // data.judge[1].score = [];
    // data.judge[0].score[0] = 1;
    // data.judge[0].score[1] = 2;
    // data.judge[1].score[0] = 1;
    // data.judge[1].score[1] = 1;

