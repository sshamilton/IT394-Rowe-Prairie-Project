# Source: https://www.youtube.com/watch?v=qwE9TFNub84
from django import forms
from django.db import models
from .models import Position, Rooms, Cadets, Inspections, Gigs

class InspectionsForm(forms.ModelForm):
    class Meta:
        model = Inspections
        fields = ('room','Date','gigs','Pass','Comments')


class SubForm(forms.Form):
    X_Num = forms.CharField(max_length=5)
    class Meta:
        fields = ('X_Num')
        
