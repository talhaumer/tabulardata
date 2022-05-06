from import_export import resources
from exceldata.models import Person


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        fields = ('id', 'name', 'email', 'birth_date', 'location')
