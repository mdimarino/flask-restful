#!/usr/bin/env python

from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

ship_put_args = reqparse.RequestParser()
ship_put_args.add_argument("name",     type=str, help="Name of the ship is required",     required=True)
ship_put_args.add_argument("class",    type=str, help="Class of the ship is required",    required=True)
ship_put_args.add_argument("owner",    type=str, help="Owner of the ship is required",    required=True)
ship_put_args.add_argument("operator", type=str, help="Operator of the ship is required", required=True)
ship_put_args.add_argument("status",   type=str, help="Status of the ship is required",   required=True)

ships = {}

def abort_if_ship_registry_doesnt_exist(ship_registry):
    if ship_registry not in ships:
        abort(404, message="Could not find ship...")

def abort_if_ship_registry_exists(ship_registry):
    if ship_registry in ships:
        abort(409, message="Ship already exists with that registry...")

class Ship(Resource):
    def get(self, ship_registry):
        abort_if_ship_registry_doesnt_exist(ship_registry)
        return ships[ship_registry]

    def post(self, ship_registry):
        abort_if_ship_registry_exists(ship_registry)
        args = ship_put_args.parse_args()
        ships[ship_registry] = args
        return ships[ship_registry], 201

    def put(self, ship_registry):
        args = ship_put_args.parse_args()
        ships[ship_registry] = args
        return ships[ship_registry], 201

    def delete(self, ship_registry):
        abort_if_ship_registry_doesnt_exist(ship_registry)
        del ships[ship_registry]
        return '', 204

class Ships(Resource):
    def get(self):
        return ships

# defining endpoints
api.add_resource(Ship, '/ship/<string:ship_registry>')
api.add_resource(Ships, '/ships')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
