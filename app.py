from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource


app = Flask(__name__)

# 우리가 만들건 restful 서버임

api = Api(app)

# 경로와 리소스(API 코드)를
api.add_resource(RecipeListResource,'/recipes')

if __name__ == '__main__':
    app.run()
    