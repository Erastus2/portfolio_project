from django.shortcuts import render
from .models import Project
# Create your views here.
def project_page(request):
    projects = Project.objects.all()
    return render(request, "projects/project.html", {
        "projects": projects
    })