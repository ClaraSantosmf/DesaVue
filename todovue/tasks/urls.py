from django.urls import path
from tasks import views

urlpatterns = [
    path('/task', views.listartask, name ="tasks" ),
    ]
