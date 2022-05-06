from django import forms

from exceldata.models import Person


class PersonForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your name', max_length=100)
    location = forms.CharField(label='Your name', max_length=100)
    birth_date = forms.DateField(label='Your name')
    location = forms.CharField(label='Your name', max_length=100)

    class Meta:
        model = Person
        fields = ('name', 'email', 'birth_date', 'location')

    def save(self):
        data = self.cleaned_data
        person = Person(name=data['name'], email=data['email'],
                        birth_date=data['birth_date'], location=data['location'])
        person.save()

        return person
