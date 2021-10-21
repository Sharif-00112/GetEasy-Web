from django.contrib import admin

# Register your models here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from GetEasyApp.models import General, Services, GetService, FAQ

admin.site.site_header = "GetEasyService Administration"
admin.site.site_title = "GetEasyService"


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['main_title', 'last_edited']


admin.site.register(General, GeneralAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', '_get_short_desc', 'service_sequence']
    ordering = ['service_sequence']

    def _get_short_desc(self, obj):
        return format_html(obj.short_desc)


admin.site.register(Services, ServiceAdmin)


class GetServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'client_name', 'phone_no', 'district']
    list_filter = ['service', 'district']

    # change_list_template = "admin/service_response.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get_all_service/', self.get_service_view)
        ]
        return custom_urls + urls

    def get_service_view(self, request):
        return HttpResponseRedirect("../")


admin.site.register(GetService, GetServiceAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ['_get_question', 'segment', 'segment_general']
    list_filter = ['segment']

    def _get_question(self, obj):
        return format_html(obj.question)


admin.site.register(FAQ, FAQAdmin)
