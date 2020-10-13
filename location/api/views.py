from .serializers import LocationSerializer
from location.models import Location
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
import dateparser
import datetime


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def location_list(request):

    current_user = request.user

    if request.method == "POST":
        start_date = dateparser.parse(request.data['start']).replace(tzinfo=datetime.timezone.utc)
        end_date = dateparser.parse(request.data['end']).replace(tzinfo=datetime.timezone.utc)
        
        locations = Location.objects.filter(
            uploaded_by=current_user.device,
            created_time__gte=start_date,
            created_time__lte=end_date).order_by('-created_time').all()
    else:
        locations = Location.objects.filter(
            uploaded_by=current_user.device).order_by('-created_time').all()

    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)
