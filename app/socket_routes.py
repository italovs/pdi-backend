from flask import Blueprint, request, current_app
from queue import Queue, Empty
from app.services.room_manager import RoomManager
from app import socket, BERTHS
import time
import threading

room_manager_main = RoomManager(BERTHS)
queue = Queue()
queue.put(room_manager_main)

socket_bp = Blueprint('socket_bp', __name__)

@socket.on('join')
def join(room):
  try:
    room_manager = queue.get(block=False)
  except Empty:
    pass
  
  if room_manager.room_state(room):
    room_manager.join_room(room, request.sid)
    queue.put(room_manager)
  else:
    room_manager.join_room(room, request.sid)
    queue.put(room_manager)
    thread = threading.Thread(target=send_data, args=(room, queue, current_app.app_context()))
    thread.start()
    
def send_data(room, queue, app_context):
  app_context.push()
  room_manager = queue.get()
  queue.put(room_manager)
  state = True
  j = 0 

  while(state):
    json = build_json(j, j, j, j, j)
    socket.emit("message", json, to=room)
    
    time.sleep(1)

    j = j+1
    try:
      room_manager = queue.get(block=False)
    except Empty:
      pass

    state = room_manager.room_state(room)
    queue.put(room_manager)
  
def build_json(speed_a, speed_b, angle, distance_a, distance_b):
  return {
    "velocity": {
      "a": speed_a,
      "b": speed_b,
      "unit": "cm/s"
    },
    "distance": {
      "a": distance_a,
      "b": distance_b,
      "unit": "m"      
    },
    "angle": {
      "value": angle,
      "unit": "°"
    }
  }