from django.urls import path

from Puddle.dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]
