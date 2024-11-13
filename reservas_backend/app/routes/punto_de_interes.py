from flask import Blueprint, request, jsonify
from app.models import db, PuntoDeInteres

bp = Blueprint('puntos_de_interes', __name__, url_prefix='/puntos-de-interes')

@bp.route('/', methods=['GET'])
def get_puntos():
    puntos = PuntoDeInteres.query.all()
    output = [punto.__dict__ for punto in puntos]
    return jsonify(output), 200

@bp.route('/<int:id>', methods=['GET'])
def get_punto(id):
    punto = PuntoDeInteres.query.get_or_404(id)
    return jsonify(punto.__dict__), 200

@bp.route('/', methods=['POST'])
def add_punto():
    data = request.get_json()
    nuevo_punto = PuntoDeInteres(**data)
    db.session.add(nuevo_punto)
    db.session.commit()
    return jsonify({'message': 'Punto de interés agregado con éxito'}), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_punto(id):
    punto = PuntoDeInteres.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(punto, key, value)
    db.session.commit()
    return jsonify({'message': 'Punto de interés actualizado'}), 200

@bp.route('/<int:id>', methods=['DELETE'])
def delete_punto(id):
    punto = PuntoDeInteres.query.get_or_404(id)
    db.session.delete(punto)
    db.session.commit()
    return jsonify({'message': 'Punto de interés eliminado'}), 200
