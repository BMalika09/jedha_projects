import streamlit as st
import pandas as pd



st.title("Dashboard for GetAround")

tab1, tab2 = st.tabs(["EDA", "Threshold"])

with tab1:
    try:
        import page1  
        page1.run_page() 
    except Exception as e:
        st.error(f"Erreur lors de l'importation de page1: {e}")

with tab2:
    try:
        import page2  
        page2.run_page()  
    except Exception as e:
        st.error(f"Erreur lors de l'importation de page2: {e}")
