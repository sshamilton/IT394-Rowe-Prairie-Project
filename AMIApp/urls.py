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
    # (1) Brad Long Barracks
    path('Brad_Long/', views.BradLong, name='Brad_Long'),
    # (2) Brad Short Barracks
    path('Brad_Short/', views.BradShort, name='Brad_Short'),
    # (3) Davis Barracks
    path('Davis/', views.Davis, name='Davis'),
    # (4) Eisenhower Barracks
    path('Eisenhower/', views.Eisenhower, name='Eisenhower'),
    # (5) Grant Barracks
    path('Grant/', views.Grant, name='Grant'),
    # (6) Lee Barracks
    path('Lee/', views.Lee, name='Lee'),
    # (7) Mac Long Barracks
    path('Mac_Long/', views.MacLong, name='Mac_Long'),
    # (8) Mac Short Barracks
    path('Mac_Short/', views.MacShort, name='MacShort'),
    # (9) Pershing Barracks
    path('Pershing/', views.Pershing, name='Pershing'),
    # (10) Scott Barracks
    path('Scott/', views.Scott, name='Scott'),
    # Room Record
    path('Rooms/<int:rooms_id>/', views.roomRecord, name='roomRecord'),
    # Cadet Record (X_Num)
    path('<int:X_Num>/', views.cadetRecord, name='cadetRecord'),
]
