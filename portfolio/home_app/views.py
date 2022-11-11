from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import FormView

#import froms
from admin_app.forms import MessageForm

#import models
from admin_app.models import Skills
from admin_app.models import Education
from admin_app.models import Expriences

# Create your views here.
class Index(TemplateView):
    template_name='home_app/index.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Personal Portfolio"
        context['skills']=Skills.objects.all()
        context['educations']=Education.objects.all().order_by('-pass_year')
        context['expriences']=Expriences.objects.all().order_by('-joning_date')
        context['form']=MessageForm()
        return context

class SenderMessage(View):
    form_class=MessageForm

    def post(self,request):
        if request.method=='POST':
            form=self.form_class(data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('home_app:home'))
