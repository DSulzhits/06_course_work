from django.urls import path
from mailing_list.apps import MailingListConfig
from mailing_list.views import IndexView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, ClientDeactivatedListView, client_toggle_activity, MailingListMessageListView, \
    MailingListMessageDetailView, MailingListMessageCreateView, MailingListMessageUpdateView, \
    MailingListMessageDeleteView

app_name = MailingListConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/deactivated/', ClientDeactivatedListView.as_view(), name='client_deactivated_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('client/toggle/<int:pk>', client_toggle_activity, name='client_toggle_activity'),
    path('mailing_list_messages/', MailingListMessageListView.as_view(), name='message_list'),
    path('mailing_list_message/<int:pk>/', MailingListMessageDetailView.as_view(), name='message_detail'),
    path('mailing_list_message/create/', MailingListMessageCreateView.as_view(), name='message_create'),
    path('mailing_list_message/update/<int:pk>/', MailingListMessageUpdateView.as_view(), name='message_update'),
    path('mailing_list_message/delete/<int:pk>/', MailingListMessageDeleteView.as_view(), name='message_delete'),
]
