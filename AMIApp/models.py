from django.db import models

# Create your models here.
class Position(models.Model):
    Position_Title = models.CharField(max_length=200)
    def __str__(self):
        return self.Position_Title


class Rooms(models.Model):
    Barracks_Name = models.CharField(max_length=100)
    Room_Number = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.Barracks_Name+" "+str(self.Room_Number)


class Cadets(models.Model):
    Name = models.CharField(max_length=200)
    X_Num = models.CharField(max_length=5)
    position = models.ForeignKey(Position,on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Rooms,blank=True,null=True,on_delete=models.DO_NOTHING)
    superior = models.ForeignKey('self',blank=True,null=True,on_delete=models.DO_NOTHING)
    def __str__(self):
        return "CDT "+self.Name+", x"+self.X_Num


class Gigs(models.Model):
    Gig_Name = models.CharField(max_length=2000)
    def __str__(self):
        return self.Gig_Name


class Inspections(models.Model):
    room = models.ForeignKey(Rooms,on_delete=models.DO_NOTHING)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    gigs = models.ManyToManyField(Gigs)
    Pass = models.BooleanField()
    Comments = models.CharField(max_length=5000)
    def __str__(self):
        passReturn = "Pass"
        if (self.Pass == 0):
            passReturn = "Fail"
        elif (self.Pass == 1):
            passReturn = "Pass"
        return str(self.Date)+" "+passReturn+", Comments: "+self.Comments
