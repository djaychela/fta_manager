from django.urls import path, include

from .views import NoteCreate, NoteDetail, NoteList, NoteUpdate, NoteAdd


urlpatterns = [
    path("new/", NoteCreate.as_view(), name="note_create"),
    path("new_add/<int:transaction>", NoteAdd.as_view(), name="note_add_new"),
    path("list/", NoteList.as_view(), name="note_list"),
    path("update/<int:pk>", NoteUpdate.as_view(), name="note_update"),
]