from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Movie
from .forms import BookingForm

def movie_list(request):
    # Fetch all movies from the database
    movies = Movie.objects.all()
    # Render the movie list template and pass the movies to the context
    return render(request, 'movies/movie_list.html', {'movies': movies})
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)  # Fetch the movie by its ID
    if request.method == "POST":
        form = BookingForm(request.POST)  # Bind the form to the POST data
        if form.is_valid():
            # Create the booking instance but don't save it yet
            booking = form.save(commit=False)
            
            # Explicitly set the movie field to the selected movie
            booking.movie = movie
            
            # Save the booking instance to the database
            booking.save()
            
            # Show a success message to the user
            messages.success(request, "Your booking was successful!")
            
            # Redirect to the movie detail page
            return redirect('movie_detail', movie_id=movie.id)
        else:
            # If form is invalid, show an error message
            messages.error(request, "There was an error with your booking. Please try again.")
    else:
        # For GET request, initialize the form with the movie data
        form = BookingForm(initial={'movie': movie})  # Pre-populate the movie field in the form
    
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'form': form})

