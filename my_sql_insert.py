import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time
import numpy as nu
import pandas as pd
import json



def my_sql_insert():

    st.subheader('책 데이터 추가')


    title = st.text_input('제목을 입력하세요.')
    author_fname = st.text_input('작가의 성을 입력하세요.')
    author_lname = st.text_input('작가의 이름을 입력하세요.')
    released_year = st.number_input('책의 출간년도를 입력하세요.', min_value=1900, max_value=3000)
    stock_quantity = st.number_input('재고 입력하세요.', min_value=1)
    pages = st.number_input('페이지 정보 입력하세요.', min_value=1)

    save = st.button('저장하기')
    
    if save :
        st.success('저장되었습니다.')

        try :
            connection = mysql.connector.connect( host = 'database-1.coqni1q3jupc.us-east-2.rds.amazonaws.com',
                                                database = 'yhdb',
                                                user = 'streamlit',
                                                password = '1234' ) 
            
            if connection.is_connected :
                
                cursor = connection.cursor(dictionary= True)
                
                query = """ insert into books (title, author_fname, author_lname, released_year, stock_quantity, pages )
	                                 values ( %s, %s, %s, %s, %s, %s); """

                data = (title, author_fname, author_lname, released_year, stock_quantity, pages)

                cursor.execute(query, data)
                
                connection.commit()
                
                print('{}개 적용됨'.format(cursor.rowcount))

        except Error as e :
            print('db관련 에러 발생', e)

        finally : 
            # 모든 데이터베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')      

