from unicodedata import name
from django.contrib import admin

from frontend.models import *
# from ocsc_project.frontend.models import Contact


# Register your models here.
admin.site.register(Team)
admin.site.register(Services)
admin.site.register(Contact)
admin.site.register(Blog)

