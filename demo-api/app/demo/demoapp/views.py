from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from demoapp.models import Dog, Cat
from demoapp.serializers import CatSerializer, DogSerializer


class CatViewSet(
    viewsets.ModelViewSet
):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "breed", "age"]
    
class DogViewSet(
    viewsets.ModelViewSet
):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "breed", "age"]