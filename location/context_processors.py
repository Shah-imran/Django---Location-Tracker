from django.conf import settings


def siteinfo(request):
    
    context = {
        'SITENAME': settings.SITENAME,
        'TAGLINE': settings.TAGLINE,
        'GOOGLE_MAP_API_KEY': settings.GOOGLE_MAP_API_KEY
    }

    return context
