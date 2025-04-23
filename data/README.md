# Data Directory

- This file contains the California Housing dataset, a well-known dataset in machine learning for regression tasks. It contains information about houses in districts across California, including features such as median income, housing median age, average number of rooms, average number of bedrooms, population, average occupancy, latitude, and longitude. The target variable is the median house value for California districts, measured in hundreds of thousands of dollars.

## Usage

The dataset is automatically fetched from scikit-learn during model training, so you don't need to manually download it. However, you can store processed versions or additional datasets in this directory.

## Data Description

### Features

1. **MedInc**: Median income in block group
2. **HouseAge**: Median house age in block group
3. **AveRooms**: Average number of rooms per household
4. **AveBedrms**: Average number of bedrooms per household
5. **Population**: Block group population
6. **AveOccup**: Average number of household members
7. **Latitude**: Block group latitude
8. **Longitude**: Block group longitude

### Target

- **MedianHouseValue**: Median house value in block group (in hundreds of thousands of dollars)

## Dataset Statistics

- Number of instances: 20,640
- Number of features: 8
- Target values range from 0.15 to 5.00 (hundred thousands of dollars)

## Important Notes

- Keep datasets in this directory for easy access and reference
- Document any preprocessing applied to the data
- Consider adding data exploration notebooks to understand the data better
- Track data versions if you modify the original dataset

# `original_dataset.csv`

- This file contains the Iris dataset, a classic dataset in machine learning and statistics. It consists of 150 samples of iris flowers, each with four features: sepal length, sepal width, petal length, and petal width. The target variable is the species of the iris, which can be one of three classes: Setosa, Versicolour, or Virginica.


- ***You can easily adapt the repository to work with any dataset of your choice.*** The structure is flexible and can be applied to various machine learning models, including ***regression, classification, and clustering***. 