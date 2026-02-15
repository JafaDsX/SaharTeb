from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from service.models import Service
from django.contrib import messages
from service.forms import ServiceRequestForm
from django.views.decorators.http import require_POST, require_GET
from django.views import View


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

# @require_GET
# @require_POST
# def service_request_view(request):
#     print("-"*100)
#     if request.method == "POST":
#         form = ServiceRequestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request,
#                 "درخواست شما با موفقیت ثبت شد 🌿 پس از بررسی با شما تماس می‌گیریم."
#             )
#             return redirect("service-request")
#     else:
#         form = ServiceRequestForm()
#     return render(request, "core/home.html", {
#         "form": ServiceRequestForm(),

#     })





def service_request_form_view(request):

    if request.method== 'GET':
        return redirect("home")

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")




