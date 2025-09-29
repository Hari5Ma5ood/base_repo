from flask import Flask, request, url_for
from libs.services.alchemy import *
from flask_restx import Api
App = Flask(__name__)

api = Api(App, version='1.0', title='Alpine-BE', prefix='/api', description='API Services Using Alchemy ORM')
from .customer_care import meeting
# from .customer_care import *


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()

    return len(defaults) >= len(arguments)


# @App.before_request
# def site_map_route():
#     routes = []
#     print(request)
#     for rule in App.url_map.iter_rules():
#         # Exclude rules that require parameters and rules you can't open in a browser
#         if "GET" in rule.methods and has_no_empty_params(rule):
#             url = url_for(rule.endpoint, **(rule.defaults or {}))
#             routes.append((url, rule.endpoint))
#
#     print(routes)
#     return routes