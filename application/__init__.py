from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    # --------------------------------------------------------------------------
    # Blueprints Registration:
    # --------------------------------------------------------------------------
    from application.api import api, views
    from application.auth import auth, views

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(auth, url_prefix='/auth')

    return app
