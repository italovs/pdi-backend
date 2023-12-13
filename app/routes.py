from flask import Blueprint, request, current_app, jsonify
from flask.templating import render_template
from app import BERTHS
from app import socket
from queue import Queue, Empty
from app.services.room_manager import RoomManager
import time
import threading
import json

main = Blueprint('main', __name__)

speed = 0
position_distance = 0

@main.route("/")
def index():
  return render_template("index.html", ids = BERTHS)

@main.route("/berth/<id>", methods=['GET'])
def berth(id):
  return render_template("berth.html", id = id)

@main.route("/dados", methods=['POST'])
def dados():
  global speed, position_distance
  body = json.loads(request.data.decode())
  print(body)
  speed = round(body["speed"], 2)
  position_distance = round(body["present_position"], 2)

  return jsonify({'status': 'success'})

@main.route("/berths", methods=['GET'])
def berths():
  berths_values = []
  for berth in BERTHS:
    berths_values.append(str(berth))

  berths_json = {
    "berths": berths_values
  }
  return berths_json

room_manager_main = RoomManager(BERTHS)
queue = Queue()
queue.put(room_manager_main)

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

@socket.on('leave')
def leave(room):
  try:
    room_manager = queue.get(block=False)
  except Empty:
    pass

  room_manager.exit_room(room)
  queue.put(room_manager)

def send_data(room, queue, app_context):
  global speed, position_distance
  app_context.push()
  room_manager = queue.get()
  queue.put(room_manager)
  state = True

  while(state):
    json = build_json(speed, speed, 0, position_distance, position_distance)
    socket.emit("message", json, to=room)
    
    time.sleep(1/30)

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