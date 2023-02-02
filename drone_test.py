import math,time
import threading
from pymavlink import mavutil
# Imports for attitude
from pymavlink.quaternion import QuaternionBase

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
 
def set_target_depth(the_connection,depth):
    """ Sets the target depth while in depth-hold mode.

    Uses https://mavlink.io/en/messages/common.html#SET_POSITION_TARGET_GLOBAL_INT

    'depth' is technically an altitude, so set as negative meters below the surface
        -> set_target_depth(-1.5) # sets target to 1.5m below the water surface.

    """
    the_connection.mav.set_position_target_global_int_send(
        int(1e3 * (time.time() - boot_time)), # ms since boot
        the_connection.target_system, the_connection.target_component,
        coordinate_frame=mavutil.mavlink.MAV_FRAME_GLOBAL_INT,
        type_mask=( # ignore everything except z position
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_X_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_Y_IGNORE |
            # DON'T mavutil.mavlink.POSITION_TARGET_TYPEMASK_Z_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VX_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VY_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VZ_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AX_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AY_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AZ_IGNORE |
            # DON'T mavutil.mavlink.POSITION_TARGET_TYPEMASK_FORCE_SET |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE
        ), lat_int=0, lon_int=0, alt=depth, # (x, y WGS84 frame pos - not used), z [m]
        vx=0, vy=0, vz=0, # velocities in NED frame [m/s] (not used)
        afx=0, afy=0, afz=0, yaw=0, yaw_rate=0
        # accelerations in NED frame [N], yaw, yaw_rate
        #  (all not supported yet, ignored in GCS Mavlink)
    )

def set_target_attitude(the_connection,roll, pitch, yaw):
    """ Sets the target attitude while in depth-hold mode.

    'roll', 'pitch', and 'yaw' are angles in degrees.

    """
    the_connection.mav.set_attitude_target_send(
        int(1e3 * (time.time() - boot_time)), # ms since boot
        the_connection.target_system, the_connection.target_component,
        # allow throttle to be controlled by depth_hold mode
        mavutil.mavlink.ATTITUDE_TARGET_TYPEMASK_THROTTLE_IGNORE,
        # -> attitude quaternion (w, x, y, z | zero-rotation is 1, 0, 0, 0)
        QuaternionBase([math.radians(angle) for angle in (roll, pitch, yaw)]),
        0, 0, 0, 1 # roll rate, pitch rate, yaw rate, thrust
    )





boot_time = time.time()

class Settings:
  def __init__(self,the_connection):
    self.throttle = 500
    self.pitch = 0
    self.roll = 0
    self.yaw = 0
    self.active = True
    self.the_connection = the_connection
  
  def change_direction(self,pitch,roll):
    self.pitch = pitch
    self.roll = roll

  def brake(self):
    self.active = False
    change_mode(self.the_connection,'GUIDED')


def move(control):
    #initially will hover
    print('moving...')
    print('active: ' + str(control.active))
    while control.active:
      control.the_connection.mav.manual_control_send(
      control.the_connection.target_system,
      control.pitch,
      control.roll,
      control.throttle,
      control.yaw,
      0,
      0)
      time.sleep(0.2)



if __name__ == "__main__":
  print("Program Started")
  the_connection = mavutil.mavlink_connection('tcp:localhost:5762')
  

  while(the_connection.target_system == 0):
    print('Checking heartbeat')
    the_connection.wait_heartbeat()
    print('heartbeat from system {system %u component %u}' % (the_connection.target_system,the_connection.target_component))

  set_guided(the_connection)
  # mission_waypoint = mission_item(0,0,-35.0,149.0,10)

  # upload_mission(the_connection,mission_waypoint)

  arm(the_connection)



  # the_connection.arducopter_arm()

  # the_connection.motors_armed_wait()

 

  # set_target_depth(the_connection,100)

  # the_connection.motors_armed_wait()

  takeoff(the_connection)
  control = Settings(the_connection)

  time.sleep(10)
  print('trying to move')
  pitch = 500
  roll = 0
  yaw = 0
  throttle = 500
  
  change_mode(the_connection,'ALT_HOLD')
  active=[True]
  thread = threading.Thread(target=move,args=(control,))
  thread.start()
  time.sleep(5)
  print('changing direction...')
  control.change_direction(500,0)
  time.sleep(5)
  print('changing direction...')
  control.change_direction(0,500)
  time.sleep(5)
  print('braking...')
  control.brake()
  # set_target_attitude(the_connection,30,0,0)
  thread.join()

  # start_mission(the_connection)
  
  # time.sleep(10)
  # change_mode(the_connection,'LAND')

  # while True:
  #   try:
  #       print('Current Height: ',get_height(the_connection))
  #   except:
  #       pass
  #   time.sleep(0.5)
  # change_alt(the_connection,50,1)

  # change_alt(the_connection,30,10)

  # change_alt(the_connection,100,20)

  #MAV_CMD_NAV_LAND