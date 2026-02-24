from django.shortcuts import render
from .models import Company

# Create your views here.
def list_companies(request):
    companies = Company.objects.all()
    return render(request, 'clients/companies_list.html', {'companies': companies})