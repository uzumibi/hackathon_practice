document.getElementById('captureButton').addEventListener('click', function() {
    // カメラ画像のキャプチャリクエストをサーバーに送信
    fetch('/capture', {
        method: 'POST'
    })
    .then(response => response.json())
});
