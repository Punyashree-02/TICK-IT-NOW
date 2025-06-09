from django.shortcuts import render, get_object_or_404, redirect
from users.models import MovieBooking
from .models import Media
from datetime import datetime
import logging
from django.db.models import Q

def movie_detail(request, pk):
    movie = get_object_or_404(Media, pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movie_detail.html', context)

def book_tickets(request, pk):
    movie = get_object_or_404(Media, pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'book_tickets.html', context)


def confirm_booking(request, pk):
    if request.method == 'POST':
        movie = get_object_or_404(Media, pk=pk)
        theater = request.POST.get('theater')
        time_str = request.POST.get('time')
        price = request.POST.get('price')
        user = request.user

        # Process time
        try:
            time_obj = datetime.strptime(time_str, '%I:%M %p').time()
        except ValueError as e:
            return render(request, 'book_tickets.html', {
                'movie': movie,
                'error_message': 'Invalid time format. Please use HH:MM AM/PM.'
            })

        # Create and save a new MovieBooking object
        try:
            booking = MovieBooking.objects.create(
                user=user,
                movie_title=movie.title,
                theater=theater,
                time=time_obj,
                price=price,
                poster=movie.poster
            )
            booking.save()
        except Exception:
            return render(request, 'book_tickets.html', {
                'movie': movie,
                'error_message': 'An error occurred while creating the booking.'
            })

        # Redirect to the profile page
        return redirect('profile_view', username=request.user.username)

    return render(request, 'book_tickets.html', {'movie': get_object_or_404(Media, pk=pk)})
def search_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        try:
            # Try to parse the query as an integer (for year)
            query_year = int(query)
            # Filter by year if query is a number
            results = Media.objects.filter(
                Q(title__icontains=query) | 
                Q(genre__icontains=query) | 
                Q(release_year__year=query_year)  # Extract year and filter
            )
        except ValueError:
            # If query is not a number, filter by title and genre only
            results = Media.objects.filter(
                Q(title__icontains=query) | 
                Q(genre__icontains=query)
            )
        return render(request, 'search_results.html', {'results': results})
    return render(request, 'search_results.html', {'results': []})