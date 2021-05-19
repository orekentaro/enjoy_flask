from flask import Blueprint
from models.main_model import MainModel


main_route = Blueprint('main_route', __name__, url_prefix='/')


MainModel = MainModel()
@main_route.route('/login')
def login():
  return MainModel.login()