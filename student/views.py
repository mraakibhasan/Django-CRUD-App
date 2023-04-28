from django.shortcuts import *
from student.models import *
from django.core.paginator import Paginator

# Registration Function
def studentRegister(request):
    student_data = student.objects.all()
    # Using search filter
    if request.method == "GET":
        search_inp = request.GET.get('search')
        if search_inp != None:
            student_data = student.objects.filter(name__icontains=search_inp)
    
    # Using Paginator
    pages = Paginator(student_data,8)
    page_number = request.GET.get('page')
    updated_page = pages.get_page(page_number) # Updated page for the list of all sutdent data
    total_page = updated_page.paginator.num_pages
    page_list = [n+1 for n in range (total_page)]

    if request.method == "POST":
        name_inp = request.POST.get('name')
        email_inp = request.POST.get('email')
        phone_inp = request.POST.get('phone')
        password_inp = request.POST.get('password')
        address_inp = request.POST.get('address')

        model_connect = student(name=name_inp, email=email_inp, phone=phone_inp, password=password_inp, address=address_inp)
        model_connect.save()

         # Set success flag in session
        request.session['form_submitted'] = True

        # Redirect to the same page
        return redirect('/')

    # Check if success flag is present in session
    form_submitted = request.session.pop('form_submitted', False)

    context = {
        'form_submitted': form_submitted,
        'student_data' : updated_page,
        'page_list' : page_list,
    }
    return render(request, 'index.html',context)


# Update Function
def updateStudent(request, id):
    students_data = student.objects.filter(pk=id)

    if students_data.exists():
        student_data = students_data.first()
    else:
        return redirect('index')

    attributes = ['name', 'email', 'phone', 'password', 'address']

    if request.method == "POST":
        for attr in attributes:
            setattr(student_data, attr, request.POST.get(attr))
            student_data.save()

        return redirect('/')

    context = {'student': student_data}
    return render(request, 'update.html', context)


# Delete Function
def deleteStudent(request,id):
        student_data = student.objects.filter(pk=id)
        student_data.delete()

        return redirect('/')


