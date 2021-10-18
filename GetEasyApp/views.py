from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from GetEasyApp.models import General, Services, GetService


def home(request):
    page = "home"
    context = {}
    context['home_details'] = General.objects.all()
    context['main_title'] = General.objects.get(id=1).main_title
    context['image_field'] = General.objects.get(id=1).image_field
    context['short_about'] = General.objects.get(id=1).short_about
    context['long_about'] = General.objects.get(id=1).long_about
    context['terms'] = General.objects.get(id=1).terms
    context['policy'] = General.objects.get(id=1).policy
    context['email'] = General.objects.get(id=1).email
    context['phone'] = General.objects.get(id=1).phone
    context['address'] = General.objects.get(id=1).address
    context['facebook_link'] = General.objects.get(id=1).facebook_link
    context['whatsapp_link'] = General.objects.get(id=1).whatsapp_link
    context['instagram_link'] = General.objects.get(id=1).instagram_link
    context['linkedin_link'] = General.objects.get(id=1).linkedin_link
    context['skype_link'] = General.objects.get(id=1).skype_link
    context['services_all'] = Services.objects.all().order_by('service_sequence').filter(home_shown="yes")

    request.session['email'] = context['email']
    request.session['phone'] = context['phone']
    request.session['address'] = context['address']
    request.session['facebook_link'] = context['facebook_link']
    request.session['instagram_link'] = context['instagram_link']
    request.session['whatsapp_link'] = context['whatsapp_link']
    request.session['skype_link'] = context['skype_link']
    request.session['linkedin_link'] = context['linkedin_link']

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


def all_services(request):
    page = 'all_services'

    context = {}
    context['services_all'] = Services.objects.all().order_by('service_sequence')
    return render(request, page + ".html", context)


def service_details(request, sid):
    page = 'service_details'

    context = {}
    context['service'] = Services.objects.get(id=sid)
    context['services_all'] = Services.objects.all().order_by('service_sequence')
    return render(request, page + ".html", context)


def make_appointment(request):
    if request.method == 'POST':
        client_name = request.POST['name']
        phone_no = request.POST['phone']
        district = request.POST['district']
        message = request.POST['message']
        service_id = request.POST['service']
        service = Services.objects.get(id=service_id)

        get_sr = GetService.objects.create(service=service, client_name=client_name, phone_no=phone_no,
                                           district=district,
                                           message=message)
        if get_sr:
            messages.success(request, "Your Appointment Submitted Successfully. "
                                      "GetEasyWeb contact with you soon! Thanks for using GetEasyWeb.")
        return redirect('home')
    return redirect('home')
