# 📁 ML Project: Customer Churn Prediction for a Telecom Company

A machine learning project focused on predicting customer churn for a telecom company. The goal is to analyze customer behavior and build a robust machine learning model to identify customers who are likely to leave the service.

---

## 🚀 Features

* ✅ Data Collection and Preprocessing
* ✅ Exploratory Data Analysis (EDA)
* ✅ Feature Engineering and Selection
* ✅ Model Building and Evaluation
* �️ Deployment (**Coming Soon**)

---

## 📊 Dataset

* **Source:** [Kaggle – Customer Churn Dataset](https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction/input)

The dataset contains historical records of telecom customers, including their service usage, contract details, and churn labels.

---

## ✅ Exploratory Data Analysis & Modeling

### 📅 Exploratory Data Analysis (EDA)

* Performed using this notebook: [EDA Notebook →](notebook/eda_telecom(original_data).ipynb)
* Visualizations include: Countplots, Histograms, Boxplots, Correlation Heatmaps
* Insights on tenure, charges, and service usage
  
---

### 🎯 Machine Learning Model

* Built using: [Model Training Notebook →](notebook/model_training.ipynb)
* Models used: Logistic Regression, AdaBoost, GradientBoosting, Random Forest
* VotingClassifier used for ensembling

---


## 📈 Final Model Metrics

* **Accuracy:** `0.8043`

* **Confusion Matrix:**

  |            | Predicted No | Predicted Yes |
  | ---------- | ------------ | ------------- |
  | Actual No  | 1397         | 152           |
  | Actual Yes | 261          | 300           |

* **Classification Report:**

  | Class            | Precision | Recall | F1-Score | Support |
  | ---------------- | --------- | ------ | -------- | ------- |
  | 0                | 0.84      | 0.90   | 0.87     | 1549    |
  | 1                | 0.66      | 0.53   | 0.59     | 561     |
  | **Accuracy**     |           |        | 0.80     | 2110    |
  | **Macro Avg**    | 0.75      | 0.72   | 0.73     | 2110    |
  | **Weighted Avg** | 0.80      | 0.80   | 0.80     | 2110    |

* **ROC AUC Score:** `0.84`

&#x20;

---

## 📂 Project Structure

```bash
ml_project_customer_churn_prediction_telecom/
├── notebooks/
│   ├── eda_telecom.ipynb           # Step 02: Exploratory Data Analysis
│   ├── model_training.ipynb        # Step 03: Machine Learning Modeling
├── .gitignore
├── app.py                          # Deployment (Coming Soon)
├── README.md
├── requirements.txt
├── setup.py
└── src/
    ├── components/
    │   ├── data_ingestion.py
    │   ├── data_transformation.py
    │   ├── model_training.py
    ├── exception/
    ├── logging/
    ├── utils/
    └── pipeline/
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Tools:** Jupyter Notebook, Git

---

## 🔍 Step-by-Step Guide

### 🧪 Step 01: EDA & Modeling

* 📊 **[EDA Notebook](https://github.com/faisalmehmood2013/ml_project_customer_churn_prediction_telecom/blob/main/notebook/2_eda_telecom%28original_data%29.ipynb)**
* 🤖 **[Model Training Notebook](https://github.com/faisalmehmood2013/ml_project_customer_churn_prediction_telecom/blob/main/notebook/model_training.ipynb)**

---

## 📦 How to Run This Project

```bash
# Step 1: Clone the repo
git clone https://github.com/your-username/ml_project_customer_churn_prediction_telecom.git

# Step 2: Navigate to the directory
cd ml_project_customer_churn_prediction_telecom

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run notebooks for EDA and model training
jupyter notebook
```

---

## 🙏 Acknowledgments

> **Thanks** to *Zeeshan Ul Hassan Usmani Sir* for motivation and inspiration during the learning journey.

---

## 📌 Note

�️ **Deployment Coming Soon** – We are currently working on deploying the model using Flask or Streamlit.

---

## 🌟 Author

* **Name:** Faisal Mehmood
* **GitHub:** [@faisalmehmood2013](https://github.com/faisalmehmood2013)
* **Domain:** Data Science | Machine Learning | AI

---