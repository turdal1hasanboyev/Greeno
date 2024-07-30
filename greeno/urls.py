from django.urls import path

from greeno import views


urlpatterns = [
    path('', views.home, name='home')
]
