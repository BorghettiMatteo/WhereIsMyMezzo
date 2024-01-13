from django.contrib import admin
from .models import Vehicle, Crew, CrewMate, Mission
import django

# Register your models here.
admin.site.register(CrewMate)#
admin.site.register(Vehicle)
admin.site.register(Crew)
admin.site.register(Mission)
