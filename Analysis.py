from asyncore import write
import streamlit as st
import numpy as np

def app ():
    st.title ('Analysis')

    st.header ('2018-2022 Google ads analytical ')
    st.subheader ('The best choice for political ads')
    st.write ('As a Data scientist we need to determine which type of ads will be the most efficient to use in USA')

    st.header ('Descriptive Statistics')
    st.subheader ('This graphs shows that the comparison between text and video ads')

    st.write ('Average daily cost each ads')
    st.image ('output.png')
    st.write ('Conclusion ')
    st.write ('Average 4 years cost of Text ads is significantlly cheaper than VIDEO,Average daily cost of Text ads is significantlly more expensive than VIDEO')
    st.write('We can concluded that surprisingly for daily ads Text is more expensive than Video, but for longer term Text is cheaper') 
    st.write('Video is the most expensive')
  

    st.header ('Inferential Statistics')
    st.subheader ('Hypotesis Testing')
    st.write ('H0 = There is a significant different of cost of Video advertisement and Text in daily basis for advertisement ')
    st.write ('Hypotesis is fail to reject because there was not a signficant different between text and video in daily cost')
    st.write ('Also it can be found that the average cost of Text and Video advertisements are very similar')

    st.image ('Finalresult.png')
    st.write('In conclusion There are multiple options people can use to advertise through Google Ads, it is clear that Text is the cheapest but have very less impressions according to the data. It means people just see the text and view it only couple seconds and they also not get the message of the advertisement. The purpose of ads are to influence people mind or behaviour to vote what they offer. Eventhough Video Average cost more for text around $42,828')


    st.write('Any Feedback?')
    st.write('Please contact my email at Tony.amg78@gmail.com')
    st.write('Thank You')