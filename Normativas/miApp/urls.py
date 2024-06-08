from django.urls import path
from django.conf import settings
from .views import NormativaListView, NormativaDetailView, NormativaCreateView, NormativaUpdateView, NormativaDeleteView
from django.conf.urls.static import static

urlpatterns = [
    path('', NormativaListView.as_view(), name='normativa_list'),
    path('<int:pk>/', NormativaDetailView.as_view(), name='normativa_detail'),
    path('new/', NormativaCreateView.as_view(), name='normativa_new'),
    path('<int:pk>/edit/', NormativaUpdateView.as_view(), name='normativa_edit'),
    path('<int:pk>/delete/', NormativaDeleteView.as_view(), name='normativa_delete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)