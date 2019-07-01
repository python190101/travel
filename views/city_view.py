from flask import jsonify
from dao.city_dao import CityDao
from flask_restful import Resource, reqparse


parser = reqparse.RequestParser()
parser.add_argument('cityname',type=str,required=True,help='输入城市名！')

class CityResource(Resource):

    def get(self):
        dao = CityDao()
        citylist = dao.city_list()
        return jsonify({
            "code":8001,
            "msg":"ok!",
            "pop":citylist[0],
            "nol":citylist[1]
        })


    def post(self):
        args = parser.parse_args()
        cityname = args.get("cityname")
        dao = CityDao()
        data = dao.dim_list(cityname)
        if data:
            return jsonify({
                "code": 8001,
                "msg": "ok!",
                "data":data
            })
        return jsonify({
            "code": 8002,
            "msg": "miss"
        })