import uuid
from flask import jsonify, request, redirect,url_for
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource, reqparse
from libs.sms import send_msg


class UserOrderCheck(Resource):

    def post(self):
        json = request.get_json()
        token = json["token"]
        result = check_token(token)
        if result:
            p_num = json["p_num"]
            user_id = r.get(token)
            dao = UserDao()
            num = dao.p_num_check(user_id)
            if p_num == num:
                return jsonify({
                    "code": 1002,
                    "msg": "请求成功！",
                })
            else:
                return jsonify({
                    "code": 1003,
                    "msg": " 手机号码有误！",
                })

        else:
            return redirect(url_for('login'))