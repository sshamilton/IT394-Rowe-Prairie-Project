from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from .models import *

class RoomsModelTests(TestCase):
    def cadet_has_room(self):
        # Returns True if room registers correctly
        roomOne = Rooms(Barracks_Name="Davis",Room_Number="101")
        cadetOne = Cadets(Name="John Doe",X_Num="00001",room=roomOne)
        cadetRoom = cadetOne.room
        cadetRoom = Rooms.objects.get(rooms_id=cadetRoom)
        testReturn = False
        if (roomOne.id == cadetRoom.id):
            testReturn = False
        else:
            testReturn = True
        return testReturn

class InspectionsModelTests(TestCase):
    def room_has_inspection(self):
        roomTwo = Rooms(Barracks_Name="Davis",Room_Number="102")
        inspectionOne = Inspections(Date=2020-05-08,Pass=1,Comments="Good room.",room=roomTwo.id)
        inspectionsList = Inspections.objects.filter(room=roomTwo)
        if (len(inspectionsList) == 1):
            return True
        else:
            return False

class CadetsModelTests(TestCase):
    def cadet_has_inspection(self):
        roomThree = Rooms(Barracks_Name="Davis",Room_Number="103")
        inspectionTwo = Inspections(Date=2020-05-08,Pass=1,Comments="Good room.",room=roomTwo.id)
        cadetTwo = Cadets(Name="Jane Doe",X_Num="00002",room=roomThree)
        cadetRoom = cadetTwo.room
        inspectionsList = Inspections.objects.filter(room=cadetRoom)
        if (len(inspectionsList) == 1):
            return True
        else:
            return False
