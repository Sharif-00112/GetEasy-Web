from gettext import ngettext

from django.contrib import admin, messages

# Register your models here.
from django.contrib.auth import get_permission_codename
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from GetEasyApp.models import General, Services, GetService, FAQ

admin.site.site_header = "GetEasyService Administration"
admin.site.site_title = "GetEasyService"


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['main_title', 'last_edited', 'mode']

    @admin.action(description='Change Mode')
    def mode_button(self, request, queryset):
        if queryset.filter(mode='1'):
            updated_mode = queryset.update(mode='2')
        else:
            updated_mode = queryset.update(mode='1')
        self.message_user(request, ngettext(
            '%d mode was successfully changed',
            '%d mode was successfully changed .',
            updated_mode,
        ) % updated_mode, messages.SUCCESS)

    actions = [mode_button]

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(General, GeneralAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', '_get_short_desc', 'service_sequence']
    ordering = ['service_sequence']

    def _get_short_desc(self, obj):
        return format_html(obj.short_desc)


admin.site.register(Services, ServiceAdmin)


class GetServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'client_name', 'phone_no', 'district', 'message_time', 'status']
    list_filter = ['service', 'district']
    search_fields = ['client_name', 'phone_no', 'district']

    @admin.action(description='Change Status', permissions=['status'])
    def status_button(self, request, queryset):
        updated_status = queryset.update(status='Completed')
        self.message_user(request, ngettext(
            '%d service was successfully marked as Completed.',
            '%d services were successfully marked as Completed.',
            updated_status,
        ) % updated_status, messages.SUCCESS)

    def has_status_permission(self, request):
        """Does the user have the Change permission?"""
        opts = self.opts
        codename = get_permission_codename('status', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    actions = [status_button]

    # change_list_template = "admin/service_response.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get_all_service/', self.get_service_view)
        ]
        return custom_urls + urls

    def get_service_view(self, request):
        return HttpResponseRedirect("../")

    @admin.display(description='Message Date & Time')
    def message_time(self, obj):
        return obj.ctime

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(GetService, GetServiceAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ['_get_question', 'segment', 'segment_general']
    list_filter = ['segment']

    def _get_question(self, obj):
        return format_html(obj.question)


admin.site.register(FAQ, FAQAdmin)
