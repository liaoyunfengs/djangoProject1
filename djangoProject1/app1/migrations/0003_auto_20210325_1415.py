# Generated by Django 3.1.7 on 2021-03-25 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_course_student_teacher_teacherassistant'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.teacher', verbose_name='课程讲师'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='app1.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='teacherassistant',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.teacher', verbose_name='讲师'),
        ),
    ]
