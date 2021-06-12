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

