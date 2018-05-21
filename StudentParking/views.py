from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from datetime import datetime, date
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# Liet ke tat ca cac sinh vien va xe cua sinh vien
    def get(self, request, format=None):
        template = loader.get_template('index.html')
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        context = {
            'svList': serializer.data,
        }
       # return Response(serializer.data)
        return HttpResponse(template.render(context, request))

# Tao moi ve xe cho sinh vien
    def post(self, request, format=None):
        if (Vehicle.objects.filter(pk = request.data["vehicle"])):
            return Response("This vehicle existed",status=status.HTTP_400_BAD_REQUEST)
        vehicle = Vehicle.objects.create(pk = request.data["vehicle"]) 
        vehicle.save()
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

# Lay thong tin cua 1 sinh vien
    def get(self, request, pk, format=None):
        student  = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

# Sua thong tin tren ve cho sinh vien
    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        if (Vehicle.objects.filter(pk = request.data["vehicle"])):
            if (student.getNumberPlate() != request.data["vehicle"]):
                return Response("This vehicle belong to other student",status=status.HTTP_400_BAD_REQUEST)
        else: 
            Vehicle.objects.filter(pk = student.getNumberPlate()).delete()
            vehicle = Vehicle.objects.create(pk = request.data["vehicle"]) 
            vehicle.save()
        if "kindOfTicket" in request.data:
            return Response("You not have permission to change this. Please register your ticket in properly way", status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Xoa thong tin ve cua sinh vien
    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        vehicle = Vehicle.objects.get(pk = student.getNumberPlate())
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Thong ke cac xe gui trong bai
class ParkingLotList(APIView):
    def get(self, request, format = None):
        tempParks = ParkingLot.objects.all()
        serializer = ParkingLotSerializer(tempParks, many=True) 
        return Response(serializer.data)

class ParkingLotDetail(APIView):
    def get_object(self, numberPlate):
        try:
            return ParkingLot.objects.get(numberPlate = numberPlate)
        except ParkingLot.DoesNotExist:
            raise Http404

# Xem ho so cua 1 xe trong bai 
    def get(self, request, numberPlate, format=None):
        tempPark  = self.get_object(numberPlate)
        serializer = ParkingLotSerializer(tempPark)
        return Response(serializer.data)


class TurnManagementList(APIView):
    def get(self, request, format = None):
        report = DailyTurnManagement.objects.all()
        serializer = DailyTurnManagementSerializer(report, many=True)
        return Response(serializer.data)

class TurnMangementDetail(APIView):
    def get_object(self, numberPlate):
        try:
            return DailyTurnManagement.objects.filter(numberPlate = numberPlate)
        except DailyTurnManagement.DoesNotExist:
            raise Http404

# Thong luot gui chi tiet trong ngay
    def get(self, request, numberPlate, format=None):
        tempPark  = self.get_object(numberPlate)
        serializer = DailyTurnManagementSerializer(tempPark, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def vehicleIn(request):
    json = request.data
    if (ParkingLot.objects.filter(numberPlate = json["numberPlate"])):
        return Response("This vehicle was parked. Please check this student", status=status.HTTP_400_BAD_REQUEST)
    try:
        student = Student.objects.get(pk=json["student"])
    except Student.DoesNotExist:
        return Response("This person did not have ticket!", status=status.HTTP_404_NOT_FOUND)
    if student.getNumberPlate() != json["numberPlate"]:
        return Response("Student has registered another vehicle.", status=status.HTTP_400_BAD_REQUEST)
    vehicle = Vehicle.objects.get(pk = json["numberPlate"])
    vehicle.status = True
    vehicle.save()
    timeIn = datetime.now()
    json["timeIn"] = timeIn
    statusSerializer = ParkingLotSerializer(data = json)
    timeOut = None
    json["timeOut"] = timeOut
    dailySerializer = DailyTurnManagementSerializer(data = json)
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
        # Lay xe ra dua theo bien so xe roi check lai so voi sinh vien
        tempPark = ParkingLot.objects.get(numberPlate = json["numberPlate"])
        if tempPark.student.studentID != json["student"]:
            return Response("This vehicle does not belong to the sutdent", status=status.HTTP_400_BAD_REQUEST)
    except ParkingLot.DoesNotExist:
        return Response("This vehicle wasn't parked here", status=status.HTTP_404_NOT_FOUND)
    vehicle = Vehicle.objects.get(pk = json["numberPlate"])
    vehicle.status = False 
    vehicle.save()
    json["timeIn"] = tempPark.timeIn
    tempPark.delete()
    json["timeOut"] = datetime.now() 
    objectReport = DailyTurnManagement.objects.get(timeIn=json["timeIn"])
    objectReport.setTimeOut(json["timeOut"])
    objectReport.save()
    return Response(json, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def registerMonthlyTicket(request):
    json = request.data
    try:
        student = Student.objects.get(pk = json["studentID"])
    except Student.DoesNotExist:
        return Response("This person haven't had ticket!", status=status.HTTP_404_NOT_FOUND)
    kindOfTicket = bool(json["kindOfTicket"])
    # Neu la ve thang
    if kindOfTicket == True:
        student.kindOfTicket = True 
        year, month, day = map(int, json["startDate"].split("-"))
        startDate = date(year, month, day)
        student.setStartDate(startDate)
        year, month, day = json["expirationDate"].split("-")
        expirationDate = date(int(year), int(month), int(day))
        student.setExpirationDate(expirationDate)
        student.save()
        return Response("Register Monthly Ticket successfully!!")
    else: 
        return Response("Ticket is still daily ticket")
