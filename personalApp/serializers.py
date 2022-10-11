from dataclasses import fields
from rest_framework import serializers
from .models import Department, Personal
from django.utils.timezone import now

class DepartmentSerializer(serializers.ModelSerializer):
    personal_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = ('id', 'name', 'personal_count')

    def get_personal_count(self, obj):
        return Personal.objects.filter(department = obj.id).count() #! 👈 We counted the personnel in the departments.

class PersonalSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    create_user = serializers.StringRelatedField()
    class Meta:
        model = Personal
        fields("__all__")

    def get_days_since_joined(self, obj):
        return (now() - obj.start_date).days #! 👈 converts the result to "days"

class DepartmentPersonalSerializer(serializers.ModelSerializer):
    personal_count = serializers.SerializerMethodField()
    departments = PersonalSerializer(many=True, read_only=True)
    #(nested serializer)obje olarak gösteriyor bütünbilgiler ve many=True yapıyoruz ki birden fazla personel gelebilsin diye
    #deparments modeldeki related name den geliyor
    # deparments = serializers.StringRelatedField(many=True)#+string olrak gösteriyor ama modeldeki __str__ içindekine göre yani admin de nasıl gözüküyorsa
    #deparments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)#öğrencinin id sini gösteriyor
    class Meta:
        model = Department
        fields = ('id', 'name', 'personal_count', 'departments')

    def get_personal_count(self, obj):
        return Personal.objects.filter(department = obj.id).count()