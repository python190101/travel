from flask import jsonify, request
from dao.country_dao import CountryDao
from flask_restful import Resource

class ScenicResource(Resource):
    def get(self):
        dao = CountryDao()
        try:
            data = dao.tn_list("scenic_type")
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

    def post(self):
        scenictype = request.form.get("scenictype")
        cityname = request.form.get("cityname")
        dao = CountryDao()
        try:
            sql = "select name,img,price,people_num,satisfaction from " \
                  "scenics where scenic_type=%s and " \
                  "city_id=(select id from cities where name='%s')" % (scenictype,cityname)
            data = dao.type_list(sql)
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