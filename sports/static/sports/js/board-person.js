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