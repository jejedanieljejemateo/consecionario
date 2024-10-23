#this file have de operation object
#importamos los modelos del archivo models
from . import models
def create_user(name, brand, brach):
    car = models.Car(name, brand, brach)

