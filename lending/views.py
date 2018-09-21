from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import User
from .forms import UserForm, LoginForm


def index(request):
    all_users = User.objects.all()
    return render(request, 'lending/index.html', { 'all_users': all_users, })

def home(request):
    return render(request, 'lending/home.html')

def dashboard(request):
    user = request.user
    return render(request, 'lending/dashboard.html', { 'user': user })

def show_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'lending/show_user.html', {'user': user})

class UserFormView(View):
    form_class = UserForm
    template_name = 'lending/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('lending:dashboard')

        return render(request, self.template_name, {'form': form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'lending/login.html'
    
    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('lending:dashboard')

        return render(request, self.template_name, {'form': form})
