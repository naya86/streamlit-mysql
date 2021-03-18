import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time





## 파이썬은 mysql connector를 이용하여 mysql(현재 aws rds) 과 연결된다. 



def main():
    # title = st.text_input('책 제목 입력:')
    # author_fname = st.text_input('이름 입력:')
    # author_lname = st.text_input('성 입력:')
    # released_year = st.number_input('년도 입력')
    # stock_quantity = st.number_input('수량 입력')
    # pages = st.number_input('페이지 입력')

    
        
    # name = st.text_input('이름 입력')
    # birthdate = st.date_input('생년월일')
    # birthtime = st.time_input('시간 입력')
    
    
    if st.button(' 저장 ') :
        st.success('저장되었습니다.')
     
        try :
            # 커넥터로부터 커넥션을 받는다.
            connection = mysql.connector.connect( host = 'database-1.coqni1q3jupc.us-east-2.rds.amazonaws.com',
                                                database = 'yhdb',
                                                user = 'streamlit',
                                                password = '1234' ) 
        
            if connection.is_connected() :          
                
                db_info = connection.get_server_info()
                print('MySQL server version : ', db_info ) 

                # 2. 커서를 가져온다.
                
                cursor = connection.cursor()
                print(cursor)
                # 3. 우리가 원하는 실행 가능
                # cursor.execute( 'select database();' )    
            
                

                query = '''insert into cats4(name, age)
                                values (%s, %s);'''         ## 쿼리의 데이터는 다 변수처리해서 한다. 하드코딩 방지.
                #변수 들어갈 자리는 %s 로 표현한다.
                record = [ ('냐웅이', 1 ), ( '나비', 3 ), ('단비', 5) ]                #여러개 insert는 리스트..
                print(record)
               

                cursor.executemany(query, record)              # 하나는 execute   , 여러개는 executemany
                # insert 는 commit 을 해줘야한다.
                connection.commit()
                print('{}개 적용됨'.format(cursor.rowcount))

                # 4. 실행 후 커서에서 결과를 빼낸다.
                #record = cursor.fetchone()                       인서트에서는 필요가 없다.
                #print('Connected to db : ', record )

        except Error as e :
            print('db관련 에러 발생', e)

        finally : 
            # 모든 데이터베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')       
                                                            




if __name__ == '__main__' :
    main()
