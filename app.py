import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the app.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(os.path.join(working_dir, 'saved_models', 'diabetes_model.sav'), 'rb'))
heart_disease_model = pickle.load(open(os.path.join(working_dir, 'saved_models', 'heart_disease_model.sav'), 'rb'))
parkinsons_model = pickle.load(open(os.path.join(working_dir, 'saved_models', 'parkinsons_model.sav'), 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies (0-17)')

    with col2:
        Glucose = st.text_input('Glucose Level (0-199)')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value (0-122)')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value (0-99)')

    with col2:
        Insulin = st.text_input('Insulin Level (0-846)')

    with col3:
        BMI = st.text_input('BMI value (0-67.1)')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value (0.078-2.42)')

    with col2:
        Age = st.text_input('Age of the Person (21-81)')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex(0 - female / 1 - male)')

    with col3:
        cp = st.text_input('Chest Pain types(0-3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (in mm Hg)')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved (in bpm)')

    with col3:
        exang = st.text_input('Exercise Induced Angina (0 = no; 1 = yes)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0-3)')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect (0-2)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz) - Average vocal fundamental frequency')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz) - Maximum vocal fundamental frequency')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz) - Minimum vocal fundamental frequency')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%) - Percent jitter')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs) - Absolute jitter')

    with col1:
        RAP = st.text_input('MDVP:RAP - Relative Average Perturbation')

    with col2:
        PPQ = st.text_input('MDVP:PPQ - Pitch Period Perturbation')

    with col3:
        DDP = st.text_input('Jitter:DDP - DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer - Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB) - Shimmer in dB')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3 - APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5 - APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ - APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA - DDA')

    with col5:
        NHR = st.text_input('NHR - Noise to Harmonics Ratio')

    with col1:
        HNR = st.text_input('HNR - Harmonics to Noise Ratio')

    with col2:
        RPDE = st.text_input('RPDE - Recurrence Period Density Entropy')

    with col3:
        DFA = st.text_input('DFA - DFA')

    with col4:
        spread1 = st.text_input('spread1 - Spread1')

    with col5:
        spread2 = st.text_input('spread2 - Spread2')

    with col1:
        D2 = st.text_input('D2 - D2')

    with col2:
        PPE = st.text_input('PPE - PPE')

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result :"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
