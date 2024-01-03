from flask import Blueprint , jsonify, request
from .models import DashBoard,QueryDB
from .schemas import DataSchema

urls = Blueprint('urls', __name__)


@urls.route('/dashboard', methods = ['GET'])
def get_data():


    result_id = DashBoard.get_id()

    result_id_serialize = DataSchema(many=False).dump(result_id)


    result = DashBoard.get_id()

    page = request.args.get('page', default=1,type=int)
    per_page = request.args.get('per_page', default=3,type=int)

    users_paginate = DashBoard.query.paginate(page=page, per_page=per_page)
    list_users = users_paginate.items
    result = DataSchema(many = True).dump(list_users)

    return jsonify ({

                        'Users' : result,
                        'total_page' : users_paginate.pages,
                        'corrent_page' : users_paginate.page,
                        'per_page' : users_paginate.per_page,
                        'total_items' : users_paginate.total,
                        'result':{'result_id_serialize':result_id_serialize}
    }), 200
  