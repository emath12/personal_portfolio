from flask import Flask

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'kaity!'
    app.secret_key = 'kaity!'
    app.config['SESSION_TYPE'] = 'filesystem'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app 


