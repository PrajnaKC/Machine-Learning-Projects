# Movie Recommendation App - Backend

This is the backend component of the Movie Recommendation App, built using FastAPI. The backend is responsible for handling API requests, processing movie data, and providing recommendations based on user input.

## Project Structure

- **main.py**: The entry point of the FastAPI application. It initializes the app, sets up routes, and runs the server.
- **models/movie.py**: Defines the `Movie` model class, representing the structure of a movie object with properties such as `id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.
- **api/recommend.py**: Contains the recommendation logic. It exports the `get_recommendations` function, which takes a movie title as input and returns a list of recommended movies based on the similarity matrix.
- **requirements.txt**: Lists the dependencies required for the backend, including FastAPI and any other necessary libraries.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd movie-recommendation-app/backend
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the FastAPI application**:
   ```
   uvicorn main:app --reload
   ```

5. **Access the API documentation**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## API Usage

- **Get Recommendations**: 
  - Endpoint: `/recommend`
  - Method: `POST`
  - Request Body: 
    ```json
    {
      "title": "Movie Title"
    }
    ```
  - Response: A list of recommended movies based on the input title.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.