from django.urls import path
from .views import contact_view,contact_success
app_name ="contacts"
urlpatterns = [
    path('',contact_view, name ='contact')
]
# contact/urls.py

urlpatterns = [
    path('', contact_view, name='contact'),  # your contact form page
    path('success/', contact_success, name='contact_success'),  # success page
]
