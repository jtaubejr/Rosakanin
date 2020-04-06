from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='compendiums-home'),
    path('Anna_Williams/', views.anna, name='compendiums-anna'),
    path('Armor_King/', views.armor_king, name='compendiums-armor_king'),
    path('Eliza/', views.eliza, name='compendiums-eliza'),
    path('Julia_Chang/', views.julia, name='compendiums-julia'),
    path('Julia_Chang/', views.julia, name='compendiums-julia'),
    path('Leo_Kliesen/', views.leo, name='compendiums-leo'),
    path('Negan/', views.negan, name='compendiums-negan'),
    path('Zafina/', views.zafina, name='compendiums-zafina')
]
