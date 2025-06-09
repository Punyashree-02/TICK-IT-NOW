from .views import login_view,signup_view,logout_view,home_view,profile_view,update_user_profile,cancel_booking,movies_view,shows_view
from django.urls import path

urlpatterns = [
    path('login/',login_view,name="login_view"),
    path('signup/',signup_view,name="signup_view"),
    path('logout/',logout_view,name="logout_view"),  # Logout view
    path('home/', home_view, name="home_view"),
    path('profile/<str:username>/', profile_view, name="profile_view"),  
    path('update_user/', update_user_profile, name="update_user_profile"),  
    path('cancel_booking/<int:booking_id>/', cancel_booking, name="cancel_booking"),   # Cancel booking view
    path('movies/', movies_view, name='movies_view'),
    path('shows/', shows_view, name='shows_view'),    
]