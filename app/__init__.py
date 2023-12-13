from flask import Flask
from flask_socketio import SocketIO
from ast import literal_eval
from os import environ
from flask_cors import CORS


socket = SocketIO(cors_allowed_origins="*")
BERTHS = literal_eval(environ.get('BERTHS'))

def create_app():
  app = Flask(__name__)
  CORS(app)

  from app.routes import main
  app.register_blueprint(main)
  
  socket.init_app(app)
  
  return app
