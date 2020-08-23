from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy

from .models import Note
from .forms import NoteForm

# Create your views here.
class NoteCreate(CreateView):
    form_class = NoteForm
    template_name = "note_create.html"
    success_url = reverse_lazy("note_list")

class NoteList(ListView):
    model = Note
    template_name = "note_list.html"

class NoteDetail(DetailView):
    model = Note
    fields = "__all__"
    template_name = "note_detail.html"

class NoteUpdate(UpdateView):
    model = Note
    fields = ["comment"]
    template_name = "note_update.html"
    success_url = reverse_lazy("note_list")
