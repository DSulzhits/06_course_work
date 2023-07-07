from django.shortcuts import render

from mailing_list.models import Client, MailingListMessage, MailingList, MailingListLogs
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404
from mailing_list.forms import ClientForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'mailing_list/index.html'
    extra_context = {
        'title': 'Домашняя страница',
        'object_list': MailingListMessage.objects.all()
    }


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Список клиентов',
        'object_list': Client.objects.all()
    }


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list:homepage')

    def form_valid(self, form):
        self.object = form.save()
        self.object.created = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.created != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing_list:index')
