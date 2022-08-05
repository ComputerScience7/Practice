import streamlit as st
import numpy as np
import pandas as pd

def app ():
    st.title ('Data Visualization')
    st.write ('This is Page For Data Visualization Dashboard')

    data = pd.read_csv('Google_ads.csv')
    if st.checkbox('Show Data'):
        st.subheader('Data')
        st.write (data)

    st.header ('Most Popular Google Type of Ads')
    st.image ('popularads.png')
    st.write('Text is the most type of ads people usually buy, followed by Video and Image which very similar')

    st.header ('Average Duration of Ads from 2018-2022 in number of Days')
    st.image ('Durationads.png')
    st.write('It is fluctuative for the last 4 years, with average for 25 days')


    st.header ('Ads Distributions and Impressions')
    st.image ('Piecharts.png')
    st.write('From the Pie Chart it can be concluded that the distribution of ads in USA is quite equal around 14 %')
    st.write('From the Graph chart it can be inferred that only 51 ads have the most impression to audience which approximately around 800000-900000 While most of the ads 74083 show very unsignificant impression to audience which approximately around 0-1000')


    st.header ('Average Ads Costs')
    st.image ('Averagecost.png')
    st.write('Based on data above it can be concluded that Video average spending around $ 40,000 followed by Text around $ 28,000 and Image Are the cheapest among all of them which cost less than $5000 ')
    