# Notebooks

This directory contains Jupyter notebooks used for data exploration, analysis, and model development.

- You can easily adapt the repository to work with any dataset of your choice.
- The structure is flexible and can be applied to various machine learning models, including regression, classification, and clustering.

## Contents

- **`01_data_exploration.ipynb`**: A Jupyter notebook that demonstrates:
  - Loading and examining the California Housing dataset
  - Exploratory Data Analysis (EDA)
  - Data visualization and statistical analysis
  - Feature analysis and relationships
  - Preparation for model training

- **`02_model_training.ipynb`**: A Jupyter notebook that demonstrates:
  - Model training on the California Housing dataset
  - Linear regression implementation
  - Model evaluation with MSE, RMSE, and R² metrics
  - Model serialization for use in the API

## Database Integration

These notebooks focus on the ML aspects of the project. For database integration:
- Trained models are saved and used by the FastAPI application
- Predictions are stored in PostgreSQL database
- The API provides endpoints to retrieve prediction history

## Usage

The notebooks can be accessed through:
- Jupyter Notebook/Lab interface
- Docker container using the provided docker-compose setup
- VS Code's built-in notebook viewer

## Important Notes

- Keep notebooks organized and well-documented
- Use clear naming conventions for notebooks
- Include markdown cells explaining the analysis
- Save visualizations in the `assets` folder if needed
- Document any dependencies or setup requirements
- Consider version controlling the notebook outputs 