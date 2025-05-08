import streamlit as st
import pandas as pd
import joblib
import os

@st.cache_data
def load_data():
    """Load and cache the crime dataset."""
    try:
        df = pd.read_csv("rwanda_crime.csv")
        st.session_state['data_loaded'] = True
        return df
    except FileNotFoundError:
        st.error("❌ Error: 'rwanda_crime.csv' not found in the working directory.")
        st.session_state['data_loaded'] = False
        return None

@st.cache_resource
def load_model_assets():
    """Load and cache the prediction model and related assets."""
    try:
        model = joblib.load("crime_model.pkl")
        label_encoder = joblib.load("label_encoder.pkl")
        model_features = joblib.load("model_features.pkl")
        return {
            "model": model,
            "label_encoder": label_encoder,
            "model_features": model_features
        }
    except Exception as e:
        st.error(f"⚠️ Model loading error: {e}")
        st.warning("Prediction functionality will be disabled.")
        return None