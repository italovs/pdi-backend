from flask import Blueprint
from flask_socketio import join_room
import random
import time
import threading

BERTHS = [1, 2, 3]
rooms = []

socket_bp = Blueprint('socket_bp', __name__)

from app import socket

@socket.on('join')
def join(room):
  if (room in rooms):
    join_room(room)
  else:
    thread = threading.Thread(target=send_data, args=(room))
    rooms.append(room)
    join_room(room)
    thread.start()
    
def send_data(room):
  x = True
  i = 0
  while(x):
    msg = random.randrange(0, 100)
    socket.emit("message", i, to=room)
    time.sleep(1)
    
    i = i+1
    if(i == 100):
      x = False
  rooms.remove(room)