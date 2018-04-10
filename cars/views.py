from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import ugettext_lazy as _

from . import (
    forms,
    models,
)


class TravelLogCreateView(CreateView):
    model = models.TravelLog
    form_class = forms.TravelLogForm
    success_url = reverse_lazy('travelentry')

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Körsträckan sparad.')
        )
        return super().form_valid(form)


def odometer_for_car_view(request, pk):
    car = get_object_or_404(
        models.Car,
        pk=pk
    )
    return JsonResponse({
        'odometer': car.odometer,
    })
