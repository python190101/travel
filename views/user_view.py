import uuid

from flask import jsonify, request
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource, reqparse
from libs.sms import send_msg


# 输出参数


parser = reqparse.RequestParser()
parser.add_argument('p_num', required=True, help="请输入用户名")
parser.add_argument('password', required=True, help="请输入密码")


# 用户注册登录 操作  其中密码做了数据安全
class UserLoginResource(Resource):
    def get(self):
        return jsonify({
            'msg':"get请求!"
        })

    def post(self):

        args = parser.parse_args()
        p_num = args.get("p_num")
        t = args.get("token","")
        if check_token(t):
            return jsonify({
                "code": 207,
                "msg": "已登录，不要重复登录!",
            })

        password = args.get("password")

        dao = UserDao()
        data = dao.tn_list(p_num,password)

        if data == 2:
            return jsonify({
                "code": 202,
                "msg": "密码错误!",
            })
        elif data == 3:
            return jsonify({
                "code": 203,
                "msg": "用户名不存在!",
            })
        elif data == 4:
            return jsonify({
                "code": 204,
                "msg": "该用户已经被封了!",
            })
        else:
            phone = data["p_num"]
            token = uuid.uuid4().hex  # token 需要转换为字符串
            save_token(token,p_num)
            return jsonify({
                "code": 201,
                "msg": 'ok',
                "token": token,
                "p_num":phone
            })


class UserregisterResource(Resource):
    def get(self):
        p_num = request.args.get("p_num")
        dao = UserDao()
        number = dao.p_list(p_num)
        if number:
            return jsonify({
                "code": 210,
                "msg": "用户名已存在，不能注册!",
            })
        else:
            send_msg(p_num)
            return jsonify({
                "code": 208,
                "msg":"发送成功！"
            })


    def post(self):
        args = parser.parse_args()

        p_num = args.get("p_num")
        v_code_send = args.get("vcode")

        v_code_c = r.get("TN" + p_num)

        if v_code_c == v_code_send:
            password = args.get("password")

            dao = UserDao()
            number = dao.p_list(p_num)
            if not number:
                password = dao.make_pwd(password)
                dao.save(**{"p_num":p_num,"password":password,"is_active":1})
                return jsonify({
                        "code": 209,
                        "msg": "注册成功!",
                })
            return jsonify({
                        "code": 210,
                        "msg": "用户名已存在，不能注册!",
            })


class UserPLoginResource(Resource):
    def get(self):
        p_num = request.args.get("p_num")
        send_msg(p_num)
        return jsonify({
            "code":208,
            "msg":"发送成功！"
        })


    def post(self):
        args = parser.parse_args()

        p_num = args.get("p_num")
        v_code_send = args.get("vcode","")

        v_code_c = r.get("TN" + p_num,"")

        if v_code_c == v_code_send:
            dao = UserDao()
            number = dao.p_list(p_num)
            if number:
                token = str(uuid.uuid4())
                return jsonify({
                    "code": 201,
                    "msg": '注册成功！',
                    "token": token,
                    "p_num":p_num
                })
            else:
                return jsonify({
                    "code": 203,
                    "msg": '用户名不存在！',
                })
        return jsonify({
            "code": 205,
            "msg": '验证码不对！',
        })
