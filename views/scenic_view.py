from flask import jsonify, request
from flask_restful import Resource

from dao.scenic_dao import ScenicDao


class ScenicResource(Resource):

    def post(self):
        json = request.get_json()
        cityid = json["cityid"]
        scenictype = json["scenictypeid"]
        dao = ScenicDao()
        try:
            data = dao.scenic_city_list(cityid,scenictype)
            return jsonify({
                "code": 8001,
                "msg": "ok!",
                "data": data
            })
        except:
            return jsonify({
                "code": 8002,
                "msg": "意外错误！"
            })


class TypeResource(Resource):

    def post(self):
        json = request.get_json()
        cityid = json["cityid"]
        dao = ScenicDao()
        try:
            data = dao.scenic_city_list(cityid,1)
            return jsonify({
                "code": 8001,
                "msg": "ok!",
                "data": data
            })
        except:
            return jsonify({
                "code": 8002,
                "msg": "意外错误！"
            })
