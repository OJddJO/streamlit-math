import streamlit as st
import streamlit_authenticator as sa
from PIL import Image
import deta
import os

#----------------------------------------------------------------------------------------------------------#
conn = deta.Deta(os.environ["deta_key"])
db = conn.Base("auth")

def encodePassword(password):
    return sa.Hasher([password]).generate()[0]

def insertUser(name, username, password):
    return db.put({"key": username, "name": name, "password": encodePassword(password), "save": []})
#----------------------------------------------------------------------------------------------------------#

icon = Image.open("icon.png")
st.set_page_config(page_title="Math", page_icon=icon, layout="wide", initial_sidebar_state="expanded")
st.title("Register")

def regPage():
    # main
    regContainer = st.form("register")
    username = regContainer.text_input(lg.username, key="username")
    password = regContainer.text_input(lg.password, type="password", key="password")

    # get all usernames to test if it already exists
    users = auth.fetchAllUsers()
    usernames = [user["key"] for user in users]

    if regContainer.form_submit_button(lg.register):
        name = username
        if username == "" or password == "":
            st.error("Please fill all the fields")
        elif username in usernames:
            st.error("This username is already used")
        else:
            st.success("You are now registered !")
            insertUser(name, username, password)

try:
    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        regPage()
    else:
        st.success("You are already logged in !")

except Exception as e:
    pass
