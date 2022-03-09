from flask import Flask
from route.main_route import main_route
from route.company_route import company_route
from datetime import timedelta
from common.middleware import before_request
from route.product_route import product_route
from route.quotation_route import quotation_route
from route.test_route import test_route

app = Flask(__name__, static_url_path='/enjoy_flask/static')
app.secret_key = 'hogehoge'


app.register_blueprint(main_route)
app.register_blueprint(company_route)
app.register_blueprint(product_route)
app.register_blueprint(quotation_route)
app.register_blueprint(test_route)

# app.permanent_session_lifetime = timedelta(minutes=120)
# app.before_request(before_request)

if __name__ == '__main__':
  app.debug = True
  app.run(host='127.0.0.1', port=5000)
