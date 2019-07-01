from flask_restful import Api

from views.city_view import *
from views.country_view import *
from views.destination_view import *
from views.scenic_detail_view import *
from views.scenic_view import *
from views.search_view import *
from views.travel_view import *
from views.user_detail_view import *
from views.user_view import *

api = Api()   # 创建Api对象

def init_api(app):
    api.init_app(app)  # Api对象与Flask程序实例关联


api.add_resource(UserLoginResource,"/login/")
api.add_resource(UserregisterResource,"/register/")
api.add_resource(CityResource,"/city/")
api.add_resource(CountryResource,"/country/")
api.add_resource(ScenicResource,"/scenic/")
api.add_resource(SearchResource,"/search/")
api.add_resource(UserDetailResource,"/user/detail/")
api.add_resource(DestinationResource,"/destination/")
api.add_resource(TravelResource,"/travel/")
api.add_resource(ScDetailResource,"/scenic/detail/")

