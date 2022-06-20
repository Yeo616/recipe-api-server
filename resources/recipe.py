from http import HTTPStatus
from multiprocessing import connection
from flask import request
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector
from mysql_connection import get_connection

### API를 만들기 ㅜ이한 클래스 작성
### class(클래스)란?? 변수와 함수로 구성된 묶음!
### 클래스는 상속이 가능하다! 
### API를 만들기 위한 클래스는, flask_restful 라이브러리의 
### Resource 클래스를 상속해서 만들어야 한다.


# 우리가 지금 만드는 API는 POST임.
class RecipeListResource(Resource):
    # restful api의 method에 해당하는 함수 작성
    def post(self):
        # 딱 요 형식으로 만들어야 한다. 이게 flask 프레임워크임. 정해져있음. 
        # 만든다음에 우리가 작성한 URL에 연결시킬것이다. 
        # api 실행 코드를 여기에 작성

        # 1. 쿨라이언트가 body에 보내준 json을 받아온다.
        # body로 받는 데이터는 아래 함수를 사용한다.
        
        # 클라이언트에서, body 부분에 작성한 json을 
        # 받아오는 코드
        data = request.get_json()

        # 받아온 데이터를 디비 저장하면 된다.
        try:
            # 데이터 insert 
            # 1. DB에 연결
            connection = get_connection()

            # 2. 쿼리문 만들기
            query = '''insert into recipe
                    (name, description, cook_time, directions)
                    values
                    (%s,%s,%s,%s);'''
            record = (data['name'],data['description'], data['cook_time'],data['directions'] )

            # 3. 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서를 이용해서 실행한다.
            cursor.execute(query,record)

            # 5. 커넥션을 커밋해줘야 한다 => 디비에 영구적으로 반영하라는 뜻
            connection.commit()

            # 6. 자원 해제
            cursor.close()
            connection.close()

        except Error as e:
            print(e)
            cursor.close()
            connection.close()
            return {"error": str(e)}, 503

        return {"result":"success"},200


    def get(self):
        # 저장되어있는 모든 API를 가져오는 것. 우선 mysql로 간다. 쿼리문을 가져와야하기 때문
        # 쿼리 스트링으로 오는 데이터는 아래처럼 처리해준다.
        offset = request.args.get('offset')
        limit = request.args.get('limit')

        # 디비로부터 데이터를 받아서, 클라이언트에 보내준다.
        try :
            connection = get_connection()

            query = '''select *
                    from recipe
                    where is_publish =1
                    limit '''+offset+''' , '''+limit+''';'''

            cursor = connection.cursor(dictionary = True)
            cursor.execute(query)

            # select문은, 아래 함수를 이용해서, 데이터를 가져온다. 
            result_list = cursor.fetchall()
            # 여기에 쿼리의 결과가 있음

            print(result_list)

            # 중요!
            # 디비에서 가져온 timestamp는 파이썬의 datetime으로 자동 변경 된다. 
            # 문제는! 이 데이터를 json으로 바로 보낼수 없으므로, 문자열로 바꿔서 다시 저장해서 보낸다. 

            i = 0
            for record in result_list :
                # 한 행씩 가져와서, 그 행에 들어있는 i번째의 created_at을 ios 포맷으로 바꿔라.  
                result_list[i]['created_at'] = record['created_at'].isoformat()
                result_list[i]['updated_at'] = record['updated_at'].isoformat()
                i = i + 1             
                
            cursor.close()
            connection.close()


        except mysql.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()

            return {"error" : str(e)}, 503
            # 503으로 보내겠다.
        

        # result_list정상적일 때는 결과가 리스트의 행이 하나, 

        # 3. result_list의 행의 갯수가 1개이면, 유저 데이터를 정상적으로 받아온것이고, 
        # 행의 갯수가 0이면, 요청한 이메일은, 회원가입이 되어있지 않은 이메일이다.



        return { "result" : "success" , 
                "count" : len(result_list) ,
                "result_list" : result_list }, 200
                # 첫번째 키값
        