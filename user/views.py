from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate


class SuperUserLoginApiView(APIView):
    def get(self, request):
        username = request.query_params.get('username')
        password = request.query_params.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            return Response({
                'username': user.username,
                'email': user.email
            })
        return Response({'error': 'Invalid credentials or not a superuser'}, status=status.HTTP_400_BAD_REQUEST)
