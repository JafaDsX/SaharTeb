from django.urls import path
from service.views import ServiceListView, ServiceDetailView

urlpatterns = [
    path("", ServiceListView.as_view(), name="service-list"),

    path("list/", ServiceListView.as_view(), name="service-list"),
    path("<str:slug>/", ServiceDetailView.as_view(), name="service-detail"),
]

