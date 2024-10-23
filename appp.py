import streamlit as st
import joblib
import sklearn
st.title('Price Predictor')
st.image('_img.jpeg')

House_size=st.number_input("please enter size of the house")
Bedrooms=st.number_input("please enter no of bedrooms")

model1=joblib.load("mul_lin_app.pkl")

if st.button('predict'):
    output=model1.predict([[House_size,Bedrooms]])
    st.write(f"the Price of the house is {output[0]}")

