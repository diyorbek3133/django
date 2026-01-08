from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myapp.models import Lugat
from rest_framework import generics
from .serializers import LugatSerializer
from rest_framework.permissions import IsAuthenticated

class LugatListView(generics.ListCreateAPIView):
    serializer_class = LugatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lugat.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)