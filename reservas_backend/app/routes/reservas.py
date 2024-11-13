from flask import Blueprint, request, jsonify
from app.models import db, Reserva

bp = Blueprint('reservas', __name__, url_prefix='/reservas')

@bp.route('/', methods=['GET'])
def get_reservas():
    reservas = Reserva.query.all()
    output = [reserva.__dict__ for reserva in reservas]
    return jsonify(output), 200

@bp.route('/<int:id>', methods=['GET'])
def get_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    return jsonify(reserva.__dict__), 200

@bp.route('/', methods=['POST'])
def add_reserva():
    data = request.get_json()
    nueva_reserva = Reserva(**data)
    db.session.add(nueva_reserva)
    db.session.commit()
    return jsonify({'message': 'Reserva agregada con éxito'}), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(reserva, key, value)
    db.session.commit()
    return jsonify({'message': 'Reserva actualizada'}), 200

@bp.route('/<int:id>', methods=['DELETE'])
def delete_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify({'message': 'Reserva eliminada'}), 200
