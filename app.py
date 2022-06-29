from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResource
from resources.user import UserLoginResource, UserLogoutResource, UserRegisterResource



app = Flask(__name__)

# 환경 변수 셋팅
app.config.from_object(Config)

# JWT 토큰 라이브러리 만들기
# JWTManager: JWT토큰이 유효한지 관리해주는 라이브러리
jwt = JWTManager(app)

# app을 넣어줘서 얘가 관리하라고 하는 것
# 회원가입 코드
# 첫번째로 유효한 이메일인지 확인, 비번이 4자리 이상 12자리 이하인지 확인, 그리고 비번을 암호화
# 암호화 하고, DB 회원 테이블에다가 insert, 인서트한 커서에 방금 insert한 user_id를 가져온다. 

#------ 로그아웃 된 토큰이 들어있는 set을, jwt에 알려준다.-----
from resources.user import jwt_blacklist

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header,jwt_payload):
    # 메뉴얼에 써져있는 내용
    jti = jwt_payload['jti']
    return jti in jwt_blacklist



# 우리가 만들건 restful 서버임

api = Api(app)

# 경로와 리소스(API 코드)를
api.add_resource(RecipeListResource,'/recipes')
# post(생성), get(조회)

api.add_resource(RecipeResource,'/recipes/<int:recipe_id>') # 이 뒤에있는 숫자를 받아, 어디로 처리하라. 
# get, put(업데이트), delete(삭제)
# 한 경로당, 한 class 임.

api.add_resource(RecipePublishResource,'/recipes/<int:recipe_id>/publish') 
# # 레시피 공개, 임시저장
# 숫자가 올것이다. 숫자가 바뀔수도 있으니, 내가 변수처리를 하겠다. 
# 어떤 숫자가 올지는 클라가 바꿔서 보낸다.
api.add_resource(UserRegisterResource,'/users/register')
api.add_resource(UserLoginResource,'/users/login')
api.add_resource(UserLogoutResource, '/users/logout')

if __name__ == '__main__':
    app.run()
    