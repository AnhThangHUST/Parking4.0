from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^Student/$', views.StudentList.as_view()),
    url(r'^Student/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
    url(r'^MomentStatus/$', views.MomentStatusList.as_view()),
    url(r'^MomentStatus/(?P<pk>[0-9]+)/$', views.MomentStatusDetail.as_view()),
    url(r'^DailyReport/$', views.DailyReportList.as_view()),
    url(r'^VehicleIn/$', views.vehicleIn),
    url(r'^VehicleOut/$', views.vehicleOut),
]

urlpatterns = format_suffix_patterns(urlpatterns)
