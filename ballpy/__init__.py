from flask import Flask
from flask_migrate import Migrate


    # factory 
def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:boilerplate@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db) 



    # # index route
    # @app.route('/reptile')
    # def index(): 
    #     return 'Welcome to Ball.py Reptile zoo!'
    
    # register reptile blueprint 
    from . import reptiles
    app.register_blueprint(reptiles.bp) 


    # return the app 
    return app