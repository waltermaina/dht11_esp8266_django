# api_app/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('v1/', views.ListData.as_view()),
    path('v1/<str:pk>/', views.DataDetail.as_view()),
    path('v2/', views.NewListData.as_view()),
    path('v2/last/', views.LastRecordData.as_view()),
    path('v2/<str:pk>/', views.NewDataDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]