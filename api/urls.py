from django.urls import path
from api import views

urlpatterns = [
    path('hello/', views.hello),
    path('companies/', views.companies),
    path('companies/<int:id>/', views.company_detailed),
    path('companies/<int:id>/vacancies/', views.company_vacancy),
    path('vacancies/', views.vacancies),
    path('vacancies/<int:id>/', views.vacancy_detailed),
    path('vacancies/top_ten/', views.vacancy_top)
]