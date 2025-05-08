import streamlit as st
from utils.data_loader import load_data, load_model_assets
from components.header import render_header
from components.quick_stats import render_quick_stats
from components.visualizations import render_visualizations
from components.data_explorer import render_data_explorer
from components.prediction import render_prediction
from components.footer import render_footer
from utils.styling import apply_styling

# Page Configuration
st.set_page_config(
    page_title="Rwanda Crime Dashboard",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom styling
apply_styling()

# Load data and model assets
df = load_data()
model_assets = load_model_assets()

if df is not None and model_assets is not None:
    # Render components
    render_header()
    render_quick_stats(df)
    render_visualizations(df)
    render_data_explorer(df)
    render_prediction(model_assets, df)
    render_footer()