import os
from dotenv import load_dotenv
from flask import Flask



# Load user environment variables
load_dotenv()


# Make sure API keys are set
if not os.environ.get("IEX_KEY"):
    raise RuntimeError("IEX_KEY is not set!")
if not os.environ.get("POLYGON_KEY"):
    raise RuntimeError("POLYGON_KEY is not set!")
 
 
# Configure application
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'papertrade.sqlite'),
    ) 
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import platform
    app.register_blueprint(platform.bp)
    app.add_url_rule('/', endpoint='index')

    return app

