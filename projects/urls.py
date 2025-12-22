from django.urls import path
from .views import project_page

app_name ="projects"

urlpatterns = [
    path('', project_page, name ='project')
]
