from flask import Blueprint
from models.quotation_model import QuotationModel

quotation_route = Blueprint('quotation_route', __name__, url_prefix='/quotation')
QuotationModel = QuotationModel()


@quotation_route.route('quotation_list')
def quotation_list():
  return QuotationModel.quotation_list()