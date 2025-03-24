from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer
from django.shortcuts import get_object_or_404

# Label Views
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_label(request):
    serializer = LabelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_label(request, label_id):
    label = get_object_or_404(Label, id=label_id, owner=request.user)
    serializer = LabelSerializer(label, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_label(request, label_id):
    label = get_object_or_404(Label, id=label_id, owner=request.user)
    label.delete()
    return Response({"message": "Label deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_labels(request):
    labels = Label.objects.filter(owner=request.user)
    serializer = LabelSerializer(labels, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Task Views
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        task = serializer.save()
        # Handle labels if provided
        label_ids = request.data.get('labels', [])
        for label_id in label_ids:
            try:
                label = Label.objects.get(id=label_id, owner=request.user)
                task.labels.add(label)
            except Label.DoesNotExist:
                pass
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        updated_task = serializer.save()
        # Update labels if provided
        if 'labels' in request.data:
            task.labels.clear()
            for label_id in request.data['labels']:
                try:
                    label = Label.objects.get(id=label_id, owner=request.user)
                    updated_task.labels.add(label)
                except Label.DoesNotExist:
                    pass
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_tasks(request):
#     tasks = Task.objects.all()  # You might want to filter by owner if needed
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def task_detail(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     serializer = TaskSerializer(task)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def toggle_task_completion(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     task.completed = not task.completed
#     task.save()
#     return Response(
#         {"message": "Task completion toggled", "completed": task.completed},
#         status=status.HTTP_200_OK
#     )