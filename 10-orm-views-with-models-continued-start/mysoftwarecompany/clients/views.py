from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# Create your views here.
from .models import Company, Employee


def list_companies(request):
    # fetching data from the database and passing it to the template
    companies = Company.objects.all()

    return render(request, 'clients/companies_list.html', {'companies': companies})

def company_detail(request, company_id):
    #fetching a specific company by its ID or return a 404 error
    company = get_object_or_404(Company, id=company_id)

    return render(request, 'clients/company_detail.html', {'company': company})

def employees_search_results(request, company_id):
    # handle the search query for employees
    query = request.GET.get('q', '')
    company = get_object_or_404(Company, id=company_id)

    if query:
        # if a query is provided, filter employees by first name
        # icontains is used for a case insensitive search
        # company.employees is a queryset of employees related to the company
            # and we filter then by first_name__icontains=query
            # which we return all employees whose first name contains the query string provided
        
        # Use Q objects to search by first or last name
        employees = company.employees.filter( # type: ignore[attr-defined]
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
         )
    else:
        #if no query is provided, return an empty queryset
        employees = Employee.objects.none()

    #return
    return render(request, 'clients/employee_search_results.html', {'employees': employees, 'query': query})

