from django.urls import path

from .views import (
    get_notifications,
    mark_as_read,
    mark_all_as_read,
)


urlpatterns = [
    path(
    'api/notifications/',
    get_notifications,
    name='get-notifications'
),

    path("<int:id>/read/", mark_as_read, name="mark-as-read"),
    path("read-all/", mark_all_as_read, name="mark-all-as-read"),
]
