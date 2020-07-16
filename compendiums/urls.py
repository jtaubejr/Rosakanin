from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='compendiums-home'),
    path('Anna_Williams/', views.anna, name='compendiums-anna'),
    path('Armor_King/', views.armor_king, name='compendiums-armor_king'),
    path('Eliza/', views.eliza, name='compendiums-eliza'),
    path('Julia_Chang/', views.julia, name='compendiums-julia'),
    path('Leo_Kliesen/', views.leo, name='compendiums-leo'),
    path('Negan/', views.negan, name='compendiums-negan'),
    path('Negan/Grabs', views.neganGrabs, name='compendiums-negan-grabs'),
    path('Negan/Punishment', views.neganPunishment, name='compendiums-negan-punishment'),
    path('Negan/Combos', views.neganCombos, name='compendiums-negan-combos'),
    path('Negan/Wall', views.neganWall, name='compendiums-negan-wall'),
    path('Nina_Williams/', views.nina, name='compendiums-nina'),
    path('Nina_Williams/Grabs', views.ninaGrabs, name='compendiums-nina-grabs'),
    path('Nina_Williams/Punishment', views.ninaPunishment, name='compendiums-nina-punishment'),
    path('Nina_Williams/Combos', views.ninaCombos, name='compendiums-nina-combos'),
    path('Nina_Williams/Wall', views.ninaWall, name='compendiums-nina-wall'),
    path('Nina_Williams/Resource', views.ninaResource, name='compendiums-nina-resource'),
    path('Zafina/', views.zafina, name='compendiums-zafina'),
    path('Seth/', views.seth, name='compendiums-seth'),
    path('Seth/Combos', views.sethCombos, name='compendiums-seth-combos')
]
