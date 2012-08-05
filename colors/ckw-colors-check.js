$(document).ready(function(){
function log(message) {
    if (typeof console == 'object') console.log(message);
}
function message(text) {
    log(text);
    var $msg = $("<p />").addClass("msg").text(text).hide();
    $("#msgbox").append($msg);
    $msg.slideDown("normal").delay(1500).slideUp("slow");
}
function format(prefix, number) {
    return prefix + (number < 10 ? "0" : "") + number;
}
function check(val) {
    return val.match(/^#[0-9a-f]{6}$/i);
}
function make_callback(i) {
    var f = function(e) {
        var n = i;
        if (e.keyCode != 13) return;
        var $t = $(this);
        var val = $t.val();
        if (!check(val)) {
            message("Value Error: " + val);
            $t.css("background-color", "#FFCCFF");
            return;
        }
        val = val.toUpperCase();
        $t.css("background-color", "#FFFFFF");
        $(format(".f", n)).css("color", val).html(val);
        $(format(".b", n)).css("background-color", val);
        switch(n) {
            case 0:
            $("body").css("color", val);
            $("table, td, th").css("border-color", val);
            break;
            case 1:
            $("body").css("background-color", val);
            break;
            default:
            break;
        }
    };
    return f;
}
for (var i = 0; i < 20; i++) {
    var s = $(format("td.f", i)).html();
    $(format("#i", i)).val(s);
    $(format("#i", i)).keyup(make_callback(i));
}
});
