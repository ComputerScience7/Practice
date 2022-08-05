import pandas as pd
import plotly.express as px
import streamlit as st
import datetime

def app ():
    st.title('Welcome to Google Intellegence Political Ads')

    st.header('Choose the type of Ads you like')
    selected_radio = st.radio('Select', 
                            ['Text', 'Video', 'Image'])
    if selected_radio == 'Text':
        st.write('Very Popular and the cheapest')
    elif selected_radio == 'Video':
        st.write('Costly but Worth to try')
    else:
        st.write('Budget Friendly')  

    st.header('States')
    st.multiselect('Choose the States you want to choose for Advertisement',
        ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Washington, D.C.', 'Delaware', 'Florida',
         'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Massachusetts',
         'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'North Carolina', 'North Dakota', 'Nebraska',
         'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
         'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia',
         'Wyoming'])

    st.header('How many Days you want your ads to be posted')
    slide = st.slider('Choose', 0, 365)
    st.write(slide, 'Days')

    if st.button('Submit'):
        st.write('Your cost will be calculated soon')
        st.write('Please contact tony.amg78@gmail.com for further information')

        