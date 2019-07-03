from flask import jsonify, request

from dao.order_status_dao import OrderStateDao
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource, reqparse,request
from libs.sms import send_msg




class OrderStatusResource(Resource):
    def get(self):

        dao = OrderStateDao()
        data = dao.order_status()
        return jsonify({
            "code":1003,
            "msg":"请求成功！",
            "data":data
        })
