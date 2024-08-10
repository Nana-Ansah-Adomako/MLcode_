Certainly! Below is a detailed `README.md` based on the provided code and analysis:

---

# Loan Prediction Model

This project involves building and evaluating machine learning models to predict the loan approval status (`Loan_Status`) of applicants based on various features. The models were trained and tested using a dataset containing information such as `Gender`, `Education`, `Marital_Status`, `Employment_Type`, `Applicant_Monthly_Income`, and more. 

## Table of Contents

- [Installation](#installation)
- [Dataset Overview](#dataset-overview)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Model Building](#model-building)
  - [Random Forest Classifier](#random-forest-classifier)
  - [Decision Tree Classifier](#decision-tree-classifier)
- [Model Evaluation](#model-evaluation)
- [Feature Importance](#feature-importance)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Conclusion](#conclusion)

## Dataset Overview

The dataset consists of 614 entries with 12 columns:

- `Loan_ID`: Unique identifier for the loan application.
- `Gender`: Gender of the applicant.
- `Education`: Education level of the applicant.
- `Marital_Status`: Marital status of the applicant.
- `Employment_Type`: Employment status of the applicant.
- `Residential_Status`: Type of residence of the applicant.
- `Dependents`: Number of dependents the applicant has.
- `Applicant_Monthly_Income`: Monthly income of the applicant.
- `Loan_Amount`: Amount of loan applied for.
- `Loan_Type`: Type of loan applied for.
- `Term_of_Loan`: Loan term in months.
- `Loan_Status`: Target variable indicating whether the loan was approved or not.

## Data Preprocessing

1. **Missing Values**: Missing values in the `Gender` and `Dependents` columns were filled using the mode of the respective columns.
   ```python
   train['Gender'].fillna(train['Gender'].mode()[0], inplace=True)
   train['Dependents'].fillna(train['Dependents'].mode()[0], inplace=True)
   ```

2. **Data Types and Structure**:
   - The dataset contains both numerical and categorical data.
   - The dataset shape is `(614, 12)`.

## Exploratory Data Analysis (EDA)

### Distribution of Applicant Monthly Income
A bar plot shows the distribution of applicants' monthly income.

### Loan Amount Distribution
- The `Loan_Amount` is skewed, which is visualized using both a distribution plot and a box plot to detect outliers.
  
### Bivariate Analysis
- Relationships between features like `Gender`, `Marital_Status`, `Dependents`, `Education`, `Employment_Type`, `Residential_Status`, `Loan_Type`, and `Loan_Status` were analyzed using stacked bar plots.

## Model Building

### Random Forest Classifier

1. **Splitting Data**:
   - The dataset was split into training, validation, and test sets using `train_test_split` with a 20% split for testing.
   
2. **Model Pipeline**:
   - A `Pipeline` was created with `OrdinalEncoder` for encoding categorical variables and `RandomForestClassifier` as the model.
   ```python
   RF_model = make_pipeline(
       OrdinalEncoder(),
       RandomForestClassifier(random_state=42)
   )
   ```
   - The model was trained on the training set and evaluated on the validation and test sets.

### Decision Tree Classifier

1. **Model Pipeline**:
   - A similar pipeline was created using `DecisionTreeClassifier`.
   ```python
   DT_model = make_pipeline(
       OrdinalEncoder(),
       DecisionTreeClassifier()
   )
   ```

## Model Evaluation

### Random Forest Classifier
- **Baseline Accuracy**: 0.66
- **Training Accuracy**: 1.0
- **Validation Accuracy**: 0.79
- **Testing Accuracy**: 0.79

### Decision Tree Classifier
- **Validation Accuracy**: 1.0
- **Training Accuracy**: 1.0
- **Test Accuracy**: Due to overfitting on training and validation set, testing on test set was not needed.

### Stratified K-Fold Cross Validation (Random Forest & Decision Tree)
- To address overfitting, Stratified K-Fold Cross Validation was used.


## Feature Importance

Feature importance was derived from the Random Forest model & Decision Tree model to identify the most impactful features:

A horizontal bar plot was used to visualize feature importance.

## Hyperparameter Tuning

Hyperparameter tuning was performed on both models using `GridSearchCV` to find the best parameters.

  
## Conclusion

- The RF model and DT model after stratified k fold validation followed by tuned hyperparameters provided a balanced performance with an accuracy of 0.80  and 0.85 respectively on the test set.
- Feature importance analysis highlighted the significance of `Term_of_Loan`, `Loan_Amount`, and `Applicant_Monthly_Income` in predicting loan approval.

- ## Note
- Still annotating data to improve model performance
