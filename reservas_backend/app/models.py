from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PuntoDeInteres(db.Model):
    __tablename__ = 'puntos_de_interes'
    id_punto_interes = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    precio_entrada = db.Column(db.Float, nullable=True)
    horario = db.Column(db.String(255), nullable=True)
    rating_promedio = db.Column(db.Float, nullable=True)
    foto_url = db.Column(db.String(255), nullable=True)
    servicios = db.Column(db.Text, nullable=True)  # JSON como string

class Reseña(db.Model):
    __tablename__ = 'resenas'
    id_resena = db.Column(db.Integer, primary_key=True)
    id_punto_interes = db.Column(db.Integer, db.ForeignKey('puntos_de_interes.id_punto_interes'), nullable=False)
    comentario = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    fecha_resena = db.Column(db.DateTime, nullable=False)

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id_reserva = db.Column(db.Integer, primary_key=True)
    id_punto_interes = db.Column(db.Integer, db.ForeignKey('puntos_de_interes.id_punto_interes'), nullable=False)
    fecha_reserva = db.Column(db.DateTime, nullable=False)
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(50), nullable=False)

class Favorito(db.Model):
    __tablename__ = 'favoritos'
    id_favorito = db.Column(db.Integer, primary_key=True)
    id_punto_interes = db.Column(db.Integer, db.ForeignKey('puntos_de_interes.id_punto_interes'), nullable=False)
    fecha_guardado = db.Column(db.DateTime, nullable=False)
