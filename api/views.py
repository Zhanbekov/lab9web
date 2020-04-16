from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer

def hello(request):
    return HttpResponse('hello')

def companies(request):
    try:
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"no data"})

def company_detailed(request, id):
    try:
        company = Company.objects.get(id = id)
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"no data"})

def company_vacancy(request, id):
    try:
        company = Company.objects.get(id = id)
        vacancies = company.vacancy_set.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"no data"})

# vacancies:
def vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"no data"})

def vacancy_detailed(request, id):
    try:
        vacancies = Vacancy.objects.get(id = id)
        serializer = VacancySerializer(vacancies)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"no data"})


def vacancy_top(request):
    try:
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({"no data"})
        