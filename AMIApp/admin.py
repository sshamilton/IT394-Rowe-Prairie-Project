from django.contrib import admin

from .models import Position, Rooms, Cadets, Inspections, Gigs

# Register your models here.
admin.site.register(Position)
admin.site.register(Rooms)
admin.site.register(Cadets)
admin.site.register(Inspections)
admin.site.register(Gigs)
