import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="About Us",page_icon=":zap:",layout="wide")
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_coding=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_msdmfngy.json")
lottie_coding1=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_3JBIRr.json")
lottie_coding2=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jzpjbmvd.json")
st.subheader("Hi, We are Webpapt :wave:")
st.title("Your Security Is Our Priority")
st.write("Webpapt makes the internet safe ,secure, & simple")
st.write("---")
with st.container():
    left_column, right_column=st.columns(2)
    with left_column:
        st.subheader("About Us 🛈")
        st.write("Managing Password In One Place Will Save You A Lot Of Time And Hassle.You Need a Password Manager You Can Trust.")
        st.write("We The Creators Of Webpapt [Web Password Protector] Will Provide You A Safe And Secure Place To Store Your Password ")
        st.write("The Passwords Here Are Stored And Secured By Three Level Of Encryption. This Method Of Securing Passwords Can Be Preferred over Other Local Computer Application Due To The Exclusive Phenomenon Of Not Consuming Space In The Users Storage. Since The Host Of The Application Is The Local Host Itself It Will Prevent Cybertheft Of Your Data. As Aleady Mentioned Above The App Assures The Security Of User Data By Using Three Levels Of Encryption. ")
        st.write("We Provide The Users With An Amazing Interactive UI Which Helps The User To Secure Password More Easily.")
        st.write("Data Privacy Is A Human Right, And It Belongs To You.")
        st.write("---")
        st.subheader("Our Creators :v:")
        st.write("Vishwaa R")
        st.write("Danvanthram KK")
        st.write("Rohith Krishna")
with right_column:
    st_lottie(lottie_coding,height=300,key="coding")
    st_lottie(lottie_coding2,height=300)
