import streamlit as st
import streamlit_authenticator as sa
import deta
import os
from PIL import Image

#---------------------------------------------------------------------------------------------------------#
conn = deta.Deta(os.environ["deta_key"])
db = conn.Base("auth")

def getUser(name):
    return db.get(name)

def fetchAllUsers():
    return db.fetch().items
#---------------------------------------------------------------------------------------------------------#

icon = Image.open("icon.png")
st.set_page_config(page_title="Math", page_icon=icon, layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 350px !important;
        }
        .css-1i2wz1k {
            width: 0 !important;
            height: 0 !important;
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-1cypcdb.eczjsme11 > div:nth-child(2) > div {
            width: 0 !important;
            height: 0 !important;
        }
        .css-1oe5cao {
            max-height: 100% !important;
        }
        .css-40ynm6 {
            width: 0 !important;
            height: 0 !important;
        }
        .css-912zdv {
            width: 0 !important;
            height: 0 !important;
            display: none !important;
        }
        .css-1pxazr7 {
            width: 0 !important;
            height: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# authentication
get_users = fetchAllUsers()
users = [user["key"] for user in get_users]
names = [user["name"] for user in get_users]
passwords = [user["password"] for user in get_users]
st.session_state.authenticator = sa.Authenticate(names, users, passwords, "streamlit-math", "secret")

st.session_state.name, authenticationStatus, username = st.session_state.authenticator.login("Login", "main")

if authenticationStatus == False:
    st.error("Username/Password incorrect")
if authenticationStatus == None:
    st.warning("Please enter your username and password")
if authenticationStatus == True:
    st.success(f"Logged in as {st.session_state.name}")
    st.session_state.authenticator.logout(lg.logout, "sidebar")
