from django.urls import path
from .views import PatientList,VeterinarianList,CoatList

urlpatterns = [
    path("patient/", PatientList.as_view()),
    path("vet/", VeterinarianList.as_view()),    
    path("coat/", CoatList.as_view()),    
]