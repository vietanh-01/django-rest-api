from pdb import post_mortem
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from car.models import Car
from car.serializers import CarSerializer

class ListCreateCarView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class UpdateDeleteCarView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return JsonResponse({'message': 'Update Car successful!'}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'message': 'Delete Car successful!'}, status=status.HTTP_200_OK)
