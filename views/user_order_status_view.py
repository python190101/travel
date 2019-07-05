from flask import jsonify, request, redirect, url_for
from libs import *
from dao.user_order_status_dao import UserStatusOrderDao
from flask_restful import Resource, reqparse

class UserOrderStatusAll(Resource):

    def get(self):
        json = request.get_json()
        token = json['token']
        result = check_token(token)
        if result:
            p_num = json["p_num"]
            dao = UserStatusOrderDao()
            data = dao.all_order(p_num)
            return jsonify({
                "code": 1010,
                "msg": "请求成功！",
                "data": data
            })
        else:
            return jsonify({
                "code": 1011,
                "msg": "请登录",

            })

class  UserOrderStatus1(Resource):

    def get(self):
        json = request.get_json()
        token = json['token']
        result = check_token(token)
        if result:
            p_num = json["p_num"]
            dao = UserStatusOrderDao()
            data = dao.check_oreder1(p_num)
            if data :
                return jsonify({
                    "code": 1012,
                    "msg": "请求成功！",
                    "data": data
                 })
            else:
                 return jsonify({
                    "code": 1013,
                    "msg": "未下单！",

                 })


        else:
            return jsonify({
            "code": 1014,
            "msg": "请登录",
            })

class  UserOrderStatus2(Resource):

    def get(self):
        json = request.get_json()
        token = json['token']
        result = check_token(token)
        if result:
            p_num = json["p_num"]
            dao = UserStatusOrderDao()
            data = dao.check_oreder2(p_num)
            return jsonify({
                "code": 1015,
                "msg": "请求成功！",
                "data": data
            })
        else:
            return jsonify({
                "code": 1016,
                "msg": "请登录",

            })