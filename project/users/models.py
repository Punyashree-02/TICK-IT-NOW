from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class UserProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profile", null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def has_profile_pic(self):
        return bool(self.profile_picture and hasattr(self.profile_picture, 'url'))

class MovieBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=255)
    theater = models.CharField(max_length=255)
    time = models.TimeField()
    #date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    poster = models.ImageField(upload_to='posters/')

    def _str_(self):
        return f"{self.movie_title} at {self.theater} on {self.date}"
    
