import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

#############
# PAGE SETUP
#############
st.set_page_config(page_title="Fire Incidents in the Philippines",
                   page_icon=":bar_chart:", layout="wide")

# Set title
st.title(":bar_chart: Fire Incidents in the Philippines")
st.markdown("_Dashboard_")
st.markdown('<style>div.block-container{padding-top:70px;text-align:center}</style>', unsafe_allow_html=True)

# Function to load data
@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)
    return data

#############
# DATA LOADING
#############
df = load_data("C:\\MyCodes\PYTHON\CSDM_2_DASH_BOARD\cleaned_data_BFP_FIreIncidents2012-2016.csv")

# Data Preview
with st.expander("Data Preview"):
    st.dataframe(
        df,
        column_config={
            "YEAR": st.column_config.NumberColumn(format="%d")
            }
    )
# Custom CSS for flexible metrics
st.markdown("""
    <style>
    .metric-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
        width: 100%;
        padding: 10px;
        margin: 5px;
    }

    .metric-title {
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 5px;
    }
    .metric-value {
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to display metrics
def display_metrics():
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

    total_damages = df['ESTIMATED_DAMAGES'].sum()
    total_incidents = df['INCIDENTS'].sum()
    total_deaths = df['DEATHS'].sum()
    total_injuries = df['INJURIES'].sum()
    average_damages = df['ESTIMATED_DAMAGES'].mean()
    
    with col1:
        st.markdown(f"""
            <div class="metric-container">
                <div class="metric-title">Total Damages</div>
                <div class="metric-value">{total_damages:,.2f}</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="metric-container">
                <div class="metric-title">Total Incidents</div>
                <div class="metric-value">{total_incidents:,}</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class="metric-container">
                <div class="metric-title">Average Damages per Incident</div>
                <div class="metric-value">{average_damages:,.2f}</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
            <div class="metric-container">
                <div class="metric-title">Total Deaths</div>
                <div class="metric-value">{total_deaths:,}</div>
            </div>
        """, unsafe_allow_html=True)

    with col5:
         st.markdown(f"""
            <div class="metric-container">
                <div class="metric-title">Total Injuries</div>
                <div class="metric-value">{total_injuries:,}</div>
            </div>
        """, unsafe_allow_html=True)

display_metrics()

#############
# SIDE BAR AREA
#############
st.sidebar.header("_DASHBOARD_")
# Sidebar Introduction
st.sidebar.header("Introduction")
st.sidebar.write("""
Welcome to the Fire Incidents Dashboard. This dashboard provides insights into fire incidents that occurred in the Philippines from 2012 to 2016. 
You can filter the data by regions, provinces, and municipalities to get specific information. 
The visualizations include line charts, pie charts, bar charts, and bubble charts to help you understand the data better.
""")

# Multiselect for Region
regions = st.sidebar.multiselect('Select Regions', df['REGION'].unique())

# Multiselect for Province
if regions:
    province_options = df[df['REGION'].isin(regions)]['PROVINCE_FIRE_DISTRICT'].unique()
else:
    province_options = df['PROVINCE_FIRE_DISTRICT'].unique()

provinces = st.sidebar.multiselect("Select Provinces", province_options)

# Multiselect for Municipality
if provinces:
    municipality_options = df[df['PROVINCE_FIRE_DISTRICT'].isin(provinces)]['CITY_MUNICIPALITY'].unique()
else:
    municipality_options = df['CITY_MUNICIPALITY'].unique()

municipalities = st.sidebar.multiselect("Choose Municipalities", municipality_options)

# Filter the data based on Region, Province, and Municipality
if not regions and not provinces and not municipalities:
    filtered_df = df
elif regions and not provinces and not municipalities:
    filtered_df = df[df['REGION'].isin(regions)]
elif not regions and provinces and not municipalities:
    filtered_df = df[df['PROVINCE_FIRE_DISTRICT'].isin(provinces)]
elif regions and provinces and not municipalities:
    filtered_df = df[(df['REGION'].isin(regions)) & (df['PROVINCE_FIRE_DISTRICT'].isin(provinces))]
elif not regions and not provinces and municipalities:
    filtered_df = df[df['CITY_MUNICIPALITY'].isin(municipalities)]
elif regions and not provinces and municipalities:
    filtered_df = df[(df['REGION'].isin(regions)) & (df['CITY_MUNICIPALITY'].isin(municipalities))]
elif not regions and provinces and municipalities:
    filtered_df = df[(df['PROVINCE_FIRE_DISTRICT'].isin(provinces)) & (df['CITY_MUNICIPALITY'].isin(municipalities))]
else:
    filtered_df = df[(df['REGION'].isin(regions)) & (df['PROVINCE_FIRE_DISTRICT'].isin(provinces)) & (df['CITY_MUNICIPALITY'].isin(municipalities))]

#############
# CREATE CHARTS
#############
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    # Line chart of incidents over the years
    fig1 = px.line(filtered_df, x='YEAR', y='INCIDENTS',
                   title='Incidents Over the Years',
                   markers=True,
                   color='REGION', width=900)
    fig1.update_layout(title={'x': 0.3})
    st.write(fig1)

    # Pie chart of total incidents by selected regions
    with st.expander("Pie Chart: Total Incidents by Region"):
        if not regions:
            pie_data = df
        else:
            pie_data = df[df['REGION'].isin(regions)]
            
        fig4 = px.pie(pie_data, values='INCIDENTS', names='REGION',
                      title='Total Incidents by Region', width=600, height=600)
        fig4.update_layout(title={'x': 0.3})
        st.write(fig4)
    
    # Box plot of estimated damages by region 
    with st.expander("Box Plot: Estimated Damages by Region"):
        fig6 = go.Figure()

        for region in filtered_df['REGION'].unique():
            region_df = filtered_df[filtered_df['REGION'] == region]
            fig6.add_trace(go.Box(
                y=region_df['ESTIMATED_DAMAGES'],
                name=region,
                boxmean=True,
                line=dict(color='royalblue'),
                marker=dict(color='rgba(0,0,139,0.5)')
            ))

        fig6.update_layout(
            title='Estimated Damages by Region',
            xaxis_title='Region',
            yaxis_title='Estimated Damages',
            title_x=0.3
        )
        st.write(fig6)

with col2:
    # Bar chart of incidents by municipality
    fig2 = px.bar(filtered_df, x='CITY_MUNICIPALITY', y='INCIDENTS',
                  title='Incidents by Municipality',width=900,
                  color='CITY_MUNICIPALITY')
    fig2.update_layout(title={'x': 0.3})
    st.write(fig2)

    # Scatter plot with connecting lines for incidents vs. estimated damages
    with st.expander("Scatter Plot: Incidents vs. Estimated Damages"):
        fig5 = go.Figure(data=go.Scatter(
            x=df['INCIDENTS'],
            y=df['ESTIMATED_DAMAGES'],
            mode='lines+markers',
            marker=dict(color=df['YEAR'], colorscale='Viridis', showscale=True),
            line=dict(color='royalblue', width=2)
        ))
        fig5.update_layout(
            title='Incidents vs. Estimated Damages',
            xaxis_title='Incidents',
            yaxis_title='Estimated Damages',
            coloraxis_colorbar=dict(title="Year"),
            height=600,
            width=600,
            title_x=0.3
        )
        st.write(fig5)

    # Bubble chart of incidents by region and year
    with st.expander("Bubble Chart of Incidents by Region and Year"):
        fig8 = px.scatter(filtered_df

, x='YEAR', y='REGION', size='INCIDENTS', color='REGION',
                          title='Bubble Chart of Incidents by Region and Year', size_max=60)
        fig8.update_layout(title={'x': 0.3})
        st.write(fig8)
