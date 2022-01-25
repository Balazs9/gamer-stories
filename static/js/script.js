setTimeout(function() {
    let messages = document.getElementById("alert_msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 500000);