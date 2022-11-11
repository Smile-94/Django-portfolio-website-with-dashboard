from django.shortcuts import render,HttpResponse
from django.shortcuts import HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login,logout,authenticate

#Authentacion Form

class LoginView(View):
    form_class=AuthenticationForm
    template_name='login_app/login.html'

    def get(self,request):
        form=self.form_class
        data_dic={'form':form}
        return render(request,self.template_name,data_dic)
    
    def post(self,request):
        if request.method=='POST':
            form=AuthenticationForm(data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')

                user=authenticate(username=username,password=password)

                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse('admin_app:admin'),)
                    
        return render(request,self.template_name,{'form':self.form_class})

class LogOut(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('login_app:login'))
