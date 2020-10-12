from .serializers import LocationSerializer
from location.models import Location
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def location_list(request):

    current_user = request.user
    
    locations = Location.objects.filter(uploaded_by=current_user).order_by('-created_time').all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)