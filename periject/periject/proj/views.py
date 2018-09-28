from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from periject.account import forms
from periject.proj.forms import AssuranceQ
from periject.proj.models import Question
from periject.proj import models 

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

class GRCPage(TemplateView):
    template_name = 'grc.html'

class SupportPage(TemplateView):
    template_name = 'support.html'

class SupplierPage(TemplateView):
    template_name = 'supplier.html'

class ProjectsPage(TemplateView):
    template_name = 'projects.html'

class CreateNewProject(TemplateView):
    template_name = 'newproject.html'

class CreateNewAssurance(TemplateView):
    template_name = 'newassurance.html'

    def get(self, request):
        form = AssuranceQ()
        return render(requests, self.template_name,{'form': form}) 

    def newassurance(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:20]
        template = loader.get_template('proj/newassurance.html')
        context = {
                'latest_questions_list': latest_question_list,
        }
        return HttpResponse(template.render(context.request))

def detail(request, question_id):
        return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class CreateNewSupplier(TemplateView):
    template_name = 'newsupplier.html'

class CreateNewGRC(TemplateView):
    template_name = 'newgrc.html'




# Create your views here.
