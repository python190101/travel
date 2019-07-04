from flask import jsonify, request, redirect, url_for
from libs import *
from dao.user_detail_dao import UserDaoDetail
from flask_restful import Resource, reqparse
from libs.sms import send_msg


# 输出参数




class UserDetailResource(Resource):

    def get(self):
        json = request.get_json()
        token =  json['token']
        result = check_token(token)
        if result:
            p_num = json["p_num"]
            dao = UserDaoDetail()
            data = dao.get_c(p_num)
            return  jsonify({
                "code":701,
                "msg":"请求成功！",
                "data":data
            })
        else:
            return redirect(url_for('login'))



    def post(self):
        pass    # args = parser.parse_args()
        # print(args)
        # img = args.get("img")
        # user_name = args.get("user_name")
        # real_name = args.get("real_name")
        # p_num = args.get("p_num")
        # birth = args.get("birth")
        # sex = args.get("sex")
        # email = args.get("email")
        # address = args.get("address")
        # marriage = args.get("marriage")
        # job = args.get("job")
        # education = args.get("education")
