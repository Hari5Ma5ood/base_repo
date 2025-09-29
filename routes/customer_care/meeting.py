from ..namspace import users
from flask_restx import Resource
from libs.services.validator import Validator

@users.route('/meeting')
class Meeting(Resource):
    def get(self):
        body = {'MEETING_ID': '123-123-12u'}
        validate = Validator.validate('meeting', body)
        if validate:
            return 'We are fine'
        else:
            return 'Params are missing'