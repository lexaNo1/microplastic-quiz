import pandas as pd
import numpy as np
import streamlit as st
import joblib
model = joblib.load("model.pkl")

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'intro'

if 'intrebare' not in st.session_state:
    st.session_state.intrebare = 1

if st.session_state.pagina == 'intro':
    st.title("Microplastic Bioaccumulation Assessment Tool")
    st.markdown("""
    This assessment aims to provide the most accurate possible estimate of microplastic bioaccumulation levels in the respondent's body, based on individual lifestyle and environmental exposure factors.
    It should be noted that this tool has inherent limitations, as it is derived from existing scientific literature rather than direct clinical biomonitoring data. Results should be interpreted as indicative estimates, not clinical diagnoses.""")
    
    if st.button("start assessment"):
        st.session_state.pagina = 'intrebari'
        st.rerun()

if st.session_state.pagina == 'intrebari':
    st.title(f"Question {st.session_state.intrebare} of 12")
    
    if st.session_state.intrebare ==1:
        st.write("What is your age?")
        varsta = st.number_input("Age", min_value=1, max_value=120)
        
        if st.button("Next"):
            st.session_state.varsta = varsta
            st.session_state.intrebare = 2
            st.rerun()


    if st.session_state.intrebare == 2:
        st.write("What is your primary source of drinking water?")
        apa = st.radio("Select one:", [
            "Tap water",
            "Filtered water",
            "Bottled water"
        ])
        if st.button("Next"):
            st.session_state.apa = apa
            st.session_state.intrebare = 3
            st.rerun()


    if st.session_state.intrebare == 3:
        st.write("How often do you consume processed food packaged in plastic?")
        alimente = st.radio("Select one:", [
            "Never",
            "Once a week",
            "3 times a week",
            "5 times a week",
            "Every day"
        ])
        if st.button("Next"):
            st.session_state.alimente = alimente
            st.session_state.intrebare = 4
            st.rerun()

    if st.session_state.intrebare == 4:
        st.write("How many portions of fish or seafood do you consume per week?")
        peste = st.number_input("Portions per week", min_value=0, max_value=30)
        if st.button("Next"):
            st.session_state.peste = peste
            st.session_state.intrebare = 5
            st.rerun()

    if st.session_state.intrebare == 5:
        st.write("How often do you use plastic containers for food or drinks?")
        recipiente = st.radio("Select one:", [
            "Never",
            "Once a week",
            "3 times a week",
            "5 times a week",
            "Every day"
        ])
        if st.button("Next"):
            st.session_state.recipiente = recipiente
            st.session_state.intrebare = 6
            st.rerun()

    if st.session_state.intrebare == 6:
        st.write("What percentage of your wardrobe consists of synthetic clothing?")
        haine = st.slider("Percentage (%)", min_value=0, max_value=100)
        if st.button("Next"):
            st.session_state.haine = haine
            st.session_state.intrebare = 7
            st.rerun()

    if st.session_state.intrebare == 7:
        st.write("What type of area do you live in?")
        zona = st.radio("Select one:", [
            "Rural",
            "Urban",
            "Industrial"
        ])
        if st.button("Next"):
            st.session_state.zona = zona
            st.session_state.intrebare = 8
            st.rerun()

    if st.session_state.intrebare == 8:
        st.write("What is your primary work environment?")
        munca = st.radio("Select one:", [
            "Office",
            "Factory/Industrial",
            "Outdoors",
            "Home"
        ])
        if st.button("Next"):
            st.session_state.munca = munca
            st.session_state.intrebare = 9
            st.rerun()

    if st.session_state.intrebare == 9:
        st.write("How many hours per day do you spend indoors?")
        interior = st.number_input("Hours per day", min_value=0, max_value=24)
        if st.button("Next"):
            st.session_state.interior = interior
            st.session_state.intrebare = 10
            st.rerun()

    if st.session_state.intrebare == 10:
        st.write("What type of salt do you primarily use?")
        sare = st.radio("Select one:", [
            "Regular salt",
            "Sea salt"
        ])
        if st.button("Next"):
            st.session_state.sare = sare
            st.session_state.intrebare = 11
            st.rerun()

    if st.session_state.intrebare == 11:
        st.write("Do you smoke?")
        fumat = st.radio("Select one:", [
            "No",
            "Occasionally",
            "Yes"
        ])
        if st.button("Next"):
            st.session_state.fumat = fumat
            st.session_state.intrebare = 12
            st.rerun()

    if st.session_state.intrebare == 12:
        st.write("How often do you use personal care products (cosmetics, creams, scrubs)?")
        cosmetice = st.radio("Select one:", [
            "Never",
            "Once a week",
            "3 times a week",
            "5 times a week",
            "Every day"
        ])
        if st.button("Submit"):
            st.session_state.cosmetice = cosmetice
            st.session_state.pagina = 'rezultat'
            st.rerun()

if st.session_state.pagina == 'rezultat':
    st.title("Your Results")


    input_data = pd.DataFrame({
        "varsta": [st.session_state.varsta],
        "sursa_de_apa": [st.session_state.apa],
        "alimente_procesate":[st.session_state.alimente],
        "peste_sau_fructe_de_mare":[st.session_state.peste],
        "recipiente_de_plastic":[st.session_state.recipiente],
        "haine_sintetice":[st.session_state.haine],
        "tipul_zonei":[st.session_state.zona],
        "mediul_de_lucru":[st.session_state.munca],
        "ore_petrecute_in_interior":[st.session_state.interior],
        "tipul_de_sare":[st.session_state.sare],
        "fumatul":[st.session_state.fumat],
        "cosmetice":[st.session_state.cosmetice]
    })

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

    rezultat = model.predict(input_data)[0]
    st.metric("Estimated microplastics in your body", f"{rezultat:.2f} mg/year")