from django.urls import path
from .views import SuperUserLoginApiView

urlpatterns = [
    path('superuser-login/', SuperUserLoginApiView.as_view(), name='superuser-login'),
]