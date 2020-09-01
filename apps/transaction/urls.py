from django.urls import path, include

from .views import TransCreate, TransList, TransUpdate, TransDetail

urlpatterns = [
    path("new/", TransCreate.as_view(), name="trans_create"),
    path("list/", TransList.as_view(), name="trans_list"),
    path("update/<int:pk>", TransUpdate.as_view(), name="trans_update"),
    path("detail/<int:pk>", TransDetail.as_view(), name="trans_detail"),
]