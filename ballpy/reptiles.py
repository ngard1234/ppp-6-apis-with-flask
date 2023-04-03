from flask import (Blueprint, request,jsonify)
from . import models 
import json


# reptiles = json.load(open('reptile.json')) 
# print(reptiles) 

bp = Blueprint('reptiles', __name__, url_prefix="/reptiles")

@bp.route('/', methods=['GET'])
def index():
    if request.method == "GET":
        results = models.ReptileInfo.query.all()
        # result_dict={ }
        for item in results:
            print(item)
        return '', 200
    # else:
    #     return {"message": "failure"}
    

@bp.route('/', methods=['POST'])
def post():
    if request.method == 'POST':
        
        new_post=models.ReptileInfo(
            common_name= "Ball python",
            scientific_name='scientific_name',
            conservation_status='conservation_status',
            native_habitat='native_habitat',
            fun_facts='fun_fact'
        )        
        models.db.session.add(new_post)
        models.db.session.commit()
        return 'Successfully posted in ballpy database ', 200

@bp.route('/<int:id>')
def show(id):
    results = models.ReptileInfo.query.filter_by(id=id).first()
    result_dict = { 'common_name' : results.common_name }
    # return jsonify(results.serialize)
    print(result_dict)
    return result_dict
