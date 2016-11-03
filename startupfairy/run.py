from flask import Flask
from views import public_views
def create_app():
    app = Flask(__name__)
    app.register_blueprint(public_views)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=80)
