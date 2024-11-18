from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('accueil', views.accueil, name='accueil'),
    path('bateau', views.boats_list, name='boats_list'),
    path('bateau/create', views.create_boats, name = 'create_boats' ),
    path('bateau/<str:pk>/', views.boats_detail, name='boats_detail'),
    path('bateau/<str:pk>/modify', views.modify_boats, name = 'modify_boats' ),
    path('bateau/<str:pk>/delete', views.delete_boats, name = 'delete_boats' ),
    path('port', views.ports_list, name='ports_list'),
    path('port/create', views.create_ports, name = 'create_ports' ),
    path('port/<str:pk>/', views.ports_detail, name='ports_detail'),
    path('port/<str:pk>/modify', views.modify_ports, name='modify_ports'),
    path('port/<str:pk>/delete', views.delete_ports, name='delete_ports'),
    path('voyager/', views.voyager, name='voyager'),
    path('maintenance/', views.maintenance, name='maintenance'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
