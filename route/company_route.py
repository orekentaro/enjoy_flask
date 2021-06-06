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

@company_route.route('/supplier_list')
def supplier_list():
  """
  仕入れ先一覧表示
  """
  return CompanyModel.supplier_list()

@company_route.route('/create_supplier', methods=['GET'])
def create_supplier():
  """
  仕入れ先追加画面
  """
  return CompanyModel.create_supplier()

@company_route.route('/create_supplier', methods=['POST'])
def create_supplier_complete():
  """
  仕入れ先追加処理
  """
  return CompanyModel.create_supplier_complete()

@company_route.route('/own_company_list')
def own_company_list():
  """
  自社一覧表示
  """
  return CompanyModel.own_company_list()

@company_route.route('/create_own_company', methods=['GET'])
def create_own_company():
  """
  自社追加画面
  """
  return CompanyModel.create_own_company()

@company_route.route('/create_own_company', methods=['POST'])
def create_own_company_complete():
  """
  自社追加処理
  """
  return CompanyModel.create_own_company_complete()

@company_route.route('/edit_clients/<id>', methods=['GET'])
def edit_clients(id):
  """
  取引先編集画面
  """
  return CompanyModel.edit_clients(id)

@company_route.route('/edit_supplier/<id>', methods=['GET'])
def edit_supplier(id):
  """
  仕入れ先編集画面
  """
  return CompanyModel.edit_supplier(id)

@company_route.route('/edit_own_company/<id>', methods=['GET'])
def edit_own_company(id):
  """
  自社編集画面
  """
  return CompanyModel.edit_own_company(id)

@company_route.route('/edit_clients/<id>', methods=['POST'])
def edit_clients_complete(id):
  """
  取引先編集画面
  """
  return CompanyModel.edit_clients_complete(id)