from flask import Flask
from flask_socketio import SocketIO

socket = SocketIO()

def create_app():
  app = Flask(__name__)

  from app.routes import main
  app.register_blueprint(main)
  
  from app.socket_routes import socket_bp
  app.register_blueprint(socket_bp)
  
  socket.init_app(app)
  
  return app
