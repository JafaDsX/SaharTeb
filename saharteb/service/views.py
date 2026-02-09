from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from service.models import Service


class ServiceListView(ListView):
    model = Service
    template_name = "service/services.html"
    context_object_name = "services"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs



class ServiceDetailView(DetailView):
    model = Service
    template_name = "service/service.html"
    context_object_name = "service"


