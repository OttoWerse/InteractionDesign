from django import forms

from UTC.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'vorname', 'strasse', 'hausnummer', 'plz', 'ort', 'land', 'geburtsdatum', 'telephone', 'mail',
                  'studiengang', 'nameDerHochschule', 'tarif_choice', 'anmerkung', 'koffer', 'zahlung_choice', 'agb']
        # label
        labels = {
            'telephone': 'Telefonnummer',
        }
        # help
        help_texts = {
            'koffer': 'Benötigen Sie Aufgabegepäck?',
        }
        # errors
        error_messages = {
            'name': {
                'max_length': "Dieser Name ist zu lang",
            }
        }
