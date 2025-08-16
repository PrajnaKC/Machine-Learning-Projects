# Movie Recommendation System - Full Stack Web Application

A content-based movie recommendation system with Django backend and modern HTML/CSS/JavaScript frontend.

## 🌟 Features

- **Web Interface**: Beautiful, responsive web application
- **Movie Search**: Real-time search with autocomplete
- **AI Recommendations**: Content-based filtering using machine learning
- **REST API**: Complete RESTful API for movie data and recommendations
- **Real-time Updates**: Dynamic loading and interactive UI
- **Mobile Friendly**: Responsive design that works on all devices

## 🚀 Quick Start

### Method 1: One-Click Start (Windows)
1. Double-click `start_webapp.bat`
2. Open your browser and go to: `http://localhost:8000`

### Method 2: Manual Start
1. **Activate virtual environment:**
   ```powershell
   movie_rec_env\Scripts\Activate.ps1
   ```

2. **Start the Django server:**
   ```powershell
   python manage.py runserver
   ```

3. **Open your browser:**
   Go to `http://localhost:8000`

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- Windows PowerShell

### Installation

1. **Clone/Download the project**
2. **Set up virtual environment:**
   ```powershell
   python -m venv movie_rec_env
   movie_rec_env\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up database:**
   ```powershell
   python manage.py migrate
   ```

5. **Verify dataset files are present:**
   - `tmdb_5000_movies.csv`
   - `tmdb_5000_credits.csv`

### Dataset Setup

The required dataset files are already included in your project:
- ✅ `tmdb_5000_movies.csv`
- ✅ `tmdb_5000_credits.csv`

If missing, download from [Kaggle TMDB Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata).

## 🎯 How to Use the Web App

1. **Search for Movies:**
   - Type in the search box to find movies
   - Results appear in real-time as you type

2. **Select a Movie:**
   - Click on any movie from search results
   - The movie will be selected for recommendations

3. **Get Recommendations:**
   - Choose number of recommendations (5-15)
   - Click "Get Recommendations"
   - View personalized movie suggestions

4. **Explore Results:**
   - Browse recommended movies
   - Each recommendation shows why it was suggested

## 🔧 API Endpoints

The application provides a REST API at `http://localhost:8000/api/`:

- `GET /api/health/` - Health check
- `GET /api/movies/` - List all movies (paginated)
- `GET /api/search/?q=query` - Search movies
- `POST /api/recommend/` - Get recommendations
- `GET /api/movie/<title>/` - Get movie details

### API Example Usage

```javascript
// Search for movies
fetch('http://localhost:8000/api/search/?q=batman')
  .then(response => response.json())
  .then(data => console.log(data.movies));

// Get recommendations
fetch('http://localhost:8000/api/recommend/', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    movie_title: 'The Dark Knight',
    num_recommendations: 5
  })
})
.then(response => response.json())
.then(data => console.log(data.recommendations));
```

## 📁 Project Structure

```
Movie Recommendation System/
├── movie_rec_env/              # Virtual environment
├── movie_rec_backend/          # Django project settings
│   ├── settings.py            # Django configuration
│   ├── urls.py                # Main URL routing
│   └── wsgi.py                # WSGI configuration
├── recommendations/            # Django app
│   ├── views.py               # API views and web pages
│   ├── urls.py                # App URL routing
│   └── models.py              # Database models
├── static/                     # Frontend files
│   └── index.html             # Main web interface
├── movie_recommendation_system.py  # ML recommendation engine
├── requirements.txt           # Python dependencies
├── start_webapp.bat          # Windows startup script
├── manage.py                 # Django management script
├── tmdb_5000_movies.csv      # Movie dataset
├── tmdb_5000_credits.csv     # Credits dataset
├── movie_list.pkl            # Processed data (auto-generated)
├── similarity.pkl            # Similarity matrix (auto-generated)
└── README.md                 # This file
```

## 🛠️ Technology Stack

### Backend
- **Django 5.2.4** - Web framework
- **Django REST Framework** - API development
- **Django CORS Headers** - Cross-origin requests
- **Python 3.13** - Programming language

### Machine Learning
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning algorithms
- **pickle** - Model persistence

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with animations
- **JavaScript (ES6+)** - Interactivity
- **Font Awesome** - Icons
- **Responsive Design** - Mobile compatibility

## 🎨 Features Overview

### Web Interface
- Modern, gradient design
- Real-time search with autocomplete
- Smooth animations and transitions
- Loading indicators and error handling
- Mobile-responsive layout

### Recommendation Engine
- Content-based filtering
- Cosine similarity calculation
- Feature extraction from movie metadata
- 4,800+ movies in database
- Intelligent text processing

### API Features
- RESTful design
- JSON responses
- Error handling
- Pagination support
- CORS enabled for frontend integration

## 🚨 Troubleshooting

### Server Won't Start
```powershell
# Make sure virtual environment is activated
movie_rec_env\Scripts\Activate.ps1

# Check if Django is installed
python -c "import django; print(django.get_version())"

# Reinstall dependencies if needed
pip install -r requirements.txt
```

### Frontend Can't Connect to API
- Ensure Django server is running on port 8000
- Check browser console for CORS errors
- Verify API endpoints are accessible: `http://localhost:8000/api/health/`

### Recommendation System Issues
- Verify dataset files are present and properly formatted
- Check if pickle files are generated: `movie_list.pkl`, `similarity.pkl`
- Run the verification script: `python download_dataset.py`

## 📱 Browser Compatibility
- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## 🔒 Security Notes
- This is a development setup
- For production, set `DEBUG = False` in settings.py
- Configure proper CORS origins
- Use a production WSGI server (not Django dev server)

## 🎯 Next Steps
- Add user authentication and profiles
- Implement collaborative filtering
- Add movie ratings and reviews
- Create recommendation history
- Add movie trailers and images
- Deploy to cloud platforms

## 🤝 Contributing
Feel free to contribute to this project by:
- Adding new features
- Improving the UI/UX
- Optimizing the recommendation algorithm
- Adding tests
- Improving documentation
