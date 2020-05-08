from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Position, Rooms, Cadets, Inspections, Gigs
from .forms import InspectionsForm, SubForm

# Create your views here.
def home(request):
    rooms_list = Rooms.objects.order_by('Barracks_Name')
    context = {'rooms_list': rooms_list}
    return render(request, 'AMIApp/home.html', context)

def allInspections(request):
    latest_inspections_list = Inspections.objects.order_by('-Date')[:100]
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

def get_subordinates(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            supX = form.cleaned_data['X_Num']
            sup = Cadets.objects.get(X_Num = supX)
            sub_list = Cadets.objects.filter(superior=sup)
            performance_list = []
            for sub in sub_list:
                p_sub_list = []
                passRate = '100'
                inspectionCount = '0'
                lastInspection = 'Never'
                if (len(sub_list) > 0):
                    inspections_list = Inspections.objects.filter(room=sub.room).order_by('-Date')
                    if (len(inspections_list) > 0):
                        lastInspection = str(inspections_list[0].Date)
                        passCount = 0
                        numInspections = len(inspections_list)
                        for inspection in inspections_list:
                            if (inspection.Pass == True):
                                passCount = passCount + 1
                        passRate = str(round(((passCount/numInspections)*100),2))
                    p_sub_list.append(sub.Name)
                    p_sub_list.append(passRate)
                    p_sub_list.append(str(len(inspections_list)))
                    p_sub_list.append(lastInspection)
                performance_list.append(p_sub_list)
            context = {'sub_list': sub_list, 'performance_list':performance_list}
            return render(request, 'AMIApp/subPerformance.html', context)
    else:
        form = SubForm()
    return render(request, 'AMIApp/sub.html', {'form':form})

# Barracks Views
def BradLong(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Brad Long')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)

def BradShort(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Brad_Short')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)

def Davis(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Davis')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)

def Eisenhower(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Eisenhower')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)

def Grant(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Grant')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)

def Lee(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Lee')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)

def MacLong(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Mac Long')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)

def MacShort(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Mac Short')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)

def Pershing(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Pershing')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)

def Scott(request):
    rooms_list = Rooms.objects.filter(Barracks_Name='Scott')
    first_room_list = rooms_list[:1]
    context = {'rooms_list': rooms_list, 'first_room_list':first_room_list}
    return render(request, 'AMIApp/Barracks.html', context)
