from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from periject.account import views

from periject.account import forms
# Create your views here.

class DashBoard(TemplateView):
    template_name = 'dashboard.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'