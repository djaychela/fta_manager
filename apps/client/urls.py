from django.urls import path, include

from .views import ClientCreate, ClientDelete, ClientList, ClientUpdate

urlpatterns = [
    path("new/", ClientCreate.as_view(), name="client_create"),
    path("list/", ClientList.as_view(), name="client_list"),
    path("update/<int:pk>", ClientUpdate.as_view(), name="client_update"),
]