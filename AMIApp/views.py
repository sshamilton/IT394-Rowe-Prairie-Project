from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Position, Cadet_Has_Superior, Rooms, Cadets, Inspections, Gigs
from .forms import InspectionsForm

# Create your views here.
def index(request):
    latest_inspections_list = Inspections.objects.order_by('-Date')
    context = {'latest_inspections_list': latest_inspections_list}
    template = loader.get_template('AMIApp/index.html')
    return render(request, 'AMIApp/index.html', context)

def detail(request, inspections_id):
    inspection = get_object_or_404(Inspections, pk=inspections_id)
    return render(request, 'AMIApp/detail.html', {'inspection': inspection})

# Source: https://www.youtube.com/watch?v=qwE9TFNub84
class EnterInspectionView(TemplateView):
    def get(request):
        form = InspectionsForm()
        return render(request, 'AMIApp/enterInspection2.html', {'form':form})
    def post(request):
        form = InspectionsForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            Date = form.cleaned_data['Date']
            gigs = form.cleaned_data['gigs']
            Pass = form.cleaned_data['Pass']
            Comments = form.cleaned_data['Comments']
            return render(request, 'AMIApp/')
        args = {'form':form, 'room':room, 'Date':Date, 'gigs':gigs, 'Pass':Pass, 'Comments':Comments}
        return render(request, 'AMIApp/enterInspections.html', args)
    
def enterInspection(request):
    rooms_list = Rooms.objects.order_by('Barracks_Name')
    gigs_list = Gigs.objects.order_by('Gig_Name')
    context = {'rooms_list':rooms_list, 'gigs_list': gigs_list}
    return render(request, 'AMIApp/enterInspection.html', context)

def roomRecord(request, Room_Number):
    room = get_object_or_404(Rooms, pk=Room_Number)
    return HttpResponse("You're looking at the inspection record for room: "+str(Room_Number)+" of "+Barracks_Name+" Barracks.")

def cadetRecord(request, X_Num):
    return HttpResponse("You're looking at the inspection record for the cadet with X Number: "+X_Num)




