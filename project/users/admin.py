from django.contrib import admin
from .models import UserProfileModel,MovieBooking

# Register your models here.

admin.site.register(UserProfileModel)
admin.site.register(MovieBooking)