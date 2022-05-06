from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from tablib import Dataset

from exceldata.forms import PersonForm
from exceldata.models import Person
from exceldata.resource import PersonResource
from django.http import HttpResponse


# Create your views here.

@login_required
def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


@login_required
@csrf_exempt
def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read().decode(), format='csv',
                                     headers=['id', 'name', 'email', 'birth_date', 'location'])
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'report/import.html')


@login_required
def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            messages.success(request, "Registration successful.")
            return redirect("frontpage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = PersonForm()
    return render(request=request, template_name="report/persons.html", context={"person_form": form})


@login_required
def get_persons(request):
    persons = Person.objects.all()
    return render(request, 'report/person.html', {'persons': persons})
