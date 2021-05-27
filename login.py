import streamlit as st
import pandas as pd
import hashlib
import sqlite3
from pymongo import MongoClient
import dns
import stock
import myPortfolio
import glossary
import home
import login
import pymongo
import portfolio
import prediction
#import model
import streamlit as st

def app():
    client = MongoClient(
        'mongodb+srv://dbShreya:vuh42u4cNDnSlmFm@cluster0.gttk9.mongodb.net/Cluster0?retryWrites=true&w=majority')

    db = client.userData

    people = db.people

    def make_hashes(password):
        return hashlib.sha256(str.encode(password)).hexdigest()

    def check_hashes(password, hashed_text):
        if make_hashes(password) == hashed_text:
            return hashed_text
        return False

    def add_userdata(username, password, email):
        people.create_index([('Email', pymongo.DESCENDING)], unique=True)
        people.insert_one({'Username': username, 'Password': password, 'Email': email})

    def login_user(username, password, email):
        myquery = {"Username": username, "Password": password, 'Email': email}
        data = people.find_one(myquery)
        return data


    #st.title("Login")
    menu = ["Login", "SignUp"]
    choice = st.radio("Login or Create a New Account",menu)



    if choice == "Login":
        st.subheader("Login Section")

        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        new_email = st.text_input("Email-id")


        if st.checkbox("Login"):
            # if password == '12345':

            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd), new_email)
            if result:
                st.success("Logged In as {}".format(username))
                st.subheader("Great! Now you can access the entire site.")

                #task = st.sidebar.radio("Menu", ["Home", "Stock", "Portfolio","My Portfolio","Prediction","Glossary"])
                #if task == "Home":
                 #  st.subheader("HomePage")
                  # home.app()

                #elif task == "Stock":
                 #  st.subheader("Stocks")
                  # stock.app()

                #elif task == "Portfolio":
                 #  st.subheader("Portfolio")
                  # portfolio.app()

                #elif task == "My Portfolio":
                 #   st.subheader("Analytics")

                #elif task == "Prediction":
                 #   st.subheader("Analytics")

                #elif task == "Glossary":
                 #   st.subheader("Analytics")

                SecuredPages = {"Home": home, "Stock": stock, "Portfolio": portfolio,
                             "My Portfolio": myPortfolio, "Prediction":prediction,"Glossary": glossary}

                #st.title("Welcome to StockPro")
                #selection = st.sidebar.radio("Add-ons", list(SecuredPages.keys()))
                selection = st.sidebar.radio("Menu", list(SecuredPages.keys()))
                sec_page = SecuredPages[selection]
                sec_page.app()



            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
        new_email = st.text_input("Email-id")



        try:
            if st.button("Signup"):
                add_userdata(new_user, make_hashes(new_password), new_email)
                st.success("You have successfully created a valid Account")
                st.info("Go to Login Menu to login")
        except pymongo.errors.DuplicateKeyError:
            st.warning("This email-id is already in use. Create another one.")
        #else:
           # st.warning("This email-id is already in use. Create another one.")


