from flask_socketio import join_room, rooms, close_room, leave_room

class RoomManager:
  def __init__(self, rooms):
    self.rooms = self.__build_rooms(rooms)
  
  def join_room(self, room_id, sid):
    join_room(room_id)
    for room in self.rooms:
      if room['id'] == room_id:
        self.rooms.remove(room)
        room['sockets_connected'].append(sid)
        self.rooms.insert(0, room)
  
  def exit_room(self, room_id):
    leave_room(room_id)
  
  def room_state(self, room_id):
    for room in self.rooms:
      if room['id'] == room_id:
        return self.__check_connections(room)
    
    return False
  
  def __build_rooms(self, rooms):
    builded_rooms = []

    for room in rooms:
      room_info = {
        'id': str(room),
        'sockets_connected': [],
      }
      
      builded_rooms.append(room_info)
    
    return builded_rooms
  
  def __check_connections(self, room):
    state = False
    for connection in room['sockets_connected']:
      for socket_room in rooms(connection, '/'):
        if socket_room == room['id']:
          state = True
          
    if state == False:
      self.__remove_connection(room)
      close_room(room, '/')

    return state
  
  def __remove_connection(self, target_room):
    for room in self.rooms:
      if room['id'] == target_room['id']:
        self.rooms.remove(room)
        room['sockets_connected'] = []
        self.rooms.insert(0, room)