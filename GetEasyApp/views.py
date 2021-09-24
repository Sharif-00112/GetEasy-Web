from django.shortcuts import render
from django.contrib import messages
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

def getservices(request, sid):
    page = "getservicesclient"
    context = {}
    context['service_get'] = Services.objects.filter(id=sid)

    if request.method == 'POST':
        client_name = request.POST['name']
        phone_no = request.POST['phone']
        district = request.POST['district']
        message = request.POST['message']
        service = Services.objects.get(id=sid)

        get_sr = GetService.objects.create(service=service, client_name=client_name, phone_no=phone_no,
                                           district=district,
                                           message=message)
        if get_sr:
            messages.success(request, "Your Appointment Submitted Successfully. "
                                      "GetEasyWeb contact with you soon! Thanks for using GetEasyWeb.")
        return render(request, page + '.html')
    return render(request, page + ".html", context)
