import deta
import os
import streamlit_authenticator as sa

conn = deta.Deta(os.environ["deta_key"])
db = conn.Base("auth")

def encodePassword(password):
    return sa.Hasher([password]).generate()[0]

def getUser(name):
    return db.get(name)

def fetchAllUsers():
    return db.fetch().items

def insertUser(name, username, password):
    return db.put({"key": username, "name": name, "password": encodePassword(password), "save": []})

def updateData(data, key):
    return db.update(data, key)