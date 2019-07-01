from flask import jsonify, request
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource, reqparse
from libs.sms import send_msg


class ScDetailResource(Resource):
    def get(self):
        data = ""
        return jsonify({
            "code":"",
            "msg":"",
            "data":data
        })