from rest_framework import serializers
from .models import HocPhan, Term

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ["id", "name", "class_id", "credits_number", "teacher_name", "schedule", "week", "quantity", "registered", "is_clc"]
        
class HocPhanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HocPhan
        fields = '__all__'
        