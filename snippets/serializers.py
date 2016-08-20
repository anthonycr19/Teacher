from rest_framework.serializers import ModelSerializer


from snippets.models import Student
from snippets.models import Teacher


class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student


class TeacherSerializer(ModelSerializer):

    class Meta:
        model = Teacher
