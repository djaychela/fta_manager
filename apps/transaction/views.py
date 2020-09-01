from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy

from apps.note.models import Note

from .models import Transaction

# Create your views here.

class TransCreate(CreateView):
    model = Transaction
    fields = "__all__"
    template_name = "trans_create.html"
    success_url = reverse_lazy('trans_list')



class TransList(ListView):
    model = Transaction
    template_name = "trans_list.html"


class TransUpdate(UpdateView):
    model = Transaction
    fields = "__all__"
    template_name = "trans_update.html"
    success_url = reverse_lazy("trans_list")


class TransDetail(DetailView):
    model = Transaction
    fields = "__all__"
    template_name = "trans_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # print(context)
        notes = Note.objects.filter(transaction=context['transaction']).all()
        context['notes'] = notes
        print(context)
        return context
