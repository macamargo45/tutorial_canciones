from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __repr__(self):
        return "{} - {} - {} - {}".format(self.titulo, self.minutos, self.segundos, self.interprete)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(128))
    contrasena = db.Column(db.String(128))

    def __repr__(self):
        return "{} - {} - {} - {}".format(self.nombre_usuario, self.contrasena)

class Medio(enum.Enum):
   DISCO = 1
   CASETE = 2
   CD = 3

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    ano = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    medio = db.Column(db.Enum(Medio))

    def __repr__(self):
        return "{} - {} - {} - {}".format(self.nombre_usuario, self.contrasena)

