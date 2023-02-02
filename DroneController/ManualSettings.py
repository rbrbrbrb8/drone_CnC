class Settings:
  def __init__(self):
    self.throttle = 500
    self.pitch = 0
    self.roll = 0
    self.yaw = 0
    self.active = True
  
  def change_direction(self,pitch,roll):
    self.pitch = pitch
    self.roll = roll

  def exit_manual(self):
    self.active = False

  def bind_connection(self,the_connection):
    self.the_connection = the_connection