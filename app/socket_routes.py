from flask import Blueprint
from flask_socketio import join_room

import time
import threading

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
    json = build_json(i,i,i,i,i)
    socket.emit("message", json, to=room)
    
    time.sleep(1)
    
    i = i+1
    if(i == 100):
      x = False
  rooms.remove(room)
  
def build_json(speed_a, speed_b, angle, distance_a, distance_b):
  return {
    "distance_a": distance_a,
    "distance_b": distance_b,
    "speed_a": speed_a,
    "speed_b": speed_a,
    "angle": angle,
  }