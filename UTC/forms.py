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
            'geburtsdatum': 'Geburtsdatum',
            'nameDerHochschule': "Name der Hochschule",
            'tarif_choice': "Welchen Tarif möchten Sie?",
            'zahlung_choice': "Welche Zahlungsart möchten Sie?",
        }
        # help
        help_texts = {
            'koffer': 'Benötigen Sie Aufgabegepäck?',
            'anmerkung': '(optional)',
        }
        # errors
        error_messages = {
            'name': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'vorname': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'strasse': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Straßen-Name ist zu lang",
            },
            'hausnummer': {
                'required': "Dieses Feld darf nicht leer sein",
            },
            'plz': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'ort': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'land': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'geburtsdatum': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'telephone': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'mail': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
                'unique': "This mail address is already in use"
            },
            'studiengang': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'nameDerHochschule': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'tarif_choice': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
            'anmerkung': {
                'max_length': "Dieser Name ist zu lang",
            },
            'zahlung_choice': {
                'required': "Dieses Feld darf nicht leer sein",
                'max_length': "Dieser Name ist zu lang",
            },
        }
