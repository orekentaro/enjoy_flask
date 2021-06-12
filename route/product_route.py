from flask import Blueprint
from models.product_model import ProductModel

product_route = Blueprint('product_route', __name__, url_prefix='/product')
ProductModel = ProductModel()


@product_route.route('product_list')
def product_list():
  """
  商品一覧表示ルート
  """
  return ProductModel.product_list()


@product_route.route('create_product')
def create_product():
  """
  商品追加
  """
  return ProductModel.create_product()

@product_route.route('create_product', methods=['POST'])
def create_product_complete():
  """
  商品追加処理
  """
  return ProductModel.create_product_complete()


@product_route.route('edit_product/<id>')
def edit_product(id):
  """
  商品編集
  """
  return ProductModel.edit_product(id)

@product_route.route('edit_product/<id>', methods=['POST'])
def edit_product_complete(id):
  """
  商品編集
  """
  return ProductModel.edit_product_complete(id)



