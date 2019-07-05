from flask import jsonify, request, redirect, url_for
from libs import *
from dao.user_detail_dao import UserDetailDao
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
            dao = UserDetailDao()
            data = dao.get_c(p_num)
            return  jsonify({
                "code":701,
                "msg":"请求成功！",
                "data":data
            })
        else:
            return redirect(url_for('login'))



    def post(self):
        json = request.get_json()
        token = json.get("token")
        user_id = r.get(token)
        # img = json.get("img")
        user_name = json.get("user_name")
        real_name = json.get("real_name")
        birth = json.get("birth")
        sex = json.get("sex")
        email = json.get("email")
        address = json.get("address")
        marriage = json.get("marriage")
        job = json.get("job")
        education = json.get("education")
        dao = UserDetailDao()
        dao.save("tn_user",**{"user_name":user_name,
                              "email":email})
        dao.save("user_detail",**{"real_name":real_name,
                                    "birth":birth,"sex":sex,"job":job,
                                  "address":address,"marriage":marriage,
                                  "education":education,"user_id":user_id})
        return  jsonify({
                "code":702,
                "msg":"请求成功！"
            })