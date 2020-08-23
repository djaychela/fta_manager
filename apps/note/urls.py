from django.urls import path, include

from .views import NoteCreate, NoteDetail, NoteList, NoteUpdate


urlpatterns = [
    path("new/", NoteCreate.as_view(), name="note_create"),
    path("list/", NoteList.as_view(), name="note_list"),
]