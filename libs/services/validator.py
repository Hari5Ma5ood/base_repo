from libs.utils.constants import APIParams

class Validator:
  def validate(apiName, body):
    getParams = getattr(APIParams, apiName)
    for value in getParams:
      if value not in body:
        return False
    return True


