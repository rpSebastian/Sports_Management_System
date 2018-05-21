$(document).ready(function () {
    console.log(100)
});

$(document).on("click", "#register", function () {
    var username = $("#username").val();
    var password = $("#password").val();
    var teamname = $("#teamname").val();
    console.log(username)
    console.log(password)
    console.log(teamname)
    $.ajax({
        type:"post",
        url:"../sports/register",
        data:{
            "username":username,
            "password":password,
            "teamname":teamname
        },

        success:function (data) {
            console.log(data);
            if (data == "1"){
                window.location.href = "../sports/pre_login"
            }
        }
    });
});