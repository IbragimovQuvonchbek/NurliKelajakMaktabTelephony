from django.urls import path
from .views import GetCallApiView, GetCallDetailApiView, CreateCallApiView, UpdateCallApiView, DeleteCallApiView

urlpatterns = [
    path('get-calls/', GetCallApiView.as_view(), name='get-calls'),
    path('get-calls/<int:pk>/', GetCallDetailApiView.as_view(), name="get-specific-call"),
    path('create-call/', CreateCallApiView.as_view(), name="create-call"),
    path('update-call/<int:pk>/', UpdateCallApiView.as_view(), name="update-call"),
    path('delete-call/<int:pk>/', DeleteCallApiView.as_view(), name="delete-call"),

]
