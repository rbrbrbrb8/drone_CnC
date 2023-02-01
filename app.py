from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
import os
import random

from DroneController.DroneController import DroneController
from pydantic import BaseModel
# py -m uvicorn app:app --reload
root = os.path.dirname(os.path.abspath(__file__))
drone = DroneController('tcp','localhost','5762')

app = FastAPI()

app.mount('/static',StaticFiles(directory='frontend/static'))

class Alt(BaseModel):
  alt:float



#enter main page V
@app.get('/')
def home():
  with open(os.path.join(root,'frontend','src','index.html')) as fh:
    data = fh.read()
  return Response(content=data,media_type='text/html')

#connect
@app.post('/connect')
def connect():
  drone.connect()
  return {'success':True}

#get current altitude
@app.get('/getAltitude')
def getAltitude():
  # return drone.get_altitude()
  return random.randint(8,9)
  

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
def change_mode(alt:int):
  return {'data':alt}


#move?

#return home?

#manual control?