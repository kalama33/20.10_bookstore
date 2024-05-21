from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import ReadOnlyOrAuthenticatedWritePermission

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

class MyCustomView(APIView):
    permission_classes = [ReadOnlyOrAuthenticatedWritePermission]

    def get(self, request):
        return Response("GET request")
    
    def post(self, request):
        return Response("POST request")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_profile(request):
    # Lógica para la creación de perfiles
    return Response("Create profile request")

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request, profile_id):
    # Lógica para la actualización de perfiles
    profile = get_object_or_404(Profile, id=profile_id)
    serializer = ProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_profile(request, profile_id):
    # Lógica para la eliminación de perfiles
    profile = get_object_or_404(Profile, id=profile_id)
    profile.delete()
    return Response("Profile deleted successfully")
