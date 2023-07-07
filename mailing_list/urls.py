from django.urls import path
from mailing_list.apps import MailingListConfig
from mailing_list.views import IndexView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, client_toggle_activity

app_name = MailingListConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('client/toggle/<int:pk>', client_toggle_activity, name='client_toggle_activity'),
]
