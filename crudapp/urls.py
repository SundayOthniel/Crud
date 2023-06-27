from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gradeStudent', views.gradeStudent, name='gradeStudent'),
    path('studentGrade', views.studentGrade, name='StudentGrade'),
    path('deleteStudentGrade/<int:pk>', views.deleteStudentGrade, name='deleteStudentGrade'),
    path('updateStudentGrade/<int:pk>', views.updateStudentGrade, name='updateStudentGrade'),
]
