import streamlit as st
import pandas as pd
import os

folder_path = "data"
excel_file_path = "data/feedbacks.csv"

if not os.path.exists(folder_path):
   os.makedirs(folder_path)

if not os.path.exists(excel_file_path):
    dataframe = pd.DataFrame(columns=["Name","Feedback","Rating"])
    dataframe.to_csv(excel_file_path,index=False)

def Clear():
    st.session_state.nam=""
    st.session_state.fed=""

name=st.text_input("Enter your name",key="nam")
feedback=st.text_input("Enter your feedback",key="fed")
rating=st.slider("Provide a rating from a scale of 1 to 5",min_value=1,max_value=5,step=1,value=1)
if rating==1:
    st.subheader("We will improve a lot")
if rating==2:
    st.subheader("Thank you for your rating")
if rating==3:
    st.subheader("Thank you!! ")
if rating==4:
    st.subheader(" Very Very happy")
col1, col2 = st.columns([0.17, 0.9])
with col1:
    submit = st.button("Submit")
with col2:
    clear = st.button("Clear :scissors:", on_click=Clear)


def insert(path):
    dataframe = pd.read_csv(excel_file_path)
    length = len(dataframe)
    dataframe.loc[length] = [name, feedback, rating]
    dataframe.to_csv(excel_file_path, index=False)


def view(path):
    dataframe = pd.read_csv(excel_file_path)
    st.dataframe(dataframe)


if submit:
    insert(excel_file_path)
    st.success("Thank you for your valuable feedback.")

st.subheader("Past feedbacks")
view(excel_file_path)
