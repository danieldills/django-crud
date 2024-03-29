from .models import Snack
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy


class SnackListView(ListView):
  template_name = "snack_list.html"
  model = Snack

class SnackDetailView(DetailView):
  template_name = "snack_detail.html"
  model = Snack

class SnackCreateView(CreateView):
  template_name = "snack_create.html"
  model = Snack
  fields = ["name", "description", "purchaser"]
  success_url = reverse_lazy("snack_list")

class SnackUpdateView(UpdateView):
  template_name = "snack_update.html"
  model = Snack
  fields = ["name", "description", "purchaser"]
  success_url = reverse_lazy("snack_list")
  
class SnackDeleteView(DeleteView):
  template_name = "snack_delete.html"
  model = Snack
  success_url = reverse_lazy("snack_list")
