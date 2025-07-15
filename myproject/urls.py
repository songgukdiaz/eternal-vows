"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('eternalvows', views.eternalvows, name="eternalvows"),
    path('logout', views.logout, name="logout"),
    path('bienvenida', views.bienvenida, name="bienvenida"),
    path('itinerario', views.itinerario, name="itinerario"),
    path('viaje-y-alojamiento', views.viaje_y_alojamiento, name="viaje_y_alojamiento"),
    path('que-hacer-y-donde-ir', views.que_hacer_y_donde_ir, name="que_hacer_y_donde_ir"),
    path('nuestro-deseo', views.nuestro_deseo, name="nuestro_deseo"),
    path('galeria', views.galeria, name="galeria"),
    path('preguntas-frecuentes', views.preguntas_frecuentes, name="preguntas_frecuentes"),
]
