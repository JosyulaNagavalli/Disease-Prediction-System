# 🏥 Disease Prediction System

## 📌 Overview
This is a **machine learning-based disease prediction system** that predicts whether a person has **Diabetes, Heart Disease, or Parkinson’s Disease** based on user input. The system is built using **Streamlit** for the frontend and **ML models** for prediction.

---

## 📁 Project Structure
disease_prediction/ │── datasets/ # Contains datasets used for training │ ├── diabetes.csv │ ├── heart.csv │ ├── parkinsons.csv │── training_modules/ # Trained ML models stored as .sav files │ ├── diabetes_model.sav │ ├── heart_model.sav │ ├── parkinson.sav │── web.py # Main Streamlit application │── README.md # Project documentation │── requirements.txt # Dependencies

yaml
Copy
Edit

---

## 🛠️ Technologies Used
- **Python 🐍**
- **Streamlit** (for UI)
- **Scikit-learn** (for model training)
- **Pandas & NumPy** (for data processing)
- **Pickle** (for model storage)

---

## ⚡ Features
✔ **Predicts Diabetes, Heart Disease, and Parkinson’s Disease**  
✔ **User-friendly Streamlit interface**  
✔ **Models trained on real-world datasets**  
✔ **Fast and accurate results**  

---

## 🚀 How to Run

### 1️⃣ Clone the repository:
sh
git clone https://github.com/Akshitha-Mothkur/disease-prediction.git
cd disease-prediction
2️⃣ Install dependencies:
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the application:
sh
Copy
Edit
streamlit run web.py
4️⃣ Enter the required details and get predictions!
📊 How It Works
User inputs health parameters
Pre-trained ML models process the data
Prediction is displayed on the UI
🏗 Future Improvements
✅ Add more diseases
✅ Improve accuracy with advanced models
✅ Deploy on cloud platforms
