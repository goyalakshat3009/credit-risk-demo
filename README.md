# 💳 Credit Scoring Model using Machine Learning

## 📌 Overview

This project predicts an individual's **creditworthiness** using Machine Learning classification algorithms. The model analyzes financial and personal information to classify applicants as either **Good Credit Risk** or **Bad Credit Risk**, helping financial institutions make informed lending decisions.

The project includes data preprocessing, feature engineering, model training, evaluation, and deployment using **Flask**.

---

## 🚀 Features

* Data Cleaning & Preprocessing
* Feature Engineering
* Missing Value Handling
* One-Hot Encoding
* Standard Scaling
* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* Model Performance Comparison
* ROC-AUC Analysis
* Flask Web Application
* Ready for Deployment on Render

---

## 📂 Dataset

The dataset contains customer financial information, including:

* Age
* Annual Income
* Home Ownership
* Employment Length
* Loan Purpose
* Loan Grade
* Loan Amount
* Interest Rate
* Loan Percent Income
* Previous Default History
* Credit History Length

Target Variable:

* **0 → Good Credit Risk**
* **1 → Bad Credit Risk**

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* Joblib
* HTML
* CSS

---

## 🤖 Machine Learning Models

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

---

## 📊 Model Performance

| Model               | Accuracy   | Precision  | Recall     | F1 Score   | ROC-AUC    |
| ------------------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| Logistic Regression | 86.89%     | 76.99%     | 57.12%     | 65.59%     | 86.79%     |
| Decision Tree       | 89.03%     | -          | -          | -          | 84.76%     |
| Random Forest       | **93.45%** | **97.06%** | **72.21%** | **82.81%** | **92.88%** |

---

## 🏆 Best Model

The **Random Forest Classifier** achieved the best performance and was selected for deployment.

* Accuracy: **93.45%**
* Precision: **97.06%**
* Recall: **72.21%**
* F1 Score: **82.81%**
* ROC-AUC: **92.88%**

---

## 📁 Project Structure

```
credit-risk-demo/
│
├── app.py
├── model.pkl
├── requirements.txt
├── Procfile
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── credit_risk_dataset.csv
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-link>
```

Move into the project directory

```bash
cd credit-risk-demo
```

Create a virtual environment

```bash
python -m venv myenv
```

Activate the virtual environment

### Windows

```bash
myenv\Scripts\activate
```

### Linux / macOS

```bash
source myenv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📷 Application

The web application allows users to enter customer financial information and instantly predicts whether the customer is a **Good Credit Risk** or **Bad Credit Risk**, along with the prediction confidence.

---

## 📈 Future Improvements

* Hyperparameter Tuning
* XGBoost & LightGBM
* Explainable AI using SHAP
* Docker Deployment
* Cloud Deployment
* REST API Integration

---

## 👨‍💻 Author

**Akshat Goyal**

Machine Learning Enthusiast | Python Developer | Mathematics & Computing Student

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.
