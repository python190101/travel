from flask import jsonify, request
from dao.country_dao import CountryDao
from flask_restful import Resource


class CountryResource(Resource):

    def get(self):
        dao = CountryDao()
        try:
            data = dao.tn_list("countries")
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
        coun_code = request.form.get("councode")
        dao = CountryDao()
        try:
            sql = "select name from cities where country_id=(select id from" \
                  " countries where code=%s) and is_popular=1" % coun_code
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
