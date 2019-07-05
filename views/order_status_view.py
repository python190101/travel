from flask import jsonify, request

from dao.order_status_dao import OrderStateDao
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource, reqparse,request
from libs.sms import send_msg




class OrderStatusResource(Resource):
    def post(self):
        json = request.get_json()
        if json['status']  == 1:
            dao = OrderStateDao()
            data = dao.order_status()
            return jsonify({
                "code":1005,
                "msg":"请求成功！",
            })
        else:
            return jsonify({
                "code":1006,
                "msg":"未支付，请支付！",
            })

