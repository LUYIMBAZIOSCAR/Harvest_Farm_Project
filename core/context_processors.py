from django.conf import settings

from .models import FarmInformation, SocialMediaLink


def site_context(request):
    farm = FarmInformation.objects.filter(is_active=True).first()
    social_links = SocialMediaLink.objects.filter(is_active=True)
    return {
        'site_farm': farm,
        'social_links': social_links,
        'whatsapp_number': getattr(settings, 'WHATSAPP_NUMBER', '+256759002954'),
    }
