const input = document.getElementById('movie-input');
const button = document.getElementById('recommend-button');
const recommendationsList = document.getElementById('recommendations-list');

button.addEventListener('click', function() {
    const movieTitle = input.value.trim();

    // Clear existing recommendations
    recommendationsList.innerHTML = '';

    fetch(`http://localhost:8000/recommend/${encodeURIComponent(movieTitle)}`)
        .then(response => {
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return response.json();
        })
        .then(data => {
            if (data.recommendations && data.recommendations.length > 0) {
                data.recommendations.forEach(movie => {
                    const listItem = document.createElement('li');
                    listItem.textContent = movie.title || movie;
                    recommendationsList.appendChild(listItem);
                });
            } else {
                recommendationsList.innerHTML = '<li>No recommendations found.</li>';
            }
        })
        .catch(error => {
            console.error('Error fetching recommendations:', error);
            recommendationsList.innerHTML = `<li>Error fetching recommendations: ${error.message}</li>`;
        });
});
