from django.views import View
from django.http import JsonResponse
from apiControle.models import Classroom, Schedule
from apiControle.serializer import ClassroomSerializer
from apiControle.repository import Repository

class ClassroomListView(View):
    def get(self, request):
        repository = Repository('classrooms')
        classrooms = repository.getAll()
        serializer = ClassroomSerializer(classrooms, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = ClassroomSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ClassroomDetailsView(View):
    def get(self, request, id):
        repository = Repository('classrooms')
        classroom = repository.getById(id)
        if classroom:
            serializer = ClassroomSerializer(classroom)
            return JsonResponse(serializer.data)
        return JsonResponse({"error": "Classroom not found"}, status=404)

    def put(self, request, id):
        repository = Repository('classrooms')
        classroom = repository.getById(id)
        if classroom:
            serializer = ClassroomSerializer(classroom, data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"error": "Classroom not found"}, status=404)

    def delete(self, request, id):
        repository = Repository('classrooms')
        classroom = repository.getById(id)
        if classroom:
            repository.delete(id)
            return JsonResponse({"message": "Classroom deleted"}, status=204)
        return JsonResponse({"error": "Classroom not found"}, status=404)
