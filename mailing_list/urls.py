from django.urls import path
from mailing_list.apps import MailingListConfig
from mailing_list.views import IndexView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, ClientDeactivatedListView, client_toggle_activity, MailingListMessageListView, \
    MailingListMessageDetailView, MailingListMessageCreateView, MailingListMessageUpdateView, \
    MailingListMessageDeleteView, MailingListListView, MailingListDetailView, MailingListCreateView, \
    MailingListUpdateView, MailingListDeleteView

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
    path('mailing_lists/', MailingListListView.as_view(), name='mailing_lists_list'),
    path('mailing_lists/<int:pk>/', MailingListDetailView.as_view(), name='mailing_list_detail'),
    path('mailing_lists/create/', MailingListCreateView.as_view(), name='mailing_list_create'),
    path('mailing_lists/update/<int:pk>/', MailingListUpdateView.as_view(), name='mailing_list_update'),
    path('mailing_lists/delete/<int:pk>/', MailingListDeleteView.as_view(), name='mailing_list_delete'),
]
