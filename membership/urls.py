from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member-card', views.memberCard, name='memberCard')
]
