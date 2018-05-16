from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^Student/$', views.StudentList.as_view()),
    url(r'^Student/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
    url(r'^ParkingLot/$', views.ParkingLotList.as_view()),
    url(r'^ParkingLot/(?P<numberPlate>[\w|\Wa-z0-9]+)/$', views.ParkingLotDetail.as_view()),
    url(r'^TurnManagement/$', views.TurnManagementList.as_view()),
    url(r'^TurnManagement/(?P<numberPlate>[\w|\Wa-z0-9]+)/$', views.TurnMangementDetail.as_view()),
    url(r'^VehicleIn/$', views.vehicleIn),
    url(r'^VehicleOut/$', views.vehicleOut),
    url(r'^RegisterMonthlyTicket/$', views.registerMonthlyTicket),
]

urlpatterns = format_suffix_patterns(urlpatterns)
