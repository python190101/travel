from flask_restful import Api

from views.city_view import *
from views.user_view import *

api = Api()   # 创建Api对象

def init_api(app):
    api.init_app(app)  # Api对象与Flask程序实例关联


api.add_resource(UserLoginResource,"/login/")
api.add_resource(UserregisterResource,"/register/")
api.add_resource(CityResource,"/city/")