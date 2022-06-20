from http import HTTPStatus
from multiprocessing import connection
from flask import request
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector
from mysql_connection import get_connection

class UserRegisterResource(Resource):
    def post(self):

        # postman에서 작성한 내용을 아래에 주석처리하고 보면서 코드를 작성한다. 

#         {
#     "username": "홍길동",
#     "email": "abc@naver.com",
#     "password": "1234"
#       }

        # 1. 쿨라이언트가 body에 보내준 json을 받아온다.
        # body로 받는 데이터는 아래 함수를 사용한다.
        data = request.get_json()

        # 2. 이메일 주소형식이 제대로 된 주소형식인지, 확인하는 코드 작성.
        # 라이브러리 설치해보고, 설명서대로 테스트까지 해보자
        # DB에 저장하지 말고, 


        return