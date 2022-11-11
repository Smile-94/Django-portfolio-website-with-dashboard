from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

#import models
from admin_app.models import Message
from admin_app.models import Skills
from admin_app.models import Education
from admin_app.models import Expriences
from login_app.models import Profile

#import Forms
from admin_app.forms import SkillsForm
from admin_app.forms import EducationForm
from admin_app.forms import ExprienceForm
from login_app.forms import ProfileForm

# Create your views here.

class AdminView(TemplateView,LoginRequiredMixin):
    template_name='admin_app/admin.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Dash Board"
        context["messages"]=Message.objects.all().order_by('-id')
        return context
         
class MessageDetail(DetailView):
    model = Message
    template_name='admin_app/message_detail.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Message details"
        return context


class DeleteMessage(DeleteView):
    model = Message
    success_url=reverse_lazy('admin_app:admin')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Delete Message"
        return context


class AddSkills(CreateView,LoginRequiredMixin):
    fields='__all__'
    model=Skills

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Add Skills"
        context['skills']=self.model.objects.order_by('-id')
        return context

class EditSkills(UpdateView,LoginRequiredMixin,View):
    fields='__all__'
    model=Skills
    template_name='admin_app/skills_form.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Edit Skills"
        context['skills']=self.model.objects.order_by('-id')
        return context

class DeleteSkills(DeleteView,LoginRequiredMixin):
    model=Skills
    success_url=reverse_lazy('admin_app:skills')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Delete Skills"
        return context

class AddEducation(CreateView,LoginRequiredMixin,View):
    fields='__all__'
    model=Education

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Add Education"
        context['educations']=Education.objects.all().order_by('-pass_year')
        return context

class UpdateEducation(UpdateView,LoginRequiredMixin,View):
    fields='__all__'
    model=Education

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Update Education"
        context['educations']=Education.objects.all().order_by('-pass_year')
        return context

class DeleteEducation(DeleteView,LoginRequiredMixin,View):
    fields='__all__'
    model=Education
    success_url=reverse_lazy('admin_app:educations')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Delete Education"
        return context

class AddExprience(CreateView,LoginRequiredMixin,View):
    fields='__all__'
    model=Expriences

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Add Exprience"
        context['expriences']=Expriences.objects.all().order_by('-joning_date')
        return context

class UpdateExprience(UpdateView,LoginRequiredMixin,View):
    fields='__all__'
    model=Expriences

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Update Exprience"
        context['expriences']=Expriences.objects.all().order_by('-joning_date')
        return context

class DeleteExprience(DeleteView,LoginRequiredMixin,View):
    fields='__all__'
    model=Expriences
    success_url=reverse_lazy('admin_app:expriences')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["title"]="Delete Exprience"
        return context

class AddPersonalInfo(View,LoginRequiredMixin):
    
    template_name='admin_app/profile_form.html'
    form_class=ProfileForm
    profiles=Profile.objects.all()

    def get(self,request):
        form=self.form_class
        dat_dic={'title':'Profile','form':form,'profiles':self.profiles}
        return render(request,self.template_name,dat_dic)
    
    def post(self,request):
        profile=Profile.objects.get(user=request.user)
        form=ProfileForm(instance=profile)

        if request.method=='POST':
            form=ProfileForm(request.POST, request.FILES, instance=profile)
            
            if form.is_valid():
                profile.save()
                return HttpResponseRedirect(reverse('admin_app:profile', ))
        return render(request,self.template_name,{'form':self.form_class,'profiles':self.profiles})

class EditInfo(UpdateView):
    fields=('fullName','address_home','address_office','phone_number','profile_pic')
    model=Profile
    template_name='admin_app/profile_form.html'
                
            