from flask import Blueprint, jsonify

_dev = Blueprint('dev', __name__)


# default
@_dev.route('/objection/', methods=['GET'])
def welcome():
    return 'OBJECTION!!'

# variable query
@_dev.route('/<int:n>/', methods=['GET'])
def num(n):
    return f"The number is {str(n)}."

# json type
@_dev.route('/person/', methods=['GET'])
def person():
    return jsonify({'name':'Jimit',
                    'address':'India'})

# special errcode
@_dev.route('/teapot/', methods=['GET'])
def teapot():
    return "Would you like some tea?", 418

# logging
# @_dev.route('/destroy/', methods=['POST'])
# def destroy():
#     print(request.form['text'])
#     _dev.logger.info('Failure to comply.')
#     abort(401)
