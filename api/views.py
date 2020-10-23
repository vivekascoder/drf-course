from django.shortcuts import render
from api.models import Todo
from django.http import JsonResponse
from api.serializers import TodoSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def todo(request, pk):
    def get_queryset():
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return JsonResponse(
                {
                    "error": f"There is no todo having primary key {pk}"
                }
            )
        return todo
    
    if request.method == "GET":
        todo = get_queryset()
        serializer = TodoSerializer(instance=todo)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def create_todo(request):
    if request.method == "GET":
        return JsonResponse({'error': "GET is not allowed"})
    elif request.method == "POST":
        serializer = TodoSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)




    