from flask import Flask
from app.models import db
from app.routes.punto_de_interes import bp as puntos_bp
from app.routes.resenas import bp as resenas_bp
from app.routes.reservas import bp as reservas_bp
from app.routes.favoritos import bp as favoritos_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:26112004@localhost/hackaton'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(puntos_bp, url_prefix='/api/puntos')
    app.register_blueprint(resenas_bp, url_prefix='/api/resenas')
    app.register_blueprint(reservas_bp, url_prefix='/api/reservas')
    app.register_blueprint(favoritos_bp, url_prefix='/api/favoritos')

    with app.app_context():
        db.create_all()

    return app
