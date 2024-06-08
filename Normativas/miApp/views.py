from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Normativa
# Create your views here.
class NormativaListView(ListView):
    model = Normativa
    template_name = 'normativa_list.html'

class NormativaDetailView(DetailView):
    model = Normativa
    template_name = 'normativa_detail.html'

class NormativaCreateView(CreateView):
    model = Normativa
    template_name = 'normativa_form.html'
    fields = ['tipo', 'detalle', 'descripcion', 'link']
    success_url = reverse_lazy('normativa_list')

class NormativaUpdateView(UpdateView):
    model = Normativa
    template_name = 'normativa_form.html'
    fields = ['tipo', 'detalle', 'descripcion', 'link']
    success_url = reverse_lazy('normativa_list')

class NormativaDeleteView(DeleteView):
    model = Normativa
    template_name = 'normativa_confirm_delete.html'
    success_url = reverse_lazy('normativa_list')