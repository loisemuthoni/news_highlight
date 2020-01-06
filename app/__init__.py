from flask import Flask
from config import config_options

  

# Initializing application
def create_app(config_name):
    app = Flask(__name__ )

    #setting up configuration
    app.config.from_object(config_options[config_name])
   
    
    #registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #setting config
    from .requests import configure_request
    configure_request(app)
    
    
    #will return the app
    return app


