from django.urls import path

from Puddle.item import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]
