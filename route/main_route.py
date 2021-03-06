from flask import Blueprint
from models.main_model import MainModel


main_route = Blueprint('main_route', __name__, url_prefix='/')


MainModel = MainModel()

@main_route.route('/login')
def login():
  """
  初期表示
  ログイン画面
  """
  return MainModel.login()

@main_route.route('/login_check', methods=['POST'])
def login_check():
  """
  ログイン認証
  """
  return MainModel.login_check()

@main_route.route('/top_page')
def top_page():
  """
  初期表示
  ログイン画面
  """
  return MainModel.top_page()

