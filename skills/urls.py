from django.urls import path
from .views import skills_page

app_name = 'skills'


urlpatterns = [
    path("", skills_page, name="skill"),
]
