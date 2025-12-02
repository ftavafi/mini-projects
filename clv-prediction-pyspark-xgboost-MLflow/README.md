# Customer Lifetime Value (CLV) Prediction – PySpark, ML, MLflow

This mini project predicts **customer lifetime value (CLV)** and **future revenue** for an online retail business using the **Online Retail II** dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii).

We treat CLV prediction as a regression problem: from each customer's historical transactions we estimate their future spending. The focus is on a realistic, production‑minded workflow using PySpark for feature engineering and a tree‑based model for prediction, tracked with MLflow.

## Tech Stack

- **PySpark** – data cleaning, aggregation, and feature engineering (RFM, tenure, product diversity, etc.)
- **pandas** – final feature table manipulation
- **scikit‑learn** – train/test split, metrics
- **Tree‑based regressor** (XGBoost or RandomForest, depending on environment)
- **MLflow** – experiment tracking and model logging
- **matplotlib / seaborn** – basic evaluation plots

## Project Structure

```text
clv-prediction-pyspark-xgboost-MLflow/
├── data/
│   └── online_retail_II.xlsx        # Raw dataset (not committed in public repos)
├── notebooks/
│   └── 01_clv_analysis.ipynb        # Main end‑to‑end CLV notebook
├── scripts/                         # (optional) helper scripts / Spark jobs
└── README.md
```

## How to Run

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate          # on macOS / Linux
pip install -r ../requirements.txt

jupyter notebook
```

Then open `notebooks/01_clv_analysis.ipynb` in your browser and run the cells top‑to‑bottom.

## Notebook Outline

The main notebook follows this flow:

1. **Introduction & Business Problem**
2. **Environment Setup & Imports**
3. **Spark Session & Data Loading**
4. **Data Cleaning & Basic EDA (PySpark)**
5. **Train / Prediction Window Definition (6‑month CLV target)**
6. **Feature Engineering (RFM & more)**
7. **Train/Test Split at Customer Level**
8. **Modeling CLV with a Tree‑Based Regressor + MLflow**
9. **Evaluation & Business Interpretation**
10. **Production Mindset & Next Steps**

This project is intentionally small and focused, designed as a portfolio‑friendly example of CLV modeling with PySpark and modern ML tooling.


