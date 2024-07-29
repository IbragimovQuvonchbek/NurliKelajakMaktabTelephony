from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Call
from .serializers import CallSerializer
from django.contrib.auth import authenticate


class SuperUserLoginApiView(APIView):
    def get(self, request):
        username = request.query_params.get('username')
        password = request.query_params.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_superuser:
            return Response({
                'username': user.username,
                'email': user.email
            })
        return Response({'error': 'Invalid credentials or not a superuser'}, status=status.HTTP_400_BAD_REQUEST)


class GetCallApiView(APIView):
    def get(self, request):
        calls = Call.objects.all()
        serializer = CallSerializer(calls, many=True)
        return Response(serializer.data)


class GetCallDetailApiView(APIView):
    def get(self, request, pk):
        try:
            call = Call.objects.get(pk=pk)
        except Call.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CallSerializer(call)
        return Response(serializer.data)


class CreateCallApiView(APIView):
    def post(self, request):
        serializer = CallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCallApiView(APIView):
    def put(self, request, pk):
        try:
            call = Call.objects.get(pk=pk)
        except Call.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CallSerializer(call, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCallApiView(APIView):
    def delete(self, request, pk):
        try:
            call = Call.objects.get(pk=pk)
        except Call.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        call.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
