from django import forms
from .models import Region


class TicketForm(forms.Form):
    datetime = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local'}))
    street_address = forms.CharField(max_length=100)
    region = forms.ModelChoiceField(queryset=Region.objects.all())


class HistoryForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    day_of_week = forms.ChoiceField(
        choices=[('Monday', 'Monday'), (
            'Tuesday',
            'Tuesday'), ('Wednesday', 'Wednesday'), (
                'Thursday',
                'Thursday'), ('Friday',
                              'Friday'), ('Saturday',
                                          'Saturday'), ('Sunday', 'Sunday')])
