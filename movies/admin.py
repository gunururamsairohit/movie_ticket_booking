# movies/admin.py
from django.contrib import admin
from .models import Movie, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration', 'trailer')  # Fields to display in the admin list view
    search_fields = ('title', 'description')  # Add a search bar for movie titles and descriptions
    list_filter = ('release_date',)  # Add a filter for release dates
    fields = ('title', 'description', 'image', 'release_date', 'duration', 'trailer')  # Fields to display in the form
    ordering = ('release_date',)  # Default ordering by release date

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'customer_name', 'show_time', 'number_of_tickets')  # Fields to display in the admin list view
    search_fields = ('customer_name', 'movie__title')  # Add a search bar for customer names and movie titles
    list_filter = ('show_time',)  # Add a filter for show times
    date_hierarchy = 'show_time'  # Add a date hierarchy for show times
    fields = ('movie', 'customer_name', 'show_time', 'number_of_tickets')  # Fields to display in the form
    ordering = ('show_time',)