import streamlit as st
import pandas as pd

def render_data_explorer(df):
    """Render the raw data explorer section."""

    # ===== CUSTOM STYLES =====
    st.markdown("""
        <style>
            /* Title styling */
            .section-title {
                font-size: 24px;
                font-weight: bold;
                color: white;
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 20px;
            }

            /* Filter label text (multiselect labels) */
            label, .stCheckbox > label {
                color: white !important;
                font-weight: bold;
            }

            /* Download button styling */
            .stDownloadButton > button {
                background-color: #ff6666;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                font-weight: bold;
                transition: 0.3s;
            }
            .stDownloadButton > button:hover {
                background-color: #ff4d4d;
                cursor: pointer;
            }

            /* Cyan background for dataframe rows */
            .stDataFrame > div {
                background-color: #e0ffff;  /* light cyan */
            }
        </style>
    """, unsafe_allow_html=True)

    # ===== SECTION HEADER =====
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("""
        <div class="section-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" 
            viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" 
            stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-database">
                <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
                <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
                <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
            </svg>
            Data Explorer
        </div>
    """, unsafe_allow_html=True)

    # ===== FILTER OPTIONS =====
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_year = st.multiselect(
            "Filter by Year:",
            options=sorted(df["Year"].unique()),
            default=[]
        )

    with col2:
        selected_province = st.multiselect(
            "Filter by Province:",
            options=sorted(df["Province"].unique()),
            default=[]
        )

    with col3:
        selected_crime = st.multiselect(
            "Filter by Crime Type:",
            options=sorted(df["Crime Detail"].unique()),
            default=[]
        )

    # ===== APPLY FILTERS =====
    filtered_df = df.copy()

    if selected_year:
        filtered_df = filtered_df[filtered_df["Year"].isin(selected_year)]

    if selected_province:
        filtered_df = filtered_df[filtered_df["Province"].isin(selected_province)]

    if selected_crime:
        filtered_df = filtered_df[filtered_df["Crime Detail"].isin(selected_crime)]

    # ===== DISPLAY FILTERED TABLE =====
    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=400,
        column_config={
            "Number of Cases": st.column_config.NumberColumn("Number of Cases", format="%d"),
            "Year": st.column_config.NumberColumn("Year", format="%d"),
        },
        hide_index=True,
    )

    # ===== DOWNLOAD BUTTON =====
    if not filtered_df.empty:
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Filtered Data as CSV",
            data=csv,
            file_name="rwanda_crime_data_filtered.csv",
            mime="text/csv",
        )

    # ===== SUMMARY STATISTICS CHECKBOX & TABLE =====
    if st.checkbox("Show Summary Statistics"):
        st.markdown("<h4 style='color:white;'>Summary Statistics</h4>", unsafe_allow_html=True)
        numeric_cols = filtered_df.select_dtypes(include=['float64', 'int64'])
        st.dataframe(numeric_cols.describe())

    st.markdown('</div>', unsafe_allow_html=True)  # Close section container
