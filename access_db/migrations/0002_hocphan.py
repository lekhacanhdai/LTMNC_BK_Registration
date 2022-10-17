# Generated by Django 4.1 on 2022-09-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HocPhan',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('term_name', models.CharField(db_column='term_name', max_length=1000, null=True)),
                ('term_code', models.CharField(db_column='term_code', max_length=50, unique=True)),
                ('credits_number', models.FloatField(db_column='credits_number', null=True)),
            ],
            options={
                'db_table': 'hoc_phans',
            },
        ),
    ]
