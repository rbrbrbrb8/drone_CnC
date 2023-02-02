from fastapi import FastAPI, Response , Depends, HTTPException
from fastapi.staticfiles import StaticFiles
import os

from DroneController.DroneController import DroneController
from pydantic import BaseModel
from DroneController.ManualSettings import Settings
# py -m uvicorn app:app --reload
root = os.path.dirname(os.path.abspath(__file__))
drone = DroneController('tcp','localhost','5762')

app = FastAPI()
#manual initial settings
settings = Settings()

#static dir
app.mount('/static',StaticFiles(directory='frontend/static'))

class Alt(BaseModel):
  alt:float

class Mode(BaseModel):
  mode:str  

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
    drone.enter_manual(settings)
  return {'data':res}

#brake
@app.post('/brake')
def brake():
  #change settings.active to false
  #change drone mode to guided
  pass

#move?

#return home?

#manual control