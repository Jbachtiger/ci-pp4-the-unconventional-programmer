// Script that executes message timeout

setTimeout(function() {
    try {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    } catch (e) {}

}, 2500);