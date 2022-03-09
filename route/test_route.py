from flask import Blueprint
from models.test_model import TestModel

test_route = Blueprint('test_route', __name__, url_prefix='/test')
TestModel = TestModel()


@test_route.route('/')
def test():
  return TestModel.test()

@test_route.route('/number/<name>')
def number(name):
  return TestModel.number(name)