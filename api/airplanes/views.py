from rest_framework import generics
from api.airplanes.serializers import AirplaneSerializer
from core.models import Airplane


class AirplaneCreateListAPI(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
