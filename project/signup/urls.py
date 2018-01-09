from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', auth_views.login, {'template_name': 'signup/login.html'}, name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^detail/(?P<id>\d+)$', views.detail, name='detail'),
]