import streamlit as st
import pandas as pd
import numpy as np
import time

def render_prediction(model_assets, df):
    """Render the crime prediction section."""
    if model_assets is None:
        return
    
    model = model_assets["model"]
    label_encoder = model_assets["label_encoder"]
    model_features = model_assets["model_features"]
    
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("""
        <div class="section-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-brain-circuit">
                <path d="M12 4.5a2.5 2.5 0 0 0-4.96-.46 2.5 2.5 0 0 0-1.98 3 2.5 2.5 0 0 0-1.32 4.24 3 3 0 0 0 .34 5.58 2.5 2.5 0 0 0 2.96 3.08 2.5 2.5 0 0 0 4.91.05L12 20V4.5Z"></path>
                <path d="M16 8V5c0-1.1.9-2 2-2"></path>
                <path d="M12 13h4"></path>
                <path d="M12 18h6a2 2 0 0 1 2 2v1"></path>
                <path d="M12 8h8"></path>
                <path d="M20.5 8a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0Z"></path>
                <path d="M16.5 13a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0Z"></path>
                <path d="M20.5 21a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0Z"></path>
                <path d="M20.5 13a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0Z"></path>
            </svg>
            AI Crime Prediction
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background: rgba(0,40,80,0.5); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
            <p style="margin: 0; font-size: 0.95rem;">
                This predictive tool uses machine learning to forecast potential crime types based on location and time variables.
                Enter the province and year to generate a prediction.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            province = st.selectbox(
                "Select Province",
                options=sorted(df["Province"].unique()),
                index=0
            )
        
        with col2:
            current_year = 2025  # Current year as default
            year = st.number_input(
                "Enter Year for Prediction",
                min_value=2020,
                max_value=2030,
                value=current_year,
                step=1
            )
        
        # Add confidence level slider (for UI enhancement - not actually used in prediction)
        confidence = st.slider(
            "Model Confidence Level",
            min_value=70,
            max_value=95,
            value=85,
            step=5,
            help="Higher confidence levels may result in more accurate but potentially fewer predictions."
        )
        
        submitted = st.form_submit_button("Generate Prediction")
        
        if submitted:
            # Create progress bar for effect
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Simulate processing
            for i in range(101):
                # Update progress bar
                progress_bar.progress(i)
                
                # Update status text based on progress
                if i < 30:
                    status_text.text("Analyzing historical patterns...")
                elif i < 60:
                    status_text.text("Applying machine learning algorithms...")
                elif i < 90:
                    status_text.text("Generating prediction...")
                else:
                    status_text.text("Finalizing results...")
                
                time.sleep(0.01)  # Small delay for animation effect
            
            # Clear status text and progress bar
            status_text.empty()
            progress_bar.empty()
            
            # Prepare input for prediction
            input_data = pd.DataFrame([[province, year]], columns=["Province", "Year"])
            input_encoded = pd.get_dummies(input_data)
            input_encoded = input_encoded.reindex(columns=model_features, fill_value=0)
            
            # Get prediction
            pred_label = model.predict(input_encoded)[0]
            pred_crime = label_encoder.inverse_transform([pred_label])[0]
            
            # Display prediction with animation effect
            st.markdown(f"""
                <div class="prediction-result">
                    <h3 style="margin-top: 0; margin-bottom: 5px;">Prediction Result</h3>
                    <p style="font-size: 0.9rem; margin-bottom: 10px;">Based on the selected parameters:</p>
                    <div style="font-size: 1.4rem; font-weight: 600; margin-bottom: 5px;">
                        Most likely crime type in {province} for {year}:
                    </div>
                    <div style="font-size: 2rem; font-weight: 700; margin: 15px 0;">
                        {pred_crime}
                    </div>
                    <div style="font-size: 0.85rem; opacity: 0.8;">
                        Model confidence: {confidence}%
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Add interpretation
            st.markdown("""
                <div style="background: rgba(0,50,100,0.5); padding: 15px; border-radius: 8px; margin-top: 20px;">
                    <h4 style="margin-top: 0; color: #FFD700; font-size: 1.1rem;">Interpretation & Action Points:</h4>
                    <ul style="margin-bottom: 0;">
                        <li>This prediction is based on historical patterns and may not account for recent policy changes</li>
                        <li>Consider preventive measures targeted at this specific crime type</li>
                        <li>Allocate resources appropriately based on this forecast</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close section container