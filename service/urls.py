from django.urls import path
from service.views import ServiceListView, ServiceDetailView, service_request_form_view

urlpatterns = [
    path("", ServiceListView.as_view(), name="service-list"),
    path("list/", ServiceListView.as_view(), name="service-list"),
    path("service-request/", service_request_form_view, name="service-request"),
    # path("<str:slug>/", ServiceDetailView.as_view(), name="service-detail"),


]

