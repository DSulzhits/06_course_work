from django.shortcuts import render

from django.urls import path
from mailing_list.models import Client, MailingListMessage, MailingList, MailingListLogs
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'mailing_list/index.html'
    extra_context = {
        'title': 'Домашняя страница',
        'object_list': MailingList.objects.all()
    }
