from django.urls import path
from . import views

urlpatterns = [
    path('api/salas/', views.list_class, name='list_rooms'),
    path('api/salas/<int:id>/', views.class_details, name='class_details'),
    path('api/salas/create/', views.create_class, name='create_class'),
    path('api/salas/<int:id>/update/', views.update_class, name='update_class'),
    path('api/salas/<int:id>/delete/', views.delete_class, name='delete_class'),
    path('api/salas/<int:id>/available-times/', views.list_available_times, name='list_available_times'),
    path('api/salas/<int:id>/reserve/', views.reserve_class, name='reserve_class'),
    path('api/reservations/<int:id>/cancel/', views.cancel_reservation, name='cancel_reservation'),
]
