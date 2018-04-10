from django.urls import path

from . import views


urlpatterns = [
    path(
        'travelentry/',
        views.TravelLogCreateView.as_view(),
        name='travelentry',
    ),
    path(
        '<int:pk>/odometer/',
        views.odometer_for_car_view,
        name='retreive-odometer',
    )
]
