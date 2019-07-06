from flask import jsonify, request
from dao.scenic_dao import ScenicDao
from flask_restful import Resource





class ScenicHomepageResource(Resource):
    def post(self):
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
    def post(self):
        json = request.get_json()
        scenics_id = json["scenics_id"]
        dao = ScenicDao()
        data = dao.s_detail(scenics_id)
        return jsonify({
            "code": 1004,
            "msg": "请求成功！",
            "data": data
        })