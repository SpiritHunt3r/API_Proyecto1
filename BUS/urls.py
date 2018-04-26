"""BUS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, re_path
from busparada.resources import BusParadaResource
from busruta.resources import BusRutaResource
from busempresa.resources import BusEmpresaResource
from busdriver.resources import BusDriverResource
#from bususer.resources import BusUserResource




parada = BusParadaResource()
ruta = BusRutaResource()
empresa = BusEmpresaResource()
driver = BusDriverResource()
#user = BusUserResource()

urlpatterns = [
    re_path(r'^', admin.site.urls),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include('bususer.urls')),
    re_path(r'^api/', include(parada.urls)),
    re_path(r'^api/', include(ruta.urls)),
    re_path(r'^api/', include(empresa.urls)),
    re_path(r'^api/', include(driver.urls)),
    #re_path(r'^api/', include(user.urls)),
]
