from rest_framework import serializers

from .models import CustomUser, Teacher, Student, StudentResult

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    user = CustomUserSerializer(required=True)
    name = serializers.SerializerMethodField()
    reporting_teacher_name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.user.get_full_name()

    def get_reporting_teacher_name(self, obj):
        return obj.reporting_teacher.user.get_full_name()

    class Meta:
        model = Student
        fields = '__all__'

    

class StudentResultSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    total_marks = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.student.user.get_full_name()

    def get_total_marks(self, obj):
        return obj.total_marks

    class Meta:
        model = StudentResult
        fields = '__all__'

