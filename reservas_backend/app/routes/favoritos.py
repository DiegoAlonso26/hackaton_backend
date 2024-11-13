from flask import Blueprint, request, jsonify
from app.models import db, Favorito

bp = Blueprint('favoritos', __name__, url_prefix='/favoritos')

@bp.route('/', methods=['GET'])
def get_favoritos():
    favoritos = Favorito.query.all()
    output = [favorito.__dict__ for favorito in favoritos]
    return jsonify(output), 200

@bp.route('/<int:id>', methods=['GET'])
def get_favorito(id):
    favorito = Favorito.query.get_or_404(id)
    return jsonify(favorito.__dict__), 200

@bp.route('/', methods=['POST'])
def add_favorito():
    data = request.get_json()
    nuevo_favorito = Favorito(**data)
    db.session.add(nuevo_favorito)
    db.session.commit()
    return jsonify({'message': 'Favorito agregado con éxito'}), 201

@bp.route('/<int:id>', methods=['DELETE'])
def delete_favorito(id):
    favorito = Favorito.query.get_or_404(id)
    db.session.delete(favorito)
    db.session.commit()
    return jsonify({'message': 'Favorito eliminado'}), 200
