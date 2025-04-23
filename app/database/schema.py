from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class HousingFeatures(BaseModel):
    """Pydantic model for California Housing prediction request"""
    median_income: float = Field(..., example=8.3252, description="Median income in block group")
    housing_median_age: float = Field(..., example=41.0, description="Median house age in block group")
    total_rooms: float = Field(..., example=6984.0, description="Total number of rooms in block group")
    total_bedrooms: float = Field(..., example=1467.0, description="Total number of bedrooms in block group")
    population: float = Field(..., example=3901.0, description="Block group population")
    households: float = Field(..., example=1193.0, description="Number of households in block group")
    latitude: float = Field(..., example=37.88, description="Block group latitude")
    longitude: float = Field(..., example=-122.23, description="Block group longitude")
    
    class Config:
        json_schema_extra = {
            "example": {
                "median_income": 8.3252,
                "housing_median_age": 41.0,
                "total_rooms": 6984.0,
                "total_bedrooms": 1467.0,
                "population": 3901.0,
                "households": 1193.0,
                "latitude": 37.88,
                "longitude": -122.23
            }
        }

class PredictionBase(BaseModel):
    """Base prediction model with common attributes"""
    median_income: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    latitude: float
    longitude: float
    predicted_price: float

class PredictionCreate(PredictionBase):
    """Model for creating a prediction (no ID or timestamp)"""
    pass

class PredictionInDB(PredictionBase):
    """Model for prediction as stored in database, including ID and timestamp"""
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class PredictionResponse(BaseModel):
    """Response model for prediction endpoint"""
    status: str
    predicted_price: float
    input_features: List[float]
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "predicted_price": 4.526,
                "input_features": [8.3252, 41.0, 6984.0, 1467.0, 3901.0, 1193.0, 37.88, -122.23]
            }
        } 