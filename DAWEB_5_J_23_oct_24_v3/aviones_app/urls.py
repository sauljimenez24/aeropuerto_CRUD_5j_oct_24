from django.urls import path
from aviones_app import views
urlpatterns = [
    path("" ,views.listadoAviones,name="listadoAviones")
]
