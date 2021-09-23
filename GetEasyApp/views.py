from django.shortcuts import render

# Create your views here.

from GetEasyApp.models import General, Services, GetService


def home(request):
    page = "home"
    context = {}
    context['home_details'] = General.objects.all()
    context['services_all'] = Services.objects.all().order_by('service_sequence').filter(home_shown="yes")

    return render(request, page + ".html", context)


# def service_response(request):
#     context = {}
#     context['all_response'] = GetService.objects.all()
#
#     return render(request, "admin/service_response.html", context)
