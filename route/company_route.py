from flask import Blueprint
from models.company_model import CompanyModel

company_route = Blueprint('company_route', __name__, url_prefix='/company')

CompanyModel = CompanyModel()

@company_route.route('/clients_list')
def clients_list():
  """
  取引先一覧表示
  """
  return CompanyModel.clients_list()

