import math,time
from pymavlink import mavutil

class mission_item:
  def __init__(self,i,command,current,x,y,z):
    self.seq = i
    self.frame = mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
    self.command = mavutil.mavlink.MAV_CMD_NAV_WAYPOINT
    self.current = current
    self.auto = 1
    self.param1 = 0.0
    self.param2 = 2.00
    self.param3 = 0
    self.param4 = math.nan
    self.param5 = x
    self.param6 = y
    self.param7 = z
    self.mission_type = 0

def arm(the_connection):
  print("Arming...")

  the_connection.mav.command_long_send(the_connection.target_system,the_connection.target_component,mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM
                                       ,0,1,0,0,0,0,0,0)

  ack(the_connection,"COMMAND_ACK")

def takeoff(the_connection):
  print("Taking off...")

  the_connection.mav.command_long_send(the_connection.target_system,the_connection.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF
                                       ,0,0,0,0,math.nan,0,0,10)

  ack(the_connection,"COMMAND_ACK")

# def change_alt(the_connection,newAlt,direction):
#   print("Changing Altitude to ",newAlt)

#   the_connection.mav.command_long_send(the_connection.target_system,the_connection.target_component,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT
#                                        ,0,0,0,0,0,0,0,newAlt)

#   ack(the_connection,"COMMAND_ACK")

def set_guided(the_connection):
  print("Changing Mode to Guided")
  mode = 'GUIDED'
  mode_id = the_connection.mode_mapping()[mode]
  # the_connection.mav.command_long_send(the_connection.target_system,the_connection.target_component,mavutil.mavlink.MAV_CMD_DO_SET_MODE
  #                                      ,0,mode_id,0,0,0,0,0,0)
  the_connection.mav.set_mode_send(the_connection.target_system,mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,mode_id)
  ack(the_connection,"COMMAND_ACK")


def change_mode(the_connection,mode):
  print("Changing Mode to ",mode)
  mode_id = the_connection.mode_mapping()[mode]
  # the_connection.mav.command_long_send(the_connection.target_system,the_connection.target_component,mavutil.mavlink.MAV_CMD_DO_SET_MODE
  #                                      ,0,mode_id,0,0,0,0,0,0)
  the_connection.mav.set_mode_send(the_connection.target_system,mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,mode_id)
  ack(the_connection,"COMMAND_ACK")

def ack(the_connection,keyword):
  print("Message Read " + str(the_connection.recv_match(type=keyword,blocking=True)))


def get_height(the_connection):
  the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE, 0,
        33,
        0, 
        0, 0, 0, 0, 
        0)
  # ack(the_connection,"COMMAND_ACK")
  hasHeight = False
  height = 0

  while not hasHeight:
    msg = the_connection.recv_match() 
    if not msg:
      continue
    if msg.get_type() == 'GLOBAL_POSITION_INT':
      # print(msg.get_type())
      height = msg.to_dict()["relative_alt"]/1000
      # print('alt: ',msg.to_dict()["relative_alt"])
      hasHeight = True
  # print('exited the loop')
  return height
 

if __name__ == "__main__":
  print("Program Started")
  the_connection = mavutil.mavlink_connection('tcp:localhost:5762')

  while(the_connection.target_system == 0):
    print('Checking heartbeat')
    the_connection.wait_heartbeat()
    print('heartbeat from system {system %u component %u}' % (the_connection.target_system,the_connection.target_component))

  set_guided(the_connection)

  arm(the_connection)

  takeoff(the_connection)


  
  time.sleep(10)
  change_mode(the_connection,'LAND')

  while True:
    try:
        print('Current Height: ',get_height(the_connection))
    except:
        pass
    time.sleep(0.5)
  # change_alt(the_connection,50,1)

  # change_alt(the_connection,30,10)

  # change_alt(the_connection,100,20)

  #MAV_CMD_NAV_LAND