from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404

# Import models
from core.models.pet import Pet
from core.models.application import Application

# Import Serializers
from core.serializers.application import ApplicationSerializer

# Create your views here.
class AdoptionView(APIView):
    def get(self, request, format=None):
        # Get all the listed pets for adoption.
        listed_pet_dogs = Pet.objects.all()
        return render(request, "index.html", {"listed_for_adoption": listed_pet_dogs})


class AdoptionApplication(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "application.html"

    def get(self, request, pk):
        # Get the pet details
        pet = get_object_or_404(Pet, pk=pk)
        application = Application.objects.create(pet=pet)
        serializer = ApplicationSerializer(application)
        return Response({"serializer": serializer, "application": application})

    def post(self, request, pk):
        application, created = Application.objects.get_or_create(pk=pk)
        serializer = ApplicationSerializer(application, data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer, "profile": application})
        serializer.save()
        return redirect("home")
