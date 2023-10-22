from flask_socketio import join_room, rooms, close_room

class RoomManager:
  def __init__(self, rooms):
    self.rooms = self.build_rooms(rooms)
  
  def join_room(self, room_id, sid):
    join_room(room_id)
    for room in self.rooms:
      if room['id'] == room_id:
        self.rooms.remove(room)
        room['sockets_connected'].append(sid)
        self.rooms.insert(0, room)
  
  def room_state(self, room_id):
    for room in self.rooms:
      if room['id'] == room_id:
        return self.check_connections(room)
    
    return False
  
  def build_rooms(self, rooms):
    builded_rooms = []

    for room in rooms:
      room_info = {
        'id': str(room),
        'sockets_connected': [],
      }
      
      builded_rooms.append(room_info)
    
    return builded_rooms
  
  def check_connections(self, room):
    state = False
    for connection in room['sockets_connected']:
      for socket_room in rooms(connection, '/'):
        if socket_room == room['id']:
          state = True
          
    if state == False:
      self.remove_connection(room)
      close_room(room, '/')

    return state
  
  def remove_connection(self, target_room):
    for room in self.rooms:
      if room['id'] == target_room['id']:
        self.rooms.remove(room)
        room['sockets_connected'] = []
        self.rooms.insert(0, room)