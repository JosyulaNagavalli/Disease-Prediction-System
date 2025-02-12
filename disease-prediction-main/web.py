import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Disease Prediction System',
                   layout='wide',
                   page_icon="⚕️")

st.markdown("<style>body { background-color: #e0f7fa; color: #333; }</style>", unsafe_allow_html=True)

diabetes_model = pickle.load(open(r"C:\Users\vigne\OneDrive\Desktop\Desktop_2\nothing\disease-prediction-main\training_modules\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\vigne\OneDrive\Desktop\Desktop_2\nothing\disease-prediction-main\training_modules\heart_model.sav", 'rb'))
parkinson_model = pickle.load(open(r"C:\Users\vigne\OneDrive\Desktop\Desktop_2\nothing\disease-prediction-main\training_modules\parkinson.sav", 'rb'))

st.sidebar.title("🔬 Disease Prediction System")
st.sidebar.markdown("Select a disease to predict from the options below:")

selected = st.sidebar.radio("Prediction Options", 
                            ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Disease Prediction'])

st.markdown("---")
if selected == 'Diabetes Prediction':
    st.header("🩸 Diabetes Prediction")
    st.markdown("Please enter the following details to check for diabetes:")
    
    cols = st.columns(4)
    Pregnancies = cols[0].number_input('Pregnancies', min_value=0, step=1)
    Glucose = cols[1].number_input('Glucose Level', min_value=0)
    BloodPressure = cols[2].number_input('Blood Pressure', min_value=0)
    SkinThickness = cols[3].number_input('Skin Thickness', min_value=0)
    
    cols = st.columns(4)
    Insulin = cols[0].number_input('Insulin Level', min_value=0)
    BMI = cols[1].number_input('BMI Value', min_value=0.0, format="%.1f")
    DiabetesPedigreeFunction = cols[2].number_input('Diabetes Pedigree Function', min_value=0.0, format="%.3f")
    Age = cols[3].number_input('Age', min_value=0, step=1)
    
    if st.button('🔍 Get Diabetes Prediction'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])
        diagnosis = "The person is diabetic" if diab_prediction[0] == 1 else "The person is not diabetic"
        st.success(diagnosis)

elif selected == 'Heart Disease Prediction':
    st.header("❤️ Heart Disease Prediction")
    st.markdown("Enter the following details to check for heart disease:")
    
    cols = st.columns(4)
    age = cols[0].number_input('Age', min_value=0, step=1)
    sex = cols[1].radio('Sex', ['Female', 'Male'])
    cp = cols[2].selectbox('Chest Pain Type (0-3)', list(range(4)))
    trestbps = cols[3].number_input('Resting BP (mm Hg)', min_value=0)
    
    cols = st.columns(4)
    chol = cols[0].number_input('Cholesterol Level', min_value=0)
    fbs = cols[1].radio('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])
    restecg = cols[2].selectbox('ECG Results', [0, 1, 2])
    thalach = cols[3].number_input('Max Heart Rate', min_value=0)
    
    cols = st.columns(4)
    exang = cols[0].radio('Exercise-Induced Angina', ['No', 'Yes'])
    oldpeak = cols[1].number_input('ST Depression', min_value=0.0, format="%.1f")
    slope = cols[2].selectbox('ST Slope', [0, 1, 2])
    ca = cols[3].selectbox('Major Vessels', [0, 1, 2, 3, 4])
    thal = st.selectbox('Thalassemia', [0, 1, 2, 3])
    
    if st.button('🔍 Get Heart Disease Prediction'):
        user_input = [age, 1 if sex == 'Male' else 0, cp, trestbps, chol, 1 if fbs == 'Yes' else 0,
                      restecg, thalach, 1 if exang == 'Yes' else 0, oldpeak, slope, ca, thal]
        heart_prediction = heart_disease_model.predict([user_input])
        diagnosis = "The person does not have heart disease" if heart_prediction[0] == 1 else "The person does not have heart disease"
        st.success(diagnosis)

elif selected == "Parkinson Disease Prediction":
    st.header("🧠 Parkinson's Disease Prediction")
    st.markdown("Enter the following voice analysis details to check for Parkinson's disease:")
    
    features_matrix = [
        ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)'],
        ['MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP'],
        ['MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer'],
        ['MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5'],
        ['MDVP:APQ', 'Shimmer:DDA', 'NHR'],
        ['HNR', 'RPDE', 'DFA'],
        ['Spread1', 'Spread2', 'D2'],
        ['PPE']
    ]
    
    user_input = []
    for row in features_matrix:
        cols = st.columns(len(row))
        for i, feature in enumerate(row):
            value = cols[i].number_input(feature, min_value=0.0, format="%.5f")
            user_input.append(value)
    
    if st.button("🔍 Get Parkinson's Prediction"):
        parkinsons_prediction = parkinson_model.predict([user_input])
        diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(diagnosis)

st.markdown("---")
st.markdown("🔹 **Disclaimer:** This is a predictive tool and should not be used as a substitute for professional medical diagnosis.")
