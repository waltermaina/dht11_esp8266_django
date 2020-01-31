# front_end_app/urls.py
from django.urls import path
from .views import temperature_chart, home, humidity_chart, humidity, about, contact_us

urlpatterns = [
path('', home, name='home'),
path('humidity/', humidity, name='humidity'),
path('about/', about, name='about'),
path('contactus/', contact_us, name='contactus'),
path('temperature_chart/', temperature_chart, name='temperature_chart'),
path('humidity_chart/', humidity_chart, name='humidity_chart'),
]