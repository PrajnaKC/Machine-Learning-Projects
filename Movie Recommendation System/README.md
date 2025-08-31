# Movie Recommendation App

This project is a movie recommendation application built using FastAPI for the backend and HTML, CSS, and JavaScript for the frontend. The application provides users with movie recommendations based on a similarity matrix derived from various movie attributes.

## Project Structure

```
movie-recommendation-app
├── backend
│   ├── main.py                # Entry point for the FastAPI application
│   ├── models
│   │   └── movie.py           # Defines the Movie model
│   ├── api
│   │   └── recommend.py        # Contains recommendation logic
│   ├── requirements.txt        # Lists backend dependencies
│   └── README.md               # Documentation for the backend
├── frontend
│   ├── index.html              # Main HTML file for the frontend
│   ├── styles
│   │   └── style.css           # Styles for the frontend
│   ├── scripts
│   │   └── app.js              # JavaScript code for the frontend
│   └── README.md               # Documentation for the frontend
└── README.md                   # Overview of the entire project
```

## Backend Setup

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn main:app --reload
   ```
4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Frontend Setup

1. Navigate to the `frontend` directory.
2. Open `index.html` in a web browser to view the application.

## Usage

- Users can search for a movie title, and the application will return a list of recommended movies based on the selected title.
- The recommendations are generated using a similarity matrix that considers various attributes of the movies.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.