from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import StudentForm
from .models import Student


class IndexView(generic.TemplateView):
    template_name = 'UTC/index.html'


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
