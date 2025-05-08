import streamlit as st
import pandas as pd
from datetime import datetime

def get_stats(df):
    """Calculate statistics from the dataset."""
    total_crimes = df['Number of Cases'].sum()
    unique_crimes = df["Crime Detail"].nunique()
    provinces = df["Province"].nunique() 
    
    # Find the province with most crimes
    province_crimes = df.groupby("Province")["Number of Cases"].sum()
    highest_crime_province = province_crimes.idxmax()
    highest_crime_count = province_crimes.max()
    
    # Get the most recent year in the dataset
    latest_year = df["Year"].max()
    
    return {
        "total_crimes": total_crimes,
        "unique_crimes": unique_crimes,
        "provinces": provinces,
        "highest_crime_province": highest_crime_province,
        "highest_crime_count": highest_crime_count,
        "latest_year": latest_year
    }

def render_quick_stats(df):
    """Render the quick statistics section."""
    stats = get_stats(df)
    
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("""
        <div class="section-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-bar-chart-3">
                <path d="M3 3v18h18"></path>
                <path d="M18 17V9"></path>
                <path d="M13 17V5"></path>
                <path d="M8 17v-3"></path>
            </svg>
            Key Crime Statistics
        </div>
    """, unsafe_allow_html=True)
    
    # Layout for stat cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Total Reported Crimes</div>
                <div class="stat-value">{stats["total_crimes"]:,}</div>
                <div style="color: #a3c2e3; font-size: 0.9rem;">Across all provinces</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Crime Categories</div>
                <div class="stat-value">{stats["unique_crimes"]}</div>
                <div style="color: #a3c2e3; font-size: 0.9rem;">Unique crime types</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Provinces Monitored</div>
                <div class="stat-value">{stats["provinces"]}</div>
                <div style="color: #a3c2e3; font-size: 0.9rem;">Geographic regions</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Highest Crime Area</div>
                <div class="stat-value" style="font-size: 1.5rem;">{stats["highest_crime_province"]}</div>
                <div style="color: #a3c2e3; font-size: 0.9rem;">{stats["highest_crime_count"]:,} reported cases</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)  # Close section container