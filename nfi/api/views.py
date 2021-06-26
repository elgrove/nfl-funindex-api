from django.shortcuts import render
from api.models import WebView
from api.serializers import WebViewSerializer
from rest_framework import viewsets #permissions

# Create your views here.

class WebViewSet(viewsets.ModelViewSet):
    '''API endpoint that serves web_view from the DB'''
    queryset = WebView.objects.all().order_by('match_id')
    serializer_class = WebViewSerializer
    # permission_classes = []
