function window_close() {
    fetch('/close_window', {
        method: 'POST'
    }).then(response => response.json())
        .then(data => {

        });
}