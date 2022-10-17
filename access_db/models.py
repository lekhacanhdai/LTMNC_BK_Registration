from django.db import models

# Create your models here.

class Term(models.Model):
    id = models.AutoField(primary_key=True,db_column='id', null=False)
    name = models.CharField(max_length=100, db_column='name_')
    class_id = models.CharField(max_length=50, unique=True, null=False, db_column='class_id')
    credits_number = models.FloatField(db_column='credits_number')
    teacher_name = models.CharField(db_column='teacher_name', max_length=100)
    schedule = models.CharField(db_column='schedule_', max_length=100)
    week = models.CharField(db_column='week_', max_length=50)
    quantity = models.IntegerField(db_column='quantity')
    registered = models.IntegerField(db_column='registered')
    is_clc = models.BooleanField(db_column='is_clc')
    class Meta:
        db_table='term'
        
class HocPhan(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', null=False)
    term_name = models.CharField(max_length=1000, null=True, db_column='term_name')
    term_code = models.CharField(max_length=50, db_column='term_code', unique=True, null=False)
    credits_number = models.FloatField(db_column='credits_number', null=True)
    class Meta:
        db_table='hoc_phans'