'''from appempresa.views import AdministradorViews, LoginViews, EmpresasViews
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Empresas/',EmpresasViews.as_view(), name="Listar"),
    path('Empresas/<int:User>',EmpresasViews.as_view(), name="Actualizar"),
    path('consultarDatosEmpresa/<int:UserID>',views.consultarempresa, name="Consultarempresa"),
    path('ingresartransccion',views.nuevatransccion, name="nuevatransccion"),
    path('borrartransccion/',views.deletetransccion, name="borrartransccion"),
]'''