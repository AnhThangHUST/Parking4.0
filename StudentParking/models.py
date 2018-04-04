from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 40)
    studentID = models.CharField(max_length = 8, primary_key = True)
    isMonthlyTicket = models.BooleanField()
    
    class Meta:
        ordering = ("studentID", )
        
    def __str__(self):
        return self.studentID


class DailyReport(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null = True, blank = True)
    numberPlate = models.CharField(max_length = 30)
    timeIn = models.DateTimeField()
    timeOut = models.DateTimeField(blank = True, null = True)
    
    def setTimeOut(self, timeout):
        self.timeOut = timeout

    def getTimeOut(self):
        return self.timeOut 

    class Meta: 
        ordering = ('timeIn','numberPlate')
    
    def __str__(self):
        #return self.timeIn.strftime("%d/%m/%y - %H:%M") 
        return self.numberPlate 
        

class MomentStatus(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null = True, blank = True)
    numberPlate = models.CharField(max_length = 30, primary_key = True)
    timeIn = models.DateTimeField()

    def getNumberPlate(self):
        return self.numberPlate

    def getTimeIn(self):
        return self.timeIn

    class Meta:
        ordering = ('timeIn', 'numberPlate' )

    def __str__(self):
        #return self.timeIn.strftime("%d/%m/%y - %H:%M") 
        return self.numberPlate 
