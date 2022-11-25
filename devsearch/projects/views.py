from email import message
from django.shortcuts import render
from django.http import HttpResponse


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
    page = "projects"
    number = 10
    context = {'page':page, 'number': number, 'projects':projectList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None 
    for i in projectList:
        if i['id'] == int(pk):
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})