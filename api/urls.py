from django.urls import path

from api.airplanes.views import AirplaneCreateListAPI

app_name = 'airplane_api'

urlpatterns = [
    path('v1/airplanes/', AirplaneCreateListAPI.as_view(), name='list_create_airplanes_api')
]
