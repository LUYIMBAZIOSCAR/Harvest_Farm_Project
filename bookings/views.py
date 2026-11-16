from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import FarmTourBookingForm


def book_tour(request):
    if request.method == 'POST':
        form = FarmTourBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.status = 'pending'
            booking.save()
            messages.success(
                request,
                'Your farm tour request has been received. It is currently pending review and the Harvest Farm team will contact you soon.'
            )
            return redirect('book_tour')
    else:
        form = FarmTourBookingForm()

    return render(request, 'bookings/book_tour.html', {'form': form})
