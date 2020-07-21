from django.urls import path
from .views import ReservationView, NewReservation

urlpatterns = [
    path('', ReservationView.as_view(), name='index'),
    path('reservation', NewReservation.as_view(), name='newreservation')
]

