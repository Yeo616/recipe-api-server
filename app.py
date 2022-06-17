from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource



app = Flask(__name__)

# 우리가 만들건 restful 서버임

api = Api(app)

# 경로와 리소스(API 코드)를
api.add_resource(RecipeListResource,'/recipes')
api.add_resource(RecipeResource,'/recipes/<int:recipe_id>') # 이 뒤에있는 숫자를 받아, 어디로 처리하라. 

if __name__ == '__main__':
    app.run()
    