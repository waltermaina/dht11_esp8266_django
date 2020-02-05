# api_app/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ListData.as_view()),
    path('<str:pk>/', views.DataDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]