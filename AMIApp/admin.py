from django.contrib import admin

from .models import Position, Cadet_Has_Superior, Rooms, Cadets, Inspections, Gigs

# Register your models here.
admin.site.register(Position)
admin.site.register(Cadet_Has_Superior)
admin.site.register(Rooms)
admin.site.register(Cadets)
admin.site.register(Inspections)
admin.site.register(Gigs)
