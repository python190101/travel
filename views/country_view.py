from flask import jsonify, request
from dao.country_dao import CountryDao
from flask_restful import Resource


class CountryResource(Resource):

    def get(self):
        dao = CountryDao()
        data = []
        try:
            countries = dao.tn_list("countries")
            data.append(countries)
            cities = dao.type_list(1)
            data.append(cities)
            return jsonify({
                "code":8001,
                "msg":"ok!",
                "data":data
            })
        except:
            return jsonify({
                "code": 8002,
                "msg": "意外错误！"
            })


    def post(self):
        json = request.get_json()
        countryid = json.get("countryid")
        dao = CountryDao()
        try:
            data = dao.type_list(countryid)
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
