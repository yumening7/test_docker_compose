from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@api_view(['POST'])
def signup(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    user, created = User.objects.get_or_create(email=email)
    if created:
        user.set_password(password)
        user.save()
    return Response({'id': user.id, 'email': user.email}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        return Response({'access_token': str(refresh.access_token), 'refresh_token': str(refresh)}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def me(request):
    if request.user.is_authenticated:
        return Response({'id': request.user.id, 'email': request.user.email}, status=status.HTTP_200_OK)
    return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

