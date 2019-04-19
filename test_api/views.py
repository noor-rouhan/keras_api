from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import permissions
from . import models

# Create your views here.


class HelloApiView(APIView):

    ####test APIView

    serializer_class = serializers.testserializer


    def get(self,request, format = None):
        and_apiview = [
        'jango rest test',
        'want to deploy keras model'
        ]
        return Response({'message':'hello','and_apiview':and_apiview})


    def post(self,request):
        ###Test posting
        serializer = serializers.testserializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')

            message = 'test api posting success {0}'.format(name)

            return Response({'message':message},status.HTTP_202_ACCEPTED)

        else:
            return Response(
            serializer.errors,status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk = None):

        return Response({'method':'put'})


    def patch(self,request,pk=None):

        return Response({'method':'patch'})


    def delete(self, request, pk = None):
        return Response({'method': ' delete'})

class testviewsets(viewsets.ViewSet):

    serializer_class = serializers.testserializer


    def list(self, request):
        a_viewset = [
        'uses action CRUD',
        'keras api test run',
        'digit recognizer',

        ]

        return Response({'message':'test run keras api viewset', 'keras_api':a_viewset})

    def create(self, request):

        serializer = serializers.testserializer(data = request.data)

        if serializer.is_valid():

            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,status= status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk = None):

        return Response({'http_method': 'GET'})

    def update(self, request, pk = None):


        return Response({'http_method': 'PUT'})

    def partial_update(self,request, pk=None):
        return Response(
            {'http_method': 'PATCH'}
        )

    def destroy(self, request,pk=None):

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self,request):

        return ObtainAuthToken().post(request)

class UserProfileFeeedViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus,IsAuthenticatedOrReadOnly,IsAuthenticated,)
    def perform_create(self,serializer):

        serializer.save(user_profile=self.request.user)
