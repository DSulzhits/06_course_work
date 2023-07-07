from django.shortcuts import render

from mailing_list.models import Client, MailingListMessage, MailingList, MailingListLogs
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import render, get_object_or_404, reverse, redirect
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
    }

    def get_queryset(self):
        """Метод благодаря которому отображаются только неактивные записи"""
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class ClientDeactivatedListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Неактивные клиенты',
    }

    def get_queryset(self):
        """Метод благодаря которому отображаются только неактивные записи"""
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=False)
        return queryset


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.created = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list:client_list')

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.created != self.request.user and not self.request.user.is_staff:
    #         raise Http404
    #     return self.object

    # def get_success_url(self):
    #     return reverse('mailing_list:client_list', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing_list:client_list')


def client_toggle_activity(request, pk):
    client_item = get_object_or_404(Client, pk=pk)
    if client_item.is_active:
        client_item.is_active = False
    else:
        client_item.is_active = True
    client_item.save()
    return redirect(reverse('mailing_list:client_list'))
