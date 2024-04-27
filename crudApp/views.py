from django.shortcuts import render , redirect
from crudApp.models import employee
from crudApp.forms import employeeForm

# Create your views here.

def retrieve_data(request):
    emp_data = employee.objects.all()
    emp_dict = {'emp_list' : emp_data}
    return render(request , 'crudApp/index.html' , context=emp_dict)

def create_date(request):
    form = employeeForm()
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/select')
    return render(request , 'crudApp/create_update_Employee.html' , {'form':form})

def delete_data(request , id):
    emp_data = employee.objects.get(id=id)
    emp_data.delete()
    return redirect('/select')

def update_date(request , id):
    emp_data = employee.objects.get(id=id)
    form = employeeForm(instance=emp_data)
    if request.method == 'POST':
        form = employeeForm(request.POST , instance=emp_data)
        if form.is_valid():
            form.save()
            return redirect('/select')
    return render(request , 'crudApp/create_update_Employee.html' , {'form':form})
