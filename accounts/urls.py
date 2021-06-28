from django.conf.urls import url
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^cargo-list/$', views.show_cargo_list, name='cargo'),
    url(r'user-page/$', views.user_page_view, name='user'),
    url('', views.logout_view, name='logout'),
]