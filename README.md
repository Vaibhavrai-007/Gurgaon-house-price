# Gurgaon Real Estate Price Predictor

An end-to-end Machine Learning web application that estimates residential property prices across 107 verified sectors in Gurgaon, India.

## Features
- **Accurate Valuations**: Powered by a trained Random Forest Regressor achieving **~89% $R^2$ Score** with a Mean Absolute Error (MAE) of **± ₹0.48 Cr**.
- **Interactive UI**: Clean, responsive single-screen dashboard built with Streamlit.
- **Detailed Insights**: Provides price in Crores, price in Lakhs, rate per sq. ft., and dynamic ±MAE valuation confidence bands.
- **Robust Pipeline**: End-to-end preprocessing with `ColumnTransformer` and `OneHotEncoder` handling categorical features and outliers.

---

## Tech Stack
- **Language**: Python 3.11+
- **Data Manipulation**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn, XGBoost
- **Web App**: Streamlit
- **Model Serialization**: Joblib

---

## Project Structure
```text
Gurgaon-house-price/
│
├── data/
│   └── gurgaon_properties.csv   # Cleaned dataset with 17,800+ listings
├── app.py                       # Streamlit web application
├── model_building.ipynb         # Data exploration, cleaning, and model training
├── model.pkl                    # Exported model pipeline & metadata
├── requirements.txt             # Python dependencies
├── run.bat                      # One-click Windows launcher
├── .gitignore                   # Ignored files (virtualenv, cache, checkpoints)
└── README.md                    # Project documentation
```

---

## Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Gurgaon-house-price.git
cd Gurgaon-house-price
```

### 2. Set up virtual environment & install dependencies
```bash
python -m venv .venv
.venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```

### 3. Launch the Application
- **Windows (One-Click)**: Double-click `run.bat`
- **Manual Command**:
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## Model Benchmark Summary

| Model | $R^2$ Score | MAE (Cr) |
| :--- | :---: | :---: |
| Linear Regression | 0.7993 | ₹0.92 Cr |
| XGBoost Regressor | 0.8579 | ₹0.73 Cr |
| **Random Forest Regressor** | **0.8889** | **₹0.48 Cr** |
