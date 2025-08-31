document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const featuresInput = document.getElementById('features').value;
    const features = featuresInput.split(',').map(Number);
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'Predicting...';
    try {
        const response = await fetch('http://localhost:8000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ features })
        });
        const data = await response.json();
        if (data.prediction) {
            resultDiv.textContent = 'Prediction: ' + data.prediction;
        } else {
            resultDiv.textContent = 'Error: ' + (data.error || 'Unknown error');
        }
    } catch (error) {
        resultDiv.textContent = 'Error connecting to backend.';
    }
});

// Dark mode toggle
const darkModeToggle = document.getElementById('darkModeToggle');
darkModeToggle.addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    if (document.body.classList.contains('dark-mode')) {
        darkModeToggle.textContent = '☀️';
    } else {
        darkModeToggle.textContent = '🌙';
    }
});
