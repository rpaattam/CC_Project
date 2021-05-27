import portfolio
import stock
import myPortfolio
import glossary
import home
import login
import streamlit as st
from PIL import Image



#Pages = {"Home": home,"Login": login5, "Stock": stock, "Portfolio": portfolio,
             #        "My Portfolio": myPortfolio "Stock": stock,  "Glossary": glossary}

image5 = Image.open("C:\\Users\\Rose\\Desktop\\SEM 2 MSC BDA\\Cloud Computing\\Project\\ccprojimg7.jpg")
st.sidebar.image(image5, use_column_width=True)

Pages = {"Home": home,"Login": login, "Stock": stock,  "Glossary": glossary}

#st.title("Welcome to StockPro")
#selection = st.sidebar.radio("Menu", list(Pages.keys()))
selection = st.selectbox("Menu", list(Pages.keys()))
page = Pages[selection]
page.app()