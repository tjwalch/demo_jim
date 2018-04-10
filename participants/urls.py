from django.urls import path

from . import views


urlpatterns = [
    path(
        'travelcosts/',
        views.SummaryView.as_view(),
        name='participants-list',
    ),
]
