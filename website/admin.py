from django.contrib import admin

from .models import Record
from .models import Ticket


admin.site.register(Record)
admin.site.register(Ticket)