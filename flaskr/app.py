from flaskr.modelos.modelos import Album
from flaskr import create_app
from .modelos import db, Song, User, Album, Medium
from .modelos import AlbumSchema, SongSchema, UserSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#Prueba
with app.app_context():
    user = User(name='miguelcamargo9', password='123445')
    album = Album(title='Album1', year=2020, description='hola', medium=Medium.CD )
    album_schema = AlbumSchema()
    user_schema = UserSchema()
    song_schema = SongSchema()
    song = Song(title='Test', minutes=2, seconds=2, artist='Miguel Camargo')
    user.albums.append(album)
    album.songs.append(song)
    db.session.add(album)
    db.session.add(user)
    db.session.add(song)
    db.session.commit()
    print([album_schema.dumps(album) for album in Album.query.all()])
    print([song_schema.dumps(song) for song in Song.query.all()])
    print([user_schema.dumps(user) for user in User.query.all()])
    # print(Album.query.all())
    # print(Album.query.all()[0].songs)
    # print(Song.query.all())
    # print(User.query.all()[0].albums)
    # db.session.delete(user)
    # print(User.query.all())
    # print(Album.query.all())