from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import UserProfileModel, MovieBooking
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseNotFound
from movies.models import Media

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_instance = authenticate(username=username, password=password)
        if user_instance is not None:
            login(request, user_instance)
            return redirect('home_view')
        else:
            print("Invalid username or password")
            return redirect('login_view')

    return render(request, 'login.html')

def signup_view(request):
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if get_user_model().objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            error_flag = True
        else:
            user_instance = get_user_model().objects.create(
                username=username, first_name=first_name, last_name=last_name, email=email)
            user_instance.set_password(password)
            user_instance.save()
            UserProfileModel.objects.create(user=user_instance)
        if not error_flag:
            return redirect('login_view')
    return render(request, 'signup.html')

def home_view(request):
    if request.user.is_authenticated:
        user_profile = UserProfileModel.objects.get(user=request.user)
        
        recommended_movies = Media.objects.filter(category='Recommended')
        '''upcoming_movies = Media.objects.filter(category='Upcoming')
        live_movies = Media.objects.filter(category='Live')
        recommended_shows = Media.objects.filter(category='Show Recommended')
        upcoming_shows = Media.objects.filter(category='Show Upcoming')'''
        live_shows = Media.objects.filter(category='Live shows')
        #All_movies=Media.objects.filter(category='All movies')
        #All_shows=Media.objects.filter(category='All shows')

        context = {
            'user_profile': user_profile,
            'recommended_movies': recommended_movies,
            'live_shows': live_shows,
            #'All_movies': All_movies,
            #'All_shows':All_shows,
        }

        return render(request, 'home.html', context)
    else:
        return redirect('login_view')

def profile_view(request, username):
    user_instance = get_user_model().objects.get(username=username)
    is_user_profile = request.user.username == username
    bookings = MovieBooking.objects.filter(user=user_instance)

    context = {
        "user": user_instance,
        "bookings": bookings,
        "is_user_profile": is_user_profile,
    }
    return render(request, 'profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('login_view')

def update_user_profile(request):
    user_instance = request.user
    if request.method == 'POST':
        user_instance.first_name = request.POST.get('first_name')
        user_instance.last_name = request.POST.get('last_name')
        if request.POST.get('username') != request.user.username:
            if get_user_model().objects.filter(username=request.POST.get('username')).exists():
                print("Username already taken")
            else:
                user_instance.username = request.POST.get('username')
        user_profile_instance = user_instance.profile
        if len(request.FILES) != 0:
            user_profile_instance.profile_picture = request.FILES['profile_picture']
        user_profile_instance.save()
        user_instance.save()
        return redirect('profile_view', username=request.user.username)
    return render(request, 'update_profile.html', context={"request": request, "user": request.user})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(MovieBooking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('profile_view', username=request.user.username)

def movies_view(request):
    all_movies = Media.objects.filter(category='All movies')
    recommended_movies = Media.objects.filter(category='Recommended')

    context = {
        'all_movies': all_movies,
        'recommended_movies': recommended_movies,
    }

    return render(request, 'movies_view.html', context)

def shows_view(request):
    live_shows = Media.objects.filter(category='Live shows')
    all_shows = Media.objects.filter(category='All shows')
    context = {
        'live_shows': live_shows,
        'all_shows': all_shows
    }
    return render(request, 'shows_view.html', context)