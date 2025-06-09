# movies/urls.py
from django.urls import path
from .views import  movie_detail  ,book_tickets  ,confirm_booking,search_view

urlpatterns = [
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
    path('book_tickets/<int:pk>/', book_tickets, name='book_tickets'),  
    path('confirm_booking/<int:pk>/', confirm_booking, name='confirm_booking'),   # Confirm booking view
    path('search/', search_view, name='search_view'),
]