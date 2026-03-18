# 🍽️ Restaurant Rating Prediction

## 📌 Project Overview
This project predicts restaurant ratings using machine learning based on features like location, cost, cuisines, and customer engagement.

---

## 📊 Dataset Features
- Votes
- Average Cost for Two
- Price Range
- City
- Cuisines
- Latitude & Longitude

---

## ⚙️ Data Preprocessing
- Removed irrelevant columns
- Handled missing values
- Converted categorical features:
  - Binary encoding (Yes/No → 0/1)
  - Multi-label encoding for cuisines
  - One-hot encoding for top cities
- Applied **log transformation** on Votes to handle skewness
- Standardized numerical features

---

## 🤖 Models Used
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## 📈 Results

| Model              | R² Score |
|-------------------|---------|
| Linear Regression | ~0.44   |
| Decision Tree     | ~0.27   |
| Random Forest     | ~0.60+  |

---

## 🧠 Key Insights
- Random Forest performed best due to ensemble learning
- Votes and cost are strong predictors
- Model performance is limited by missing real-world features like food quality and service

---

## 🚀 Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## 📌 Future Improvements
- Hyperparameter tuning
- Advanced feature engineering
- Use of Gradient Boosting models

---

## 📷 Sample Visualization
(Add screenshots of graphs here)

---

## 🔗 How to Run

```bash
pip install -r requirements.txt
jupyter notebook