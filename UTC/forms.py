from django import forms


class Student(forms. ModelForm):
    STUDIERENDENTARIF = 'ST'
    NORMALTARIF = 'NO'
    DOPPELTARIF = 'DO'
    EINZELZIMMER = 'EI'
    TARIF_CHOICE = [
        (STUDIERENDENTARIF, 'Studierendentarif'),
        (NORMALTARIF, 'Normaltarif'),
        (DOPPELTARIF, 'Doppeltarif'),
        (EINZELZIMMER, 'Einzelzimmer'),
    ]
    name = forms.CharField(max_length=300)
    vorname = forms.CharField(max_length=300)
    strasse = forms.CharField(max_length=100)
    hausnummer = forms.IntegerField()
    plz = forms.IntegerField()
    ort = forms.CharField(max_length=100)
    land = forms.CharField(max_length=100)
    geburtsdatum = forms.DateTimeField()
    telephone = forms.IntegerField()
    mail = forms.EmailField()
    studiengang = forms.CharField(max_length=100)
    nameDerHochschule = forms.CharField(max_length=100)
    tarif_choice = forms.CharField(
        max_length=2,
        choices=TARIF_CHOICE,
        default=NORMALTARIF,
    )
    anmerkung = forms.CharField(max_length=300)
    koffer = forms.BooleanField()
    EINMALZAHLUNG = 'EZ'
    RATENZAHLUNG = 'RZ'
    ANZAHLUNG = 'AZ'
    GUTHABEN = 'GU'
    GUTSCHEIN = 'GS'
    ZAHLUNG_CHOICE = [
        (EINMALZAHLUNG, 'Einmalzahlung'),
        (RATENZAHLUNG, 'Ratenzahlung'),
        (ANZAHLUNG, 'Anzahlung'),
        (GUTHABEN, 'Guthaben'),
        (GUTSCHEIN, 'Gutschein'),
    ]
    agb = forms.BooleanField()
