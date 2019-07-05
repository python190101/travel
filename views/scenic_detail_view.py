from flask import jsonify, request

from dao.senic_dao import ScenicDao
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource, reqparse,request
from libs.sms import send_msg




class ScenicHomepageResource(Resource):
    def get(self):
        json = request.get_json()
        title1 = json['title1']
        title2 = json['title2']

        dao = ScenicDao()
        data = dao.scenic_homepage(title1,title2)
        return jsonify({
            "code":1003,
            "msg":"请求成功！",
            "data":data
        })

class ScenicDetail(Resource):
    def get(self):
        json = request.get_json()
        scenics_id = json["scenics_id"]
        dao = ScenicDao()
        data = dao.s_detail(scenics_id)
        return jsonify({
            "code": 1004,
            "msg": "请求成功！",
            "data": data
        })