from django.db import models


class Rooms(models.Model):
    Barracks_Name = models.CharField(max_length=25)
    Room_Number = models.IntegerField(default=0)


##Inspection Branch##

class Inspections(models.Model):
    Date = models.DateTimeField('Date Inspected: ')
    Pass = models.BooleanField(db_index=True, default=False)
    Comments = models.CharField(max_length=200)

##In case of deleted entry/room##
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)

class Gigs(models.Model):
    Gig_Name = models.IntegerField(default=0)



##Cadet Branch##

class Cadets(models.Model):
    Name = models.CharField(max_length=30)
    X_Num = models.IntegerField(default=0)
    Barracks_Name = models.CharField(max_length=25)
    Room_Number = models.IntegerField(default=0)
    cadet = models.ForeignKey(Cadets, on_delete=models.CASCADE)

class Cadet_Has_Superior(models.Model):
    CDT_X_Num = models.IntegerField(default=0)
    CDT_Sup_X_Num = models.IntegerField(default=0)

class Position(models.Model):
    Position_Title = models.CharField(max_length=25)
