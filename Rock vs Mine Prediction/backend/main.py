import os
import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np

# User database file
USER_DB_FILE = "users.json"

def load_users():
    if not os.path.exists(USER_DB_FILE):
        return {}
    with open(USER_DB_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f)

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
with open("trained_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/login")
async def login(request: Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")
    users = load_users()
    if username in users:
        if users[username] == password:
            return {"success": True}
        else:
            return {"success": False, "error": "Invalid credentials"}
    else:
        # Register new user
        users[username] = password
        save_users(users)
        return {"success": True, "message": "User created and logged in"}

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    features = data.get("features")
    if not features or not isinstance(features, list):
        return {"error": "Invalid input"}
    prediction = model.predict([np.array(features)])
    result = "Rock" if prediction[0] == "R" else "Mine"
    return {"prediction": result}
