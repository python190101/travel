from flask import jsonify, request

from dao.city_dao import CityDao
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource, reqparse
from libs.sms import send_msg




class DestinationResource(Resource):

    def get(self):

        dao = CityDao()
        data = dao.elegant_city()

        return jsonify({
            "code":1001,
            "msg":"ok~",
            "data":data
        })
