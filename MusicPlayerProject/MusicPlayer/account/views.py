from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserRegistraionForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from account.models import User
from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model

# User = get_user_model()

class UserRegisterView(View): 
    form_class = UserRegistraionForm
    template_name = 'account/register.html'
        
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'you registered succussfully', 'success')
            return redirect('music:home')
        return render(request, self.template_name, {'form':form})
    

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you loged in successfully', 'success')
                return redirect('music:home')
            messages.error(request, 'username or password is wrong', 'warning')
        return render(request, self.template_name, {'form':form})
    
class UserlogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('music:home')
    
