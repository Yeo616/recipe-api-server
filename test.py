# # 데이터베이스에 접속해서, 데이터 처리하는 테스트 코드

# import mysql.connector
# from mysql_conncetion import get_connection

# # 예외처리문
# # mysql.connector이라는 라이브러를 사용하는 중, 근데 저거 만든 사람이 만약에 데이터베이스에 
# # 접속이 안되면, 에러를 내게 만들어주는 코드. 
# # 메뉴얼에 명시했다. 이 코드를 이용하려면, 

# # try-except가 같이 움직인다.
# # try에는 정상적인 코드를 작성한다. 
# # 에러가 발생하면, except에 있는 코드를 작성하라. 
# # 정상적인 동작을 하지 않을 때는 except안에 명령어를 써라. 

# # connection은 쟤네가 만들어준거. cursor도 쟤네가 만들어준거. 
# try : 
#     # 데이터 insert 
#     # 1. DB에 연결
#     connection = get_connection()

#     # 2. 쿼리문을 만든다.
#     # 아까 recipe_db에 내용을 넣을 것임
#     query = '''insert into recipe
#             (name, description, cook_time, directions)
#             values
#             ('된장찌게','맛있는 김치찌게 만드는 방법', 30, '먼저 고기를 볶은 후, 물을 넣고, 된장넣고, 끓인다');'''
#     # 3. 커서를 가져온다.
#     cursor = connection.cursor()

#     # 4, 쿼리문을 커서를 이용해서 실행한다.
#     cursor.execute(query)

#     # 5. 컨넥션을 커밋해줘야한다. => 데이터 베이스에 영구적으로 반영하라는 뜻
#     connection.commit()

#     # 6. 자원 해제
#     cursor.close()
#     connection.close()


# except mysql.connector.Error as e:
#     print(e)
#     cursor.close()
#     connection.close()

import mysql.connector
from mysql_connection import get_connection

name = '순두부찌게'
description = '순두부 찌게'
cook_time = 30
directions = '이렇게 저렇게 끓인다'

try :
    # 데이터 insert 
    # 1. DB에 연결
    connection = get_connection()

    # 2. 쿼리문 만들기
    query = '''insert into recipe
            (name, description, cook_time, directions)
            values
            (%s,'순두부 찌게',30,'이렇게 저렇게 끓인다' );'''
    record = (name, )

    # 3. 커서를 가져온다.
    cursor = connection.cursor()

    # 4. 쿼리문을 커서를 이용해서 실행한다.
    cursor.execute(query,record)

    # 5. 커넥션을 커밋해줘야 한다 => 디비에 영구적으로 반영하라는 뜻
    connection.commit()

    # 6. 자원 해제
    cursor.close()
    connection.close()

except mysql.connector.Error as e :
    print(e)
    cursor.close()
    connection.close()
