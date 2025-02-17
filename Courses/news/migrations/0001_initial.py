# Generated by Django 5.1.4 on 2024-12-13 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Kurs nomi')),
                ('descriptions', models.TextField(verbose_name='Kurs tavsifi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Talaba ismi')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('enrolled_at', models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqti")),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='news.courses', verbose_name='Kurs')),
            ],
        ),
    ]
