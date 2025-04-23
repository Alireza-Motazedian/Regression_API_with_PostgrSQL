from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class HousingPrediction(Base):
    """SQLAlchemy model for storing California Housing price predictions"""
    __tablename__ = "housing_predictions"

    id = Column(Integer, primary_key=True, index=True)
    # California Housing dataset features
    median_income = Column(Float, nullable=False)
    housing_median_age = Column(Float, nullable=False)
    total_rooms = Column(Float, nullable=False)
    total_bedrooms = Column(Float, nullable=False)
    population = Column(Float, nullable=False)
    households = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    # Prediction
    predicted_price = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    @classmethod
    def from_request(cls, features, prediction):
        """Create a prediction object from request features and model prediction"""
        return cls(
            median_income=features[0],
            housing_median_age=features[1],
            total_rooms=features[2],
            total_bedrooms=features[3],
            population=features[4],
            households=features[5],
            latitude=features[6],
            longitude=features[7],
            predicted_price=prediction
        ) 