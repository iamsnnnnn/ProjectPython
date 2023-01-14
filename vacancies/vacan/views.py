from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from vacan.models import SalaryByYear, VacancieByYear, SalaryByYearsForCurrentJob, VacancieByYearForCurrentJob, AvgSalaryByCity, FractionVacancyByCity, KeySkills


def index(request):
    home = {
        'title': 'iOS-разработчик'
    }
    return render(request, 'index.html', home)


def demand(request):
    dem = SalaryByYear.objects.all()
    dem_2 = VacancieByYear.objects.all()
    dem_3 = SalaryByYearsForCurrentJob.objects.all()
    dem_4 = VacancieByYearForCurrentJob.objects.all()

    print(dem)
    print(dem_2)
    print(dem_3)
    print(dem_4)

    template = loader.get_template('demand.html')
    context = {
        'x': dem,
        'y': dem_2,
        'z': dem_3,
        'w': dem_4
    }
    return HttpResponse(template.render(context, request))

def geography(request):
    geo = AvgSalaryByCity.objects.all()
    geo_2 = FractionVacancyByCity.objects.all()

    print(geo)
    print(geo_2)

    template = loader.get_template('geography.html')
    context = {
        'one': geo,
        'two': geo_2
    }
    return HttpResponse(template.render(context, request))

def skills(request):
    skls = KeySkills.objects.all()
    years = (skl.year for skl in skls)
    d_skill = {}
    for year in years:
        d_skill[year] = []
        for skl in skls:
            if skl.year == year:
                d_skill[year].append((skl.skill, skl.count))

    template = loader.get_template('skills.html')
    context = {
        'skills': d_skill
    }
    return HttpResponse(template.render(context, request))

def recent_vac(request):
    return render(request, 'recent_vac.html')
