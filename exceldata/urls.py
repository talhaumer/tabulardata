from django.urls import path

from exceldata.views import export, simple_upload, add_person, get_persons

urlpatterns = [
    path('export', export, name="export"),
    path('import', simple_upload, name='import'),
    path('add-person', add_person, name='add person'),
    path('get-persons', get_persons, name='get persons')
]