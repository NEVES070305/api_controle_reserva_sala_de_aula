from django.views import View
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from apiControle.models import Classroom
from apiControle.serializer import ClassroomSerializer
from apiControle.repository import Repository


class ClassroomListView(View):
    def get(self, request):
        repository = Repository('classrooms')
        classrooms = repository.getAll()
        context = {'classrooms': classrooms}
        return render(request, 'index.html', context)

    def post(self, request):
        repository = Repository('classrooms')
        serializer = ClassroomSerializer(data=request.POST)
        if serializer.is_valid():
            dados_validos = serializer.save()
            dados_dict = {
                'id': dados_validos.id,
                'name': dados_validos.name,
                'capacity': dados_validos.capacity
            }
            repository.insert(dados_dict)
            return HttpResponseRedirect(reverse('list_rooms'))
        return JsonResponse(serializer.errors, status=400)


class ClassroomDetailsView(View):
    def get(self, request, id):
        repository = Repository('classrooms')
        classroom = repository.getById(id)
        if classroom:
            serializer = ClassroomSerializer(classroom)
            context = {'classroom': serializer.data}
            return render(request, 'index.html', context)
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
        success = repository.delete(id)
        
        if success:
            return JsonResponse({"message": "Classroom deleted"}, status=204)
        return JsonResponse({"error": "Classroom not found"}, status=404)
