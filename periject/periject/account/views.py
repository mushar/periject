from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView


from periject.account import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('dashboard')
    template_name = 'signup.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class DashBoard(TemplateView):
    template_name = 'dashboard.html'

class GRC(TemplateView):
    template_name = 'grc.html'

class SupportPage(TemplateView):
    template_name = 'support.html'

class SupplierPage(TemplateView):
    template_name = 'supplier.html'

class ProjectsPage(TemplateView):
    template_name = 'projects.html'

class CreateNewProject(TemplateView):
    template_name = 'newproject.html'
# Create your views here.
