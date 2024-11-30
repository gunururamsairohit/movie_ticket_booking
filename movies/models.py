# movies/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    release_date = models.DateField()
    duration = models.PositiveIntegerField()  # Duration in minutes
    trailer = models.CharField(
        max_length=100, 
        blank=True, 
        help_text="YouTube video ID for the trailer"
    )  # Add trailer field

    def __str__(self):
        return self.title

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    show_time = models.DateTimeField()
    number_of_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking for {self.movie.title} by {self.customer_name}"