var athlete_num = 1;
$(document).ready(function () {

});
$(document).on("change", ".select-sex", function () {
    var id = $(this).attr("id");
    var num = id.substring(10, id.length);
    console.log(num);
    var option = $("#select-sex" + num + " option:selected");
    if (option.val() == 1) {
        $("#athlete-project-man" + num).show();
        $("#athlete-project-woman" + num).hide();
    } else if (option.val() == 2) {
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
    swal({
            title: "Success!",
            text: "",
            type: "success",
            confirmButtonText: "OK"
        },
        function () {
            window.location.href = "../index";
        });
})