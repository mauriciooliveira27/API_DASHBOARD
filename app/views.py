from flask import Blueprint , jsonify, request
from .models import DashBoard,QueryDB
from .schemas import DataSchema

views = Blueprint('views', __name__)


@views.route('/dashboard', methods = ['GET'])
def get_data():

    result_id = DashBoard.get_last_record_by_id()   
    result_id_serialize = DataSchema(many=False).dump(result_id)

    return jsonify ({

                        'result':{'result_id_serialize':result_id_serialize}
                    
                    }), 200




@views.route('/dashboard/all', methods = ['GET'])
def get_all_data():
        
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=3, type=int)

    data_paginate = DashBoard.query.paginate(page=page , per_page=per_page)
    data_list = data_paginate.items()
    result = DataSchema(many=True).dump(data_list)

    return jsonify({

                        'Data' : result,
                        'total_page' : data_paginate.pages,
                        'corrent_page' : data_paginate.page,
                        'per_page' : data_paginate.per_page,
                        'total_items' : data_paginate.total
                    
                    }), 200