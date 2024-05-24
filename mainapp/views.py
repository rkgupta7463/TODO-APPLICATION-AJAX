from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import TaskModel
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    taskAll=TaskModel.objects.all().order_by('-created')
    return render(request,"index.html",{"taskAll":taskAll})

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('taskTitle')
        task_message = request.POST.get('taskMessage')
        if task_title and task_message:
            task = TaskModel(taskTitle=task_title, taskMessage=task_message)
            task.save()
            return JsonResponse({'status': 'success', 'message': 'Task added successfully'})
        else:
            return JsonResponse({'status': 'fail', 'message': 'Invalid data'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})

@csrf_exempt
def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('taskId')
        try:
            task = TaskModel.objects.get(id=task_id)
            task.delete()
            return JsonResponse({'status': 'success', 'message': 'Task deleted successfully'})
        except TaskModel.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Task does not exist'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})



@csrf_exempt
def update_task(request):
    if request.method == "POST":
        try:
            task_id = request.POST.get('taskId')
            task_title = request.POST.get('taskTitle')
            task_message = request.POST.get('taskMessage')

            if not (task_id and task_title and task_message):
                return JsonResponse({'status': 'fail', 'message': 'Missing required parameters!'})

            get_task = TaskModel.objects.get(id=task_id)
            get_task.taskTitle = task_title
            get_task.taskMessage = task_message
            get_task.save()

            return JsonResponse({'status': 'success', 'message': 'Task updated successfully'})
        except TaskModel.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Task does not exist!'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'message': 'Invalid JSON!'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method!'})