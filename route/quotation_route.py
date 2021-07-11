from flask import Blueprint
from models.quotation_model import QuotationModel

quotation_route = Blueprint('quotation_route', __name__, url_prefix='/quotation')
QuotationModel = QuotationModel()


@quotation_route.route('quotation_list')
def quotation_list():
  return QuotationModel.quotation_list()

@quotation_route.route('create_quotation')
def create_quotation():
  return QuotationModel.create_quotation()

@quotation_route.route('get_price', methods=['POST'])
def get_price():
  return QuotationModel.get_price()