from rest_framework import generics
from .models import Patient, Veterinarian,Coat
from .serializers import PatientSerializer,VeterinarianSerializer,CoatSerializer


class PatientList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        name = self.request.query_params.get('name', None) 
        birth_date_from = self.request.query_params.get('birth_date_until', None)
        birth_date_until = self.request.query_params.get('birth_date_until', None)
        is_castrated = self.request.query_params.get('is_castrated', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        if birth_date_from is not None:
            queryset = queryset.filter(birth_date__gt=birth_date_from)

        if birth_date_until is not None:
            queryset = queryset.filter(birth_date__lt=birth_date_until) 

        if is_castrated is not None:
            queryset = queryset.filter(is_castrated=is_castrated)

        return queryset


class VeterinarianList(generics.ListCreateAPIView):
    queryset = Veterinarian.objects.all()
    serializer_class = VeterinarianSerializer


class CoatList(generics.ListCreateAPIView):
    queryset = Coat.objects.all()
    serializer_class = CoatSerializer
   
