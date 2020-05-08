from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Position, Cadet_Has_Superior, Rooms, Cadets, Inspections, Gigs
from .forms import InspectionsForm

# Create your views here.
def home(request):
    rooms_list = Rooms.objects.order_by('Barracks_Name')
    context = {'rooms_list': rooms_list}
    return render(request, 'AMIApp/home.html', context)

def allInspections(request):
    latest_inspections_list = Inspections.objects.order_by('-Date')
    context = {'latest_inspections_list': latest_inspections_list}
    return render(request, 'AMIApp/index.html', context)

def detail(request, inspections_id):
    inspection = get_object_or_404(Inspections, pk=inspections_id)
    return render(request, 'AMIApp/detail.html', {'inspection': inspection})

# Source: https://www.youtube.com/watch?v=qwE9TFNub84
# Source: https://stackoverflow.com/questions/45256493/post-request-done-successfully-but-data-not-saved-in-database
def get_inspection(request):
    if request.method == 'POST':
        form = InspectionsForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save(commit=True)
            return redirect('/AMIApp/')
            #return render(request, 'AMIApp/index.html')
    else:
        form = InspectionsForm()
    return render(request, 'AMIApp/enterInspection.html', {'form':form})

def allBarracks(request):
    return render(request, 'AMIApp/allBarracks.html')

def Davis(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Davis')
    context = {'rooms_list': rooms_list}
    return render(request, 'AMIApp/Davis.html', context)

def roomRecord(request, rooms_id):
    room = Rooms.objects.filter(pk=rooms_id)
    inspections_list = Inspections.objects.filter(room=rooms_id).order_by('-Date')
    passRate = '100'
    if (len(inspections_list) > 0):
        passCount = 0
        numInspections = len(inspections_list)
        for inspection in inspections_list:
            if (inspection.Pass == True):
                passCount = passCount + 1
        passRate = str(round(((passCount / numInspections)*100),2))
    context = {'inspections_list': inspections_list, 'room':room, 'passRate':passRate}
    return render(request, 'AMIApp/roomRecord.html', context)

def cadetRecord(request, X_Num):
    return HttpResponse("You're looking at the inspection record for the cadet with X Number: "+X_Num)




