from flask import jsonify, request, redirect, url_for
from libs import *
from dao.user_dao import UserDao
from flask_restful import Resource, reqparse
from libs.sms import send_msg


# 输出参数


parser = reqparse.RequestParser()
parser.add_argument('img')
parser.add_argument('user_name')
parser.add_argument('real_name')
parser.add_argument('p_num')
parser.add_argument('birth')
parser.add_argument('sex')
parser.add_argument('email')
parser.add_argument('address')
parser.add_argument('marriage')
parser.add_argument('job')
parser.add_argument('education')


class UserDetailResource(Resource):

    def get(self):
        token = request.args.get("token")
        result = check_token(token)
        if result:
            p_num = request.args.get("p_num")
            dao = UserDao()
            data = dao.p_list(p_num)
            return  jsonify({
                "code":701,
                "msg":"请求成功！",
                "data":data
            })
        else:
            return redirect(url_for('login'))



    def post(self):
        args = parser.parse_args()
        print(args)
        img = args.get("img")
        user_name = args.get("user_name")
        real_name = args.get("real_name")
        p_num = args.get("p_num")
        birth = args.get("birth")
        sex = args.get("sex")
        email = args.get("email")
        address = args.get("address")
        marriage = args.get("marriage")
        job = args.get("job")
        education = args.get("education")
