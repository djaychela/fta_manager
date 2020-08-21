from django.urls import path, include

from .views import TransCreate, TransList

urlpatterns = [
    path("new/", TransCreate.as_view(), name="trans_create"),
    path("list/", TransList.as_view(), name="trans_list"),
    # path("update/<int:pk>", TransUpdate.as_view(), name="client_update"),
]