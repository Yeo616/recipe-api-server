from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResource



app = Flask(__name__)

# 우리가 만들건 restful 서버임

api = Api(app)

# 경로와 리소스(API 코드)를
api.add_resource(RecipeListResource,'/recipes')
api.add_resource(RecipeResource,'/recipes/<int:recipe_id>') # 이 뒤에있는 숫자를 받아, 어디로 처리하라. 
# 한 경로당, 한 class 임.
api.add_resource(RecipePublishResource,'/recipes/<int:recipe_id>/publish') 
# 숫자가 올것이다. 숫자가 바뀔수도 있으니, 내가 변수처리를 하겠다. 
# 어떤 숫자가 올지는 클라가 바꿔서 보낸다.

if __name__ == '__main__':
    app.run()
    