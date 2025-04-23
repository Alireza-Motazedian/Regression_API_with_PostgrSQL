# Export database components for easy import

# Core database components
from app.database.session import engine, SessionLocal
from app.database.models import Base, HousingPrediction
from app.database.deps import get_db

# CRUD operations
from app.database.crud import (
    create_prediction,
    get_prediction,
    get_all_predictions,
    delete_prediction
)

# Pydantic models for API
from app.database.schema import (
    HousingFeatures,
    PredictionResponse,
    PredictionInDB,
    PredictionCreate,
    PredictionBase
)

__all__ = [
    "engine", "SessionLocal", "Base", "get_db",
    "HousingPrediction", "create_prediction", "get_prediction", "get_all_predictions",
    "HousingFeatures", "PredictionResponse", "PredictionInDB",
    "PredictionCreate", "PredictionBase"
] 