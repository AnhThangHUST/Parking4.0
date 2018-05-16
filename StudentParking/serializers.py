from rest_framework import serializers
from StudentParking.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'studentID', 'faculty', 'birthday', 'vehicle', 'kindOfTicket', 'startDate', 'expirationDate')

class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = ('student', 'numberPlate', 'timeIn')

class DailyTurnManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTurnManagement
        fields = ("id", 'student', 'numberPlate', 'timeIn', 'timeOut')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('numberPlate', 'status')
