# Create your views here.
from rest_framework.generics import ListAPIView


from .serializers import StudentSerializer, TeacherSerializer
from .models import Student, Teacher


class StudentListAPIView(ListAPIView):

    serializer_class = StudentSerializer

    def get_queryset(self):
        try:
            return Teacher.objects.get(
                id=self.kwargs.get('teacher_id')).student.all()
        except:
            return Student.objects.all()


class TeacherListAPIView(ListAPIView):

    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
