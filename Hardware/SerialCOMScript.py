from serial import Serial
import firebase_admin
import time
import datetime
import ast
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("cred.json")

default_app = firebase_admin.initialize_app(cred,{
    'databaseURL': 'your database url'
})

ref = db.reference("/")

arduino = Serial('COM9', 9600, timeout=.1)

def toFirebase(Celsius,Fahrenheit):
    print(Celsius)
    print(Fahrenheit)
    print(datetime.datetime.now().time().strftime("%H:%M:%S"))
    timeNow = datetime.datetime.now().time()
    formattedTime = timeNow.strftime("%H:%M:%S")
    ref.update({'temp':{"Celsius": Celsius, "Fahrenheit": Fahrenheit, "time":str(formattedTime)}})

while True:
    data = arduino.readline()[:-2].decode("utf-8")
    if data!="":
        Celsius = ast.literal_eval(data)['Celsius']
        Fahrenheit = ast.literal_eval(data)['Fahrenheit']
        toFirebase(Celsius,Fahrenheit)
