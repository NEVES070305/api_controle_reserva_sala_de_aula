from django.views import View
from django.http import JsonResponse
from apiControle.models import Classroom, Schedule
from apiControle.serializer import ClassroomSerializer, ScheduleSerializer
from apiControle.repository import Repository

class ClassroomAvailableTimesView(View):
    def get(self, request, id):
        repository = Repository('schedules')
        schedules = repository.getByAttribute('class_id', id)
        serializer = ScheduleSerializer(schedules, many=True)
        return JsonResponse(serializer.data, safe=False)

class ClassroomReserveView(View):
    def post(self, request, id):
        # Verificar se a sala de aula está disponível para reserva
        schedule_data = {
            'class_id': id,
            'hour': request.data.get('hour'),
            'reserved': True
        }
        serializer = ScheduleSerializer(data=schedule_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ClassroomCancelReservationView(View):
    def delete(self, request, id):
        repository = Repository('schedules')
        schedule = repository.getById(id)
        if schedule:
            repository.delete(id)
            return JsonResponse({"message": "Reservation canceled"}, status=204)
        return JsonResponse({"error": "Schedule not found"}, status=404)
