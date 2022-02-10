import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Student(models.Model):
    STUDIERENDENTARIF = 'ST'
    NORMALTARIF = 'NO'
    DOPPELTARIF = 'DO'
    EINZELZIMMER = 'EI'
    TARIF_CHOICE = [
        (STUDIERENDENTARIF, 'Studierendentarif'),
        (NORMALTARIF, 'Normaltarif'),
        (DOPPELTARIF, 'Doppelzimmer'),
        (EINZELZIMMER, 'Einzelzimmer'),
    ]
    name = models.CharField(max_length=300)
    vorname = models.CharField(max_length=300)
    strasse = models.CharField(max_length=100)
    hausnummer = models.PositiveIntegerField()
    plz = models.PositiveIntegerField()
    ort = models.CharField(max_length=100)
    land = models.CharField(max_length=100)
    geburtsdatum = models.DateField('date of birth')
    telephone = models.PositiveIntegerField()
    mail = models.EmailField()
    studiengang = models.CharField(max_length=100)
    nameDerHochschule = models.CharField(max_length=100)
    tarif_choice = models.CharField(
        max_length=2,
        choices=TARIF_CHOICE,
        default=NORMALTARIF,
    )
    anmerkung = models.CharField(max_length=300, blank=True)
    koffer = models.BooleanField()
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
    zahlung_choice = models.CharField(
        max_length=2,
        choices=ZAHLUNG_CHOICE,
        default=EINMALZAHLUNG,
    )
    agb = models.BooleanField()
