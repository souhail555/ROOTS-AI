from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

User = get_user_model()


# ======================
# Home API
# ======================
@api_view(['GET'])
def home(request):
    return Response({
        "message": "ROOTS AI API is working 🚀",
        "status": "success"
    })


# ======================
# Register API
# ======================
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User created successfully 🚀"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)