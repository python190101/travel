from flask import jsonify, request

from dao.city_dao import CityDao

from flask_restful import Resource




class DestinationResource(Resource):

    def get(self):

        dao = CityDao()
        data = dao.elegant_city()

        return jsonify({
            "code":1001,
            "msg":"ok~",
            "data":data
        })
