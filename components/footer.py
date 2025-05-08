import streamlit as st
from datetime import datetime

def render_footer():
    """Render the dashboard footer."""
    current_year = datetime.now().year
    
    st.markdown("""
        <div class="footer">
            <div style="margin-bottom: 10px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-shield-check">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                    <path d="m9 12 2 2 4-4"></path>
                </svg>
                Rwanda Crime Analytics Dashboard {current_year} | v1.0.0
            </div>
            <div style="font-size: 0.75rem; opacity: 0.7;">
                Data is updated periodically. Last update: {current_year}-06-15
            </div>
            <div style="margin-top: 15px; font-size: 0.75rem; opacity: 0.7;">
                Created with 
                <span style="color: #FF4B4B;">❤</span> 
                using Streamlit by Group 4
            </div>
        </div>
    """.format(current_year=current_year), unsafe_allow_html=True)