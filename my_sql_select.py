import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time
import numpy as nu
import pandas as pd
import json




def my_sql_select() :

    column_list = ['title', 'author_fname', 'author_lname', 'released_year', 'stock_quantity', 'pages']

    selected_column_list = st.multiselect('컬럼을 선택하세요.', column_list)

    try :
        connection = mysql.connector.connect( host = 'database-1.coqni1q3jupc.us-east-2.rds.amazonaws.com',
                                            database = 'yhdb',
                                            user = 'streamlit',
                                            password = '1234' ) 

        if connection.is_connected():
            cursor = connection.cursor(dictionary = True)
            
            # 쿼리 만들어 실행

            if len(selected_column_list) == 0 :
            
                query = """ select * from books ; """
            else :
                column_str = ','.join(selected_column_list)
                #st.write(column_str)
                query = """select book_id, """ + column_str + ' from books;'
                
            #st.write(query)

            cursor.execute(query)
            
            #select이므로 fetchall() 한다

            results = cursor.fetchall()

            json_results = json.dumps(results)
            # st.write(type(json_results))    # 파이썬의 리스트+딕셔너리 조합을  => json 형식으로 바꾸는것

            # for row in results :
                # st.write(row)

            # 판다스 프레임으로 읽기               # 판다스 프레임으로 읽고 싶으면 꼭 json으로 바꿔줘라.
            df = pd.read_json(json_results)
            st.dataframe(df)

            

           


    except Error as e :
        print('DB관련 에러 발생',e)



    finally :
        cursor.close()
        connection.close()        

