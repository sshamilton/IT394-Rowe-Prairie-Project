from django.urls import path

from . import views

urlpatterns = [
    # Index
    path('', views.index, name='index'),
    # Detail
    path('<int:inspections_id>/', views.detail, name='detail'),
    # Enter Inspection
    path('enterInspection/', views.get_inspection, name='enterInspection'),
    # Enter Inspection 2
    path('enterInspection2/', views.get_inspection,name='enterInspection2'),
    # Room Record
    path('<int:rooms_id>/', views.roomRecord, name='roomRecord'),
    # Cadet Record (X_Num)
    path('<int:X_Num>/', views.cadetRecord, name='cadetRecord'),
]
