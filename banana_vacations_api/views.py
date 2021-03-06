from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from banana_vacations_api import serializers
from banana_vacations_api import models
from banana_vacations_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as finctions (get, post, patch , put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(seld, reques, pk=None):
        """Delete an object"""
        return Response ({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs uing Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, reauest, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, reauest, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class PlannerNotesApiViewSet(viewsets.ModelViewSet):
    """Handle creating and updating planner notes"""
    serializer_class = serializers.PlannerNotesSerializer
    queryset = models.PlannerNote.objects.all()

    def index(request):
        """Displays the 3 latest notes in the system"""
        latest_notes_list = models.PlannerNote.objects.order_by('-pub_date')[:3]
        output = ', '.join([q.note_text for q in latest_notes_list])
        return HttpResponse(output)

    def detail(request, notes_id):
        """Raising a 404 error if a note with the requested id doesn't exist"""
        try:
            notes = models.PlannerNote.objects.get(pk=notes_id)
        except models.PlannerNote.DoesNotExist:
            raise Http404("PlannerNote does not exist")
        return render(request, 'api/planner-notes.html', {'notes': notes})

class DiaryApiViewSet(viewsets.ModelViewSet):
    """Handles creating and updating diary entries"""
    serializer_class = serializers.DiaryEntrySerializer
    queryset = models.Diary.objects.all()

    def index(request):
        return HttpResponse("Hello, you're at the diary entries index.")

    def detail(request, entry_id):
        """Raising a 404 error  if an entry with the requested id doesn't exist"""
        try:
            entries = models.Diary.objects.get(pk=entry_id)
        except models.Diary.DoesNotExist:
            raise Http404("Diary does not exist")
        return render(request, 'api/diary.html', {'entries': entries})

    def get_queryset(self):
        """Return the last pulished entry (do not include those set to be published in the future)."""
        """models.Diary.objects.filter(pub_date_lte=timezone.now()).order_by('-pub_date')[:2] returns a queryset containing Diary entries whose pub_date is less than or equal to - that is, earlier than or equal to -timezone.now"""
        return models.Diary.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

    

