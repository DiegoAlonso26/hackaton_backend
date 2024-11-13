from flask import Blueprint, request, jsonify
from app.models import db, Reseña

bp = Blueprint('resenas', __name__, url_prefix='/resenas')

@bp.route('/', methods=['GET'])
def get_resenas():
    resenas = Reseña.query.all()
    output = [resena.__dict__ for resena in resenas]
    return jsonify(output), 200

@bp.route('/<int:id>', methods=['GET'])
def get_resena(id):
    resena = Reseña.query.get_or_404(id)
    return jsonify(resena.__dict__), 200

@bp.route('/', methods=['POST'])
def add_resena():
    data = request.get_json()
    nueva_resena = Reseña(**data)
    db.session.add(nueva_resena)
    db.session.commit()
    return jsonify({'message': 'Reseña agregada con éxito'}), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_resena(id):
    resena = Reseña.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(resena, key, value)
    db.session.commit()
    return jsonify({'message': 'Reseña actualizada'}), 200

@bp.route('/<int:id>', methods=['DELETE'])
def delete_resena(id):
    resena = Reseña.query.get_or_404(id)
    db.session.delete(resena)
    db.session.commit()
    return jsonify({'message': 'Reseña eliminada'}), 200
