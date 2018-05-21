
$(document).on("click", "#login", function () {
    var username = $("#username").val();
    var password = $("#password").val();
    $.ajax({
        type:"post",
        url:"../sports/login",
        data:{
            'username':username,
            'password':password
        },
        success:function (data) {
            console.log(data);
            if (data == "1"){
                window.location.href = "../sports/group/register/"
                // window.location.href("../group-register.html/")
            }
            if(data == "2"){
                console.log("ggsmd")
                location.href = '../sports/pre_login'
                // window.location.href = '../sports/pre_login/';
                // window.location.href("../pre_login/")

            }
        }
    });
});
