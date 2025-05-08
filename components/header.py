import streamlit as st

def render_header():
    """Render the dashboard header with title and description."""
    st.markdown("""
        <div style="text-align: center; padding: 20px 0 30px 0;">
            <h1 style="font-size: 2.8rem; margin-bottom: 0; background: linear-gradient(90deg, #FFD700, #FFA500); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
               Rwanda AI Crime Prediction System
            </h1>
            <p style="font-size: 1.2rem; opacity: 0.8; max-width: 800px; margin: 10px auto 20px auto;">
                Interactive dashboard providing insights into crime patterns across Rwanda, powered by data analysis and AI predictions.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Dashboard tabs for future expansion
    tabs = st.tabs(["📊 Dashboard", "ℹ️ About", "📋 Documentation"])
    
    with tabs[1]:
        st.markdown("""
            ### About This Dashboard
            
            This dashboard provides comprehensive analytics on crime patterns in Rwanda,
            offering insights through interactive visualizations and predictive analytics.
            
            #### Data Sources
            
            The data presented in this dashboard is sourced from official Rwandan police records
            and has been processed to ensure accuracy and relevance.
            
            #### Predictive Model
            
            The crime prediction feature uses a machine learning model trained on historical data
            to predict potential crime types based on location and time variables.
        """)
        
    with tabs[2]:
        st.markdown("""
            ### Documentation
            
            #### Dashboard Features
            
            1. **Quick Stats**: Overview of key metrics
            2. **Visualizations**: Interactive charts showing crime patterns
            3. **Raw Data Explorer**: Access to the underlying dataset
            4. **AI Prediction**: Predictive analytics for crime types
            
            #### Using the Prediction Tool
            
            1. Select a province from the dropdown
            2. Enter the year for prediction
            3. Click the "Predict" button to get the AI-generated crime type prediction
        """)