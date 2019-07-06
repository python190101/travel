from flask_restful import Api

from views.city_view import *
from views.country_view import *
from views.delete_order_view import *
from views.destination_view import *
from views.order_status_view import *
from views.order_view import *
from views.scenic_detail_view import *
from views.scenic_view import *
from views.search_view import *
from views.user_detail_view import *
from views.user_order_check_view import *
from views.user_order_status_view import *
from views.user_view import *

api = Api()   # 创建Api对象

def init_api(app):
    api.init_app(app)  # Api对象与Flask程序实例关联


api.add_resource(UserLoginResource,"/login/")
api.add_resource(UserPLoginResource,"/plogin/")
api.add_resource(PloginResource,"/numlogin/")
api.add_resource(UserregisterResource,"/register/")
api.add_resource(UserPregisterResource,"/pregister/")
api.add_resource(LoginOutResource,"/loginout/")
api.add_resource(PForgetResource,"/pforget/")
api.add_resource(ForgetResource,"/forget/")

api.add_resource(CityResource,"/city/")
api.add_resource(CountryResource,"/country/")
api.add_resource(ScenicResource,"/scenic/")
api.add_resource(TypeResource,"/type/")
api.add_resource(SearchResource,"/search/")
api.add_resource(SortResource,"/sort/")
api.add_resource(DestinationResource,"/destination/")
api.add_resource(ScenicHomepageResource,"/scenic/homepage/")
api.add_resource(ScenicDetail,"/scenic/detail/")


api.add_resource(UserDetailUpdateResource,"/user/update/")
api.add_resource(UserDetailResource,"/user/detail/")


api.add_resource(DatePriceResource,"/dateprice/")
api.add_resource(TotalResource,"/total/")
api.add_resource(OrderStatusResource,"/order/status/")
api.add_resource(TravelInfoResource,"/info/")
api.add_resource(UserOrderStatusAll,"/order/status/all/")
api.add_resource(UserOrderStatus1,"/order/status/after/")
api.add_resource(UserOrderStatus2,"/order/status/defore/")
api.add_resource(OrderResource,"/order/")
api.add_resource(PriceResource,"/price/")
api.add_resource(DeleteOrder,"/order/delete/")
api.add_resource(UserOrderCheck,"/order/check/")

