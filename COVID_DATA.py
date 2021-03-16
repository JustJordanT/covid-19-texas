import pandas as pd
import streamlit as st
import ssl
import altair as alt
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

#fixes ssl issue
ssl._create_default_https_context = ssl._create_unverified_context



# Daily data
#Load Data
data_daily = pd.read_csv('https://api.covidtracking.com/v1/states/tx/daily.csv')
data_daily['datetime'] = data_daily['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
data_tx = data_daily.filter(['datetime', 'state', 'positive', 'hospitalizedCurrently', 'death', 'recovered'])



#Racial dataset for cases
#Load Data
#data_racial = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vR_xmYt4ACPDZCDJcY12kCiMiH0ODyx3E1ZvgOHB8ae1tRcjXbs_yWBOA4j4uoCEADVfC1PS2jYO68B/pub?gid=43720681&single=true&output=csv')
#data_racialTX = data_racial.loc[data_racial['State'] == 'TX' ]
#data_racialTX['Datetime'] = data_racialTX['Date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
#data_racialTX = data_racialTX.filter(['Datetime','Cases_White' , 'Cases_Black', 'Cases_LatinX', 'Cases_Asian'])
#Deaths
#data_racialTX_deaths = data_racialTX.filter(['Deaths_White','Deaths_Black','Deaths_LatinX','Deaths_Asian'])

#Cache


st.title("Covid-19 Dashboard For Texas")
st.markdown('The dashboard will visualize the 🔬 Covid-19 data in 🐮 Texas')
'![pic](https://www.dshs.texas.gov/uploadedImages/Content/Prevention_and_Preparedness/immunize/images/covid19-banner.jpg)'


st.markdown('Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.')


'## 🦠 COVID-19 Data'
'### ↖️ Check out the side bar to view the data, charts and, plots'
#st.area_chart(data_tx)
#st.area_chart(data_daily)
#'COVID-19 daily data for Texas'


#Sidebar
st.sidebar.title("Data-Set Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")
if st.sidebar.checkbox('Charts: Show Me The Data - "CSV Data-Set"'):
        '### Data for from an hisstorical basis'
        st.dataframe(data_tx, width=3000, height= 700)
if st.sidebar.checkbox('Plot: Positive to Recovered Cases Texas'):
    '### Positive to Recovered Cases Texas'
    'As we look at our scatter plot we are able to see that as we see the amount of cases rise, we are also see a rise in recovered cases as well'
    
    'Looking at the "hue" change we are able to see the breaking point for this data around the middle of 2020-06'
    ax = sns.relplot(x='datetime', y='positive', hue='recovered', data=data_tx)
    ax = ax.set_xticklabels(rotation=30)
    ax =ax.set_ylabels('Positive Cases in hundred thousands')
    st.pyplot(ax)
if st.sidebar.checkbox("Plot: 'Deaths' To 'Hospitalized Currently' Cases In Texas"):
    "### Plot: 'Deaths' To 'Hospitalized Currently' Cases In Texas"
    'When we take a look at the "deaths" we are spike in "deaths" almost 1 month after the initial spike of "positive" cases.'
    ax1 = sns.relplot(x='datetime', y='death', hue='hospitalizedCurrently',data=data_tx)
    ax1 = ax1.set_xticklabels(rotation=30)
    ax1 =ax1.set_ylabels('Current Death Counts')
    st.pyplot(ax1)


#st.vega_lite_chart(data_daily)


# select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
# if not st.sidebar.checkbox("Hide", True, key='1'):
#     if select=='Bar plot':
#             st.title("Selected Top 5 Cities")
#             fig = go.Figure(data=[
#             go.Bar(name='positive', x=data_tx['state'][:5], y=data_tx['positive'][:5]),
#             go.Bar(name='Recovered', x=data_tx['recovered'][:5], y=data_tx['recovered'][:5]),
#             go.Bar(name='Active', x=data_tx['hospitalizedCurrently'][:5], y=data_tx['death'][:5])])
#             st.plotly_chart(fig)



# 'Positive to Recovered Cases Texas'
# ax = sns.relplot(x='datetime', y='positive', hue='recovered', data=data_tx)
# ax = ax.set_xticklabels(rotation=30)
# ax =ax.set_ylabels('Positive Cases in hundred thousands')
# st.pyplot(ax)

# "'Deaths' To 'Hospitalized Currently' Cases In Texas"
# ax1 = sns.relplot(x='datetime', y='death', hue='hospitalizedCurrently',data=data_tx)
# ax1 = ax1.set_xticklabels(rotation=30)
# ax1 =ax1.set_ylabels('Current Death Counts')
# st.pyplot(ax1)

# "Current Cases by race."
# # ax2 = sns.relplot(x = 'Cases_Black', y = 'Cases_White',hue='Cases_LatinX',palette="ch:.25", data=data_racialTX)
# ax2 = sns.relplot(x = 'Datetime', y = 'Cases_White',hue='Cases_LatinX',palette="ch:.25", data=data_racialTX)
# ax2 = ax2.set_xticklabels(rotation=30)
# ax2 = ax2.set_yticklabels(rotation=-30)
# st.pyplot(ax2)

# st.dataframe(data_racialTX)

