from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from datetime import datetime
from rest_framework.decorators import api_view

# Create your views here.
class StudentList(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student  = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MomentStatusList(APIView):
    def get(self, request, format = None):
        tempParks = MomentStatus.objects.all()
        serializer = MomentStatusSerializer(tempParks, many=True)
        return Response(serializer.data)

class MomentStatusDetail(APIView):
    def get_object(self, pk):
        try:
            return MomentStatus.objects.get(pk=pk)
        except MomentStatus.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tempPark  = self.get_object(pk)
        serializer = MomentStatusSerializer(tempPark)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tempPark = self.get_object(pk)
        serializer = MomentStatusSerializer(tempPark, data=request.data)
        print (request.data)
        print (type(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tempPark = self.get_object(pk)
        tempPark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DailyReportList(APIView):
    def get(self, request, format = None):
        report = DailyReport.objects.all()
        serializer = DailyReportSerializer(report, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def vehicleIn(request):
    json = request.data
    try:
        student = Student.objects.get(pk=json["studentID"])
        if len(MomentStatus.objects.filter(pk=json["numberPlate"])):
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    del json["studentID"]
    timeIn = datetime.now()
    json["timeIn"] = timeIn
    json["student"] = student
    statusSerializer = MomentStatusSerializer(data = json)
    timeOut = None
    json["timeOut"] = timeOut
    dailySerializer = DailyReportSerializer(data = json)
    if statusSerializer.is_valid():
        statusSerializer.save()
        if dailySerializer.is_valid():
            dailySerializer.save()
        return Response(statusSerializer.data, status=status.HTTP_201_CREATED)
    return Response(statusSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def vehicleOut(request):
    json = request.data
    try:
        tempPark = MomentStatus.objects.get(pk=json["numberPlate"])
    except MomentStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    json["timeIn"] = tempPark.getTimeIn()
    tempPark.delete()
    json["timeOut"] = datetime.now() 
    objectReport = DailyReport.objects.get(timeIn=json["timeIn"])
    objectReport.setTimeOut(json["timeOut"])
    objectReport.save()
    return Response(json, status=status.HTTP_201_CREATED)
