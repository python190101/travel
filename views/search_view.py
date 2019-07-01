from flask import jsonify, request
from dao.country_dao import CountryDao
from flask_restful import Resource, reqparse

from libs.es import ESearch
from views.country_view import CountryResource

parser = reqparse.RequestParser()
parser.add_argument('scname',type=str)


class SearchResource(Resource):

    def get(self):
        country = CountryResource()
        data = country.get()
        return data

    def post(self):
        args = parser.parse_args()
        scname = args.get("scname")
        es = ESearch("tnindex")
        items = es.query(scname)
        return items