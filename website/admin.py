from django.contrib import admin

from .models import Client
from .models import Ticket


admin.site.register(Client)
admin.site.register(Ticket)