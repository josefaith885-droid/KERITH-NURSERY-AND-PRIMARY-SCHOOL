from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student, Grade

@login_required
def student_dashboard(request):
    if request.user.user_type != 3:
        return render(request, '403.html', status=403)
        
    student_profile = Student.objects.get(user=request.user)
    grades = Grade.objects.filter(student=student_profile)
    
    return render(request, 'dashboard/student.html', {
        'profile': student_profile,
        'grades': grades
    })


# Create your views here.
