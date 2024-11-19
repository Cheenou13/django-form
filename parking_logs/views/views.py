from django.shortcuts import render, redirect
from datetime import datetime
from ..models.models import Ticket, Region
from ..models.form import TicketForm, HistoryForm
from django.core.management import call_command


def home_view(request):
    # Populate regions only if they do not exist
    if not Region.objects.exists():
        try:
            call_command('populate_regions')
        except Exception as e:
            print(f"Error populating regions: {e}")

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            datetime_str = form.cleaned_data['datetime'].strftime(
                '%Y-%m-%dT%H:%M')
            dt = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
            day_of_week = dt.strftime('%A')
            ticket = Ticket(datetime=dt,
                            day_of_week=day_of_week,
                            region=form.cleaned_data['region'],
                            street_address=form.cleaned_data['street_address'])
            ticket.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request, 'home.html', {'form': form})


def history_view(request):
    tickets = None
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            region = form.cleaned_data['region']
            day_of_week = form.cleaned_data['day_of_week']
            tickets = Ticket.objects.filter(day_of_week=day_of_week,
                                            region=region)
    else:
        form = HistoryForm()
    return render(request, 'history.html', {'form': form, 'tickets': tickets})
