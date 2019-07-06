import uuid

from flask import jsonify, request
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource
from libs.sms import send_msg


# 输出参数



# 用户注册登录 操作  其中密码做了数据安全
class UserLoginResource(Resource):

    def post(self):
        json = request.get_json()
        p_num = json.get("p_num")
        token = json.get("token","")
        if check_token(token):
            return jsonify({
                "code": 207,
                "msg": "已登录，不要重复登录!"
            })

        password = str(json.get("password"))

        dao = UserDao()
        password = dao.make_pwd(password)
        data = dao.tn_list(p_num,password)

        if data == 2:
            return jsonify({
                "code": 202,
                "msg": "密码错误!"
            })
        elif data == 3:
            return jsonify({
                "code": 203,
                "msg": "用户名不存在!"
            })
        elif data == 4:
            return jsonify({
                "code": 204,
                "msg": "该用户已经被封了!"
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

    def post(self):
        json = request.get_json()

        p_num = json.get("p_num")
        vzm = json.get("vzm")
        local_vzm = r.get("TN" + p_num).decode()
        if int(local_vzm) == vzm:
            password = str(json.get("password"))

            dao = UserDao()

            password = dao.make_pwd(password)
            dao.save(**{"p_num":p_num,"password":password,"is_active":1})
            return jsonify({
                    "code": 209,
                    "msg": "注册成功!"
            })
        else:
            return jsonify({
                "code": 205,
                "msg": "验证码错误!"
            })


class UserPLoginResource(Resource):
    def post(self):
        json = request.get_json()
        p_num = json["p_num"]
        dao = UserDao()
        res = dao.p_list(p_num)
        if res:
            send_msg(p_num)
            return jsonify({
                "code":208,
                "msg":"发送成功！"
            })
        else:
            return jsonify({
                "code": 203,
                "msg": "用户名不存在！"
            })


class UserPregisterResource(Resource):
    def post(self):
        json = request.get_json()
        p_num = json["p_num"]
        dao = UserDao()
        res = dao.p_list(p_num)
        if not res:
            send_msg(p_num)
            return jsonify({
                "code":206,
                "msg":"ok！"
            })
        else:
            return jsonify({
                "code": 210,
                "msg": "手机号已存在，不能注册!"
            })


class PloginResource(Resource):

    def post(self):
        json = request.get_json()

        token = json.get("token","")
        res = check_token(token)

        if not res:
            p_num = json["p_num"]
            vzm = json["vzm"]

            local_vzm = r.get("TN" + p_num).decode()

            if local_vzm == vzm:

                token = uuid.uuid4().hex
                save_token(token, p_num)

                return jsonify({
                    "code": 201,
                    "msg": '登录成功！',
                    "token": token,
                    "p_num":p_num
                })
            else:
                return jsonify({
                    "code": 205,
                    "msg": "验证码错误!"
                })

        return jsonify({
            "code": 207,
            "msg": "已登录，不要重复登录!"
        })


class LoginOutResource(Resource):
    def post(self):
        json = request.get_json()
        token = json.get("token","")
        if token:
            r.delete(token)
            return jsonify({
                "code": 211,
                "msg": "退出成功!"
            })
        else:
            return jsonify({
                "code": 212,
                "msg": "未登录!"
            })


class PForgetResource(Resource):
    def post(self):
        json = request.get_json()
        p_num = json["p_num"]
        dao = UserDao()
        res = dao.p_list(p_num)
        if res:
            send_msg(p_num)
            return jsonify({
                "code":206,
                "msg":"ok！"
            })
        else:
            return jsonify({
                "code": 203,
                "msg": "手机号没有注册!",
            })

class ForgetResource(Resource):
    def post(self):
        json = request.get_json()

        p_num = json.get("p_num")
        vzm = json.get("vzm")
        local_vzm = r.get("TN" + p_num).decode()
        if local_vzm == vzm:
            password = str(json.get("password"))

            dao = UserDao()

            password = dao.make_pwd(password)
            dao.update_pwd(password)
            return jsonify({
                "code": 211,
                "msg": "更改成功!"
            })
        else:
            return jsonify({
                "code": 205,
                "msg": "验证码错误!"
            })
