import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time




def main() :
    


    book_id_list = []
   
    try :
        connection = mysql.connector.connect( host = 'database-1.coqni1q3jupc.us-east-2.rds.amazonaws.com',
                                            database = 'yhdb',
                                            user = 'streamlit',
                                            password = '1234' ) 

        if connection.is_connected():
            cursor = connection.cursor(dictionary = True)
            query = """ select * from books limit 5 ; """

            cursor.execute(query)

            results = cursor.fetchall()

            

            for row in results :
                    print(row)
                    st.write(row)
                    book_id_list.append( row['book_id'] )


    except Error as e :
            print('DB관련 에러 발생',e)



    finally :
        cursor.close()
        connection.close()        



    book_id = st.number_input('책 아이디 입력', 
                                min_value= book_id_list[0],
                                max_value= book_id_list[-1])

    if st.button(' 실행 ') :
        
        try :
            connection = mysql.connector.connect( host = 'database-1.coqni1q3jupc.us-east-2.rds.amazonaws.com',
                                                database = 'yhdb',
                                                user = 'streamlit',
                                                password = '1234' ) 
           
            if connection.is_connected():
                cursor = connection.cursor()
                
                
                #원하는거 실행

                query = """ delete from books
                            where book_id = %s ; """

                

                            
                data = (book_id, )

                cursor.execute( query, data )

                connection.commit()   

               

                             


        except Error as e :
            print('DB관련 에러 발생',e)

        finally :
            cursor.close()
            connection.close()    
        




if __name__ == '__main__' :
    main()