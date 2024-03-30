from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Course


# Create your views here.
def Home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def Signup(request):
    courses = Course.objects.all()
    if request.method == "POST":
        full_name = request.POST['fullname']
        roll_no = request.POST['rollno']
        email = request.POST['email']
        date_birth = request.POST['dob']
        course_id = request.POST['course']
        course = Course.objects.get(pk=course_id)
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # check existence
        user = Student.objects.filter(roll_number=roll_no)

        if user:

            messages.warning(request, 'Student already exist !')
            return redirect('signup')

        else:
            if password == confirm_password:
                new_user = Student.objects.create(name=full_name, roll_number=roll_no, email=email, dob=date_birth,
                                                  course=course, password=password)

                return redirect('register_success')

            else:
                messages.error(request, 'Password does not match with confirm password')
                return redirect('signup')

    return render(request, 'index.html', {'courses': courses})


def login(request):
    if request.method == "POST":
        roll_no = request.POST['rollno']
        password = request.POST['password']
        # confirm_password = request.POST['confirm_password']
        try:
            user = Student.objects.get(roll_number=roll_no)

            if user.password == password:
                request.session['student_id'] = user.id

                return redirect('dashboard')
            else:
                messages.error(request, 'Wrong password')
                return redirect('login')

        except:
            messages.warning(request, 'Student does not exist having this roll no.')
            return redirect('login')

    return render(request, "login.html")


def dashboard(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        image = request.FILES['profile']
        student.profile_photo.delete()
        student.profile_photo = image
        student.save()
        return redirect('dashboard')
    return render(request, "dash.html", {'student': student})


def success_register(request):
    return render(request, "registered.html")
