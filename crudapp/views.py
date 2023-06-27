from django.shortcuts import get_object_or_404, redirect, render
from .models import GradeStudent
from .form import courseform


def index(request):
    return render(request, 'index.html')


def gradeStudent(request):
    form = courseform()
    if request.method == "POST":
        form = courseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'gradeStudent.html', {'form': form})


def studentGrade(request):
    grades = GradeStudent.objects.all()
    return render(request, 'studentGrade.html', {'grades': grades})


def deleteStudentGrade(request, pk):
    grade = get_object_or_404(GradeStudent, pk=pk)
    grade.delete()
    return redirect('/')


def updateStudentGrade(request, pk):
    grade = GradeStudent.objects.get(pk=pk)
    if request.method == "POST":
        form = courseform(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('/studentGrade')
    return render(request, 'updateStudentGrade.html', {'grade':grade})
