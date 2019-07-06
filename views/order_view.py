from datetime import datetime

from flask import jsonify, request

from dao.user_dao import UserDao
from libs import *
from dao.city_dao import CityDao
from dao.order_dao import OrderDao
from flask_restful import Resource
from dao.te_order_dao import TeOrderDao
from libs.options import getcode



class DatePriceResource(Resource):

    def post(self):
        json = request.get_json()
        scenicid = json.get("scenicid")
        dao = OrderDao()
        data = dao.price_list("scenic_date_price",scenicid)
        if data:
            return jsonify({
                "code":8101,
                "msg":"查询成功！",
                "data":data
            })
        else:
            return jsonify({
                "code":8102,
                "msg":"没有该景点！"
            })

class TotalResource(Resource):

    def post(self):
        json = request.get_json()
        dao = OrderDao()
        peo_count = json.get("peo_count")
        child_count = json.get("child_count")
        if child_count is None:
            child_count = 0

        date = json.get("date")
        price = json.get("price")

        scenicid = json.get("scenicid")
        scenic_name = dao.scenic_list("scenics",scenicid)[0]["name"]

        cityname = json.get("cityname")

        price_z = price*peo_count + price*child_count*0.8

        lals  = getcode(scenic_name)
        dao.scenic_insert(lals,scenicid)

        lal = getcode(cityname)  # 经纬度

        dis = dao.travel_type(lal[1],lal[0],scenicid)

        sc_items = dao.scenic_list("scenics", scenicid)
        cityid = sc_items[0]["city_id"]
        city_dao = CityDao()
        sc_city_name = city_dao.city_name(cityid)[0]["name"]

        if float(dis[0]["dis"]) > 800:
            f_dict = {
                "出发地":cityname,
                "目的地":sc_city_name,
                "出发日期":date,
                "出发时间":"07:05",
                "到达时间":"09:25",
                "类型":"惠选经济舱",
                "航班号":"国航HU7137",
                "飞行时间":"2小时20分钟"
            }

        else:
            f_dict = {
                "出发时间":"07:00:00",
                "返回": "国贸",
                "备注": "距离远的游客请自行前往集合点"
            }


        ins_items = dao.tn_list("insurances")

        return jsonify({
            "code":8103,
            "msg":"返回数据！",
            "data":{
                "scenic_name":scenic_name,
                "pro_code":"210107045",
                "peo_count":peo_count,
                "child_count":child_count,
                "date":date,
                "f_dict":f_dict,
                "insurances":ins_items,
                "price_z":price_z
            }
        })


class OrderResource(Resource):
    def post(self):
        json = request.get_json()
        dao = OrderDao()
        peo_count = json.get("peo_count")
        child_count = json.get("child_count")

        scenicid = json.get("scenicid")
        date = request.form.get("date")
        price = request.form.get("price")
        order_time = datetime.now()

        username = json.get("username")
        phone_num = json.get("phone_num")
        email = json.get("email")

        token = json.get("token")
        p_num = r.get(token)
        user_dao = UserDao()
        user_id = user_dao.user_id_list(p_num)

        todao = TeOrderDao()
        order_code = todao.next_order_num()

        try:
            dao.save("travel_infor", **{
                "code":order_code,
                "order_status":0,
                "start_time":date,
                "order_time":order_time,
                "price":price,
                "scenic_id":scenicid,
                "user_id": user_id
            })
            dao.save("contact_infor",**{
                "name":username,
                "phone_num":phone_num,
                "email":email,
                "user_id":user_id
            })
            order_id = dao.order_list(order_code)
            dao.save("order_detail", **{
                "adult_num": peo_count,
                "child_num": child_count,
                "flight_id": 1,
                "insurance": 1,
                "order_id":order_id
            })
            return jsonify({
                "code": 703,
                "msg": "成功！"
            })
        except:
            return jsonify({
                "code": 704,
                "msg": "保存失败！"
            })


class TravelInfoResource(Resource):

    def get(self):
        dao = OrderDao()
        data = dao.tn_list("travel_infor")
        if data:
            return jsonify({
                "code":701,
                "msg":"成功！",
                "data":data
            })
        else:
            return jsonify({
                "code": 702,
                "msg": "没有数据！"
            })

    def post(self):
        json = request.get_json()
        name = json.get("name")
        phone_num = json.get("phone_num")
        email = json.get("email")
        document_type = json.get("document_type")
        id_number = json.get("id_number")
        token = json.get("token")
        p_num = r.get(token)
        user_dao = UserDao()
        user_id = user_dao.user_id_list(p_num)
        dao = OrderDao()
        try:
            dao.save("travel_infor",**{
                "name":name,
                "phone_num":phone_num,
                "email":email,
                "document_type":document_type,
                "id_number":id_number,
                "user_id":user_id
            })
            return jsonify({
                "code":705,
                "msg":"成功！",
                "data":{
                    "name":name,
                    "phone_num":phone_num,
                    "email":email,
                    "document_type":document_type,
                    "id_number":id_number
                }
            })
        except:
            return jsonify({
                "code":706,
                "msg":"保存失败！"
            })


class PriceResource(Resource):
    def post(self):
        json = request.get_json()
        code = json.get("code")
        price = json.get("price")
        if code == 1:
            price += 50
        else:
            price -= 50
        return jsonify({
            "code": 707,
            "msg": "成功！",
            "price":price
        })

