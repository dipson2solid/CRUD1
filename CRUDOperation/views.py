from email import message
from django.shortcuts import render
from CRUDOperation.models import EmpModel
from django.contrib import messages
from CRUDOperation.forms import Empforms

def showemp(request):
    showall=EmpModel.objects.all()
    return render(request, 'index.html', {'data':showall})


def insertemp(request):
    if request.method == "POST":
        if request.POST.get("first_name") and request.POST.get("last_name") and request.POST.get("email") and request.POST.get("gender") and request.POST.get("salary") and request.POST.get("occupation"):
            saverecord = EmpModel()
            saverecord.first_name = request.POST.get("first_name")
            saverecord.last_name = request.POST.get("last_name")
            saverecord.email = request.POST.get("email")
            saverecord.gender = request.POST.get("gender")
            saverecord.salary = request.POST.get("salary")
            saverecord.occupation = request.POST.get("occupation")
            saverecord.save()
            messages.success(request, saverecord.first_name+ ' is saved succesfully... ')
            return render(request, 'insert.html')

    else:
            return render(request, 'insert.html')


def editemp(request, id):
    editempobj=EmpModel.objects.get(id=id)
    return render(request,'edit.html',{'EmpModel':editempobj})


def updateemp(request, id):
    updateemp=EmpModel.objects.get(id=id)
    form=Empforms(request.POST, instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record updated successfully...')
        return render(request,'edit.html',{'EmpModel':updateemp})


def delemp(request, id):
    delempobj=EmpModel.objects.get(id=id)
    delempobj.delete()
    showdata=EmpModel.objects.all()
    return render(request,'index.html',{'data':showdata})
