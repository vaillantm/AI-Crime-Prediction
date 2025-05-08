import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def create_crime_type_chart(df):
    """Create the crime type distribution chart."""
    # Get top 10 crime types
    crime_counts = df.groupby("Crime Detail")["Number of Cases"].sum().reset_index()
    crime_counts = crime_counts.sort_values("Number of Cases", ascending=False).head(10)
    
    # Custom color scale
    colors = px.colors.sequential.Blues[-10:]
    
    fig = px.bar(
        crime_counts, 
        x="Crime Detail", 
        y="Number of Cases",
        color="Number of Cases",
        color_continuous_scale=colors,
        title="Top Crime Types by Frequency"
    )
    
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=50, b=10),
        title_font=dict(size=20, color="#FFFFFF"),
        xaxis_title="Crime Type",
        yaxis_title="Number of Cases",
        xaxis=dict(showgrid=False, tickangle=30),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.1)"),
        coloraxis_showscale=False,
        hoverlabel=dict(bgcolor="rgba(0,30,60,0.8)", font_size=12),
    )
    
    # Add hover effect
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Cases: %{y:,}<extra></extra>",
        marker_line_width=0,
    )
    
    return fig

def create_time_trend_chart(df):
    """Create the crime over time chart."""
    crime_over_time = df.groupby("Year")["Number of Cases"].sum().reset_index()
    
    fig = go.Figure()
    
    # Add main line
    fig.add_trace(go.Scatter(
        x=crime_over_time["Year"],
        y=crime_over_time["Number of Cases"],
        mode="lines+markers",
        line=dict(color="#FFD700", width=4),
        marker=dict(size=10, color="#FFD700", line=dict(width=2, color="#000000")),
        name="Total Cases"
    ))
    
    # Add shaded area under the line
    fig.add_trace(go.Scatter(
        x=crime_over_time["Year"],
        y=crime_over_time["Number of Cases"],
        fill="tozeroy",
        fillcolor="rgba(255, 215, 0, 0.2)",
        line=dict(width=0),
        showlegend=False
    ))
    
    fig.update_layout(
        title="Crime Trend Over Years",
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=50, b=10),
        title_font=dict(size=20, color="#FFFFFF"),
        xaxis_title="Year",
        yaxis_title="Number of Cases",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.1)"),
        hoverlabel=dict(bgcolor="rgba(0,30,60,0.8)", font_size=12),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    # Add annotations for highest and lowest points
    highest_point = crime_over_time.loc[crime_over_time["Number of Cases"].idxmax()]
    lowest_point = crime_over_time.loc[crime_over_time["Number of Cases"].idxmin()]
    
    fig.add_annotation(
        x=highest_point["Year"],
        y=highest_point["Number of Cases"],
        text=f"Peak: {int(highest_point['Number of Cases']):,}",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#FFD700",
        arrowsize=1,
        arrowwidth=2,
        ax=40,
        ay=-40
    )
    
    fig.add_annotation(
        x=lowest_point["Year"],
        y=lowest_point["Number of Cases"],
        text=f"Low: {int(lowest_point['Number of Cases']):,}",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#FFD700",
        arrowsize=1,
        arrowwidth=2,
        ax=-40,
        ay=40
    )
    
    return fig

def create_province_chart(df):
    """Create the province distribution chart."""
    crime_by_province = df.groupby("Province")["Number of Cases"].sum().reset_index()
    crime_by_province = crime_by_province.sort_values("Number of Cases", ascending=True)
    
    colors = ["#001F3F", "#003366", "#004080", "#0059B3", "#0073E6", "#1A8CFF", "#4DA6FF", "#80BFFF"]
    if len(crime_by_province) > len(colors):
        # If we have more provinces than colors, just cycle through the colors
        colors = colors * (len(crime_by_province) // len(colors) + 1)
    
    colors = colors[:len(crime_by_province)]
    
    fig = go.Figure()
    
    # Add horizontal bars
    fig.add_trace(go.Bar(
        y=crime_by_province["Province"],
        x=crime_by_province["Number of Cases"],
        orientation='h',
        marker=dict(
            color=colors,
            line=dict(width=0)
        ),
        hovertemplate="<b>%{y}</b><br>Cases: %{x:,}<extra></extra>"
    ))
    
    # Add percentage labels
    total_cases = crime_by_province["Number of Cases"].sum()
    percentages = crime_by_province["Number of Cases"] / total_cases * 100
    
    for i, (province, cases, percentage) in enumerate(zip(
        crime_by_province["Province"],
        crime_by_province["Number of Cases"],
        percentages
    )):
        fig.add_annotation(
            x=cases,
            y=province,
            text=f"{percentage:.1f}%",
            showarrow=False,
            xanchor="left",
            xshift=10,
            font=dict(color="white", size=12)
        )
    
    fig.update_layout(
        title="Crime Distribution by Province",
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=50, b=10),
        title_font=dict(size=20, color="#FFFFFF"),
        xaxis_title="Number of Cases",
        yaxis_title="",
        xaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.1)"),
        yaxis=dict(showgrid=False),
        hoverlabel=dict(bgcolor="rgba(0,30,60,0.8)", font_size=12),
    )
    
    return fig

def render_visualizations(df):
    """Render the visualization section with charts."""
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("""
        <div class="section-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-bar-chart-3">
                <path d="M3 3v18h18"></path>
                <path d="M18 17V9"></path>
                <path d="M13 17V5"></path>
                <path d="M8 17v-3"></path>
            </svg>
            Crime Analytics
        </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for different visualizations
    viz_tabs = st.tabs(["📊 Crime Types", "📈 Time Trends", "🗺️ Geographic Distribution"])
    
    with viz_tabs[0]:
        crime_type_fig = create_crime_type_chart(df)
        st.plotly_chart(crime_type_fig, use_container_width=True)
        
        # Add analysis
        st.markdown("""
            <div style="background: rgba(0,40,80,0.5); padding: 15px; border-radius: 8px; margin-top: 15px;">
                <h4 style="margin-top: 0; color: #FFD700;">Key Insights:</h4>
                <ul style="margin-bottom: 0;">
                    <li>Certain crime types consistently appear more frequently in reports</li>
                    <li>Understanding the most common crimes helps in prioritizing preventive measures</li>
                    <li>Specialized enforcement teams may be needed for specific high-frequency crimes</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with viz_tabs[1]:
        time_trend_fig = create_time_trend_chart(df)
        st.plotly_chart(time_trend_fig, use_container_width=True)
        
        # Add analysis
        st.markdown("""
            <div style="background: rgba(0,40,80,0.5); padding: 15px; border-radius: 8px; margin-top: 15px;">
                <h4 style="margin-top: 0; color: #FFD700;">Trend Analysis:</h4>
                <ul style="margin-bottom: 0;">
                    <li>The chart reveals crime patterns over time, showing peaks and valleys</li>
                    <li>Year-over-year changes may correlate with policy implementations or socioeconomic factors</li>
                    <li>Understanding seasonal or annual patterns helps in resource allocation</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with viz_tabs[2]:
        province_fig = create_province_chart(df)
        st.plotly_chart(province_fig, use_container_width=True)
        
        # Add analysis
        st.markdown("""
            <div style="background: rgba(0,40,80,0.5); padding: 15px; border-radius: 8px; margin-top: 15px;">
                <h4 style="margin-top: 0; color: #FFD700;">Regional Insights:</h4>
                <ul style="margin-bottom: 0;">
                    <li>Crime distribution varies significantly by province</li>
                    <li>Population density and urbanization may correlate with higher crime rates</li>
                    <li>Regional differences suggest the need for tailored prevention strategies</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close section container