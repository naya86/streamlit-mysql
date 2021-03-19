import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time
from my_sql_select import my_sql_select  
from my_sql_insert import my_sql_insert
     
    
    
def main():    
    
    menu = ['SELECT', 'INSERT', 'UPDATE','DELETE']
    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == 'SELECT' : 
        my_sql_select()


    if choice == 'INSERT' :
        my_sql_insert()

    if choice == 'UPDATE' :
        pass
             
     






if __name__ == '__main__' :
    main()    