from django.conf.urls import url
from .views import StudentListAPIView, TeacherListAPIView

urlpatterns = [
    url(r'^students/$', StudentListAPIView.as_view()),
    url(r'^teachers/$', TeacherListAPIView.as_view()),
    url(
        r'^teachers/(?P<teacher_id>\d+)/students/$',
        StudentListAPIView.as_view()),
]
