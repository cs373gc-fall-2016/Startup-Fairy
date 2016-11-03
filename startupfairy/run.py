from flask import Flask
from views import public_views
from models import *
def create_app():
    app = Flask(__name__)
    app.register_blueprint(public_views)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sweteam:sweteamajmal@localhost/startupfairydb3"
    db.init_app(app)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
