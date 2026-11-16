from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import PartnershipApplicationForm


def partnerships(request):
    if request.method == 'POST':
        form = PartnershipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your partnership enquiry has been submitted successfully. The Harvest Farm team will review it and get back to you soon.')
            return redirect('partnerships')
    else:
        form = PartnershipApplicationForm()

    return render(request, 'partnerships/partnerships.html', {'form': form})
