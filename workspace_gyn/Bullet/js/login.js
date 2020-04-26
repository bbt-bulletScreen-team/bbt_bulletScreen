var TurnToLogin = () => {
    document.getElementById('loginback').style.display = "block";
    document.getElementById('registback').style.display = "none";
}
var TurnToRegister = () => {
    document.getElementById('registback').style.display = "block";
    document.getElementById('loginback').style.display = "none";
}

function loading() {
    document.getElementById('loading').style.display = "block"; //显示
}

function closeLoading() {
    document.getElementById('loading').style.display = "none"; //隐藏
}

function reload() {
    window.location.reload();
}

function postLogin(argPhone, argUserPass) {
    //创建一个XMLHttpRequest 对象
    var xhr = new XMLHttpRequest();
    //准备发送请求的数据：url
    var url = "129.204.250.51/Login";
    //使用HTTP POST请求与服务器交互数据
    xhr.open("POST", url, true);
    //设置发送数据的请求格式
    xhr.setRequestHeader('content-type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 3) {
            //loading();
        } else if (xhr.readyState == 4) {
            closeLoading();
            //根据服务器的响应内容格式处理响应结果
            if (xhr.getResponseHeader('content-type') === 'application/json') {
                console.log(xhr.responseText);
                var resultJSON = JSON.parse(xhr.responseText);
                if (resultJSON.errcode === 0) {
                    localStorage.setItem("username", argUserName);
                    window.location.href = "http://localhost/index4.html";
                } else {
                    alert(resultJSON.errmsg);
                }
            } else {
                console.log(xhr.responseText);
                alert("发生错误");
            }
        }
    }

    var sendData = {
        "phone": argPhone,
        "password": argUserPass
    };
    //将用户输入值序列化成字符串
    console.log(JSON.stringify(sendData));
    xhr.send(JSON.stringify(sendData));

}

function login() {
    var phone = document.getElementById("phone").value;
    var password = document.getElementById("password").value;
    console.log("用户输入:", phone, password)
    postLogin(phone, password);

}



function postRegist(argUserName, argUserPass, argNickname) {
    //创建一个XMLHttpRequest 对象
    var xhr = new XMLHttpRequest();
    //准备发送请求的数据：url
    var url = "129.204.250.51/Regist";
    //使用HTTP POST请求与服务器交互数据
    xhr.open("POST", url, true);
    //设置发送数据的请求格式
    xhr.setRequestHeader('content-type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 3) {
            loading();
        } else if (xhr.readyState == 4) {
            closeLoading();
            //根据服务器的响应内容格式处理响应结果
            if (xhr.getResponseHeader('content-type') === 'application/json') {
                console.log(xhr.responseText);
                var resultJSON = JSON.parse(xhr.responseText);
                if (resultJSON.errcode === 0) {
                    alert("注册成功!");
                    reload();
                } else {
                    alert(resultJSON.errmsg);
                }
            }
        }
    }

    var sendData = {
        "phone": argPhone,
        "nick_name": argNickname,
        "password": argUserPass
    };
    //将用户输入值序列化成字符串
    console.log(JSON.stringify(sendData));
    xhr.send(JSON.stringify(sendData));

}

function regist() {
    var registUser = registPassword1 = document.getElementById("registPassword1").value;
    console.log("用户输入:", registUser, registPassword1)

}