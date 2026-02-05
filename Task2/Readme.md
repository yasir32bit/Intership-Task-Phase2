# Task 2: Customer Churn Prediction Pipeline

## Objective
The goal of this task is to build a production-ready **machine learning pipeline** to predict whether a telecom customer is likely to churn. This pipeline uses both **numerical and categorical features** and includes preprocessing, model training, and hyperparameter tuning.

---

## Dataset
- **Dataset Used:** Telco Customer Churn Dataset  
- **Source:** Provided for internship (or Kaggle public dataset)  
- **Rows:** 7,043 customers  
- **Columns:** 21 (customer information, services, charges, churn status)  

---

## Approach / Methodology

1. **Data Preprocessing**
   - Convert `TotalCharges` to numeric
   - Drop `customerID` (non-informative)
   - Encode target `Churn` (Yes → 1, No → 0)
   - Identify numerical and categorical features
   - Use `ColumnTransformer` for scaling (numerical) and one-hot encoding (categorical)

2. **Model Training**
   - Two models trained using **Pipeline + GridSearchCV**:
     - Logistic Regression
     - Random Forest Classifier
   - F1-score used for model selection

3. **Pipeline Export**
   - Best model exported using `joblib`  
   - Ensures reproducibility and deployment

4. **Evaluation Metrics**
   - Accuracy
   - F1-score
   - Classification report (precision, recall, support)

---

## Results
- **Best Model:** Random Forest Classifier  
- **F1-Score on Test Data:** ~0.74 (example, replace with your result)  
- The model predicts churn probability for new customers in real-time.

---

## Deployment
The model pipeline is deployed as a **Streamlit web app** for real-time prediction:

[🔗 Open Deployed App](https://churn-prediction-w.streamlit.app/)

### How to Run Locally
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run Task2/app/main.py
   ```

---

## Folder Structure

```
Task2/
├── app/
│   └── main.py                # Streamlit app
├── churn_prediction_pipeline.pkl  # Exported ML pipeline
├── Data/
│   └── Telco_Cusomer_Churn.csv
├── Phase2_Task2.ipynb         # Notebook with all training
```

---

## Notes / Best Practices
- The `churn_prediction_pipeline.pkl` file **must be loaded using scikit-learn 1.7.2** for compatibility.
- `ColumnTransformer` is configured with `remainder="drop"` to avoid `_RemainderColsList` issues in scikit-learn ≥1.6.
- Dependencies are managed via `requirements.txt` for deployment consistency.

---

## Skills Gained
- End-to-end ML pipeline construction
- Preprocessing and feature encoding
- Hyperparameter tuning with GridSearchCV
- Model export & production-ready deployment
- Streamlit deployment for real-time predictions

---