from flask import Blueprint , jsonify


get_data = Blueprint('get_data', __name__)


@get_data.route('/dashboard', methods = ['GET'])
def get_data():


    return jsonify ({'message':'data_dashboard'})