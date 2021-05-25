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

@company_route.route('/create_clients', methods=['GET'])
def create_clients():
  """
  取引先追加画面
  """
  return CompanyModel.create_clients()

@company_route.route('/create_clients', methods=['POST'])
def create_clients_complete():
  """
  取引先追加処理
  """
  return CompanyModel.create_clients_complete()