from django.urls import path

from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Index
    path('allInspections/', views.allInspections, name='allInspections'),
    # Detail
    path('<int:inspections_id>/', views.detail, name='detail'),
    # Enter Inspection
    path('enterInspection/', views.get_inspection, name='enterInspection'),
    # All Barracks
    path('allBarracks/', views.allBarracks, name='allBarracks'),
    # Brad Long Barracks
    path('Brad_Long/', views.BradLong, name='Brad_Long'),
    # Brad Short Barracks
    path('Brad_Short/', views.Davis, name='Davis'),
    # Davis Barracks
    path('Davis/', views.Davis, name='Davis'),
    # Davis Barracks
    path('Davis/', views.Davis, name='Davis'),
    # Davis Barracks
    path('Davis/', views.Davis, name='Davis'),
    # Davis Barracks
    path('Davis/', views.Davis, name='Davis'),
    # Davis Barracks
    path('Davis/', views.Davis, name='Davis'),
    # Davis Barracks
    path('Davis/', views.Davis, name='Davis'),
    # Davis Barracks
    path('Davis/', views.Davis, name='Davis'),
    # Davis Barracks
    path('Davis/', views.Davis, name='Davis'),
    # Room Record
    path('Davis/<int:rooms_id>/', views.roomRecord, name='roomRecord'),
    # Cadet Record (X_Num)
    path('<int:X_Num>/', views.cadetRecord, name='cadetRecord'),
]
