# Rock vs Mine Prediction - Full Stack Project

This project is a full stack web application for predicting whether an object is a rock or a mine using a trained machine learning model.

## Features
- **Login/Registration:** Users can log in or create an account (credentials stored in `users.json`).
- **Prediction:** Enter 60 features to get a prediction (Rock or Mine).
- **Frontend:** HTML, CSS, JavaScript (with dark mode toggle).
- **Backend:** FastAPI (Python) serving model predictions and authentication.

## Getting Started

### 1. Install Dependencies
Activate your Python virtual environment and install required packages:
```powershell
pip install fastapi uvicorn numpy scikit-learn
```

### 2. Run the Backend
```powershell
uvicorn backend.main:app --reload
```

### 3. Run the Frontend
```powershell
cd frontend
python -m http.server 8080
```

### 4. Access the App
Open your browser and go to:
- Login: [http://localhost:8080/login.html](http://localhost:8080/login.html)
- Prediction: [http://localhost:8080/index.html](http://localhost:8080/index.html)

## Usage
- **Login:** Enter a username and password. If the username does not exist, it will be created.
- **Prediction:** After login, enter 60 comma-separated numeric features and click Predict.
- **Dark Mode:** Toggle dark mode using the button in the header.

## File Structure
```
Rock vs Mine Prediction/
├── backend/
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── style.css
│   ├── script.js
│   └── login.js
├── trained_model.pkl
├── users.json
└── README.md
```

## Notes
- The model expects 60 features. Enter them as comma-separated values.
- User credentials are stored in plain text in `users.json` (for demo purposes).
- No OTP or email verification is implemented.

## Customization
- To change login logic, edit `backend/main.py`.
- To change UI, edit files in `frontend/`.

## License
MIT
