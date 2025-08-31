from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np

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

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    features = data.get("features")
    if not features or not isinstance(features, list):
        return {"error": "Invalid input"}
    prediction = model.predict([np.array(features)])
    result = "Rock" if prediction[0] == "R" else "Mine"
    return {"prediction": result}
