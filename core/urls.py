from django.urls import path
from apiControle.views.views_classroom import ClassroomDetailsView,ClassroomListView
from apiControle.views.views_reserve import ClassroomAvailableTimesView,ClassroomCancelReservationView, ClassroomReserveView

urlpatterns = [
    path('api/salas/', ClassroomListView.as_view(), name='list_rooms'),
    path('api/salas/<int:id>/', ClassroomDetailsView.as_view(), name='class_details'),
    path('api/salas/criar/', ClassroomListView.as_view(), name='create_class'),
    path('api/salas/<int:id>/atualizar/', ClassroomDetailsView.as_view(), name='update_class'),
    path('api/salas/<int:id>/excluir/', ClassroomDetailsView.as_view(), name='delete_class'),
    path('api/salas/<int:id>/horarios/', ClassroomAvailableTimesView.as_view() , name='list_available_times'),
    path('api/salas/<int:id>/reservar/', ClassroomReserveView.as_view(), name='reserve_class'),
    path('api/reservas/<int:id>/cancelar/', ClassroomCancelReservationView.as_view() , name='cancel_reservation'),
]
