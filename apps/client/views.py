from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Client
from django.urls import reverse_lazy
# Create your views here.

class ClientCreate(CreateView):
    model = Client
    fields = "__all__"
    template_name = "client_create.html"
    success_url = reverse_lazy('client_list')

class ClientDetail(DetailView):
    model = Client
    fields = "__all__"

class ClientUpdate(UpdateView):
    model = Client
    fields = "__all__"
    template_name = "client_update.html"
    success_url = reverse_lazy('client_list')

class ClientDelete(DeleteView):
    model = Client

class ClientList(ListView):
    model = Client
    template_name = "client_list.html"

