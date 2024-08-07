document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('urlForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        handleSubmit();
    });

    function handleSubmit() {
        const url = document.getElementById('urlSearchInput').value;

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'url=' + encodeURIComponent(url),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `URL: ${data.url}<br>Predicted Label: ${data.label}<br>Confidence Score: ${data.score}`;
        })
        .catch(error => console.error('Error:', error));
    }
});
