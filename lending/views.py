from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Profile, Object
from .forms import UserForm, LoginForm


def home(request):
    if request.user.is_authenticated:
        return redirect('lending:dashboard')
    return render(request, 'lending/home.html')

def dashboard(request):
    user = request.user
    return render(request, 'lending/dashboard.html', { 'user': user })

def show_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'lending/show_user.html', {'user': user})

def show_profile(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'lending/show_profile.html', {'profile': profile})

def show_objects(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    users_objects = Object.objects.filter(ownedBy=user_id)
    return render(request, 'lending/show_objects.html', {'owner': user, 'objects': users_objects})

def log_out(request):
    logout(request) 
    return redirect('lending:home')

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
                profile = Profile.objects.create(user=user)
                if user.is_active:
                    login(request, user)
                    return redirect('lending:profile-edit', pk=profile.id)

        return render(request, self.template_name, {'form': form})

class UpdateProfile(UpdateView):
    model = Profile
    fields = ['address', 'city', 'state', 'bio']
    success_url = reverse_lazy('lending:dashboard')

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('lending:login')
        return super(UpdateProfile, self).dispatch(request, *args, **kwargs)

class CreateObject(CreateView):
    model = Object
    fields = ['name', 'description']
    success_url = reverse_lazy('lending:dashboard')

    def form_valid(self, form):
        form.instance.ownedBy = self.request.user
        return super(CreateObject, self).form_valid(form)

class UpdateObject(UpdateView):
    model = Object
    fields = ['name', 'description']
    success_url = reverse_lazy('lending:dashboard')

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.ownedBy == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('lending:login')
        return super(UpdateObject, self).dispatch(request, *args, **kwargs)

class DeleteObject(DeleteView):
    model = Object
    success_url = reverse_lazy('lending:dashboard')

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.ownedBy == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('lending:login')
        return super(DeleteObject, self).dispatch(request, *args, **kwargs)


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
                # Create a profile for the user if it is missing.
                try:
                    user.profile
                except ObjectDoesNotExist:
                    profile = Profile.objects.create(user=user)

                if user.is_active:
                    login(request, user)
                    return redirect('lending:dashboard')

        return render(request, self.template_name, {'form': form})
