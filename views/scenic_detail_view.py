from flask import jsonify, request

from dao.senic_dao import ScenicDao
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource, reqparse,request
from libs.sms import send_msg




class ScDetailResource(Resource):
    def get(self):
        dao = ScenicDao()
        data = dao.s_all()
        return jsonify({
            "code":1003,
            "msg":"请求成功！",
            "data":data
        })

class ScDetail(Resource):
    def get(self):
        scenic_id = request.args.get("scenic_id")
        dao = ScenicDao()
        data = dao.s_detail(scenic_id)
        return jsonify({
            "code": 1003,
            "msg": "请求成功！",
            "data": data
        })