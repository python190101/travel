from flask import jsonify, request
from flask_restful import Resource

from dao.scenic_dao import ScenicDao
from libs.es import ESearch


class SearchResource(Resource):

    def post(self):
        json = request.get_json()
        scname = json.get("cityname")
        es = ESearch("tnindex")
        items = es.query(scname)
        return items


class SortResource(Resource):
    def post(self):
        json = request.get_json()
        cityid = json["cityid"]
        scenictype = json["scenictypeid"]
        code = json["code"]
        dao = ScenicDao()
        try:
            data = dao.scenic_city_list(cityid, scenictype)
            return jsonify({
                "code": 8008,
                "msg": "ok!",
                "data": data
            })
        except:
            return jsonify({
                "code": 8009,
                "msg": "意外错误！"
            })