from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy

from apps.transaction.models import Transaction

from .models import Note
from .forms import NoteForm, NoteAddForm

# Create your views here.
class NoteCreate(CreateView):
    form_class = NoteForm
    template_name = "note_create.html"
    success_url = reverse_lazy("note_list")

class NoteAdd(CreateView):
    form_class = NoteAddForm
    template_name = "note_create.html"
    success_url = reverse_lazy("note_list")

    def get_form_kwargs(self):
        try:
            trans = Transaction.objects.filter(id=self.kwargs['transaction']).first()
        except KeyError:
            trans = "0"
        if self.request.method == "POST":
            kwargs = super().get_form_kwargs()
            print("**** PRE ****")
            print(kwargs)
            kwargs['data'] = kwargs['data'].copy()
            kwargs['data']['transaction'] = trans.id
            print("**** POST ****")
            print(kwargs)
            return kwargs
        return super().get_form_kwargs()

class NoteList(ListView):
    model = Note
    template_name = "note_list.html"

class NoteDetail(DetailView):
    model = Note
    fields = "__all__"
    template_name = "note_detail.html"

class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note_update.html"
    success_url = reverse_lazy("note_list")
