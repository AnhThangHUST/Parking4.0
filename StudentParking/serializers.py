from rest_framework import serializers
from StudentParking.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('studentID', 'name', 'isMonthlyTicket')

class MomentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomentStatus
        fields = ('student', 'numberPlate', 'timeIn')

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ("id", 'student', 'numberPlate', 'timeIn', 'timeOut')
