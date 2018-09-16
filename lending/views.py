from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import User
from .forms import UserForm


def index(request):
    all_users = User.objects.all()
    return render(request, 'lending/index.html', { 'all_users': all_users, })

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
            #firstName = form.cleaned_data['firstName']
            #lastName = form.cleaned_data['lastName']
            #email = form.cleaned_data['email']
            #phone = form.cleaned_data['phone']
            #address = form.cleaned_data['address']
            #city = form.cleaned_data['city']
            #state = form.cleaned_data['state']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('lending:index')

        return render(request, self.template_name, {'form': form})
