import pickle
import streamlit as st
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Loading the saved model
heart_disease_model = pickle.load(open("C:/Users/SivaRanjan.s/Downloads/uci-heart-disease/uci-heart-disease/heart_disease_model.sav", 'rb'))

# Heart Disease Prediction Page
st.title('Heart Disease Prediction')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')

with col2:
    sex = st.text_input('Sex')

with col3:
    cp = st.text_input('Chest Pain types')

with col1:
    trestbps = st.text_input('Resting Blood Pressure')

with col2:
    chol = st.text_input('Serum Cholestoral in mg/dl')

with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
    restecg = st.text_input('Resting Electrocardiographic results')

with col2:
    thalach = st.text_input('Maximum Heart Rate achieved')

with col3:
    exang = st.text_input('Exercise Induced Angina')

with col1:
    oldpeak = st.text_input('ST depression induced by exercise')

with col2:
    slope = st.text_input('Slope of the peak exercise ST segment')

with col3:
    ca = st.text_input('Major vessels colored by flourosopy')

with col1:
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

# Convert inputs to numeric values
try:
    # Check if the input is not empty before converting to float
    if age:
        age = float(age)
    if sex:
        sex = float(sex)
    if cp:
        cp = float(cp)
    if trestbps:
        trestbps = float(trestbps)
    if chol:
        chol = float(chol)
    if fbs:
        fbs = float(fbs)
    if restecg:
        restecg = float(restecg)
    if thalach:
        thalach = float(thalach)
    if exang:
        exang = float(exang)
    if oldpeak:
        oldpeak = float(oldpeak)
    if slope:
        slope = float(slope)
    if ca:
        ca = float(ca)
    if thal:
        thal = float(thal)

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction with a unique key
    if st.button('Heart Disease Test Result', key='heart_diagnosis_button'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if heart_prediction[0] == 0:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

        st.success(heart_diagnosis)

except ValueError as e:
    st.error(f"Error: {e}. Please enter valid numeric values for the input features.")
