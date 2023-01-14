from django.contrib import admin
from vacan.models import SalaryByYearsForCurrentJob, SalaryByYear, KeySkills, VacancieByYear, VacancieByYearForCurrentJob, \
    AvgSalaryByCity, FractionVacancyByCity

admin.site.register(SalaryByYearsForCurrentJob)
admin.site.register(SalaryByYear)
admin.site.register(KeySkills)
admin.site.register(VacancieByYear)
admin.site.register(VacancieByYearForCurrentJob)
admin.site.register(AvgSalaryByCity)
admin.site.register(FractionVacancyByCity)