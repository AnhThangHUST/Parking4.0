from django.db import models

# Create your models here.


# Class nay chua thong tin cua xe
class Vehicle(models.Model):
    numberPlate = models.CharField(max_length =30, primary_key = True)
    status = models.BooleanField(default = False)  # False la dang khong duoc gui

    def setNumberPlate(self, newNumberPlate):
        self.numberPlate = newNumberPlate
    
    class Meta:
        ordering = ('numberPlate',)

    def __str__(self):
        return self.numberPlate


# Ve xe di kem luon voi sinh vien
class Student(models.Model):
    name = models.CharField(max_length = 40)
    studentID = models.CharField(max_length = 8, primary_key = True)
    faculty = models.CharField(max_length = 100)
    birthday = models.DateField()
    vehicle = models.OneToOneField(Vehicle, on_delete = models.CASCADE)
    kindOfTicket = models.BooleanField(default = False)         #false co nghia la ve ngay
    startDate = models.DateField(default = None, null = True, blank = True)
    expirationDate = models.DateField(default = None, null = True, blank =  True) 
    
    def setStartDate(self, startDate):
        self.startDate = startDate

    def setExpirationDate(self, expirationDate):
        self.expirationDate = expirationDate

    def getNumberPlate(self):
        return self.vehicle.numberPlate
    
    class Meta:
        ordering = ("studentID", )
        
    def __str__(self):
        return "Student: %s" % self.studentID


# Thong ke tat ca ca xe da gui trong ngay
class DailyTurnManagement(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null = True, blank = True)
    numberPlate = models.CharField(max_length =30)
    timeIn = models.DateTimeField()
    timeOut = models.DateTimeField(blank = True, null = True)
    
    def setTimeIn(self, timeIn):
        self.timeIn = timeIn
    
    def setTimeOut(self, timeOut):
        self.timeOut = timeOut

    class Meta: 
        ordering = ('timeIn', 'numberPlate')
    
    def __str__(self):
       return self.numberPlate 


# Thong ke cac xe dang gui trong nha xe
class ParkingLot(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null = True, blank = True)
    numberPlate = models.CharField(max_length = 30)
    timeIn = models.DateTimeField()
    
    def setTimeIn(self,timeIn):
        self.timeIn = timeIn

    class Meta:
        ordering = ('timeIn', 'numberPlate' )

    def __str__(self):
        return self.numberPlate 


#Thong ke doanh thu theo ngay
class Revenue(models.Model):
    date = models.DateField() 
    revenue = models.CharField(max_length = 30)
    
    class Meta: 
        ordering = ('date',)

    def __str__(self):
        return self.date

