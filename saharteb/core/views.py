from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, "core/home.html")

class AboutUsView(View):
    def get(self, request):
        return render(request, "core/about.html")

class ContactUsView(View):
    def get(self, request):
        return render(request, "core/contact.html")

