from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projects(request):
    return HttpResponse('Here are your projects')

def project(request, pk):
    return HttpResponse(f'Single project {pk}')