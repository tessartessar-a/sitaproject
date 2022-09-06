from django.contrib import admin
from .models import Data,jobs
from .models import Status

admin.site.register(Data)
admin.site.register(Status)
admin.site.register(jobs)