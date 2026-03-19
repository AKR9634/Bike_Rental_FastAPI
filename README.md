# 🚴‍♂️ Bike Rental Demand Prediction API

### FastAPI • Machine Learning • Production-Ready

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Model-blue?style=for-the-badge&logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Status-Production--Ready-brightgreen?style=for-the-badge" />
</p>

---

## 📌 Overview

This project is a **production-ready FastAPI application** that predicts **bike rental demand** using Machine Learning models trained on real-world bike-sharing data.

Bike-sharing systems act as **urban mobility sensors**, capturing patterns influenced by:

* 🌦️ Weather conditions
* 📅 Seasonal trends
* 🏙️ Human activity patterns

👉 This API enables **real-time predictions** of bike rentals (`cnt`) based on these features.

---

## 🎯 Problem Statement

> Predict the total number of bike rentals (`cnt`) using environmental and temporal features.

### Type:

* 📈 **Supervised Learning**
* 🔢 **Regression Problem**

---

## 📊 Dataset Description

The dataset is based on the **Capital Bikeshare system (Washington D.C., USA)** covering years **2011–2012**.

### 📁 Files:

* `day.csv` → Daily aggregated data (731 records)
* `hour.csv` → Hourly aggregated data (17,379 records)

---

## 🧾 Feature Overview

| Feature      | Description                              |
| ------------ | ---------------------------------------- |
| `season`     | 1: Spring, 2: Summer, 3: Fall, 4: Winter |
| `yr`         | 0: 2011, 1: 2012                         |
| `mnth`       | Month (1–12)                             |
| `holiday`    | Holiday indicator                        |
| `weekday`    | Day of week                              |
| `workingday` | Working day indicator                    |
| `weathersit` | Weather condition (1–4)                  |
| `temp`       | Normalized temperature                   |
| `atemp`      | Feels-like temperature                   |
| `hum`        | Humidity                                 |
| `windspeed`  | Wind speed                               |
| `cnt`        | 🎯 Target: Total rentals                 |

---

## 🧠 Machine Learning Pipeline

* ✅ Data Cleaning & Preprocessing
* ✅ Feature Engineering
* ✅ Model Training
* ✅ Hyperparameter Tuning (GridSearchCV)
* ✅ Model Evaluation (RMSE, R²)
* ✅ Model Selection
* ✅ Model Serialization (`joblib`)

---

## 🤖 Models Used

* Linear Regression
* Decision Tree
* Random Forest 🌲
* Gradient Boosting 🚀 *(Best Performing)*
* Support Vector Machine (SVM)

---

## 📈 Performance Summary

| Model             | Performance       |
| ----------------- | ----------------- |
| Linear Regression | Baseline          |
| Decision Tree     | Overfitting prone |
| Random Forest     | Strong            |
| Gradient Boosting | ⭐ Best            |
| SVM               | Moderate          |

---

## 🚀 API Endpoints

### 🔮 Predict Bike Rentals

```http
POST /predict
```

#### 📥 Request Body

```json
{
  "season": 2,
  "yr": 1,
  "mnth": 6,
  "holiday": 0,
  "weekday": 3,
  "workingday": 1,
  "weathersit": 1,
  "temp": 0.6,
  "atemp": 0.58,
  "hum": 0.5,
  "windspeed": 0.2
}
```

#### 📤 Response

```json
{
  "prediction": 3450
}
```

---

### 📊 View Dataset (With Sorting)

```http
GET /data?sort_by=cnt&order=desc
```

#### Features:

* 🔽 Sort by column
* 🔼 Ascending / Descending
* 📄 Limit results

---

## 🛠️ Tech Stack

| Category         | Tools                   |
| ---------------- | ----------------------- |
| Backend          | FastAPI                 |
| ML               | Scikit-learn            |
| Data             | Pandas, NumPy           |
| Model Saving     | Joblib                  |
| UI (Optional)    | Streamlit               |
| Deployment Ready | Docker / AWS (Optional) |

---

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 🔹 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

### 🔹 5. Open API Docs

👉 http://127.0.0.1:8000/docs

---

## 💾 Model Persistence

The trained model is saved as:

```bash
best_bike_model.pkl
```

Load model:

```python
import joblib
model = joblib.load("best_bike_model.pkl")
```

---

## 📂 Project Structure

```bash
├── app/
│   ├── main.py
│   ├── schema.py
│   └── utils.py
├── model/
│   ├── training.py
│   └── best_bike_model.pkl
├── data/
│   └── day.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Key Insights

* 🌡️ Temperature significantly impacts demand
* 📅 Weekdays vs weekends show distinct usage patterns
* 🌧️ Weather conditions strongly affect rentals
* 📈 Demand shows seasonal trends

---

## 🔮 Future Enhancements

* ⏱️ Time-series forecasting (LSTM / ARIMA)
* 📊 Advanced feature engineering
* 🌐 Deployment on AWS / Docker
* 📱 Interactive dashboard (Streamlit)
* 📈 Real-time monitoring

---

## 📚 Citation

If you use this dataset, please cite:

> Fanaee-T, Hadi & Gama, Joao (2013)
> *Event labeling combining ensemble detectors and background knowledge*

---

## 👨‍💻 Author

**Developed by:** *Your Name*
📌 FastAPI • Machine Learning • Backend Systems

---

## ⭐ Support

If you found this project useful:

⭐ Star this repository
🔁 Share with others
🤝 Contribute improvements

---

<p align="center">
  Built with ❤️ using FastAPI & Machine Learning
</p>
