import math,time
from pymavlink import mavutil
import threading
command_results = ['ACCEPTED','TEMP_REJECTED','DENIED','UNSUPPORTED','FAILED','IN_PROGRESS','CANCELLED']



def move(settings):
    #initially will hover
  print('moving...')
  print('active: ' + str(settings.active))
  while settings.active:
    settings.the_connection.mav.manual_settings_send(
    settings.the_connection.target_system,
    settings.pitch,
    settings.roll,
    settings.throttle,
    settings.yaw,
    0,
    0)
    time.sleep(0.2)

class DroneController:
  def __init__(self,protocol,host,port):
    self.connection_str ='{}:{}:{}'.format(protocol,host,port)
    self.mode='STABILIZE'
  
  def connect(self,settings):
    the_connection = mavutil.mavlink_connection(self.connection_str)
    success = False
    while(the_connection.target_system == 0):
      print('Checking heartbeat')
      the_connection.wait_heartbeat()
      print('heartbeat from system {system %u component %u}' % (the_connection.target_system,the_connection.target_component))
      success = True
    self.the_connection = the_connection
    settings.bind_connection(the_connection)
    return success

  def ack(self,keyword):
    msg = self.the_connection.recv_match(type=keyword,blocking=True)
    return command_results[msg.to_dict()['result']]

  def arm(self):
    print("Arming...")
    self.the_connection.mav.command_long_send(self.the_connection.target_system,self.the_connection.target_component,mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM
                                        ,0,1,0,0,0,0,0,0)

    return self.ack("COMMAND_ACK")
  
  def takeoff(self,takeoff_alt):
    print("Taking off...")

    self.the_connection.mav.command_long_send(self.the_connection.target_system,self.the_connection.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF
                                       ,0,0,0,0,math.nan,0,0,takeoff_alt)

    return self.ack("COMMAND_ACK")

  def change_mode(self,mode):
    print("Changing Mode to ",mode)
    self.mode = mode
    mode_id = self.the_connection.mode_mapping()[mode]
    self.the_connection.mav.set_mode_send(self.the_connection.target_system,mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,mode_id)
    return self.ack("COMMAND_ACK")

  def get_altitude(self):
    self.the_connection.mav.command_long_send(self.the_connection.target_system, self.the_connection.target_component,
          mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE, 0,
          33,
          0, 
          0, 0, 0, 0, 
          0)
    # ack(self.the_connection,"COMMAND_ACK")
    hasAltitude = False
    altitude = 0

    while not hasAltitude:
      msg = self.the_connection.recv_match() 
      if not msg:
        continue
      if msg.get_type() == 'GLOBAL_POSITION_INT':
        # print(msg.get_type())
        altitude = msg.to_dict()["relative_alt"]/1000
        # print('alt: ',msg.to_dict()["relative_alt"])
        hasAltitude = True
    # print('exited the loop')
    return altitude

  def enter_manual(self,settings):
    self.thread = threading.Thread(target=move,args=(settings,))
    self.thread.start()

  def exit_manual(self):
    self.thread.join()
