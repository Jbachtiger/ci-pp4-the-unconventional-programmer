// Script that executes message timeout

setTimeout(function() {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);