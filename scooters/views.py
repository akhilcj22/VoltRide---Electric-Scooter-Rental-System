from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Scooter, Ride
from .forms import ScooterForm

# ------------------------------
# User Views
# ------------------------------

@method_decorator(login_required, name='dispatch')
class ScooterListView(ListView):
    model = Scooter
    template_name = 'scooters/scooter_list.html'  # Corrected template path
    context_object_name = 'scooters'

@method_decorator(login_required, name='dispatch')
class RideHistoryView(ListView):
    model = Ride
    template_name = 'scooters/ride_history.html'  # Corrected template path
    context_object_name = 'rides'

    def get_queryset(self):
        return Ride.objects.filter(user=self.request.user).order_by('-start_time')


@login_required
def start_ride(request, scooter_id):
    scooter = get_object_or_404(Scooter, id=scooter_id)
    if not scooter.is_available:
        messages.error(request, 'Scooter is not available.')
        return redirect('scooter_list')

    ongoing_ride = Ride.objects.filter(user=request.user, end_time__isnull=True).first()
    if ongoing_ride:
        messages.error(request, 'You already have an ongoing ride.')
        return redirect('ride_history')

    if request.method == 'POST':
        scooter.is_available = False
        scooter.save()
        ride = Ride.objects.create(user=request.user, scooter=scooter, start_time=timezone.now())
        messages.success(request, f'Ride started on scooter {scooter.identifier}.')
        return redirect('ride_history')

    return render(request, 'scooters/start_ride.html', {'scooter': scooter})


@login_required
def end_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id, user=request.user)
    if ride.end_time:
        messages.error(request, 'This ride has already ended.')
        return redirect('ride_history')

    if request.method == 'POST':
        ride.end_time = timezone.now()
        ride.cost = ride.calculate_cost()
        ride.save()

        scooter = ride.scooter
        scooter.is_available = True
        scooter.save()

        messages.success(request, f'Ride ended. Total cost: {ride.cost}')
        return redirect('ride_history')

    return render(request, 'scooters/end_ride.html', {'ride': ride})

# ------------------------------
# Admin Views
# ------------------------------

def admin_required(user):
    return user.is_staff

@user_passes_test(admin_required)
def admin_dashboard(request):
    total_scooters = Scooter.objects.count()
    rented_scooters = Scooter.objects.filter(is_available=False).count()
    available_scooters = Scooter.objects.filter(is_available=True).count()
    active_rides = Ride.objects.filter(end_time__isnull=True).count()
    total_rides = Ride.objects.count()

    context = {
        'total_scooters': total_scooters,
        'rented_scooters': rented_scooters,
        'available_scooters': available_scooters,
        'active_rides': active_rides,
        'total_rides': total_rides,
    }
    return render(request, 'scooters/admin_dashboard.html', context)


@method_decorator(user_passes_test(admin_required), name='dispatch')
class ScooterAdminListView(ListView):
    model = Scooter
    template_name = 'scooters/scooter_admin_list.html'
    context_object_name = 'scooters'


@method_decorator(user_passes_test(admin_required), name='dispatch')
class ScooterCreateView(CreateView):
    model = Scooter
    form_class = ScooterForm
    template_name = 'scooters/scooter_form.html'
    success_url = reverse_lazy('scooter_admin_list')


@method_decorator(user_passes_test(admin_required), name='dispatch')
class ScooterUpdateView(UpdateView):
    model = Scooter
    form_class = ScooterForm
    template_name = 'scooters/scooter_form.html'
    success_url = reverse_lazy('scooter_admin_list')


@method_decorator(user_passes_test(admin_required), name='dispatch')
class ScooterDeleteView(DeleteView):
    model = Scooter
    template_name = 'scooters/scooter_confirm_delete.html'
    success_url = reverse_lazy('scooter_admin_list')
