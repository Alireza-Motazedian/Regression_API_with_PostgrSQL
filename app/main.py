import os
import joblib
import logging
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.config import settings

# Import database components
from app.database import (
    engine, Base, get_db, HousingPrediction, create_prediction,
    get_prediction, get_all_predictions, HousingFeatures, PredictionResponse, PredictionInDB
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create database tables
try:
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")
except Exception as e:
    logger.error(f"Error creating database tables: {str(e)}")
    raise

app = FastAPI(
    title="Housing Price Prediction API with PostgreSQL",
    description="A FastAPI application for housing price regression predictions with PostgreSQL integration",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the ML model
try:
    model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "models", "ml_model.pkl")
    logger.info(f"Loading model from {model_path}")
    model = joblib.load(model_path)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise

@app.get("/")
async def root():
    return {"message": "Welcome to Housing Price Prediction API with PostgreSQL Integration"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "Service is running"
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(data: HousingFeatures, db: Session = Depends(get_db)):
    try:
        # Extract features from the request
        features = [
            data.median_income,
            data.housing_median_age,
            data.total_rooms,
            data.total_bedrooms,
            data.population,
            data.households,
            data.latitude,
            data.longitude
        ]
        
        # Make prediction using the model
        predicted_price = float(model.predict([features])[0])
        
        # Save the prediction to the database
        prediction_obj = HousingPrediction.from_request(features, predicted_price)
        db_prediction = create_prediction(db, prediction_obj)
        
        # Return prediction response
        return {
            "status": "success",
            "predicted_price": predicted_price,
            "input_features": features
        }
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/predictions", response_model=list[PredictionInDB])
async def get_predictions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all predictions from the database with pagination"""
    predictions = get_all_predictions(db, skip=skip, limit=limit)
    return predictions

@app.get("/predictions/{prediction_id}", response_model=PredictionInDB)
async def get_prediction_by_id(prediction_id: int, db: Session = Depends(get_db)):
    """Get a specific prediction by ID"""
    prediction = get_prediction(db, prediction_id)
    if prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return prediction 