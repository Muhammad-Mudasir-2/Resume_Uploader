from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework import status


class ProfileView(APIView):

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Resume Uploaded', 'status': 'success',
                             'candidate': serializer.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return Response({'status': 'success',
                         'candidate': serializer.data},
                        status=status.HTTP_200_OK)
