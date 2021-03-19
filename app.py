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
    
    st.subheader('몇년도 이후 몇페이지 이상되는 책을 검색하고 싶은가요.')
    released_year = st.number_input('년도 입력', min_value=1800, max_value=2050)
    pages = st.number_input('페이지수 입력', min_value=10)
    order = 'asc'
    if st.checkbox("오름차순 / 내림차순") :
        order = 'desc'
    if st.button(' 검색 ') :
        st.success('검색되었습니다.')
     
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
            
                

                query = '''select * from books;'''         ## 쿼리의 데이터는 다 변수처리해서 한다. 하드코딩 방지.
                #변수 들어갈 자리는 %s 로 표현한다.
                #record = [ ('냐웅이', 1 ), ( '나비', 3 ), ('단비', 5) ]                #여러개 insert는 리스트..
                #print(record) 
               

                cursor.execute(query)    # select용
                #cursor.execute(query, record)              # 하나는 execute   , 여러개는 executemany , insert 용
                # insert 는 commit 을 해줘야한다.
                #connection.commit()             #insert용  , 데이터베이스에 반영하라!
                print('{}개 적용됨'.format(cursor.rowcount))   # insert 확인용

                # 4. 실행 후 커서에서 결과를 빼낸다.
                results = cursor.fetchall()               # select용     인서트에서는 필요가 없다.
                print('Connected to db : ', results )

                #  추가 작업 하고 싶은거  (책 제목 가져와보기)
                #for data in results :
                    #print(data[1])

                # 같은 쿼리문으로 다른 결과가 나온다 . 차이점 보기.
                
                #released_year = 2005
                #pages = 400
                param = (released_year, pages  )              # 콤마로 튜플 만들어줘야됨
                cursor = connection.cursor(dictionary = True)        # 딕셔너리 형식으로 나온다. 컬럼도 나옴.
                if order == 'asc' :
                    query = """ select title, released_year, pages
                            from books
                            where released_year > %s and pages > %s
                            order by released_year asc ; """
                else :
                    query = """ select title, released_year, pages
                            from books
                            where released_year > %s and pages > %s
                            order by released_year desc ; """
                cursor.execute(query, param)          
                results = cursor.fetchall()
                print(results)
                st.write(results)

                for data in results :
                    print(data['title'], data['released_year'])

        except Error as e :
            print('db관련 에러 발생', e)

        finally : 
            # 모든 데이터베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')       
                                                            




if __name__ == '__main__' :
    main()
