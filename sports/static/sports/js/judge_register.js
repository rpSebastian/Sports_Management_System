$(document).ready(function () {
    console.log(100)
});

$(document).on("click", "#register", function () {
    var username = $("#username").val();
    var password = $("#password").val();
    var judgename = $("#judgename").val();
    var idcardname = $("#idcardnumber").val();
    var phonenumber = $("#phonenumber").val();
    console.log(username);
    console.log(judgename);
    console.log(idcardname);
    console.log(phonenumber);
    $.ajax({
        type:"post",
        url:"../sports/judge_register",
        data:{
            "username":username,
            "password":password,
            "judgename":judgename,
            "idcardnumber":idcardname,
            "phonenumber":phonenumber,
        },

        success:function (data) {
            console.log(data);
            if (data == "1"){
                window.location.href = "../sports/pre_judge_login"
            }
            if (data == "2"){
                window.location.href = "../sports/pre_judge_register"
            }
        }
    });
});