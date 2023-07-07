from django.urls import path
from mailing_list.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    ]
