# Source: https://www.youtube.com/watch?v=qwE9TFNub84
from django import forms
from django.db import models
from .models import Position, Cadet_Has_Superior, Rooms, Cadets, Inspections, Gigs

class InspectionsForm(forms.ModelForm):
    #Pass = forms.BooleanField()
    #Comments = forms.CharField(max_length=5000)
    class Meta:
        model = Inspections
        fields = ('room','Date','gigs','Pass','Comments')
