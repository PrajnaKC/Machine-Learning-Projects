# Insurance Premium Prediction API

## Overview

This project provides a FastAPI-based web service for predicting insurance premium categories using a machine learning model trained on patient data. The model is built and trained using Python and scikit-learn, and is served via an API for easy integration into other applications or systems.

## Features

- **Insurance Premium Prediction:** Predicts the insurance premium category (`High`, `Medium`, `Low`) for a user based on demographic, health, and lifestyle information.
- **Machine Learning Model:** Utilizes a RandomForestClassifier trained on derived features such as BMI, age group, lifestyle risk, city tier, income, and occupation.
- **FastAPI Framework:** Provides a RESTful endpoint for prediction (`/predict`).
- **Model Serialization:** The trained machine learning pipeline is saved as `model.pkl` and loaded by the API.

## Project Structure

```
.
├── app.py                 # FastAPI app serving the prediction endpoint
├── fastapi_ml_model.ipynb # Jupyter notebook for data preparation and ML training
├── model.pkl              # Serialized ML pipeline for prediction
├── insurance.csv          # Sample data used for training (not included)
└── README.md              # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8+
- Required Python packages (see below)

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/<owner>/<repo>.git
    cd <repo>
    ```

2. **Install dependencies**
    ```bash
    pip install fastapi uvicorn pandas scikit-learn pydantic
    ```

3. **Train the model (optional)**
    - Use `fastapi_ml_model.ipynb` to preprocess `insurance.csv`, engineer features, train the RandomForest model, and save it as `model.pkl`.

4. **Run the API server**
    ```bash
    uvicorn app:app --reload
    ```

5. **Test the API**
    - Open [Swagger UI](http://localhost:8000/docs) for interactive API testing.

## API Usage

### Endpoint

- **POST** `/predict`
    - Accepts JSON payload with user data.
    - Returns predicted insurance premium category.

#### Sample Request Body

```json
{
  "age": 40,
  "weight": 80,
  "height": 1.75,
  "income_lpa": 10,
  "smoker": false,
  "city": "Bangalore",
  "occupation": "private_job"
}
```

#### Sample Response

```json
{
  "predicted_category": "Medium"
}
```

### Input Fields

- `age`: Integer (1-119)
- `weight`: Float (>0)
- `height`: Float (>0, <2.5 meters)
- `income_lpa`: Float (>0, annual income in lakhs)
- `smoker`: Boolean
- `city`: String (used to determine city tier)
- `occupation`: Enum (`retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job`)

### Derived Features

The API will internally compute:
- **BMI** (Body Mass Index)
- **Lifestyle Risk** (`high`, `medium`, `low`)
- **Age Group** (`young`, `adult`, `middle_aged`, `senior`)
- **City Tier** (`1`, `2`, `3`)

## Model Training

The Jupyter notebook (`fastapi_ml_model.ipynb`) covers:
- Data loading and exploration
- Feature engineering (BMI, age group, lifestyle risk, city tier)
- Model training using a pipeline (ColumnTransformer + RandomForest)
- Model evaluation (accuracy, classification report)
- Saving the trained pipeline with pickle

## Contributing

Feel free to open issues or pull requests for improvements, bug fixes, or new features.

## Contact

For questions or support, contact prajnakudkuli@gmail.com
