from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from service.forms import ServiceRequestForm


class HomeView(View):
    def get(self, request):
        form = ServiceRequestForm()
        return render(request, "core/home.html", {"service_request_form": form})

class AboutUsView(View):
    def get(self, request):
        return render(request, "core/about.html")

class ContactUsView(View):
    def get(self, request):
        return render(request, "core/contact.html")


def custom_page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)


def custom_error_view(request):
    return render(request, 'errors/500.html', status=500)

def custom_permission_denied_view(request, exception):
    return render(request, 'errors/403.html', status=403)


def custom_bad_request_view(request, exception):
    return render(request, 'errors/400.html', status=400)
