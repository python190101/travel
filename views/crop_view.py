from flask import jsonify, request
from dao.order_dao import OrderDao
from flask_restful import Resource, reqparse


class DestinationResource(Resource):

    def get(self):
        scenicid = request.args.get("scenicid")
        dao = OrderDao()
        data = dao.price_list("senic_date_price",scenicid)
        if data:
            return jsonify({
                "code":8101,
                "msg":"查询成功！",
                "data":data
            })
        else:
            return jsonify({
                "code":8102,
                "msg":"没有该景点！"
            })

    def post(self):
        peo_count = request.form.get("peo_count")
        child_count = request.form.get("child_count")
        date = request.form.get("date")
        scenicid = request.form.get("scenicid")
        cityname = request.form.get("cityname")
        dao = OrderDao()
        data = dao.scenic_list("scenics",scenicid)
        return jsonify({
            "code":8103,
            "msg":"返回数据！",
            "data":{
                "peo_count":peo_count,
                "child_count":child_count,
                "date":date,
                "name":data[0]["name"]
            }
        })