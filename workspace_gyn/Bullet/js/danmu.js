$(function() {
    var ws = new WebSocket('ws://127.0.0.1/ws');
    var $message = $('#message');

    console.log('websocket object init over')
    var height = $(document).height();
    var width = $(document).width();

    function random(num) {
        return parseInt(Math.random() * num);
    }
    var colors = ['black', '#1f8dd6', 'rgb(128, 88, 165)', '#5eb95e', '#dd514c', 'rgb(243, 123, 29)', 'rgb(250, 210, 50)'];
    var sizes = [0, 1];

    var $danmu = $('#danmu');
    var $input = $('#text');
    $danmu.danmu({
        height: height, //弹幕区高度
        width: width,
        top: 0,
        speed: random(2000) + 4000,
        fontSizeSmall: 12, //小弹幕的字号大小
        FontSizeBig: 20,
    }); // 初始化
    $danmu.danmu('danmuStart'); // 启动

    $('#say').on('click', function(e) {
        e.preventDefault();
        var color = colors[random(colors.length)];
        var size = sizes[random(2)];
        ws.send(JSON.stringify({
            message: $input.val(),
            color: color,
            size: size
        }));
        $input.val('');
    });

    ws.onmessage = function(ev) {
        $message.attr("class", 'label label-info');
        $message.hide();
        $message.fadeIn("slow");
        $message.text('recieved message');

        data = JSON.parse(JSON.parse(ev.data));
        console.log(data)

        $danmu.danmu("addDanmu", [{
            text: data.message,
            color: data.color,
            size: data.size,
            position: 0,
            top: random(200) + 200,
            time: $danmu.data("nowTime") + 1
        }]);
    };

    ws.onopen = function() {
        $message.attr("class", 'label label-success');
        $message.text('open');
    };
    ws.onclose = function(ev) {
        $message.attr("class", 'label label-important');
        $message.text('closed');
    };
    ws.onerror = function(ev) {
        $message.attr("class", 'label label-warning');
        $message.text('error occurred');
    };
});