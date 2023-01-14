# Generated by Django 4.1.5 on 2023-01-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvgSalaryByCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(verbose_name='Город')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
            ],
        ),
        migrations.CreateModel(
            name='FractionVacancyByCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(verbose_name='Город')),
                ('fraction', models.FloatField(verbose_name='Зарплата')),
            ],
        ),
        migrations.CreateModel(
            name='KeySkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.TextField(verbose_name='Название')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('count', models.IntegerField(verbose_name='Количество повторений')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryByYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryByYearsForCurrentJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(max_length=50, verbose_name='Город')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
            ],
        ),
        migrations.CreateModel(
            name='VacancieByYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancie', models.TextField(verbose_name='Вакансия')),
                ('year', models.IntegerField(verbose_name='Год')),
            ],
        ),
        migrations.CreateModel(
            name='VacancieByYearForCurrentJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy', models.TextField(verbose_name='Вакансия')),
                ('year', models.IntegerField(verbose_name='Год')),
            ],
        ),
    ]