from django.contrib import admin

# Register your models here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path

from GetEasyApp.models import General, Services, GetService

admin.site.site_header = "GetEasyWeb Adminstration"

admin.site.register(General)
admin.site.register(Services)


class GetServiceAdmin(admin.ModelAdmin):
    list_display = ['service','client_name', 'phone_no', 'district']
    change_list_template = "admin/service_response.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get_all_service/', self.get_service_view)
        ]
        return custom_urls + urls

    def get_service_view(self, request):
        return HttpResponseRedirect("../")


admin.site.register(GetService, GetServiceAdmin)
