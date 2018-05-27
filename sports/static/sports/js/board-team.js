$(document).ready(function () {
    get_form();
});
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
    }
});
$("#search").on("click", function (e) {
    get_form();
});

function get_form() {
    var cond = {};
    cond.sex = $("#select-sex").val();
    cond.age = $("#select-age").val();
    if (cond.sex == 1)
        cond.project = $("#select-project-male").val();
    else
        cond.project = $("#select-project-female").val();
    
    $.ajax({
        type: "post",
        url: "get_form/",
        data: cond,
        dataType: "json",
        success: function (data) {
            console.log(data);
            $(".form-list").empty();
            for (var i = 0; i < data.project.length; ++i) {
                var project = data.project[i];
                if (project.athlete.length > 0)
                {
                    var tr = $("<tr />")
                    .append('<td>' + get_name(project.name) + '</td>')
                    .append('<td>' + get_sex(project.sex) + '</td>')
                    .append('<td>' + get_age(project.age_group) + '</td>');
                    for (var j = 0; j < project.athlete.length; ++j)
                    {
                        tr.append('<td>' + project.athlete[j].name + '</td>');
                        tr.append('<td>' + project.athlete[j].score + '</td>');
                    }
                    for (var j = project    .athlete.length; j < 6; ++j)
                    {
                        tr.append('<td>' + '</td>');
                        tr.append('<td>' + '</td>');
                    } 
                    $(".form-list").append(tr);
                }
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

function get_name(data){
    var result;
    switch (data) {
        case '1':
            result = '单杠'
            break;
        case '2':
            result = '双杠'
            break;
        case '3':
            result = '吊环'
            break;
        case '4':
            result = '跳马'
            break;
        case '5':
            result = '自由体操'
            break;
        case '6':
            result = '鞍马'
            break;
        case '7':
            result = '蹦床'
            break;
        case '8':
            result = '高低杠'
            break;
        case '9':
            result = '平衡木'
            break;
        default:
            break;
    }
    return result;
}

function get_sex(data){
    var result;
    switch (data) {
        case '1':
            result = "男"
            break;
        case '2':
            result = "女"
            break
        default:
            break;
    }
    return result;
}

function get_age(data){
    var result;
    switch (data) {
        case '1':
            result = "7-8"
            break;
        case '2':
            result = "9-10"
            break
        case '3':
            result = "11-12"
            break
        default:
            break;
    }
    return result;
}