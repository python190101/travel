from flask_restful import Api

from views.city_view import *
from views.country_view import *
from views.destination_view import *
from views.order_status_view import OrderStatusResource, UserOrderCheck
from views.scenic_detail_view import *
from views.scenic_view import *
from views.search_view import *
from views.travel_view import *
from views.user_detail_view import *
from views.user_oder_status_view import UserOrderStatusAll, UserOrderStatus1, UserOrderStatus2
from views.user_view import *

api = Api()   # 创建Api对象

def init_api(app):
    api.init_app(app)  # Api对象与Flask程序实例关联


api.add_resource(UserLoginResource,"/login/")
api.add_resource(UserregisterResource,"/register/")
api.add_resource(UserOrderCheck,"/order/check/")
api.add_resource(CityResource,"/city/")
api.add_resource(CountryResource,"/country/")
api.add_resource(ScenicResource,"/scenic/")
api.add_resource(SearchResource,"/search/")
api.add_resource(UserDetailResource,"/user/detail/")
api.add_resource(DestinationResource,"/destination/")
api.add_resource(TravelResource,"/travel/")
api.add_resource(ScenicHomepageResource,"/scenic/homepage/")
api.add_resource(ScenicDetail,"/scenic/detail/")
api.add_resource(OrderStatusResource,"/order/status/")
api.add_resource(UserOrderStatusAll,"/order/status/all/")
api.add_resource(UserOrderStatus1,"/order/status/after/")
api.add_resource(UserOrderStatus2,"/order/status/defore/")


