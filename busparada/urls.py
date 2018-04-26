from django.conf.urls import re_path
from djoser import views as djoser_views
from rest_framework_jwt import views as jwt_views
from busparada import views

urlpatterns = [
    # Views are defined in Djoser, but we're assigning custom paths.
    #re_path(r'^parada/view/$', djoser_views.UserView.as_view(), name='parada-view'),
    #re_path(r'^parada/delete/$', djoser_views.UserDeleteView.as_view(), name='parada-delete'),
    #re_path(r'^parada/create/$', djoser_views.UserCreateView.as_view(), name='parada-create'),

]
