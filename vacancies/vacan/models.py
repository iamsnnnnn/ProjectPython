from django.db import models


class SalaryByYearsForCurrentJob(models.Model):
    city = models.TextField('Город', max_length=50)
    year = models.IntegerField('Год')
    salary = models.FloatField('Зарплата')


class SalaryByYear(models.Model):
    year = models.IntegerField('Год')
    salary = models.FloatField('Зарплата')


class KeySkills(models.Model):
    skill = models.TextField('Название')
    year = models.IntegerField('Год')
    count = models.IntegerField('Количество повторений')


class VacancieByYear(models.Model):
    vacancie = models.TextField('Вакансия')
    year = models.IntegerField('Год')


class VacancieByYearForCurrentJob(models.Model):
    vacancy = models.TextField('Вакансия')
    year = models.IntegerField('Год')


class AvgSalaryByCity(models.Model):
    city = models.TextField('Город')
    salary = models.FloatField('Зарплата')


class FractionVacancyByCity(models.Model):
    city = models.TextField('Город')
    fraction = models.FloatField('Зарплата')
