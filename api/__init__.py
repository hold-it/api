from flask import Flask 
from api.routes.dev import _dev

def create_app(config_file=None):
    
    app = Flask(__name__)

    # config
    if (config_file is not None):
        app.config.from_pyfile(config_file, silent=True)
        
    app.register_blueprint(_dev, url_prefix='/dev')

    @app.route('/', methods=['GET'])
    def hello():
        return 'Hello!'

    return app 
