import streamlit as st

def apply_styling():
    """Apply custom styling to the app."""
    st.markdown("""
        <style>
            /* Base styling */
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(135deg, #001429 0%, #002952 100%);
                color: #e5e5e5;
            }
            
            [data-testid="stHeader"] {
                background-color: rgba(0,0,0,0.2);
                backdrop-filter: blur(10px);
            }
            
            h1, h2, h3, h4, h5, h6 {
                color: #ffffff;
                font-weight: 600;
            }
            
            /* Card styling */
            .stat-card {
                background: linear-gradient(135deg, rgba(0,36,73,0.8) 0%, rgba(0,56,112,0.8) 100%);
                border-radius: 12px;
                padding: 20px;
                border-left: 4px solid #FFD700;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                height: 100%;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            
            .stat-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            }
            
            .stat-value {
                font-size: 2.2rem;
                font-weight: 700;
                color: #FFD700;
                margin: 10px 0;
            }
            
            .stat-label {
                font-size: 1rem;
                color: #a3c2e3;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            
            /* Section styling */
            .section-container {
                background: rgba(0,30,60,0.7);
                border-radius: 12px;
                padding: 25px;
                margin-bottom: 25px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.1);
            }
            
            .section-title {
                color: #FFD700;
                font-size: 1.5rem;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
            }
            
            .section-title svg {
                margin-right: 10px;
            }
            
            /* Form styling */
            [data-testid="stForm"] {
                background: rgba(0,40,80,0.7);
                border-radius: 12px;
                padding: 25px;
                border: 1px solid rgba(255,255,255,0.1);
            }
            
            [data-testid="stFormSubmitButton"] > button {
                background: linear-gradient(90deg, #FF4B4B 0%, #FF8080 100%);
                color: white;
                border-radius: 6px;
                padding: 8px 25px;
                font-weight: 600;
                border: none;
                transition: all 0.3s ease;
            }
            
            [data-testid="stFormSubmitButton"] > button:hover {
                background: linear-gradient(90deg, #FF6B6B 0%, #FFA0A0 100%);
                box-shadow: 0 4px 12px rgba(255,75,75,0.3);
            }
            
            /* Plot styling */
            [data-testid="stPlotlyChart"] {
                background: rgba(0,30,60,0.5);
                border-radius: 12px;
                padding: 10px;
                border: 1px solid rgba(255,255,255,0.05);
            }
            
            /* Dataframe styling */
            [data-testid="stDataFrame"] {
                background: rgba(0,30,60,0.5);
                border-radius: 8px;
            }
            
            [data-testid="stDataFrameResizable"] {
                border: 1px solid rgba(255,255,255,0.1);
            }
            
            /* Inputs styling */
            [data-testid="stSelectbox"], [data-testid="stNumberInput"] {
                margin-bottom: 15px;
            }
            
            /* Animation for prediction result */
            @keyframes highlight {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            .prediction-result {
                background: linear-gradient(270deg, #004080, #0060b6, #0080ff);
                background-size: 600% 600%;
                animation: highlight 8s ease infinite;
                color: white;
                padding: 20px;
                border-radius: 8px;
                text-align: center;
                margin-top: 20px;
                box-shadow: 0 4px 15px rgba(0,100,255,0.3);
            }
            
            /* Footer styling */
            .footer {
                text-align: center;
                padding: 20px;
                color: rgba(255,255,255,0.5);
                font-size: 0.85rem;
                margin-top: 30px;
            }
        </style>
    """, unsafe_allow_html=True)