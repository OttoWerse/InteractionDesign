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



