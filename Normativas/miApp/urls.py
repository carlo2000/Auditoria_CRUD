from django.urls import path
from django.conf import settings
from .views import ComunicadoListView, NormativaListView, NormativaDetailView, NormativaCreateView, NormativaUpdateView, NormativaDeleteView,NormativaListViewTabla,IncidenteListView, IncidenteCreateView, IncidenteUpdateView, IncidenteDeleteView

from django.conf.urls.static import static

urlpatterns = [
    path('', ComunicadoListView.as_view(), name='comunicado_list'),
    path('tabla/', NormativaListViewTabla.as_view(), name='normativa_list_tabla'),
    path('<int:pk>/', NormativaDetailView.as_view(), name='normativa_detail'),
    path('new/', NormativaCreateView.as_view(), name='normativa_new'),
    path('<int:pk>/edit/', NormativaUpdateView.as_view(), name='normativa_edit'),
    path('<int:pk>/delete/', NormativaDeleteView.as_view(), name='normativa_delete'),
    
    path('incidentes/', IncidenteListView.as_view(), name='incidente_list'),
    path('incidentes/crear/', IncidenteCreateView.as_view(), name='incidente_create'),
    path('incidentes/<int:pk>/editar/', IncidenteUpdateView.as_view(), name='incidente_update'),
    path('incidentes/<int:pk>/eliminar/', IncidenteDeleteView.as_view(), name='incidente_delete'),

    path('normativa/', NormativaListView.as_view(), name='normativa_list'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)