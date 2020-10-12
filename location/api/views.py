from .serializers import LocationSerializer
from location.models import Location
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def location_list(request, username):

    current_user = request.user

    user = User.objects.filter(username=username).first()

    if current_user == user:

        locations = Location.objects.filter(uploaded_by=current_user).order_by('-created_time').all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    return Response([])


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def location_create(request):

    current_user = request.user

    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)