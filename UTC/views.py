from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import StudentForm
from .models import Student


class IndexView(generic.TemplateView):
    template_name = 'UTC/index.html'


class SchottlandView(generic.TemplateView):
    template_name = 'UTC/schottland.html'


class IndienView(generic.TemplateView):
    template_name = 'UTC/indien.html'


class GeorgienArmenienView(generic.TemplateView):
    template_name = 'UTC/georgien-armenien.html'


class TansaniaView(generic.TemplateView):
    template_name = 'UTC/tansania.html'


class NorwegenView(generic.TemplateView):
    template_name = 'UTC/norwegen.html'


class HawaiiView(generic.TemplateView):
    template_name = 'UTC/hawaii.html'


class AlaskaView(generic.TemplateView):
    template_name = 'UTC/alaska.html'


class IslandView(generic.TemplateView):
    template_name = 'UTC/island.html'


class DetailView(generic.DetailView):
    model = Student
    template_name = 'UTC/detail.html'


class ResultsView(generic.DetailView):
    model = Student
    template_name = 'UTC/results.html'


class FormVIew(generic.FormView):
    form_class = StudentForm
    template_name = 'UTC/form.html'
    success_url = '/UTC/'


def registered(request):
    form = StudentForm(request.POST)
    form.save()
    return render(request, 'UTC/success.html', {'form': form})


'''
    form = StudentForm(request.POST)
    form.save()
    return render(request, 'UTC/index.html', {'form': form})
    
    print('Surenhohn')
    name = request.POST['name']
    vorname = request.POST['vorname']
    strasse = request.POST['strasse']
    hausnummer = request.POST['hausnummer']
    plz = request.POST['plz']
    ort = request.POST['ort']
    land = request.POST['land']
    geburtsdatum = request.POST['geburtsdatum']
    telephone = request.POST['telephone']
    mail = request.POST['mail']
    studiengang = request.POST['studiengang']
    nameDerHochschule = request.POST['nameDerHochschule']
    tarif_choice = request.POST['tarif_choice']
    anmerkung = request.POST['anmerkung']
    koffer = request.POST['koffer']
    zahlung_choice = request.POST['zahlung_choice']
    agb = request.POST['agb']

    s = Student(name=name, vorname=vorname, strasse=strasse, hausnummer=hausnummer, plz=plz, ort=ort,
                land=land, geburtsdatum=geburtsdatum, telephone=telephone, mail=mail,
                studiengang=studiengang, nameDerHochschule=nameDerHochschule, tarif_choice=tarif_choice,
                anmerkung=anmerkung, koffer=koffer, zahlung_choice=zahlung_choice, agb=agb)
    s.save()
    return render(request, 'UTC/registered.html', {'name': name})


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/UTC/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'UTC/index.html', {'form': form})
'''
