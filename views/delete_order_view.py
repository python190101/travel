from dao.delete_order_dao import  DeleteOrderDao
from libs import *
from dao.user_dao import UserDao
from flask import jsonify, request
from flask_restful import Resource, reqparse,request

class DeleteOrder(Resource):
    def post(self):
        json = request.get_json()
        p_num = json["p_num"]
        dao = DeleteOrderDao()
        dao.delete_order(p_num)
        return jsonify({
            "code":1020,
            "msg":"ok~",
        })
