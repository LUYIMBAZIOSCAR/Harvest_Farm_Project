from django.contrib import messages
from django.shortcuts import redirect, render

from core.models import FarmInformation
from .forms import ContactMessageForm


def contact(request):
    farm = FarmInformation.objects.filter(is_active=True).first()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully. The Harvest Farm team will contact you soon.')
            return redirect('contact')
    else:
        form = ContactMessageForm()

    return render(request, 'contact/contact.html', {'form': form, 'farm': farm})
