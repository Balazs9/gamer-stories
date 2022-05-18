setTimeout(function() {
    let messages = document.getElementById("alert_msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 5000);

/*
    w3school.com how to scroll back to top button
*/
topButton = document.getElementById('btnTop');
window.onscroll = function() {scrollFunction()};


// when the user scroll down 10px, the back to top button will display

function scrollFunction() {
    if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
        topButton.style.display = 'block';
    }
    else {
        topButton.style.display = 'none';
    }
}

// when the user clicks on the button that brings back to the top of the page

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}