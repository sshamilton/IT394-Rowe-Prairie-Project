from django.db import models

# Create your models here.
class Position(models.Model):
    Position_Title = models.CharField(max_length=200)


class Cadet_Has_Superior(models.Model):
    CDT_X_Num = models.CharField(max_length=6)
    CDT_Sup_X_Num = models.CharField(max_length=6)


class Rooms(models.Model):
    Barracks_Name = models.CharField(max_length=100)
    Room_Number = models.PositiveSmallIntegerField()


class Cadets(models.Model):
    Name = models.CharField(max_length=200)
    X_Num = models.CharField(max_length=6)
    Barracks_Name = models.CharField(max_length=20)
    Room_Number = models.PositiveSmallIntegerField()
    position = models.ForeignKey(Position,on_delete=models.DO_NOTHING)
    cadet_has_superior =  models.ForeignKey(Cadet_Has_Superior,on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Rooms,on_delete=models.DO_NOTHING)


class Inspections(models.Model):
    room = models.ForeignKey(Rooms,on_delete=models.DO_NOTHING)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    Pass = models.BooleanField()
    Comments = models.CharField(max_length=5000)


class Gigs(models.Model):
    inspection = models.ManyToManyField(Inspections)
    Gig_Name = models.CharField(max_length=1000)
