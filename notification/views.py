from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer


@api_view(["GET"])
def get_notifications(request):
    notifications = Notification.objects.all().order_by("-created_at")

    serializer = NotificationSerializer(notifications, many=True)

    return Response(serializer.data)


@api_view(["PATCH"])
def mark_as_read(request, id):
    try:
        notification = Notification.objects.get(id=id)
    except Notification.DoesNotExist:
        return Response(
            {"detail": "Notification not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    notification.is_read = True
    notification.save(update_fields=["is_read"])

    serializer = NotificationSerializer(notification)

    return Response(serializer.data)


@api_view(["POST"])
def mark_all_as_read(request):
    Notification.objects.filter(is_read=False).update(is_read=True)

    return Response(
        {"message": "All notifications marked as read."},
        status=status.HTTP_200_OK,
    )
