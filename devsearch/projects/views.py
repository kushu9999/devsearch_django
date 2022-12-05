from email import message
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectList = [
    {
        'id':1,
        'title': "Ecom Website",
        'description': "Fully functional ecom site"
    },
    {
        'id':2,
        'title': "Fully Functional Website",
        'description': "Fully functional ecom site"
    },
    {
        'id':3,
        'title': "Book Website",
        'description': "Fully functional ecom site"
    },
]
# Create your views here.
def projects(request):
    project = Project.objects.all()
    context = {'projects':project}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})