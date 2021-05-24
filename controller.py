from flask import Flask
from route.main_route import main_route
from route.company_route import company_route
from datetime import timedelta

app = Flask(__name__, static_url_path='/enjoy_flask/static')
app.secret_key = 'hogehoge'  # セッションが動かなかったんで仮で置きました。


app.register_blueprint(main_route)
app.register_blueprint(company_route)

app.permanent_session_lifetime = timedelta(minutes=120)

if __name__ == '__main__':
  app.debug = True
  app.run(host='127.0.0.1', port=5000)
