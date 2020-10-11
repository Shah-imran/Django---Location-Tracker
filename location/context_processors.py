from django.conf import settings


def siteinfo(request):
    
    context = {
        'SITENAME': settings.SITENAME,
        'TAGLINE': settings.TAGLINE
    }

    return context
