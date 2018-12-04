from django.contrib import admin

from .models import Agreeement

admin.autodiscover()

admin.site.register(Agreeement)
