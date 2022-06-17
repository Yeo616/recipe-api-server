from flask import request
from flask_restful import Resource
from mysql.connector.errors import Error
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

        # 클라이언트에서, body 부분에 작성한 json을 
        # 받아오는 코드
        data = request.get_json()

        print(data)

        return 