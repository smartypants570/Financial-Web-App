import streamlit as st
import pandas as pd
import os

folder_path = "data"
excel_file_path = "data/expense.csv"

if not os.path.exists(folder_path): # if no folder named data ,then make data folder
   os.makedirs(folder_path)

if not os.path.exists(excel_file_path): # if no file named expense.csv
      expenses = pd.DataFrame(columns=["Date","Category","Description","Currency Type","Amount"])
      expenses.to_csv("data/expense.csv",index=False)

def clear():
        st.session_state.am=0
        st.session_state.desc=""

def insert(date,category,description,currency_type,amount):

       dataframe = pd.read_csv(excel_file_path)
       length = len(dataframe)

       if description!="" and amount>0:

            dataframe.loc[length] = [date,category,description,currency_type,amount]

            dataframe.to_csv(excel_file_path,index=False)

            st.balloons()

       else:
            st.error('Please provide a description and a valid amount value greater than zero.', icon="🚨")

date = st.date_input('Date :date:',key="da")

category=st.selectbox("Category:card_index_dividers:",("Housing","Utilities","Transportation","Food","Healthcare","Insurance","DebtPayments","Entertainment","PersonalCare","Education","Savings","Taxes","Miscellaneous"),key="cat")

description=st.text_input('Description :flashlight:',key='desc')

currency_type = st.selectbox("Currency type :heavy_dollar_sign: /  :euro:",("Dollars","Euros"))

amount=st.number_input('Amount :money_mouth_face:',key='am',min_value=0,step=1,max_value=20000)

col1,col2 = st.columns([0.24,0.9])

with col1:
          add_button = st.button("Add Expense :money_with_wings:")
with col2:
          clear_button = st.button("Clear :scissors:",on_click=clear)


if  add_button:
      insert(date,category,description,currency_type,amount)

