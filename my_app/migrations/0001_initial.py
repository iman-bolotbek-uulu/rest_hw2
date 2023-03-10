# Generated by Django 3.2 on 2022-12-23 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positions', models.CharField(max_length=30)),
                ('departments', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('date_birth', models.DateField()),
                ('salary', models.IntegerField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='my_app.position')),
            ],
        ),
    ]
