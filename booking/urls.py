from django.urls import include, path
from rest_framework import routers

from booking import views

urlpatterns = [
	path('', views.BookingList.as_view(), name='booking_list'),
    path('<int:studio_id>/percent/', views.percentage_booked, name='percentage_booked'),
]