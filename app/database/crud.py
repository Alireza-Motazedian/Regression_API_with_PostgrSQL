from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.models import HousingPrediction

def create_prediction(db: Session, prediction: HousingPrediction) -> HousingPrediction:
    """
    Create a new housing price prediction record in the database.
    
    Args:
        db: Database session
        prediction: HousingPrediction object to save
        
    Returns:
        The saved prediction with ID assigned
    """
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction

def get_prediction(db: Session, prediction_id: int) -> Optional[HousingPrediction]:
    """
    Get a specific prediction by ID.
    
    Args:
        db: Database session
        prediction_id: ID of the prediction to retrieve
        
    Returns:
        The prediction if found, None otherwise
    """
    return db.query(HousingPrediction).filter(HousingPrediction.id == prediction_id).first()

def get_all_predictions(db: Session, skip: int = 0, limit: int = 100) -> List[HousingPrediction]:
    """
    Get all predictions with pagination.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of predictions ordered by most recent first
    """
    return db.query(HousingPrediction).order_by(HousingPrediction.created_at.desc()).offset(skip).limit(limit).all()

def delete_prediction(db: Session, prediction_id: int) -> bool:
    """
    Delete a prediction by ID.
    
    Args:
        db: Database session
        prediction_id: ID of the prediction to delete
        
    Returns:
        True if deleted, False if not found
    """
    prediction = db.query(HousingPrediction).filter(HousingPrediction.id == prediction_id).first()
    if prediction:
        db.delete(prediction)
        db.commit()
        return True
    return False 