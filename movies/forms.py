from django import forms
from .models import Booking, Movie

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'show_time', 'number_of_tickets']  # Only include fields that the user interacts with

    # We don't need to expose the 'movie' field to the user. So, we use a hidden input field.
    movie = forms.ModelChoiceField(queryset=Movie.objects.all(), widget=forms.HiddenInput(), required=False)


