import streamlit as st
from PIL import Image


def app():
    st.title("Welcome to StockPro!!")

    st.subheader("Know all about the stocks that you're interested in, create portfolios and also get a predicted trend of the stock prices!!")

    st.write("   ")
    image = Image.open("C:\\Users\\Rose\\Desktop\\SEM 2 MSC BDA\\Cloud Computing\\Project\\ccprojimg1.jpg")
    st.image(image, use_column_width=True)
    st.text("   ")



    st.subheader("And much more! Sign-in to access all the features!")



