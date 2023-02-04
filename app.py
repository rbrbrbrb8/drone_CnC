from fastapi import FastAPI, Response , Depends, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import threading,time

from DroneController.DroneController import DroneController
from pydantic import BaseModel
from DroneController.ManualSettings import Settings
# py -m uvicorn app:app --reload
root = os.path.dirname(os.path.abspath(__file__))
drone = DroneController('tcp','localhost','5762')

app = FastAPI()
#manual initial settings
settings = Settings()

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

#static dir
app.mount('/static',StaticFiles(directory='frontend/static'))

class Alt(BaseModel):
  alt:float

class Mode(BaseModel):
  mode:str  

class Directions(BaseModel):
  pitch:int
  roll:int

def check_connected():
  if(not hasattr(drone,'the_connection')):
    return False
  return True

#enter main page V
@app.get('/')
def home():
  with open(os.path.join(root,'frontend','src','index.html')) as fh:
    data = fh.read()
  return Response(content=data,media_type='text/html')

#connect
@app.post('/connect')
def connect():
  res =drone.connect(settings)
  return {'success':res}

#get current altitude
@app.get('/getAltitude')
def getAltitude():
  if(not check_connected()):
    return {'result':0}
  res= drone.get_altitude()
  return {'result':res}
  # return random.randint(8,9)
  

#takeoff
@app.post('/takeoff')
def takeoff(alt:Alt):
  print('alt: ' + str(alt.alt))
  drone.change_mode('GUIDED')
  drone.arm()
  res = drone.takeoff(alt.alt)
  return {'result':res}

#land
@app.post('/land')
def land():
  res = drone.change_mode('LAND')
  return {'result':res}

#change mode
@app.post('/changeMode')
def change_mode(mode:Mode):
  res =drone.change_mode(mode.mode)
   
  if mode.mode == 'ALT_HOLD':
    print('starting manual hover')
    settings.active = True
    # drone.enter_manual(settings)
    drone.thread = threading.Thread(target=move,args=(settings,))
    drone.thread.start()
  else:
    settings.active = False
    if hasattr(drone,'thread'):
      drone.thread.join()
  return {'data':res}


#change direction
@app.post('/changeDirection')
def change_direction_manual(directions:Directions):
  settings.change_direction(directions.pitch,directions.roll)
  return {'res':{'pitch':settings.pitch,'roll':settings.roll}}

#move?

#return home?

#manual control