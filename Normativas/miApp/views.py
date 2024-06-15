from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Incidente
from .models import Normativa
# Create your views here.
class NormativaListView(ListView):
    model = Normativa
    template_name = 'normativa_list.html'

class NormativaListViewTabla(ListView):
    model = Normativa
    template_name = 'normativa_list_tabla.html'

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

class IncidenteListView(ListView):
    model = Incidente
    template_name = 'incidente_list.html'

class IncidenteCreateView(CreateView):
    model = Incidente
    fields = [ 'descripcion', 'fecha_creacion','motivo', 'tipo', 'severidad', 'equipo_afectado', 'descripcion_equipo_afectado', 'accion_tomada', 'fecha_accion', 'conclusion', 'recomendacion']
    template_name = 'incidente_form.html'
    success_url = reverse_lazy('incidente_list')

class IncidenteUpdateView(UpdateView):
    model = Incidente
    fields = [ 'descripcion','fecha_creacion', 'motivo', 'tipo', 'severidad', 'equipo_afectado', 'descripcion_equipo_afectado', 'accion_tomada', 'fecha_accion', 'conclusion', 'recomendacion', 'estado']
    template_name = 'incidente_form.html'
    success_url = reverse_lazy('incidente_list')

class IncidenteDeleteView(DeleteView):
    model = Incidente
    template_name = 'incidente_confirm_delete.html'
    success_url = reverse_lazy('incidente_list')