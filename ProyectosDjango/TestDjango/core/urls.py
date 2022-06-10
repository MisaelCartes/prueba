from django.urls import path
from core import views

urlpatterns = [
    path ('',views.home, name="home"),
    path ('insumos/',views.insumos, name="insumos"),
    path ('maceteros/',views.maceteros, name="maceteros"),
    path ('perfil/',views.perfil, name="perfil"),
    path ('paginalogin/',views.paginalogin, name="paginalogin"),
    path ('registro/',views.registro, name="registro"),
    path ('donaciones/',views.donaciones, name="donaciones"),
]