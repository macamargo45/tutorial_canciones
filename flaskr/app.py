from flaskr import create_app
from .modelos import db, Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#Prueba
with app.app_context():
    cancion = Cancion(titulo='Preuba', minutos=2, segundos=2, interprete='Miguel Camargo')
    db.session.add(cancion)
    db.session.commit()
    print(Cancion.query.all())