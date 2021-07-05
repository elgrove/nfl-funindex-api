from django.shortcuts import render
from api.models import WebView
from api.serializers import WebViewSerializer
from rest_framework import viewsets #permissions
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class RawViewSet(viewsets.ModelViewSet):
    '''API endpoint that serves web_view as is from the DB'''
    queryset = WebView.objects.all().order_by('match_id')
    serializer_class = WebViewSerializer
    # permission_classes = []

class FilterViewSet(viewsets.ModelViewSet):
    '''API endpoint that serves web_view filtered by season, week'''
    queryset = WebView.objects.all().order_by('match_id')
    serializer_class = WebViewSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['season', 'week']
    # permission_classes = []

