from django.conf.urls import url
from cargos import views

app_name = 'cargos'

urlpatterns = [
    url(r'^add/$', views.add_cargo, name='add'),
    url(r'^transfer/$', views.add_transfer, name='transfer'),
    url(r'^rent/$', views.rent, name='rent'),
    url(r'^root-tr/$', views.rootTr, name='root')
]
