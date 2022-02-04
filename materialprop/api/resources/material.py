from flask import Flask, jsonify, request
import requests
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from materialprop.api.schemas import UserSchema
from materialprop.models import User
from materialprop.extensions import db

from flask import Flask, jsonify, request
import requests



class MaterialResource(Resource):
    def get(self,material_name):
        # schema = UserSchema(many=True)
        # query = User.query
        # return paginate(query, schema)
        #return [{'success': material_name}]
        resp = requests.get(
            'https://materialsproject.org/rest/v2/materials/' + material_name + '/vasp?API_KEY=f1LkJWIeTSafFFQnDai')
        if (resp.status_code == 200):
            resp_data = resp.json()['response']
            for i in range(4):
                print(resp_data[i]['energy'])
            return jsonify(resp.json()['response'])
        else:
            return jsonify(resp.json()['error'])