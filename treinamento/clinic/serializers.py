from rest_framework import serializers
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from .models import Patient, Veterinarian, Tutor,Procedure,Payment,Coat

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class VeterinarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinarian
        fields = '__all__'

class CoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coat
        fields = '__all__'

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):

    age = serializers.SerializerMethodField('get_age')
    is_castrated =  serializers.SerializerMethodField('get_is_castrated')

    tutor = TutorSerializer() 
    veterinarian = VeterinarianSerializer() 
    coat= CoatSerializer()

    # procedures=ProcedureSerializer()
    # payments=PaymentSerializer()
    def get_age(self,obj):
        return relativedelta(timezone.now(),obj.birth_date).years
    
    def get_is_castrated(self,obj):
        return obj.castration_date is not None


    class Meta:
        model = Patient
        fields = ['name','birth_date','age','coat','is_castrated','tutor','veterinarian']