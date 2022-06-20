from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResource
from resources.user import UserLoginResource, UserRegisterResource



app = Flask(__name__)

# 환경 변수 셋팅
app.config.from_object(Config)

# JWT 토큰 라이브러리 만들기
# JWTManager: JWT토큰이 유효한지 관리해주는 라이브러리
jwt = JWTManager(app)


# 우리가 만들건 restful 서버임

api = Api(app)

# 경로와 리소스(API 코드)를
api.add_resource(RecipeListResource,'/recipes')
api.add_resource(RecipeResource,'/recipes/<int:recipe_id>') # 이 뒤에있는 숫자를 받아, 어디로 처리하라. 
# 한 경로당, 한 class 임.
api.add_resource(RecipePublishResource,'/recipes/<int:recipe_id>/publish') 
# 숫자가 올것이다. 숫자가 바뀔수도 있으니, 내가 변수처리를 하겠다. 
# 어떤 숫자가 올지는 클라가 바꿔서 보낸다.
api.add_resource(UserRegisterResource,'/users/register')
api.add_resource(UserLoginResource,'/users/login')

if __name__ == '__main__':
    app.run()
    